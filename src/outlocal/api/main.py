"""FastAPI application for OUTLOCAL."""

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import Any

from fastapi import APIRouter, FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from src.outlocal import __version__
from src.outlocal.compliance.engine import ComplianceEngine
from src.outlocal.core.config import get_settings
from src.outlocal.core.database import Database
from src.outlocal.crm.campaigns import CampaignManager
from src.outlocal.crm.pipeline import LeadPipeline

db = Database()


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Application lifespan — init DB on startup, close on shutdown."""
    settings = get_settings()
    db_path = settings.database_url.replace("sqlite:///", "")
    db._db_path = db_path
    await db.init_db()
    yield
    await db.close()


app = FastAPI(
    title="OUTLOCAL",
    description="AI-Powered Cold Outreach Platform for UK Local Businesses",
    version=__version__,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health_check() -> dict:
    """Health check endpoint."""
    return {
        "status": "healthy",
        "version": __version__,
        "service": "outlocal",
    }


# === Request/Response Models ===


class LeadCreate(BaseModel):
    business_name: str
    town: str
    source: str = "manual"
    owner_name: str | None = None
    email: str | None = None
    phone: str | None = None
    website: str | None = None


class LeadUpdate(BaseModel):
    business_name: str | None = None
    owner_name: str | None = None
    email: str | None = None
    phone: str | None = None
    website: str | None = None
    town: str | None = None
    status: str | None = None


class CampaignCreate(BaseModel):
    name: str
    target_criteria: dict[str, Any] = {}
    template: str | None = None


class ErasureRequest(BaseModel):
    email: str


# === API v1 Router ===

api_v1 = APIRouter(prefix="/api/v1")


# --- Leads ---


@api_v1.post("/leads", status_code=201)
async def create_lead(lead: LeadCreate) -> dict:
    """Create a new lead."""
    async with db.connection() as conn:
        cursor = await conn.execute(
            "INSERT INTO leads (business_name, owner_name, email, phone, website, town, source) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (
                lead.business_name,
                lead.owner_name,
                lead.email,
                lead.phone,
                lead.website,
                lead.town,
                lead.source,
            ),
        )
        await conn.commit()
        return {"id": cursor.lastrowid, "status": "created"}


@api_v1.get("/leads")
async def list_leads(
    status: str | None = None,
    town: str | None = None,
    min_score: int | None = None,
    limit: int = Query(default=100, le=500),
    offset: int = 0,
) -> list[dict]:
    """List leads with optional filters."""
    pipeline = LeadPipeline(db)
    return await pipeline.filter_leads(
        status=status,
        town=town,
        min_score=min_score,
        limit=limit,
        offset=offset,
    )


@api_v1.get("/leads/{lead_id}")
async def get_lead(lead_id: int) -> dict:
    """Get lead detail with activity log."""
    pipeline = LeadPipeline(db)
    lead = await pipeline.get_lead(lead_id)
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")
    lead["activity_log"] = await pipeline.get_activity_log(lead_id)
    return lead


@api_v1.put("/leads/{lead_id}")
async def update_lead(lead_id: int, update: LeadUpdate) -> dict:
    """Update lead fields."""
    allowed_columns = frozenset(LeadUpdate.model_fields.keys())
    fields = {k: v for k, v in update.model_dump().items() if v is not None}
    if not fields:
        raise HTTPException(status_code=400, detail="No fields to update")

    # Validate column names against allowlist to prevent SQL injection
    for col in fields:
        if col not in allowed_columns:
            raise HTTPException(status_code=400, detail=f"Invalid field: {col}")

    set_clause = ", ".join(f"{k} = ?" for k in fields)
    values = list(fields.values()) + [lead_id]

    async with db.connection() as conn:
        cursor = await conn.execute(
            f"UPDATE leads SET {set_clause}, updated_at = datetime('now') WHERE id = ?",
            values,
        )
        await conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Lead not found")
    return {"id": lead_id, "status": "updated"}


@api_v1.delete("/leads/{lead_id}")
async def delete_lead(lead_id: int) -> dict:
    """Soft delete a lead by setting status to 'lost'."""
    async with db.connection() as conn:
        cursor = await conn.execute(
            "UPDATE leads SET status = 'lost', updated_at = datetime('now') WHERE id = ?",
            (lead_id,),
        )
        await conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Lead not found")
    return {"id": lead_id, "status": "deleted"}


# --- Campaigns ---


@api_v1.post("/campaigns", status_code=201)
async def create_campaign(campaign: CampaignCreate) -> dict:
    """Create a new campaign."""
    mgr = CampaignManager(db)
    campaign_id = await mgr.create_campaign(
        name=campaign.name,
        target_criteria=campaign.target_criteria,
        template=campaign.template,
    )
    return {"id": campaign_id, "status": "created"}


@api_v1.get("/campaigns")
async def list_campaigns() -> list[dict]:
    """List all campaigns."""
    mgr = CampaignManager(db)
    return await mgr.list_campaigns()


@api_v1.get("/campaigns/{campaign_id}/stats")
async def campaign_stats(campaign_id: int) -> dict:
    """Get campaign statistics."""
    mgr = CampaignManager(db)
    campaign = await mgr.get_campaign(campaign_id)
    if not campaign:
        raise HTTPException(status_code=404, detail="Campaign not found")
    stats = await mgr.get_campaign_stats(campaign_id)
    return {"campaign": campaign, "stats": stats}


# --- Compliance ---


@api_v1.post("/compliance/unsubscribe/{email}")
async def unsubscribe(email: str) -> dict:
    """One-click unsubscribe. Email address must contain @."""
    if "@" not in email:
        raise HTTPException(status_code=400, detail="Invalid email address")
    compliance = ComplianceEngine(db)
    await compliance.add_suppression(email, "unsubscribe")
    return {"status": "unsubscribed", "email": email}


@api_v1.post("/compliance/erasure")
async def erasure(request: ErasureRequest) -> dict:
    """GDPR right to erasure."""
    compliance = ComplianceEngine(db)
    return await compliance.erase_by_email(request.email)


@api_v1.get("/compliance/audit/{email}")
async def audit_trail(email: str) -> list[dict]:
    """Get consent audit trail for an email."""
    compliance = ComplianceEngine(db)
    return await compliance.get_consent_log(email)


app.include_router(api_v1)
