"""Tests for reply classification (F014)."""

import pytest
from unittest.mock import AsyncMock, patch

from src.outlocal.classifier.reply_classifier import ReplyClassifier


@pytest.fixture
def classifier():
    providers = [{
        "name": "groq", "base_url": "x", "api_key": "test",
        "model": "test", "daily_limit": 100, "rpm": 30,
    }]
    return ReplyClassifier(providers)


class TestReplyClassifier:
    """Tests for LLM-based reply classification."""

    @pytest.mark.asyncio
    async def test_classify_interested(self, classifier):
        with patch.object(classifier._engine, "_call_provider", new_callable=AsyncMock, return_value="INTERESTED"):
            result = await classifier.classify("Yes, I'd love to hear more about your services!")
        assert result.classification == "INTERESTED"

    @pytest.mark.asyncio
    async def test_classify_not_interested(self, classifier):
        with patch.object(classifier._engine, "_call_provider", new_callable=AsyncMock, return_value="NOT_INTERESTED"):
            result = await classifier.classify("No thanks, we're not interested at this time.")
        assert result.classification == "NOT_INTERESTED"

    @pytest.mark.asyncio
    async def test_classify_out_of_office(self, classifier):
        with patch.object(classifier._engine, "_call_provider", new_callable=AsyncMock, return_value="OUT_OF_OFFICE"):
            result = await classifier.classify("I'm out of office until January 5th.")
        assert result.classification == "OUT_OF_OFFICE"

    @pytest.mark.asyncio
    async def test_classify_unsubscribe(self, classifier):
        with patch.object(classifier._engine, "_call_provider", new_callable=AsyncMock, return_value="UNSUBSCRIBE"):
            result = await classifier.classify("Please remove me from your mailing list.")
        assert result.classification == "UNSUBSCRIBE"

    @pytest.mark.asyncio
    async def test_classify_wrong_person(self, classifier):
        with patch.object(classifier._engine, "_call_provider", new_callable=AsyncMock, return_value="WRONG_PERSON"):
            result = await classifier.classify("I think you've got the wrong person, I don't own this business.")
        assert result.classification == "WRONG_PERSON"

    @pytest.mark.asyncio
    async def test_unsubscribe_triggers_flag(self, classifier):
        with patch.object(classifier._engine, "_call_provider", new_callable=AsyncMock, return_value="UNSUBSCRIBE"):
            result = await classifier.classify("Remove me please.")
        assert result.should_suppress is True

    @pytest.mark.asyncio
    async def test_interested_flags_attention(self, classifier):
        with patch.object(classifier._engine, "_call_provider", new_callable=AsyncMock, return_value="INTERESTED"):
            result = await classifier.classify("Yes, let's talk!")
        assert result.needs_attention is True

    @pytest.mark.asyncio
    async def test_fallback_on_engine_exhausted(self, classifier):
        classifier._engine._daily_counts["groq"] = 100
        result = await classifier.classify("Some reply")
        assert result.classification == "UNCLASSIFIED"
