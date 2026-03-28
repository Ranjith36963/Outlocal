"""Follow-up sequence engine for OUTLOCAL.

Manages automated follow-up email sequences with configurable
timing and conditions. Skips leads that replied or unsubscribed.
"""

import logging
from dataclasses import dataclass
from datetime import datetime, timezone, timedelta
from typing import Any

from src.outlocal.core.database import Database

logger = logging.getLogger(__name__)

# Statuses that should NOT receive follow-ups
_SKIP_STATUSES = frozenset({
    "replied", "interested", "converted", "lost", "unsubscribed",
})


@dataclass
class FollowUpStep:
    """A step in a follow-up sequence."""

    delay_days: int
    condition: str = "no_reply"  # "no_reply" or "no_open"
    max_followups: int = 3


class FollowUpEngine:
    """Manages follow-up sequences for sent emails."""

    def __init__(self, db: Database) -> None:
        self._db = db

    def default_sequence(self) -> list[FollowUpStep]:
        """Default follow-up sequence: 3 follow-ups at day 3, 7, 14."""
        return [
            FollowUpStep(delay_days=3, condition="no_reply"),
            FollowUpStep(delay_days=7, condition="no_reply"),
            FollowUpStep(delay_days=14, condition="no_reply"),
        ]

    async def find_due_followups(
        self,
        sequence: list[FollowUpStep] | None = None,
    ) -> list[dict[str, Any]]:
        """Find emails that are due for follow-up.

        Returns list of dicts with email_id, lead_id, lead_email,
        followup_number, and original subject/body.
        """
        if sequence is None:
            sequence = self.default_sequence()

        due: list[dict[str, Any]] = []

        async with self._db.connection() as conn:
            # Get sent emails with leads that haven't replied/unsubscribed
            cursor = await conn.execute(
                "SELECT e.id, e.lead_id, e.subject, e.body, e.sent_at, e.campaign_id, "
                "l.email, l.status, l.business_name "
                "FROM emails e "
                "JOIN leads l ON e.lead_id = l.id "
                "WHERE e.status = 'sent' AND l.status NOT IN "
                f"({','.join('?' for _ in _SKIP_STATUSES)})",
                tuple(_SKIP_STATUSES),
            )
            emails = await cursor.fetchall()

            for row in emails:
                email_id = row[0]
                lead_id = row[1]
                sent_at_str = row[4]
                lead_status = row[7]

                if not sent_at_str:
                    continue

                sent_at = datetime.fromisoformat(sent_at_str)
                if sent_at.tzinfo is None:
                    sent_at = sent_at.replace(tzinfo=timezone.utc)
                now = datetime.now(timezone.utc)

                # Check how many follow-ups already sent
                followup_count = await self.count_followups_for_email(email_id)

                # Find the next step in the sequence
                if followup_count >= len(sequence):
                    continue  # All follow-ups sent

                step = sequence[followup_count]
                days_since_sent = (now - sent_at).days

                if days_since_sent >= step.delay_days:
                    # Check no reply exists
                    reply_cursor = await conn.execute(
                        "SELECT 1 FROM replies WHERE email_id = ? LIMIT 1",
                        (email_id,),
                    )
                    has_reply = await reply_cursor.fetchone() is not None
                    if has_reply:
                        continue

                    due.append({
                        "email_id": email_id,
                        "lead_id": lead_id,
                        "lead_email": row[6],
                        "business_name": row[8],
                        "original_subject": row[2],
                        "original_body": row[3],
                        "campaign_id": row[5],
                        "followup_number": followup_count + 1,
                    })

        return due

    async def count_followups_for_email(self, email_id: int) -> int:
        """Count follow-up emails already sent for a given original email."""
        async with self._db.connection() as conn:
            cursor = await conn.execute(
                "SELECT COUNT(*) FROM emails WHERE lead_id = ("
                "  SELECT lead_id FROM emails WHERE id = ?"
                ") AND id > ? AND status IN ('sent', 'pending')",
                (email_id, email_id),
            )
            row = await cursor.fetchone()
            return row[0] if row else 0
