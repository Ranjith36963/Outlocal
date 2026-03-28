"""Lead scoring engine for OUTLOCAL.

Rule-based scoring: 0-100 based on contact completeness,
website quality, and business signals.
"""

from typing import Any


class LeadScorer:
    """Score leads based on configurable rule-based criteria."""

    def score(self, lead_data: dict[str, Any]) -> dict[str, Any]:
        """Score a lead 0-100 with component breakdown.

        Args:
            lead_data: Dict with lead fields and enrichment signals.

        Returns:
            Dict with 'score' (int 0-100) and 'breakdown' (component scores).
        """
        breakdown: dict[str, int] = {}

        # Contact signals (max 35 points)
        contact_score = 0
        if lead_data.get("email"):
            contact_score += 15
        if lead_data.get("phone"):
            contact_score += 10
        if lead_data.get("owner_name"):
            contact_score += 5
        if lead_data.get("website"):
            contact_score += 5
        breakdown["contact"] = contact_score

        # Website quality signals (max 25 points)
        website_score = 0
        if lead_data.get("website"):
            website_score += 5  # Has a website at all
            if lead_data.get("website_has_ssl"):
                website_score += 10
            if lead_data.get("website_is_mobile_friendly"):
                website_score += 10
        breakdown["website"] = website_score

        # Business signals (max 30 points)
        business_score = 0
        rating = lead_data.get("rating")
        if rating is not None:
            if rating >= 4.0:
                business_score += 15
            elif rating >= 3.0:
                business_score += 8
            elif rating < 2.0:
                business_score -= 5

        review_count = lead_data.get("review_count", 0)
        if review_count >= 50:
            business_score += 10
        elif review_count >= 10:
            business_score += 5
        elif review_count >= 1:
            business_score += 2

        if lead_data.get("has_social_media"):
            business_score += 5

        breakdown["business"] = max(0, business_score)

        # Base score (every lead gets 10 for existing)
        breakdown["base"] = 10

        # Calculate total, clamp 0-100
        total = sum(breakdown.values())
        total = max(0, min(100, total))

        return {
            "score": total,
            "breakdown": breakdown,
        }
