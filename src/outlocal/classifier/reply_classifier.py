"""Reply classification using free LLM.

Classifies email replies into: INTERESTED, NOT_INTERESTED,
OUT_OF_OFFICE, WRONG_PERSON, UNSUBSCRIBE.
"""

import logging
from dataclasses import dataclass
from typing import Any

from src.outlocal.ai_engine.engine import FreeAIEngine

logger = logging.getLogger(__name__)


@dataclass
class ClassificationResult:
    """Result of classifying an email reply."""

    classification: str
    needs_attention: bool = False
    should_suppress: bool = False


class ReplyClassifier:
    """Classify email replies using FreeAIEngine."""

    def __init__(self, providers: list[dict[str, Any]]) -> None:
        self._engine = FreeAIEngine(providers)

    async def classify(self, reply_text: str) -> ClassificationResult:
        """Classify a reply and return result with action flags.

        INTERESTED → needs_attention=True (human should respond)
        UNSUBSCRIBE → should_suppress=True (add to suppression list)
        """
        classification = await self._engine.classify_reply(reply_text)

        needs_attention = classification == "INTERESTED"
        should_suppress = classification == "UNSUBSCRIBE"

        return ClassificationResult(
            classification=classification,
            needs_attention=needs_attention,
            should_suppress=should_suppress,
        )
