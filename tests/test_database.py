"""Tests for database initialisation and table schema (F001)."""

import pytest
from src.outlocal.core.database import Database


@pytest.fixture
async def db(tmp_path):
    """Create a temporary database for testing."""
    db_path = str(tmp_path / "test.db")
    database = Database(db_path)
    await database.init_db()
    yield database
    await database.close()


class TestDatabaseInit:
    """Tests for database initialisation."""

    @pytest.mark.asyncio
    async def test_database_creates_tables(self, db):
        """All required tables should exist after init."""
        async with db.connection() as conn:
            cursor = await conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
            )
            tables = [row[0] for row in await cursor.fetchall()]

        assert "leads" in tables
        assert "campaigns" in tables
        assert "emails" in tables
        assert "replies" in tables
        assert "audit_log" in tables

    @pytest.mark.asyncio
    async def test_leads_table_schema(self, db):
        """Leads table should have all required columns."""
        async with db.connection() as conn:
            cursor = await conn.execute("PRAGMA table_info(leads)")
            columns = {row[1]: row[2] for row in await cursor.fetchall()}

        assert "id" in columns
        assert "business_name" in columns
        assert "owner_name" in columns
        assert "email" in columns
        assert "phone" in columns
        assert "website" in columns
        assert "town" in columns
        assert "source" in columns
        assert "score" in columns
        assert "status" in columns
        assert "created_at" in columns
        assert "updated_at" in columns

    @pytest.mark.asyncio
    async def test_campaigns_table_schema(self, db):
        """Campaigns table should have all required columns."""
        async with db.connection() as conn:
            cursor = await conn.execute("PRAGMA table_info(campaigns)")
            columns = {row[1]: row[2] for row in await cursor.fetchall()}

        assert "id" in columns
        assert "name" in columns
        assert "status" in columns
        assert "template" in columns
        assert "target_criteria" in columns
        assert "created_at" in columns

    @pytest.mark.asyncio
    async def test_emails_table_schema(self, db):
        """Emails table should have all required columns."""
        async with db.connection() as conn:
            cursor = await conn.execute("PRAGMA table_info(emails)")
            columns = {row[1]: row[2] for row in await cursor.fetchall()}

        assert "id" in columns
        assert "lead_id" in columns
        assert "campaign_id" in columns
        assert "subject" in columns
        assert "body" in columns
        assert "provider" in columns
        assert "status" in columns
        assert "sent_at" in columns
        assert "opened_at" in columns
        assert "clicked_at" in columns

    @pytest.mark.asyncio
    async def test_replies_table_schema(self, db):
        """Replies table should have all required columns."""
        async with db.connection() as conn:
            cursor = await conn.execute("PRAGMA table_info(replies)")
            columns = {row[1]: row[2] for row in await cursor.fetchall()}

        assert "id" in columns
        assert "email_id" in columns
        assert "raw_text" in columns
        assert "classification" in columns
        assert "classified_at" in columns

    @pytest.mark.asyncio
    async def test_audit_log_table_schema(self, db):
        """Audit log table should have required columns."""
        async with db.connection() as conn:
            cursor = await conn.execute("PRAGMA table_info(audit_log)")
            columns = {row[1]: row[2] for row in await cursor.fetchall()}

        assert "id" in columns
        assert "entity_type" in columns
        assert "entity_id" in columns
        assert "action" in columns
        assert "timestamp" in columns

    @pytest.mark.asyncio
    async def test_database_idempotent_init(self, db):
        """Calling init_db() twice should not raise errors."""
        await db.init_db()  # Second call should be safe

    @pytest.mark.asyncio
    async def test_database_connection_context_manager(self, db):
        """Connection context manager should work correctly."""
        async with db.connection() as conn:
            assert conn is not None
            cursor = await conn.execute("SELECT 1")
            result = await cursor.fetchone()
            assert result[0] == 1
