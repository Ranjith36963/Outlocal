"""Email template system with AI personalisation.

Derives pain points from enrichment data and generates
personalised cold emails via FreeAIEngine.
"""

from typing import Any

from src.outlocal.ai_engine.engine import FreeAIEngine


class EmailTemplateEngine:
    """Generate personalised cold emails using AI and enrichment data."""

    def __init__(self, providers: list[dict[str, Any]]) -> None:
        self._engine = FreeAIEngine(providers)

    def derive_pain_points(self, enrichment_data: dict[str, Any]) -> list[str]:
        """Derive pain points from website crawl and business data.

        Returns list of pain point strings suitable for email personalisation.
        """
        pain_points: list[str] = []

        if enrichment_data.get("website") is None:
            pain_points.append("No website found — missing out on online customers")

        if enrichment_data.get("website_has_ssl") is False:
            pain_points.append("Website lacks SSL certificate — browsers show 'Not Secure' warning")

        if enrichment_data.get("website_is_mobile_friendly") is False:
            pain_points.append("Website not mobile-friendly — losing mobile visitors")

        rating = enrichment_data.get("rating")
        review_count = enrichment_data.get("review_count", 0)
        if rating is not None and rating < 3.5:
            pain_points.append(
                f"Google rating is {rating}/5 with {review_count} reviews — "
                "could benefit from a review management strategy"
            )

        if not enrichment_data.get("has_social_media"):
            pain_points.append("No social media presence detected")

        if not pain_points:
            pain_points.append("Website could be improved to attract more local customers")

        return pain_points

    async def generate(
        self,
        business_name: str,
        owner_name: str | None,
        town: str,
        pain_point: str,
        service: str,
    ) -> dict[str, Any]:
        """Generate a personalised cold email.

        Uses FreeAIEngine with provider failover.
        Returns dict with subject, body, provider, model, cost.
        """
        return await self._engine.generate_email(
            business_name=business_name,
            owner_name=owner_name,
            town=town,
            pain_point=pain_point,
            service=service,
        )
