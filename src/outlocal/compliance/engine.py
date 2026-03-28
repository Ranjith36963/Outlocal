"""GDPR and CAN-SPAM compliance engine for OUTLOCAL.

Handles suppression lists, right to erasure, consent tracking,
and audit trails.
"""

import logging
from datetime import datetime, timezone
from typing import Any

from src.outlocal.core.database import Database

logger = logging.getLogger(__name__)


class ComplianceEngine:
    """Compliance engine for GDPR and CAN-SPAM requirements."""

    def __init__(self, db: Database) -> None:
        self._db = db

    async def add_suppression(self, email: str, reason: str) -> None:
        """Add an email to the suppression list.

        Suppressed emails will never receive further outreach.
        """
        async with self._db.connection() as conn:
            await conn.execute(
                "INSERT OR IGNORE INTO suppression_list (email, reason) VALUES (?, ?)",
                (email.lower(), reason),
            )
            await conn.commit()
        await self.log_consent(email, "suppression_added", details=reason)
        logger.info("Added %s to suppression list: %s", email, reason)

    async def is_suppressed(self, email: str) -> bool:
        """Check if an email is on the suppression list."""
        async with self._db.connection() as conn:
            cursor = await conn.execute(
                "SELECT 1 FROM suppression_list WHERE email = ?",
                (email.lower(),),
            )
            return await cursor.fetchone() is not None

    async def can_send_to(self, email: str) -> bool:
        """Check if we can send an email to this address.

        Returns False if the email is suppressed (unsubscribed, bounced, etc.).
        """
        return not await self.is_suppressed(email)

    async def erase_by_email(self, email: str) -> dict[str, Any]:
        """GDPR right to erasure — delete all data for an email.

        Removes lead data, adds to suppression list, logs the erasure.
        """
        async with self._db.connection() as conn:
            # Delete lead records
            await conn.execute(
                "DELETE FROM leads WHERE email = ?",
                (email.lower(),),
            )
            # Add to suppression list to prevent re-scraping
            await conn.execute(
                "INSERT OR IGNORE INTO suppression_list (email, reason) VALUES (?, ?)",
                (email.lower(), "gdpr_erasure"),
            )
            await conn.commit()

        await self.log_consent(email, "erasure", details="GDPR right to erasure exercised")
        logger.info("GDPR erasure completed for %s", email)

        return {"erased": True, "email": email}

    async def log_consent(
        self,
        email: str,
        action: str,
        source: str | None = None,
        details: str | None = None,
    ) -> None:
        """Log a consent event for audit trail."""
        async with self._db.connection() as conn:
            await conn.execute(
                "INSERT INTO consent_log (email, action, source, details) VALUES (?, ?, ?, ?)",
                (email.lower(), action, source, details),
            )
            await conn.commit()

    async def get_consent_log(self, email: str) -> list[dict[str, Any]]:
        """Get all consent events for an email address."""
        async with self._db.connection() as conn:
            cursor = await conn.execute(
                "SELECT email, action, source, details, timestamp "
                "FROM consent_log WHERE email = ? ORDER BY timestamp DESC",
                (email.lower(),),
            )
            rows = await cursor.fetchall()
            return [
                {
                    "email": row[0],
                    "action": row[1],
                    "source": row[2],
                    "details": row[3],
                    "timestamp": row[4],
                }
                for row in rows
            ]
