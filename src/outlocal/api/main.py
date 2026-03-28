"""FastAPI application for OUTLOCAL."""

from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.outlocal import __version__
from src.outlocal.core.config import get_settings
from src.outlocal.core.database import Database

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

# CORS — permissive in development
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


# === API v1 Router ===
from fastapi import APIRouter

api_v1 = APIRouter(prefix="/api/v1")


@api_v1.get("/leads")
async def list_leads() -> list:
    """List leads (stub — full implementation in F021)."""
    return []


app.include_router(api_v1)
