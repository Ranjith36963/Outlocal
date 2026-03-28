"""Tests for lead pipeline and CRM (F015)."""

import pytest

from src.outlocal.crm.pipeline import LeadPipeline
from src.outlocal.core.database import Database
from src.outlocal.core.models import LeadStatus


@pytest.fixture
async def db(tmp_path):
    db_path = str(tmp_path / "test_crm.db")
    database = Database(db_path)
    await database.init_db()
    yield database
    await database.close()


@pytest.fixture
def pipeline(db):
    return LeadPipeline(db)


@pytest.fixture
async def sample_lead(db):
    """Insert a sample lead and return its ID."""
    async with db.connection() as conn:
        cursor = await conn.execute(
            "INSERT INTO leads (business_name, town, source, status) VALUES (?, ?, ?, ?)",
            ("Test Biz", "Bristol", "google_maps", "new"),
        )
        await conn.commit()
        return cursor.lastrowid


class TestLeadPipeline:
    """Tests for lead status tracking."""

    @pytest.mark.asyncio
    async def test_update_status(self, pipeline, sample_lead):
        await pipeline.update_status(sample_lead, LeadStatus.ENRICHED)
        lead = await pipeline.get_lead(sample_lead)
        assert lead["status"] == "enriched"

    @pytest.mark.asyncio
    async def test_status_transition_logged(self, pipeline, sample_lead):
        await pipeline.update_status(sample_lead, LeadStatus.ENRICHED)
        log = await pipeline.get_activity_log(sample_lead)
        assert len(log) >= 1
        assert log[0]["action"] == "status_change"

    @pytest.mark.asyncio
    async def test_get_pipeline_counts(self, pipeline, db):
        """Pipeline view shows count per status."""
        async with db.connection() as conn:
            await conn.execute(
                "INSERT INTO leads (business_name, town, source, status) VALUES (?, ?, ?, ?)",
                ("A", "London", "manual", "new"),
            )
            await conn.execute(
                "INSERT INTO leads (business_name, town, source, status) VALUES (?, ?, ?, ?)",
                ("B", "London", "manual", "new"),
            )
            await conn.execute(
                "INSERT INTO leads (business_name, town, source, status) VALUES (?, ?, ?, ?)",
                ("C", "London", "manual", "enriched"),
            )
            await conn.commit()

        counts = await pipeline.get_pipeline_counts()
        assert counts.get("new", 0) >= 2
        assert counts.get("enriched", 0) >= 1

    @pytest.mark.asyncio
    async def test_filter_leads_by_status(self, pipeline, db):
        async with db.connection() as conn:
            await conn.execute(
                "INSERT INTO leads (business_name, town, source, status) VALUES (?, ?, ?, ?)",
                ("X", "Bath", "manual", "scored"),
            )
            await conn.commit()

        leads = await pipeline.filter_leads(status="scored")
        assert len(leads) >= 1
        assert all(l["status"] == "scored" for l in leads)

    @pytest.mark.asyncio
    async def test_filter_leads_by_town(self, pipeline, db):
        async with db.connection() as conn:
            await conn.execute(
                "INSERT INTO leads (business_name, town, source, status) VALUES (?, ?, ?, ?)",
                ("Y", "Oxford", "manual", "new"),
            )
            await conn.commit()

        leads = await pipeline.filter_leads(town="Oxford")
        assert len(leads) >= 1
        assert all(l["town"] == "Oxford" for l in leads)

    @pytest.mark.asyncio
    async def test_log_activity(self, pipeline, sample_lead):
        await pipeline.log_activity(sample_lead, "scraped", details="From Google Maps")
        log = await pipeline.get_activity_log(sample_lead)
        assert any(e["action"] == "scraped" for e in log)
