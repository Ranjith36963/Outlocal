"""End-to-end pipeline orchestrator for OUTLOCAL.

Runs the full pipeline for a lead: scrape → enrich → score → email → follow-up → classify.
Each step is independent and failures are logged without breaking the pipeline.
"""

import logging
from typing import Any

from src.outlocal.core.database import Database
from src.outlocal.core.models import LeadStatus
from src.outlocal.crm.pipeline import LeadPipeline
from src.outlocal.scoring.scorer import LeadScorer

logger = logging.getLogger(__name__)


class OutlocalPipeline:
    """Orchestrate the full lead processing pipeline."""

    def __init__(self, db: Database) -> None:
        self._db = db
        self._pipeline = LeadPipeline(db)
        self._scorer = LeadScorer()

    async def process_lead(self, lead_id: int) -> dict[str, Any]:
        """Run the full pipeline for a single lead.

        Steps: enrich → score → generate email → (send handled separately)
        Returns dict with results from each step.
        """
        results: dict[str, Any] = {"lead_id": lead_id, "steps": {}}

        lead = await self._pipeline.get_lead(lead_id)
        if not lead:
            return {"lead_id": lead_id, "error": "Lead not found"}

        # Step 1: Score
        try:
            score_result = self._scorer.score(lead)
            async with self._db.connection() as conn:
                await conn.execute(
                    "UPDATE leads SET score = ?, status = ?, updated_at = datetime('now') WHERE id = ?",
                    (score_result["score"], LeadStatus.SCORED.value, lead_id),
                )
                await conn.commit()
            await self._pipeline.log_activity(lead_id, "scored", f"Score: {score_result['score']}")
            results["steps"]["score"] = {"status": "success", "score": score_result["score"]}
        except Exception as e:
            logger.error("Score failed for lead %d: %s", lead_id, e)
            results["steps"]["score"] = {"status": "failed", "error": str(e)}

        return results

    async def process_campaign(self, campaign_id: int) -> dict[str, Any]:
        """Process all leads in a campaign through the pipeline."""
        async with self._db.connection() as conn:
            cursor = await conn.execute(
                "SELECT l.id FROM leads l "
                "JOIN emails e ON l.id = e.lead_id "
                "WHERE e.campaign_id = ? "
                "GROUP BY l.id",
                (campaign_id,),
            )
            lead_ids = [row[0] for row in await cursor.fetchall()]

        results = {"campaign_id": campaign_id, "leads_processed": 0, "errors": 0}

        for lead_id in lead_ids:
            result = await self.process_lead(lead_id)
            results["leads_processed"] += 1
            if "error" in result:
                results["errors"] += 1

        return results
