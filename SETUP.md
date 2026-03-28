# OUTLOCAL Setup Guide

## Prerequisites
- Python 3.11+
- Git

## 1. Clone and Configure

```bash
git clone <repo-url>
cd outlocal
cp .env.example .env
```

Edit `.env` with your API keys:
- **Groq** (free): https://console.groq.com → Create API Key
- **OpenRouter** (free): https://openrouter.ai → Create API Key
- **Google AI Studio** (free): https://aistudio.google.com → Get API Key
- **SMTP**: Your email provider's SMTP credentials

## 2. Install Dependencies

```bash
python -m venv venv
source venv/Scripts/activate  # Windows
# source venv/bin/activate    # Linux/Mac
pip install -r requirements.txt
playwright install chromium
```

## 3. Run

```bash
./init.sh
# Or directly:
uvicorn src.outlocal.api.main:app --reload --port 8000
```

API docs at http://localhost:8000/docs

## 4. Docker (Alternative)

```bash
docker compose up -d
```

## Environment Variables

See `.env.example` for all required variables with descriptions.
