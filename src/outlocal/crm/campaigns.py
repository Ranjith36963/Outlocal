"""Campaign management for OUTLOCAL.

Handles campaign CRUD, lead assignment, and batch operations.
"""

import json
import logging
from typing import Any

from src.outlocal.core.database import Database
from src.outlocal.core.models import CampaignStatus

logger = logging.getLogger(__name__)


class CampaignManager:
    """Manage campaigns with target criteria and batch operations."""

    def __init__(self, db: Database) -> None:
        self._db = db

    async def create_campaign(
        self,
        name: str,
        target_criteria: dict[str, Any],
        template: str | None = None,
    ) -> int:
        """Create a new campaign. Returns campaign ID."""
        async with self._db.connection() as conn:
            cursor = await conn.execute(
                "INSERT INTO campaigns (name, target_criteria, template) VALUES (?, ?, ?)",
                (name, json.dumps(target_criteria), template),
            )
            await conn.commit()
            return cursor.lastrowid or 0

    async def get_campaign(self, campaign_id: int) -> dict[str, Any] | None:
        """Get campaign by ID."""
        async with self._db.connection() as conn:
            cursor = await conn.execute(
                "SELECT id, name, status, template, target_criteria, created_at "
                "FROM campaigns WHERE id = ?",
                (campaign_id,),
            )
            row = await cursor.fetchone()
            if row is None:
                return None
            return {
                "id": row[0],
                "name": row[1],
                "status": row[2],
                "template": row[3],
                "target_criteria": json.loads(row[4]) if row[4] else {},
                "created_at": row[5],
            }

    async def list_campaigns(self) -> list[dict[str, Any]]:
        """List all campaigns."""
        async with self._db.connection() as conn:
            cursor = await conn.execute(
                "SELECT id, name, status, template, target_criteria, created_at "
                "FROM campaigns ORDER BY created_at DESC"
            )
            rows = await cursor.fetchall()
            return [
                {
                    "id": row[0],
                    "name": row[1],
                    "status": row[2],
                    "template": row[3],
                    "target_criteria": json.loads(row[4]) if row[4] else {},
                    "created_at": row[5],
                }
                for row in rows
            ]

    async def update_status(self, campaign_id: int, status: CampaignStatus) -> None:
        """Update campaign status."""
        async with self._db.connection() as conn:
            await conn.execute(
                "UPDATE campaigns SET status = ? WHERE id = ?",
                (status.value, campaign_id),
            )
            await conn.commit()

    async def get_campaign_stats(self, campaign_id: int) -> dict[str, int]:
        """Get campaign statistics."""
        async with self._db.connection() as conn:
            cursor = await conn.execute(
                "SELECT status, COUNT(*) FROM emails WHERE campaign_id = ? GROUP BY status",
                (campaign_id,),
            )
            rows = await cursor.fetchall()
            stats = {row[0]: row[1] for row in rows}

            # Count replies
            cursor = await conn.execute(
                "SELECT r.classification, COUNT(*) FROM replies r "
                "JOIN emails e ON r.email_id = e.id "
                "WHERE e.campaign_id = ? GROUP BY r.classification",
                (campaign_id,),
            )
            reply_rows = await cursor.fetchall()
            for row in reply_rows:
                stats[f"reply_{row[0]}"] = row[1]

            return stats

    async def assign_leads(self, campaign_id: int, criteria: dict[str, Any]) -> list[int]:
        """Find leads matching criteria and return their IDs."""
        conditions: list[str] = []
        params: list[Any] = []

        if "town" in criteria:
            conditions.append("town = ?")
            params.append(criteria["town"])
        if "min_score" in criteria:
            conditions.append("score >= ?")
            params.append(criteria["min_score"])
        if "status" in criteria:
            conditions.append("status = ?")
            params.append(criteria["status"])

        where = " AND ".join(conditions) if conditions else "1=1"

        async with self._db.connection() as conn:
            cursor = await conn.execute(f"SELECT id FROM leads WHERE {where}", params)
            rows = await cursor.fetchall()
            return [row[0] for row in rows]
