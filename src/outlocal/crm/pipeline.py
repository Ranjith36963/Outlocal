"""Lead pipeline and CRM tracking for OUTLOCAL.

Tracks lead status transitions, activity logs, and pipeline views.
"""

import logging
from typing import Any

from src.outlocal.core.database import Database
from src.outlocal.core.models import LeadStatus

logger = logging.getLogger(__name__)


class LeadPipeline:
    """Lead pipeline with status tracking and activity log."""

    def __init__(self, db: Database) -> None:
        self._db = db

    async def get_lead(self, lead_id: int) -> dict[str, Any] | None:
        """Get a single lead by ID."""
        async with self._db.connection() as conn:
            cursor = await conn.execute(
                "SELECT id, business_name, owner_name, email, phone, website, "
                "town, source, score, status, created_at, updated_at "
                "FROM leads WHERE id = ?",
                (lead_id,),
            )
            row = await cursor.fetchone()
            if row is None:
                return None
            return {
                "id": row[0],
                "business_name": row[1],
                "owner_name": row[2],
                "email": row[3],
                "phone": row[4],
                "website": row[5],
                "town": row[6],
                "source": row[7],
                "score": row[8],
                "status": row[9],
                "created_at": row[10],
                "updated_at": row[11],
            }

    async def update_status(self, lead_id: int, new_status: LeadStatus) -> None:
        """Update a lead's status and log the transition."""
        async with self._db.connection() as conn:
            await conn.execute(
                "UPDATE leads SET status = ?, updated_at = datetime('now') WHERE id = ?",
                (new_status.value, lead_id),
            )
            await conn.commit()

        await self.log_activity(
            lead_id,
            "status_change",
            details=f"Status changed to {new_status.value}",
        )

    async def log_activity(
        self,
        lead_id: int,
        action: str,
        details: str | None = None,
    ) -> None:
        """Log an activity event for a lead."""
        async with self._db.connection() as conn:
            await conn.execute(
                "INSERT INTO audit_log (entity_type, entity_id, action, details) "
                "VALUES (?, ?, ?, ?)",
                ("lead", lead_id, action, details),
            )
            await conn.commit()

    async def get_activity_log(self, lead_id: int) -> list[dict[str, Any]]:
        """Get activity log for a lead."""
        async with self._db.connection() as conn:
            cursor = await conn.execute(
                "SELECT action, details, timestamp FROM audit_log "
                "WHERE entity_type = 'lead' AND entity_id = ? ORDER BY timestamp DESC",
                (lead_id,),
            )
            rows = await cursor.fetchall()
            return [
                {"action": row[0], "details": row[1], "timestamp": row[2]}
                for row in rows
            ]

    async def get_pipeline_counts(self) -> dict[str, int]:
        """Get count of leads in each status."""
        async with self._db.connection() as conn:
            cursor = await conn.execute(
                "SELECT status, COUNT(*) FROM leads GROUP BY status"
            )
            rows = await cursor.fetchall()
            return {row[0]: row[1] for row in rows}

    async def filter_leads(
        self,
        status: str | None = None,
        town: str | None = None,
        min_score: int | None = None,
        max_score: int | None = None,
        campaign_id: int | None = None,
        limit: int = 100,
        offset: int = 0,
    ) -> list[dict[str, Any]]:
        """Filter leads by criteria."""
        conditions: list[str] = []
        params: list[Any] = []

        if status:
            conditions.append("status = ?")
            params.append(status)
        if town:
            conditions.append("town = ?")
            params.append(town)
        if min_score is not None:
            conditions.append("score >= ?")
            params.append(min_score)
        if max_score is not None:
            conditions.append("score <= ?")
            params.append(max_score)

        where_clause = " AND ".join(conditions) if conditions else "1=1"
        query = (
            f"SELECT id, business_name, owner_name, email, phone, website, "
            f"town, source, score, status, created_at, updated_at "
            f"FROM leads WHERE {where_clause} "
            f"ORDER BY created_at DESC LIMIT ? OFFSET ?"
        )
        params.extend([limit, offset])

        async with self._db.connection() as conn:
            cursor = await conn.execute(query, params)
            rows = await cursor.fetchall()
            return [
                {
                    "id": row[0],
                    "business_name": row[1],
                    "owner_name": row[2],
                    "email": row[3],
                    "phone": row[4],
                    "website": row[5],
                    "town": row[6],
                    "source": row[7],
                    "score": row[8],
                    "status": row[9],
                    "created_at": row[10],
                    "updated_at": row[11],
                }
                for row in rows
            ]
