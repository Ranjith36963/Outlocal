"""Tests for follow-up sequence engine (F012)."""

import pytest
from datetime import datetime, timezone, timedelta
from unittest.mock import AsyncMock, patch

from src.outlocal.followup.sequence import FollowUpEngine, FollowUpStep
from src.outlocal.core.database import Database


@pytest.fixture
async def db(tmp_path):
    db_path = str(tmp_path / "test_followup.db")
    database = Database(db_path)
    await database.init_db()
    # Seed data
    async with database.connection() as conn:
        await conn.execute(
            "INSERT INTO campaigns (name, status) VALUES (?, ?)",
            ("Test Campaign", "active"),
        )
        await conn.execute(
            "INSERT INTO leads (business_name, town, source, email, status) VALUES (?, ?, ?, ?, ?)",
            ("Test Biz", "London", "manual", "test@example.com", "contacted"),
        )
        await conn.execute(
            "INSERT INTO emails (lead_id, campaign_id, subject, body, provider, status, sent_at) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (1, 1, "Original Email", "Hi there", "groq", "sent",
             (datetime.now(timezone.utc) - timedelta(days=4)).isoformat()),
        )
        await conn.commit()
    yield database
    await database.close()


@pytest.fixture
def engine(db):
    return FollowUpEngine(db)


class TestFollowUpSequence:
    """Tests for follow-up sequence logic."""

    def test_default_sequence(self, engine):
        """Default sequence should have 3 follow-ups at day 3, 7, 14."""
        seq = engine.default_sequence()
        assert len(seq) == 3
        assert seq[0].delay_days == 3
        assert seq[1].delay_days == 7
        assert seq[2].delay_days == 14

    @pytest.mark.asyncio
    async def test_find_due_followups(self, engine):
        """Should find emails that need follow-up based on timing."""
        due = await engine.find_due_followups()
        # Email was sent 4 days ago, first follow-up is at day 3 — should be due
        assert len(due) >= 1

    @pytest.mark.asyncio
    async def test_skip_if_replied(self, engine, db):
        """Should skip follow-up if lead has replied."""
        async with db.connection() as conn:
            await conn.execute(
                "INSERT INTO replies (email_id, raw_text) VALUES (?, ?)",
                (1, "Thanks for your email!"),
            )
            await conn.execute(
                "UPDATE leads SET status = 'replied' WHERE id = 1",
            )
            await conn.commit()

        due = await engine.find_due_followups()
        # Should not include emails where lead replied
        lead_ids = [d["lead_id"] for d in due]
        assert 1 not in lead_ids

    @pytest.mark.asyncio
    async def test_skip_if_unsubscribed(self, engine, db):
        """Should skip follow-up if lead is unsubscribed."""
        async with db.connection() as conn:
            await conn.execute(
                "UPDATE leads SET status = 'unsubscribed' WHERE id = 1",
            )
            await conn.commit()

        due = await engine.find_due_followups()
        lead_ids = [d["lead_id"] for d in due]
        assert 1 not in lead_ids

    def test_followup_step_structure(self):
        step = FollowUpStep(delay_days=3, condition="no_reply", max_followups=3)
        assert step.delay_days == 3
        assert step.condition == "no_reply"

    @pytest.mark.asyncio
    async def test_count_followups_sent(self, engine, db):
        """Should count how many follow-ups already sent for an email."""
        count = await engine.count_followups_for_email(1)
        assert count == 0  # No follow-ups sent yet
