# OUTLOCAL — AI-Powered Cold Outreach Platform for UK Local Businesses

Zero-cost lead generation pipeline: scrape local businesses → crawl websites → find emails → score leads → generate personalised cold emails with free cloud LLMs → send → follow up → classify replies → track in CRM → report → stay compliant.

## Tech Stack
- **Language:** Python 3.11+
- **Framework:** FastAPI (async API server)
- **Database:** SQLite via aiosqlite (lightweight, zero-config)
- **AI Engine:** Free cloud LLMs — Groq (primary) → OpenRouter → Gemini (failover) via OpenAI SDK
- **Scraping:** Playwright (headless browser), aiohttp (HTTP), BeautifulSoup4 (parsing)
- **Email:** aiosmtplib (async SMTP sending), email-validator
- **Testing:** pytest, pytest-asyncio, pytest-cov, Playwright (E2E)
- **Linting:** ruff (lint + format), mypy (types)
- **Task Queue:** APScheduler (lightweight scheduling)

## Commands
```bash
# Dev server
./init.sh                           # Start dev server
uvicorn src.outlocal.api.main:app --reload --port 8000

# Tests
pytest tests/ -v                    # Full test suite
pytest tests/ -v --fast             # Random 10% subsample
pytest tests/ -v --cov=src/outlocal # With coverage

# Lint & Type Check
ruff check src/ tests/              # Lint
ruff format src/ tests/             # Format
mypy src/                           # Type check

# All checks
ruff check src/ tests/ && mypy src/ && pytest tests/ -v
```

## Architecture
@./docs/architecture/current.md

## Workflow Rules
IMPORTANT: Read HANDOFF.md and CHANGELOG.md before starting ANY work.
IMPORTANT: Run smoke test before implementing new features.
IMPORTANT: ONE feature at a time. Never one-shot everything.
IMPORTANT: Write tests FIRST, implementation SECOND (TDD).
IMPORTANT: NEVER delete or modify existing tests.
IMPORTANT: Commit and push after every meaningful unit of work.
IMPORTANT: Run tests before every commit. Never commit code that breaks existing tests.
IMPORTANT: Update HANDOFF.md before every session exit or compaction.
IMPORTANT: If approaching max-turns limit, write HANDOFF.md IMMEDIATELY before your final turn.
IMPORTANT: Log failed approaches in CHANGELOG.md with WHY they failed.
IMPORTANT: Use open-source research before writing implementation code — study the best repos first.
Do not stop tasks early. Continue until ALL features in feature_list.json pass.
Your context window will be automatically compacted as it approaches its limit. Save progress to HANDOFF.md before compaction. Do not stop early due to token concerns.

## Code Style
- Type hints on ALL functions
- Docstrings on public functions
- Async-first (aiohttp, aiosqlite, aiosmtplib)
- Pydantic models for all data structures
- Specific exceptions (never bare try/except)
- UK English in user-facing strings

## Security Rules
- NEVER commit secrets — use .env + python-dotenv
- Validate ALL inputs with Pydantic
- Parameterise ALL SQL queries
- Rate limit all external API calls
- See: .claude/rules/security.md

## Project Structure
```
src/outlocal/
├── core/          # Config, database, models
├── scrapers/      # Google Maps, website crawling
├── enrichment/    # Email finding, contact extraction
├── scoring/       # Lead scoring engine
├── ai_engine/     # FreeAIEngine (multi-provider LLM)
├── email_sender/  # SMTP sending, deliverability
├── followup/      # Follow-up sequence automation
├── classifier/    # Reply classification
├── crm/           # Pipeline tracking, CRM
├── analytics/     # Campaign analytics, A/B testing
├── compliance/    # GDPR, CAN-SPAM compliance
└── api/           # FastAPI endpoints
```
