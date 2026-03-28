# OUTLOCAL Architecture

## Overview

OUTLOCAL is a 12-step automated cold outreach pipeline for UK local businesses. All components are Python async, sharing a single SQLite database.

## System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    FastAPI Server                         │
│                   (src/outlocal/api/)                     │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐ │
│  │ Scrapers │→│ Enrichment│→│ Scoring  │→│ AI Engine│ │
│  │ (G.Maps) │  │(Web+Email)│  │(0-100)   │  │(LLM Gen) │ │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘ │
│       │              │              │              │       │
│       ▼              ▼              ▼              ▼       │
│  ┌────────────────────────────────────────────────────┐  │
│  │              SQLite Database (aiosqlite)            │  │
│  │  leads | campaigns | emails | replies | audit_log  │  │
│  └────────────────────────────────────────────────────┘  │
│       │              │              │              │       │
│       ▼              ▼              ▼              ▼       │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐ │
│  │  Sender  │→│ Follow-up│→│Classifier│→│   CRM    │ │
│  │  (SMTP)  │  │(Sequence)│  │(LLM Sort)│  │(Pipeline)│ │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘ │
│       │              │              │              │       │
│       ▼              ▼              ▼              ▼       │
│  ┌──────────┐  ┌──────────┐                              │
│  │Analytics │  │Compliance│  ← APScheduler (background)  │
│  │(Metrics) │  │(GDPR/CAN)│                              │
│  └──────────┘  └──────────┘                              │
│                                                           │
└─────────────────────────────────────────────────────────┘
```

## Data Flow

1. **Scrape** → leads table (status: new)
2. **Enrich** → leads table updated (status: enriched)
3. **Score** → leads table updated (status: scored)
4. **Generate** → emails table (status: draft)
5. **Send** → emails table (status: sent)
6. **Follow-up** → new emails linked to original
7. **Classify** → replies table with classification
8. **Track** → leads status updated (interested/converted/lost)

## Key Design Decisions

- **SQLite over PostgreSQL**: Zero-config, single-file, sufficient for solo founder scale (~300 emails/day)
- **Async-first**: aiosqlite, aiohttp, aiosmtplib — everything non-blocking
- **Free LLMs**: Groq → OpenRouter → Gemini failover chain, zero cost
- **No ORM**: Raw SQL with parameterised queries via aiosqlite — simpler, faster, no magic
- **Monolith**: Single FastAPI app with module boundaries, not microservices
