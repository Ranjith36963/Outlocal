"""Tests for A/B testing (F018)."""

import pytest

from src.outlocal.analytics.ab_testing import ABTestManager
from src.outlocal.core.database import Database


@pytest.fixture
async def db(tmp_path):
    db_path = str(tmp_path / "test_ab.db")
    database = Database(db_path)
    await database.init_db()
    async with database.connection() as conn:
        await conn.execute("INSERT INTO campaigns (name, status) VALUES (?, ?)", ("Test", "active"))
        for i in range(5):
            await conn.execute(
                "INSERT INTO leads (business_name, town, source) VALUES (?, ?, ?)",
                (f"Biz {i}", "London", "manual"),
            )
        await conn.commit()
    yield database
    await database.close()


@pytest.fixture
def ab_mgr(db):
    return ABTestManager(db)


class TestABTesting:
    @pytest.mark.asyncio
    async def test_create_test(self, ab_mgr):
        test_id = await ab_mgr.create_test(
            campaign_id=1,
            variant_a={"subject": "Subject A"},
            variant_b={"subject": "Subject B"},
        )
        assert test_id > 0

    @pytest.mark.asyncio
    async def test_assign_variant(self, ab_mgr):
        test_id = await ab_mgr.create_test(1, {"subject": "A"}, {"subject": "B"})
        variant = await ab_mgr.assign_variant(test_id, 1)
        assert variant in ("A", "B")

    @pytest.mark.asyncio
    async def test_get_results_structure(self, ab_mgr):
        test_id = await ab_mgr.create_test(1, {"subject": "A"}, {"subject": "B"})
        await ab_mgr.assign_variant(test_id, 1)
        await ab_mgr.assign_variant(test_id, 2)
        results = await ab_mgr.get_results(test_id)
        assert "variant_a" in results
        assert "variant_b" in results
        assert "winner" in results

    @pytest.mark.asyncio
    async def test_insufficient_data_no_winner(self, ab_mgr):
        test_id = await ab_mgr.create_test(1, {"subject": "A"}, {"subject": "B"})
        await ab_mgr.assign_variant(test_id, 1)
        results = await ab_mgr.get_results(test_id)
        assert results["winner"] == "insufficient_data"

    @pytest.mark.asyncio
    async def test_results_have_rates(self, ab_mgr):
        test_id = await ab_mgr.create_test(1, {"subject": "A"}, {"subject": "B"})
        for i in range(1, 6):
            await ab_mgr.assign_variant(test_id, i)
        results = await ab_mgr.get_results(test_id)
        for v in ["variant_a", "variant_b"]:
            assert "open_rate" in results[v]
            assert "reply_rate" in results[v]
