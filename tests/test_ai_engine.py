"""Tests for FreeAIEngine with multi-provider failover (F008)."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from src.outlocal.ai_engine.engine import FreeAIEngine


@pytest.fixture
def engine():
    """Create FreeAIEngine with test provider configs."""
    providers = [
        {
            "name": "groq",
            "base_url": "https://api.groq.com/openai/v1",
            "api_key": "gsk_test",
            "model": "llama-3.3-70b-versatile",
            "daily_limit": 3,
            "rpm": 30,
        },
        {
            "name": "openrouter",
            "base_url": "https://openrouter.ai/api/v1",
            "api_key": "sk-or-test",
            "model": "meta-llama/llama-3.3-70b-instruct:free",
            "daily_limit": 2,
            "rpm": 20,
        },
        {
            "name": "gemini",
            "base_url": "https://generativelanguage.googleapis.com/v1beta/openai/",
            "api_key": "AIza_test",
            "model": "gemini-2.5-flash",
            "daily_limit": 2,
            "rpm": 10,
        },
    ]
    return FreeAIEngine(providers)


def _mock_completion(text: str = "SUBJECT: Test Subject\nBODY: Test email body"):
    """Create a mock OpenAI chat completion response."""
    mock_choice = MagicMock()
    mock_choice.message.content = text
    mock_response = MagicMock()
    mock_response.choices = [mock_choice]
    return mock_response


class TestFreeAIEngineInit:
    """Tests for engine initialization."""

    def test_engine_initialises_with_providers(self, engine):
        assert len(engine._providers) == 3

    def test_engine_tracks_daily_counts(self, engine):
        assert engine._daily_counts["groq"] == 0
        assert engine._daily_counts["openrouter"] == 0
        assert engine._daily_counts["gemini"] == 0

    def test_engine_skips_providers_without_keys(self):
        providers = [
            {
                "name": "groq",
                "base_url": "x",
                "api_key": None,
                "model": "x",
                "daily_limit": 10,
                "rpm": 5,
            },
            {
                "name": "gemini",
                "base_url": "x",
                "api_key": "key",
                "model": "x",
                "daily_limit": 10,
                "rpm": 5,
            },
        ]
        engine = FreeAIEngine(providers)
        available = engine._get_available_provider()
        assert available["name"] == "gemini"


class TestEmailGeneration:
    """Tests for email generation."""

    @pytest.mark.asyncio
    async def test_generate_email_returns_subject_and_body(self, engine):
        with patch.object(engine, "_call_provider", new_callable=AsyncMock) as mock_call:
            mock_call.return_value = (
                "SUBJECT: Website Fix for Joe's\nBODY: Hi Joe, noticed your site..."
            )
            result = await engine.generate_email(
                business_name="Joe's Fish & Chips",
                owner_name="Joe",
                town="Bristol",
                pain_point="No SSL certificate",
                service="web development",
            )

        assert "subject" in result
        assert "body" in result
        assert result["subject"] == "Website Fix for Joe's"
        assert "Joe" in result["body"]

    @pytest.mark.asyncio
    async def test_generate_email_returns_provider_info(self, engine):
        with patch.object(engine, "_call_provider", new_callable=AsyncMock) as mock_call:
            mock_call.return_value = "SUBJECT: Test\nBODY: Body"
            result = await engine.generate_email(
                business_name="Test Biz",
                owner_name="Owner",
                town="London",
                pain_point="Slow website",
                service="optimisation",
            )

        assert "provider" in result
        assert "model" in result
        assert result["cost"] == 0.00

    @pytest.mark.asyncio
    async def test_generate_email_increments_daily_count(self, engine):
        with patch.object(engine, "_call_provider", new_callable=AsyncMock) as mock_call:
            mock_call.return_value = "SUBJECT: Test\nBODY: Body"
            await engine.generate_email("Biz", "Owner", "Town", "Issue", "Service")

        assert engine._daily_counts["groq"] == 1


class TestProviderFailover:
    """Tests for provider failover mechanism."""

    @pytest.mark.asyncio
    async def test_failover_to_next_provider_on_limit(self, engine):
        # Exhaust groq
        engine._daily_counts["groq"] = 3
        provider = engine._get_available_provider()
        assert provider["name"] == "openrouter"

    @pytest.mark.asyncio
    async def test_failover_to_third_provider(self, engine):
        engine._daily_counts["groq"] = 3
        engine._daily_counts["openrouter"] = 2
        provider = engine._get_available_provider()
        assert provider["name"] == "gemini"

    @pytest.mark.asyncio
    async def test_all_exhausted_returns_none(self, engine):
        engine._daily_counts["groq"] = 3
        engine._daily_counts["openrouter"] = 2
        engine._daily_counts["gemini"] = 2
        provider = engine._get_available_provider()
        assert provider is None

    @pytest.mark.asyncio
    async def test_generate_email_returns_error_when_exhausted(self, engine):
        engine._daily_counts["groq"] = 3
        engine._daily_counts["openrouter"] = 2
        engine._daily_counts["gemini"] = 2
        result = await engine.generate_email("Biz", "Owner", "Town", "Issue", "Service")
        assert "error" in result

    @pytest.mark.asyncio
    async def test_failover_on_api_error(self, engine):
        call_count = 0

        async def mock_call(provider, messages, max_tokens=300, temperature=0.7):
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                raise Exception("API Error")
            return "SUBJECT: Fallback\nBODY: Fallback body"

        with patch.object(engine, "_call_provider", side_effect=mock_call):
            result = await engine.generate_email("Biz", "Owner", "Town", "Issue", "Service")

        assert result["subject"] == "Fallback"
        assert call_count == 2


class TestReplyClassification:
    """Tests for reply classification."""

    @pytest.mark.asyncio
    async def test_classify_reply_returns_category(self, engine):
        with patch.object(engine, "_call_provider", new_callable=AsyncMock) as mock_call:
            mock_call.return_value = "INTERESTED"
            result = await engine.classify_reply("Yes, I'd love to hear more!")

        assert result == "INTERESTED"

    @pytest.mark.asyncio
    async def test_classify_reply_when_exhausted(self, engine):
        engine._daily_counts["groq"] = 3
        engine._daily_counts["openrouter"] = 2
        engine._daily_counts["gemini"] = 2
        result = await engine.classify_reply("Some reply text")
        assert result == "UNCLASSIFIED"


class TestDailyReset:
    """Tests for daily counter reset."""

    def test_reset_daily_counts(self, engine):
        engine._daily_counts["groq"] = 100
        engine._daily_counts["openrouter"] = 50
        engine.reset_daily_counts()
        assert engine._daily_counts["groq"] == 0
        assert engine._daily_counts["openrouter"] == 0
        assert engine._daily_counts["gemini"] == 0
