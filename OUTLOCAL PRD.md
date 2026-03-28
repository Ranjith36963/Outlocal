# OUTLOCAL PRD v3.1 — AI ENGINE UPDATE
## Free Cloud LLMs (No Local Hardware Required)

**This replaces the Ollama section in PRD v3.0. Everything else stays the same.**

---

## FREE CLOUD LLM STRATEGY: Multi-Provider Fallback

Instead of running Ollama locally (which needs 8GB+ RAM and decent CPU), use **3 free cloud LLM providers** with automatic failover. If one hits its daily limit, the system switches to the next.

### Provider Ranking (March 2026)

| Priority | Provider | Free Tier | Daily Limit | Best Model | Quality | Latency |
|----------|----------|-----------|-------------|------------|---------|---------|
| **1 (Primary)** | **Groq** | Forever free, no credit card | ~1,000 requests/day, 500K tokens/day | `llama-3.3-70b-versatile` | 95% of Claude | Ultra-fast (inference on custom chips) |
| **2 (Fallback)** | **OpenRouter** | Forever free, no credit card | 200 requests/day, 20 req/min | `meta-llama/llama-3.3-70b-instruct:free` | 95% of Claude | Fast |
| **3 (Fallback)** | **Google AI Studio** | Forever free, no credit card | 250 requests/day (Gemini 2.5 Flash) | `gemini-2.5-flash` | 90% of Claude | Fast |
| **4 (Emergency)** | **Ollama (local)** | Always free | Unlimited | `llama3.1:8b` | 85% of Claude | Depends on hardware |

### Why This Order

- **Groq first:** Highest free limit (1,000/day), fastest inference, Llama 3.3 70B is near-Claude quality for short email writing. No credit card needed.
- **OpenRouter second:** 200/day covers a full day's email generation if Groq goes down. 29 free models available. OpenAI-compatible API (easy to swap).
- **Google AI Studio third:** 250/day on Gemini 2.5 Flash. Limits were slashed Dec 2025 but still enough for backup. Quality is excellent.
- **Ollama last resort:** Only if all cloud providers fail simultaneously. Requires local hardware.

### Daily Email Capacity on Free Tiers

```
OUTLOCAL needs per day:
  - 200 initial emails × 1 API call each = 200 calls
  - 200 follow-ups (from previous days) × 1 API call each = 200 calls (pre-generated in batch)
  - Reply classification × ~20 calls = 20 calls
  ─────────────────────────────────────
  TOTAL: ~420 API calls/day at peak

Groq free tier alone:        1,000/day → covers 420 calls with 580 to spare ✅
If Groq down, OpenRouter:    200/day → covers initial emails, batch follow-ups overnight
If both down, Gemini:        250/day → covers the day
All three combined:           1,450/day → more than enough headroom
```

### Implementation: All Providers Use OpenAI-Compatible API

Every provider below uses the same `openai` Python SDK — just change `base_url` and `api_key`. Zero code changes when switching providers.

