"""Tests for GDPR and CAN-SPAM compliance engine (F019)."""

import pytest
from src.outlocal.compliance.engine import ComplianceEngine
from src.outlocal.core.database import Database


@pytest.fixture
async def db(tmp_path):
    """Create temp database with schema."""
    db_path = str(tmp_path / "test_compliance.db")
    database = Database(db_path)
    await database.init_db()
    # Add suppression_list and consent_log tables
    async with database.connection() as conn:
        await conn.executescript("""
            CREATE TABLE IF NOT EXISTS suppression_list (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL UNIQUE,
                reason TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT (datetime('now'))
            );
            CREATE TABLE IF NOT EXISTS consent_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL,
                action TEXT NOT NULL,
                source TEXT,
                details TEXT,
                timestamp TEXT NOT NULL DEFAULT (datetime('now'))
            );
        """)
    yield database
    await database.close()


@pytest.fixture
def engine(db):
    return ComplianceEngine(db)


class TestSuppressionList:
    """Tests for the suppression list (unsubscribe tracking)."""

    @pytest.mark.asyncio
    async def test_add_to_suppression_list(self, engine):
        await engine.add_suppression("user@example.com", "unsubscribe")
        assert await engine.is_suppressed("user@example.com")

    @pytest.mark.asyncio
    async def test_not_suppressed_by_default(self, engine):
        assert not await engine.is_suppressed("new@example.com")

    @pytest.mark.asyncio
    async def test_suppressed_email_blocks_send(self, engine):
        await engine.add_suppression("blocked@example.com", "unsubscribe")
        can_send = await engine.can_send_to("blocked@example.com")
        assert not can_send

    @pytest.mark.asyncio
    async def test_unsuppressed_email_allows_send(self, engine):
        can_send = await engine.can_send_to("allowed@example.com")
        assert can_send


class TestRightToErasure:
    """Tests for GDPR right to erasure."""

    @pytest.mark.asyncio
    async def test_erase_by_email(self, engine, db):
        """Right to erasure should delete all data for an email."""
        # Insert test lead
        async with db.connection() as conn:
            await conn.execute(
                "INSERT INTO leads (business_name, town, source, email) VALUES (?, ?, ?, ?)",
                ("Test Biz", "London", "manual", "erase@example.com"),
            )
            await conn.commit()

        result = await engine.erase_by_email("erase@example.com")
        assert result["erased"] is True

        # Verify lead data cleared
        async with db.connection() as conn:
            cursor = await conn.execute(
                "SELECT email, owner_name, phone FROM leads WHERE email = ?",
                ("erase@example.com",),
            )
            row = await cursor.fetchone()
            # Should be deleted or anonymised
            assert row is None or row[0] is None

    @pytest.mark.asyncio
    async def test_erase_logs_consent_event(self, engine):
        await engine.erase_by_email("erase@example.com")
        # Should log the erasure
        logs = await engine.get_consent_log("erase@example.com")
        assert any(log["action"] == "erasure" for log in logs)


class TestConsentTracking:
    """Tests for consent/audit trail."""

    @pytest.mark.asyncio
    async def test_log_consent_event(self, engine):
        await engine.log_consent("user@example.com", "opt_in", source="website_form")
        logs = await engine.get_consent_log("user@example.com")
        assert len(logs) >= 1
        assert logs[0]["action"] == "opt_in"

    @pytest.mark.asyncio
    async def test_consent_log_searchable_by_email(self, engine):
        await engine.log_consent("a@example.com", "opt_in")
        await engine.log_consent("b@example.com", "opt_in")
        logs_a = await engine.get_consent_log("a@example.com")
        logs_b = await engine.get_consent_log("b@example.com")
        assert all(log["email"] == "a@example.com" for log in logs_a)
        assert all(log["email"] == "b@example.com" for log in logs_b)
