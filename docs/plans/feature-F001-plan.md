# Feature F001 Plan: Database Schema and Core Models

## Scope
### In Scope
- SQLite database init with all tables (leads, campaigns, emails, replies, audit_log)
- Pydantic models for Lead, Campaign, Email, Reply
- Database class with async connection management
- Table creation DDL with proper types, constraints, indexes

### Out of Scope
- CRUD operations (F015, F016, F021)
- API endpoints (F003, F021)
- Migration system (not needed for v1, single schema)

## Done When
- [x] SQLite database initialises with all required tables
- [x] Lead model validates: business_name, owner_name, email, phone, website, town, source, score, status
- [x] Campaign model validates: name, status, template, target_criteria, created_at
- [x] Email model validates: lead_id, campaign_id, subject, body, provider, status, sent_at, opened_at, clicked_at
- [x] Reply model validates: email_id, raw_text, classification, classified_at
- [x] All models use Pydantic validation with proper types

## Implementation Order
1. Write tests for models and database init
2. Create Pydantic models in src/outlocal/core/models.py
3. Create database module in src/outlocal/core/database.py
4. Verify all tests pass
