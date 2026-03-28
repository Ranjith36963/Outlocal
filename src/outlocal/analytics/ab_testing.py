"""A/B testing for email subject lines and body variants.

Splits leads into groups, tracks performance per variant,
and auto-selects winners after reaching statistical significance.
"""

import json
import logging
import random
from typing import Any

from src.outlocal.core.database import Database

logger = logging.getLogger(__name__)

# Minimum sample size before declaring a winner
MIN_SAMPLE_SIZE = 20


class ABTestManager:
    """Manage A/B tests for email campaigns."""

    def __init__(self, db: Database) -> None:
        self._db = db

    async def create_test(
        self,
        campaign_id: int,
        variant_a: dict[str, str],
        variant_b: dict[str, str],
    ) -> int:
        """Create an A/B test with two variants.

        variant_a/b: dict with 'subject' and/or 'body' keys.
        """
        async with self._db.connection() as conn:
            cursor = await conn.execute(
                "INSERT INTO ab_tests (campaign_id, variant_a, variant_b, status) "
                "VALUES (?, ?, ?, ?)",
                (campaign_id, json.dumps(variant_a), json.dumps(variant_b), "active"),
            )
            await conn.commit()
            return cursor.lastrowid

    async def assign_variant(self, test_id: int, lead_id: int) -> str:
        """Randomly assign a lead to variant A or B. Returns 'A' or 'B'."""
        variant = random.choice(["A", "B"])
        async with self._db.connection() as conn:
            await conn.execute(
                "INSERT INTO ab_assignments (test_id, lead_id, variant) VALUES (?, ?, ?)",
                (test_id, lead_id, variant),
            )
            await conn.commit()
        return variant

    async def get_results(self, test_id: int) -> dict[str, Any]:
        """Get A/B test results with per-variant metrics."""
        async with self._db.connection() as conn:
            # Get test info
            cursor = await conn.execute(
                "SELECT campaign_id, variant_a, variant_b, status FROM ab_tests WHERE id = ?",
                (test_id,),
            )
            test = await cursor.fetchone()
            if not test:
                return {"error": "Test not found"}

            results: dict[str, Any] = {"test_id": test_id, "status": test[3]}

            for variant in ["A", "B"]:
                cursor = await conn.execute(
                    "SELECT COUNT(*) FROM ab_assignments WHERE test_id = ? AND variant = ?",
                    (test_id, variant),
                )
                total = (await cursor.fetchone())[0]

                cursor = await conn.execute(
                    "SELECT COUNT(*) FROM ab_assignments a "
                    "JOIN emails e ON a.lead_id = e.lead_id "
                    "WHERE a.test_id = ? AND a.variant = ? AND e.opened_at IS NOT NULL",
                    (test_id, variant),
                )
                opened = (await cursor.fetchone())[0]

                cursor = await conn.execute(
                    "SELECT COUNT(DISTINCT r.email_id) FROM ab_assignments a "
                    "JOIN emails e ON a.lead_id = e.lead_id "
                    "JOIN replies r ON r.email_id = e.id "
                    "WHERE a.test_id = ? AND a.variant = ?",
                    (test_id, variant),
                )
                replied = (await cursor.fetchone())[0]

                results[f"variant_{variant.lower()}"] = {
                    "total": total,
                    "opened": opened,
                    "replied": replied,
                    "open_rate": round(opened / total * 100, 1) if total > 0 else 0,
                    "reply_rate": round(replied / total * 100, 1) if total > 0 else 0,
                }

            # Auto-select winner if sample size met
            a = results["variant_a"]
            b = results["variant_b"]
            if a["total"] >= MIN_SAMPLE_SIZE and b["total"] >= MIN_SAMPLE_SIZE:
                if a["open_rate"] > b["open_rate"] + 5:  # 5% significance threshold
                    results["winner"] = "A"
                elif b["open_rate"] > a["open_rate"] + 5:
                    results["winner"] = "B"
                else:
                    results["winner"] = "tie"
            else:
                results["winner"] = "insufficient_data"

            return results
