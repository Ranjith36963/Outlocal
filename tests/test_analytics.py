"""Tests for campaign analytics (F017)."""

import pytest

from src.outlocal.analytics.metrics import CampaignAnalytics
from src.outlocal.core.database import Database


@pytest.fixture
async def db(tmp_path):
    db_path = str(tmp_path / "test_analytics.db")
    database = Database(db_path)
    await database.init_db()
    # Seed test data
    async with database.connection() as conn:
        await conn.execute("INSERT INTO campaigns (name, status) VALUES (?, ?)", ("Test", "active"))
        await conn.execute("INSERT INTO leads (business_name, town, source) VALUES (?, ?, ?)", ("A", "London", "manual"))
        await conn.execute("INSERT INTO leads (business_name, town, source) VALUES (?, ?, ?)", ("B", "London", "manual"))
        # 2 sent emails, 1 opened, 1 clicked
        await conn.execute(
            "INSERT INTO emails (lead_id, campaign_id, subject, body, provider, status, sent_at, opened_at) "
            "VALUES (?, ?, ?, ?, ?, ?, datetime('now'), datetime('now'))",
            (1, 1, "Subject 1", "Body", "groq", "sent"),
        )
        await conn.execute(
            "INSERT INTO emails (lead_id, campaign_id, subject, body, provider, status, sent_at, clicked_at) "
            "VALUES (?, ?, ?, ?, ?, ?, datetime('now'), datetime('now'))",
            (2, 1, "Subject 2", "Body", "groq", "sent"),
        )
        # 1 reply classified as interested
        await conn.execute(
            "INSERT INTO replies (email_id, raw_text, classification) VALUES (?, ?, ?)",
            (1, "Yes!", "interested"),
        )
        await conn.commit()
    yield database
    await database.close()


@pytest.fixture
def analytics(db):
    return CampaignAnalytics(db)


class TestCampaignAnalytics:
    @pytest.mark.asyncio
    async def test_total_sent(self, analytics):
        metrics = await analytics.get_campaign_metrics(1)
        assert metrics["total_sent"] == 2

    @pytest.mark.asyncio
    async def test_open_rate(self, analytics):
        metrics = await analytics.get_campaign_metrics(1)
        assert metrics["total_opened"] == 1
        assert metrics["open_rate"] == 50.0

    @pytest.mark.asyncio
    async def test_click_rate(self, analytics):
        metrics = await analytics.get_campaign_metrics(1)
        assert metrics["total_clicked"] == 1

    @pytest.mark.asyncio
    async def test_reply_rate(self, analytics):
        metrics = await analytics.get_campaign_metrics(1)
        assert metrics["total_replied"] == 1
        assert metrics["reply_rate"] == 50.0

    @pytest.mark.asyncio
    async def test_conversion_rate(self, analytics):
        metrics = await analytics.get_campaign_metrics(1)
        assert metrics["total_interested"] == 1
        assert metrics["conversion_rate"] == 50.0

    @pytest.mark.asyncio
    async def test_daily_stats(self, analytics):
        daily = await analytics.get_daily_stats(1)
        assert len(daily) >= 1
        assert "day" in daily[0]
        assert "sent" in daily[0]

    @pytest.mark.asyncio
    async def test_empty_campaign_metrics(self, analytics):
        metrics = await analytics.get_campaign_metrics(999)
        assert metrics["total_sent"] == 0
        assert metrics["open_rate"] == 0
