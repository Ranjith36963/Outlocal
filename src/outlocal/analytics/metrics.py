"""Campaign analytics and metrics for OUTLOCAL.

Calculates open rates, click rates, reply rates, conversion rates,
and per-campaign breakdowns.
"""

import logging
from typing import Any

from src.outlocal.core.database import Database

logger = logging.getLogger(__name__)


class CampaignAnalytics:
    """Calculate campaign performance metrics."""

    def __init__(self, db: Database) -> None:
        self._db = db

    async def get_campaign_metrics(self, campaign_id: int) -> dict[str, Any]:
        """Get full metrics for a campaign."""
        async with self._db.connection() as conn:
            # Total sent
            cursor = await conn.execute(
                "SELECT COUNT(*) FROM emails WHERE campaign_id = ? AND status = 'sent'",
                (campaign_id,),
            )
            row = await cursor.fetchone()
            total_sent = row[0] if row else 0

            # Opens
            cursor = await conn.execute(
                "SELECT COUNT(*) FROM emails WHERE campaign_id = ? AND opened_at IS NOT NULL",
                (campaign_id,),
            )
            row = await cursor.fetchone()
            total_opened = row[0] if row else 0

            # Clicks
            cursor = await conn.execute(
                "SELECT COUNT(*) FROM emails WHERE campaign_id = ? AND clicked_at IS NOT NULL",
                (campaign_id,),
            )
            row = await cursor.fetchone()
            total_clicked = row[0] if row else 0

            # Replies
            cursor = await conn.execute(
                "SELECT COUNT(DISTINCT r.email_id) FROM replies r "
                "JOIN emails e ON r.email_id = e.id "
                "WHERE e.campaign_id = ?",
                (campaign_id,),
            )
            row = await cursor.fetchone()
            total_replied = row[0] if row else 0

            # Interested (from classification)
            cursor = await conn.execute(
                "SELECT COUNT(*) FROM replies r "
                "JOIN emails e ON r.email_id = e.id "
                "WHERE e.campaign_id = ? AND r.classification = 'interested'",
                (campaign_id,),
            )
            row = await cursor.fetchone()
            total_interested = row[0] if row else 0

        open_rate = (total_opened / total_sent * 100) if total_sent > 0 else 0
        click_rate = (total_clicked / total_sent * 100) if total_sent > 0 else 0
        reply_rate = (total_replied / total_sent * 100) if total_sent > 0 else 0
        conversion_rate = (total_interested / total_sent * 100) if total_sent > 0 else 0

        return {
            "campaign_id": campaign_id,
            "total_sent": total_sent,
            "total_opened": total_opened,
            "total_clicked": total_clicked,
            "total_replied": total_replied,
            "total_interested": total_interested,
            "open_rate": round(open_rate, 1),
            "click_rate": round(click_rate, 1),
            "reply_rate": round(reply_rate, 1),
            "conversion_rate": round(conversion_rate, 1),
        }

    async def get_daily_stats(self, campaign_id: int, days: int = 30) -> list[dict[str, Any]]:
        """Get daily send/open/reply counts for a campaign."""
        async with self._db.connection() as conn:
            cursor = await conn.execute(
                "SELECT date(sent_at) as day, "
                "COUNT(*) as sent, "
                "SUM(CASE WHEN opened_at IS NOT NULL THEN 1 ELSE 0 END) as opened, "
                "SUM(CASE WHEN clicked_at IS NOT NULL THEN 1 ELSE 0 END) as clicked "
                "FROM emails WHERE campaign_id = ? AND sent_at IS NOT NULL "
                "GROUP BY date(sent_at) ORDER BY day DESC LIMIT ?",
                (campaign_id, days),
            )
            rows = await cursor.fetchall()
            return [
                {"day": row[0], "sent": row[1], "opened": row[2], "clicked": row[3]} for row in rows
            ]

    async def get_best_subject_lines(
        self, campaign_id: int, limit: int = 5
    ) -> list[dict[str, Any]]:
        """Get best-performing subject lines by open rate."""
        async with self._db.connection() as conn:
            cursor = await conn.execute(
                "SELECT subject, "
                "COUNT(*) as sent, "
                "SUM(CASE WHEN opened_at IS NOT NULL THEN 1 ELSE 0 END) as opened "
                "FROM emails WHERE campaign_id = ? AND status = 'sent' "
                "GROUP BY subject HAVING sent >= 2 "
                "ORDER BY (CAST(opened AS FLOAT) / sent) DESC LIMIT ?",
                (campaign_id, limit),
            )
            rows = await cursor.fetchall()
            return [
                {
                    "subject": row[0],
                    "sent": row[1],
                    "opened": row[2],
                    "open_rate": round(row[2] / row[1] * 100, 1) if row[1] > 0 else 0,
                }
                for row in rows
            ]
