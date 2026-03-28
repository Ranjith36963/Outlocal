"""FreeAIEngine — Multi-provider LLM engine with automatic failover.

Uses free cloud LLM tiers (Groq → OpenRouter → Gemini) via the OpenAI-compatible API.
Zero cost. All providers use the same openai Python SDK.
"""

import logging
from typing import Any

from openai import AsyncOpenAI

logger = logging.getLogger(__name__)

# System prompt for cold email generation — UK-focused, anti-slop
_EMAIL_SYSTEM_PROMPT = """You are a cold email copywriter for a UK digital services company.
Write a cold email under 80 words to a local business owner.
Reference the EXACT website issue provided. Be helpful, not salesy.
Subject line under 60 characters, mention business name or town.
Tone: friendly local expert. UK English spelling.
End with ONE clear CTA: book a 15-min call OR reply "YES".
Do NOT use: "I hope this finds you well", "delve", "leverage",
"digital landscape", or any corporate AI phrases.
Sound like a busy human, not a marketing email.
Output ONLY in this format:
SUBJECT: [subject line]
BODY: [email body]"""

_CLASSIFY_PROMPT = """Classify this email reply into exactly ONE category:
INTERESTED, NOT_INTERESTED, OUT_OF_OFFICE, WRONG_PERSON, UNSUBSCRIBE

Reply with ONLY the category name, nothing else.

Email reply:
{reply_text}"""


class FreeAIEngine:
    """Multi-provider LLM engine with automatic failover. Zero cost."""

    def __init__(self, providers: list[dict[str, Any]]) -> None:
        self._providers = providers
        self._daily_counts: dict[str, int] = {p["name"]: 0 for p in providers}
        self._clients: dict[str, AsyncOpenAI] = {}

    def _get_client(self, provider: dict[str, Any]) -> AsyncOpenAI:
        """Get or create an AsyncOpenAI client for a provider."""
        name = provider["name"]
        if name not in self._clients:
            self._clients[name] = AsyncOpenAI(
                base_url=provider["base_url"],
                api_key=provider["api_key"],
            )
        return self._clients[name]

    def _get_available_provider(self) -> dict[str, Any] | None:
        """Find next provider that hasn't hit its daily limit and has an API key."""
        for provider in self._providers:
            if provider.get("api_key") is None:
                continue
            if self._daily_counts[provider["name"]] < provider["daily_limit"]:
                return provider
        return None

    async def _call_provider(
        self,
        provider: dict[str, Any],
        messages: list[dict[str, str]],
        max_tokens: int = 300,
        temperature: float = 0.7,
    ) -> str:
        """Call an LLM provider and return the response text."""
        client = self._get_client(provider)
        response = await client.chat.completions.create(
            model=provider["model"],
            messages=messages,  # type: ignore[arg-type]
            max_tokens=max_tokens,
            temperature=temperature,
        )
        return response.choices[0].message.content or ""

    async def generate_email(
        self,
        business_name: str,
        owner_name: str | None,
        town: str,
        pain_point: str,
        service: str,
    ) -> dict[str, Any]:
        """Generate a personalised cold email using free cloud LLM.

        Returns dict with subject, body, provider, model, cost.
        Falls over to next provider on error or daily limit.
        """
        provider = self._get_available_provider()
        if not provider:
            return {"error": "All free providers exhausted. Queued for tomorrow."}

        user_prompt = (
            f"Business: {business_name}\n"
            f"Owner: {owner_name or 'the owner'}\n"
            f"Town: {town}\n"
            f"Website issue: {pain_point}\n"
            f"Service to offer: {service}"
        )

        messages = [
            {"role": "system", "content": _EMAIL_SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ]

        try:
            text = await self._call_provider(provider, messages)
            self._daily_counts[provider["name"]] += 1

            # Parse SUBJECT: / BODY: format
            subject = ""
            body = text
            if "SUBJECT:" in text:
                subject = text.split("SUBJECT:")[1].split("\n")[0].strip()
            if "BODY:" in text:
                body = text.split("BODY:")[1].strip()

            return {
                "subject": subject,
                "body": body,
                "provider": provider["name"],
                "model": provider["model"],
                "cost": 0.00,
            }
        except Exception as e:
            logger.warning("Provider %s failed: %s — trying next", provider["name"], e)
            # Mark as exhausted and try next provider
            self._daily_counts[provider["name"]] = provider["daily_limit"]
            return await self.generate_email(business_name, owner_name, town, pain_point, service)

    async def classify_reply(self, reply_text: str) -> str:
        """Classify an email reply using free LLM. Returns category string."""
        provider = self._get_available_provider()
        if not provider:
            return "UNCLASSIFIED"

        messages = [
            {"role": "user", "content": _CLASSIFY_PROMPT.format(reply_text=reply_text)},
        ]

        try:
            result = await self._call_provider(provider, messages, max_tokens=20, temperature=0.0)
            self._daily_counts[provider["name"]] += 1
            return result.strip().upper()
        except Exception as e:
            logger.warning("Classification failed on %s: %s", provider["name"], e)
            self._daily_counts[provider["name"]] = provider["daily_limit"]
            return await self.classify_reply(reply_text)

    def reset_daily_counts(self) -> None:
        """Call at midnight to reset all provider counters."""
        self._daily_counts = {p["name"]: 0 for p in self._providers}
