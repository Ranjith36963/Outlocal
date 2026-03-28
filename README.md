# OUTLOCAL

AI-powered cold outreach platform for UK local businesses. Zero-cost lead generation using free cloud LLMs.

## What It Does

12-step automated pipeline:
1. **Scrape** local businesses from Google Maps
2. **Crawl** their websites for contact info and tech stack
3. **Find** and validate email addresses
4. **Score** leads based on website quality and business signals
5. **Generate** personalised cold emails with free AI (Groq/OpenRouter/Gemini)
6. **Send** emails with rate limiting and deliverability checks
7. **Follow up** automatically on configurable schedules
8. **Classify** replies (interested/not interested/OOO/unsubscribe)
9. **Track** leads in built-in CRM pipeline
10. **Analyse** campaign performance with A/B testing
11. **Comply** with GDPR and CAN-SPAM automatically
12. **Report** on everything

## Quick Start

```bash
# Clone and setup
git clone <repo-url> && cd outlocal
cp .env.example .env  # Fill in API keys

# Install
python -m venv venv && source venv/Scripts/activate
pip install -r requirements.txt

# Run
./init.sh
```

## Cost

£0/month. All AI runs on free cloud LLM tiers (Groq + OpenRouter + Gemini).

## Tech Stack

- Python 3.11+ / FastAPI / aiosqlite
- Free LLMs via OpenAI SDK (Groq, OpenRouter, Gemini)
- Playwright for web scraping
- APScheduler for background tasks

See [SETUP.md](SETUP.md) for detailed instructions.