```python
import os
from openai import OpenAI

# Provider configs — all use identical OpenAI-compatible API
PROVIDERS = [
    {
        "name": "groq",
        "base_url": "https://api.groq.com/openai/v1",
        "api_key": os.environ.get("GROQ_API_KEY"),
        "model": "llama-3.3-70b-versatile",
        "daily_limit": 1000,
        "rpm": 30,
    },
    {
        "name": "openrouter",
        "base_url": "https://openrouter.ai/api/v1",
        "api_key": os.environ.get("OPENROUTER_API_KEY"),
        "model": "meta-llama/llama-3.3-70b-instruct:free",
        "daily_limit": 200,
        "rpm": 20,
    },
    {
        "name": "gemini",
        "base_url": "https://generativelanguage.googleapis.com/v1beta/openai/",
        "api_key": os.environ.get("GEMINI_API_KEY"),
        "model": "gemini-2.5-flash",
        "daily_limit": 250,
        "rpm": 10,
    },
]

class FreeAIEngine:
    """Multi-provider LLM engine with automatic failover. Zero cost."""

    def __init__(self):
        self.daily_counts = {p["name"]: 0 for p in PROVIDERS}
        self.current_provider_idx = 0

    def _get_available_provider(self):
        """Find next provider that hasn't hit its daily limit."""
        for i, provider in enumerate(PROVIDERS):
            if self.daily_counts[provider["name"]] < provider["daily_limit"]:
                return provider
        return None  # All providers exhausted — queue for tomorrow

    def generate_email(self, business_name: str, owner_name: str,
                       town: str, pain_point: str, service: str) -> dict:
        """Generate a personalised cold email using free cloud LLM."""
        provider = self._get_available_provider()
        if not provider:
            return {"error": "All free providers exhausted. Queued for tomorrow."}

        client = OpenAI(
            base_url=provider["base_url"],
            api_key=provider["api_key"],
        )

        system_prompt = """You are a cold email copywriter for a UK digital services company.
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

        user_prompt = f"""Business: {business_name}
Owner: {owner_name or 'the owner'}
Town: {town}
Website issue: {pain_point}
Service to offer: {service}"""

        try:
            response = client.chat.completions.create(
                model=provider["model"],
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                max_tokens=300,
                temperature=0.7,
            )
            text = response.choices[0].message.content
            self.daily_counts[provider["name"]] += 1

            # Parse response
            subject = text.split("SUBJECT:")[1].split("\n")[0].strip() if "SUBJECT:" in text else ""
            body = text.split("BODY:")[1].strip() if "BODY:" in text else text

            return {
                "subject": subject,
                "body": body,
                "provider": provider["name"],
                "model": provider["model"],
                "cost": 0.00,
            }
        except Exception as e:
            # Provider failed — try next one
            self.daily_counts[provider["name"]] = provider["daily_limit"]  # Mark as exhausted
            return self.generate_email(business_name, owner_name, town, pain_point, service)

    def classify_reply(self, reply_text: str) -> str:
        """Classify an email reply using free LLM. Returns category string."""
        provider = self._get_available_provider()
        if not provider:
            return "UNCLASSIFIED"

        client = OpenAI(
            base_url=provider["base_url"],
            api_key=provider["api_key"],
        )

        response = client.chat.completions.create(
            model=provider["model"],
            messages=[{
                "role": "user",
                "content": f"""Classify this email reply into exactly ONE category:
INTERESTED, NOT_INTERESTED, OUT_OF_OFFICE, WRONG_PERSON, UNSUBSCRIBE

Reply with ONLY the category name, nothing else.

Email reply:
{reply_text}"""
            }],
            max_tokens=20,
            temperature=0,
        )
        self.daily_counts[provider["name"]] += 1
        return response.choices[0].message.content.strip().upper()

    def reset_daily_counts(self):
        """Call at midnight to reset all provider counters."""
        self.daily_counts = {p["name"]: 0 for p in PROVIDERS}
```

### API Key Setup (All Free, No Credit Card)

```bash
# 1. Groq (Primary) — https://console.groq.com → Create API Key
#    No credit card required. Free forever.
export GROQ_API_KEY="gsk_..."

# 2. OpenRouter — https://openrouter.ai → Create API Key
#    No credit card required. Free models end with :free
export OPENROUTER_API_KEY="sk-or-..."

# 3. Google AI Studio — https://aistudio.google.com → Get API Key
#    No credit card required. Free tier auto-applied.
export GEMINI_API_KEY="AIza..."

# All three: sign up in under 2 minutes each. Zero payment info needed.
```

### Cost Summary: STILL £0

```
Groq free tier:           £0 (1,000 requests/day)
OpenRouter free tier:     £0 (200 requests/day)
Google AI Studio free:    £0 (250 requests/day)
───────────────────────
Total AI cost:            £0/month

Combined daily capacity:  1,450 requests/day
OUTLOCAL daily need:      ~420 requests/day at peak
Headroom:                 3.4x your maximum need ✅
```

### When Free Tiers Stop Being Enough (Scaling Past ~300 emails/day)

If you scale past 300 emails/day consistently and exhaust Groq's 1,000/day limit:

| Option | Cost | When to Switch |
|--------|------|---------------|
| Add Groq paid ($0.05/1M tokens) | ~£2/month at 500 emails/day | Past 300/day consistently |
| Add Claude API Haiku ($0.25/1M) | ~£5/month at 500 emails/day | If quality needs upgrading |
| Self-host Ollama | £0 (hardware cost) | If you get a GPU machine |

**But at 300 emails/day you should already have 5+ paying clients generating £3,000+/month. The £2-5/month upgrade is trivial at that point.**

---

## CHANGES TO PRD v3.0

Replace every instance of "Ollama" in the pipeline with `FreeAIEngine` (the multi-provider class above).

Specifically:

| PRD Section | Old | New |
|-------------|-----|-----|
| Tech Stack → AI Engine | Ollama (local, free) | Groq + OpenRouter + Gemini (cloud, free, no hardware) |
| Step 9: Generate Email | Ollama API call | `FreeAIEngine.generate_email()` with auto-failover |
| Step 14: Reply Classification | Ollama NLP classification | `FreeAIEngine.classify_reply()` with auto-failover |
| Monthly cost | £0 (local compute) | £0 (cloud free tiers) |
| Hardware requirement | 8GB+ RAM, decent CPU | **Any machine with internet** — even a £30/month VPS |
| Backup/fallback | Claude API (paid) | Ollama local (if all 3 cloud providers fail simultaneously) |

**Everything else in PRD v3.0 remains unchanged.**
