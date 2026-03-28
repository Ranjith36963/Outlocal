"""Tests for end-to-end pipeline (F025)."""

import pytest
from src.outlocal.core.database import Database
from src.outlocal.core.pipeline import OutlocalPipeline


@pytest.fixture
async def db(tmp_path):
    db_path = str(tmp_path / "test_pipeline.db")
    database = Database(db_path)
    await database.init_db()
    async with database.connection() as conn:
        await conn.execute(
            "INSERT INTO leads (business_name, owner_name, email, phone, website, town, source, status) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (
                "Pipeline Test Biz",
                "Jane",
                "jane@test.co.uk",
                "+44 117 123 4567",
                "https://test.co.uk",
                "Bristol",
                "google_maps",
                "new",
            ),
        )
        await conn.commit()
    yield database
    await database.close()


@pytest.fixture
def pipeline(db):
    return OutlocalPipeline(db)


class TestOutlocalPipeline:
    @pytest.mark.asyncio
    async def test_process_lead_returns_results(self, pipeline):
        result = await pipeline.process_lead(1)
        assert result["lead_id"] == 1
        assert "steps" in result

    @pytest.mark.asyncio
    async def test_process_lead_scores(self, pipeline):
        result = await pipeline.process_lead(1)
        assert result["steps"]["score"]["status"] == "success"
        assert result["steps"]["score"]["score"] > 0

    @pytest.mark.asyncio
    async def test_process_lead_updates_status(self, pipeline, db):
        await pipeline.process_lead(1)
        async with db.connection() as conn:
            cursor = await conn.execute("SELECT status, score FROM leads WHERE id = 1")
            row = await cursor.fetchone()
        assert row[0] == "scored"
        assert row[1] is not None

    @pytest.mark.asyncio
    async def test_process_lead_logs_activity(self, pipeline):
        await pipeline.process_lead(1)
        log = await pipeline._pipeline.get_activity_log(1)
        assert any("scored" in e["action"] for e in log)

    @pytest.mark.asyncio
    async def test_process_nonexistent_lead(self, pipeline):
        result = await pipeline.process_lead(999)
        assert "error" in result

    @pytest.mark.asyncio
    async def test_pipeline_steps_execute_in_order(self, pipeline):
        result = await pipeline.process_lead(1)
        assert "score" in result["steps"]
