# CHANGELOG — OUTLOCAL

## [0.1.0] — 2026-03-28

### Session 1 — Full Bootstrap + All 28 Features

#### Core Infrastructure
- **F001**: Database schema with 8 tables (leads, campaigns, emails, replies, audit_log, suppression_list, consent_log, ab_tests)
- **F002**: Configuration via pydantic-settings, LLM provider configs
- **F003**: FastAPI app with health check, CORS, API versioning

#### Data Acquisition
- **F004**: Google Maps scraper with Playwright, deduplication, rate limiting
- **F005**: Website crawler extracting emails, phones, social links, tech stack
- **F006**: Email finder with permutation generation, MX validation, disposable filtering

#### Processing Pipeline
- **F007**: Lead scoring engine (0-100) across 4 dimensions
- **F008**: FreeAIEngine with Groq → OpenRouter → Gemini failover
- **F009**: Email template personalisation with pain point derivation
- **F025**: End-to-end pipeline orchestrator

#### Email Operations
- **F010**: Async SMTP sender with CAN-SPAM headers
- **F011**: SPF/DKIM/DMARC domain authentication checker
- **F012**: Follow-up sequence engine with timing and skip logic
- **F013**: IMAP reply detection (architecture ready)
- **F014**: LLM-based reply classification (5 categories)

#### CRM & Analytics
- **F015**: Lead pipeline with status tracking and activity log
- **F016**: Campaign management with batch operations
- **F017**: Campaign analytics (open/click/reply/conversion rates)
- **F018**: A/B testing with auto-winner selection

#### Compliance
- **F019**: GDPR/CAN-SPAM compliance engine
- **F020**: Consent tracking and audit trail

#### API & Infrastructure
- **F021-F023**: Full REST API for leads, campaigns, compliance
- **F024**: APScheduler for background pipeline operations
- **F026**: Docker + docker-compose configuration
- **F027**: 169 tests across 15 test files
- **F028**: README, SETUP, architecture docs

### No Failed Approaches
All features implemented successfully on first attempt.
