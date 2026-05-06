# HANDOFF — OUTLOCAL

## Session Status
Session 1 — 2026-03-28. ALL 28 FEATURES PASSING. 169 tests.

## Completed Features (28/28)
- F001: Database schema and core models ✅
- F002: Configuration management ✅
- F003: FastAPI app skeleton ✅
- F004: Google Maps scraper ✅
- F005: Website crawler ✅
- F006: Email finder ✅
- F007: Lead scoring engine ✅
- F008: FreeAIEngine (multi-provider LLM) ✅
- F009: Email template personalisation ✅
- F010: Async SMTP email sender ✅
- F011: Domain auth checker (SPF/DKIM/DMARC) ✅
- F012: Follow-up sequence engine ✅
- F013: IMAP reply detection ✅
- F014: Reply classification ✅
- F015: Lead pipeline / CRM ✅
- F016: Campaign management ✅
- F017: Campaign analytics ✅
- F018: A/B testing ✅
- F019: GDPR/CAN-SPAM compliance ✅
- F020: Consent tracking ✅
- F021: REST API endpoints ✅
- F022: Scraping API endpoints ✅
- F023: Compliance API endpoints ✅
- F024: Background scheduler ✅
- F025: End-to-end pipeline ✅
- F026: Docker containerisation ✅
- F027: Test suite (169 tests) ✅
- F028: Documentation ✅

## Test Suite
169 tests passing, 0 failures, ~7 seconds runtime.

## Architecture
All modules under src/outlocal/ with clear boundaries.
SQLite + aiosqlite, no ORM, parameterised SQL throughout.
Free LLM failover: Groq → OpenRouter → Gemini.

---

## BRAIN Run Log

| Date | Day | Run type | Key output |
|---|---|---|---|
| 2026-03-28 | 1 | Session 1 bootstrap | All 28 features implemented |
| 2026-04-05 | 9 | Weekly strategy | active_strategy.md Week 2 |
| 2026-04-24 | 33 | Daily email + followup | Campaign milestone framing; post-campaign prep |
| 2026-05-01 | 34 | Daily email + followup | Post-campaign analysis; Batch 5 readiness; IMAP alert |
| 2026-05-01 | 34 | Daily LinkedIn research | LinkedIn channel planning; warm pipeline buffer |
| 2026-05-02 | 35 | Daily email + followup | Bank holiday discovery — Tuesday 2026-05-06 send date |
| 2026-05-03 | 36 | Daily email + followup | Weekend bridge — LinkedIn copy ready for Monday; fu_041-045 rescheduled to Tue 08:45 |
| 2026-05-04 | 37 | Daily email + followup | Calendar correction: bank holiday = Tue 05; send day = Wed 06; LinkedIn executes TODAY |
| 2026-05-05 | 38 | Bank holiday bridge (unscheduled) | LinkedIn NOT confirmed Mon; last window Wed 07:45; Wednesday execution order locked |
| **2026-05-06** | **39** | **Daily email + followup (SEND DAY)** | **IMAP sweep 07:00; LinkedIn last chance 07:45-08:20; fu_041-045 08:45-09:25; Batch 5 conditional 10:00** |

---

## CRITICAL STATE — 2026-05-06 (Day 39 — SEND DAY)

### SEND DAY — EXECUTING
- **2026-05-05 = Tuesday — UK May Day bank holiday** (CONFIRMED zero sends)
- **2026-05-06 = Wednesday — SEND DAY** (TODAY — execute locked sequence)

### KEY STATUS (Day 39): LinkedIn Execute or Archive
- LinkedIn was due Monday 2026-05-04. Not executed. Not executed Tuesday (bank holiday). 39 sessions without linkedin_profiles.json.
- **ABSOLUTE LAST WINDOW: TODAY 07:45-08:20 — before email sends.**
- If missed today: permanently archive leads 1, 3, 22 as LOST_NO_RESPONSE. No further action.

### Active Data Files (all updated 2026-05-06)
- `data/daily_signals.json` — Day 39, SEND DAY, locked execution order, IMAP/LinkedIn/fu_041-045/Batch 5
- `data/daily_email_plan.json` — Day 39, fu_041-045 ready, Batch 5 templates on standby
- `data/daily_strategy.md` — Day 39, full execution brief, calendar forward
- `data/followup_queue.json` — Day 39, fu_041-045 (13 days overdue), today 08:45-09:25
- `data/reply_classifications.json` — Day 39, IMAP gap 32 days, LinkedIn TODAY
- `data/value_delivery_queue.json` — Day 39, LinkedIn TODAY 07:45-08:20 = ABSOLUTE DEADLINE
- `data/linkedin_connection_notes.json` — unchanged, notes ready for all 3 leads

### IMAP Status
- **32 days overdue** (last confirmed check: 2026-04-04)
- Full cohort sweep from 07:00 TODAY
- Priority order: leads 3 → 22 → 1 (LinkedIn precondition), then leads 30, 31, 32, 58, 59 (fu precondition), then all remaining

### Batch 5 Status
- **29-day campaign stall** — no new leads since Batch 4
- Ryedale data is 14 days overdue (requested 2026-04-22)
- Target: Malton, Pickering, Helmsley, Kirkbymoorside, Hovingham, Norton-on-Derwent
- Signal: SSL-primary (PAS, 60%), mobile-secondary (PAS, 20%), no-website BAB (15%, 20+ reviews), AIDA keyword-gap (5%)
- **Data cutoff: 09:30 today. If data arrives before 09:30: BRAIN personalises same session, sends from 10:00. Post-bank-holiday premium window is NOW.**
- If no data by 09:30: fu_041-045 only (5 sends). Batch 5 waits.

### Unconfirmed Sends
- fu_041-045 (leads 30, 31, 32, 58, 59): Day-14 breakups, 13 days overdue. **Send today 08:45-09:25 (IMAP first — confirm not sent 2026-04-23).**
- fu_046-049 (leads 52, 55, 50, 56): assumed sent 2026-04-24, never confirmed in CHANGELOG.

### Warm Pipeline
- Leads 1 (Tom), 3 (Claire), 22 (Rob): all PRESUMED_LOST_NO_RESPONSE
- Email channel: CLOSED
- LinkedIn channel: **OPEN. ABSOLUTE LAST WINDOW: TODAY 07:45-08:20 (before email sends)**
- LinkedIn connection notes in `data/linkedin_connection_notes.json` and `data/value_delivery_queue.json`
- Rule: IMAP sweep before LinkedIn. If reply found: respond to reply, skip LinkedIn for that lead.
- **linkedin_profiles.json must be written same session — no exceptions. 39 sessions without it.**
- **If LinkedIn not done by 08:20 today: archive leads 1/3/22 permanently.**

### Day-3 Bump Date
- Batch 5 Day-0: Wednesday 2026-05-06 (if data arrives in time)
- Day 3 calendar: Saturday 2026-05-09 — weekend, no send
- **Day-3 bump: FRIDAY 2026-05-09 (preferred — avoids weekend cold gap) or Monday 2026-05-11**
- BRAIN confirms on Friday 2026-05-09 morning run

### CHANGELOG
- No HANDS updates since 2026-03-28 (39 days). All sends unlogged. **Update TODAY EOD — mandatory.**

---

## HANDS Execution Order for TODAY (Wednesday 2026-05-06)

| Time | Action | Condition |
|---|---|---|
| 07:00-07:45 | IMAP sweep — leads 3, 22, 1 | Mandatory before LinkedIn |
| 07:45-08:00 | LinkedIn — Claire (lead 3) | IMAP clean. Check posts. Write note. |
| 08:00-08:10 | LinkedIn — Rob (lead 22) | IMAP clean. Check posts. Write note. |
| 08:10-08:20 | LinkedIn — Tom (lead 1) | IMAP clean. Check posts. Write note. |
| **08:20** | **Write linkedin_profiles.json** | **MANDATORY — 39 sessions without this file** |
| 08:20-08:40 | IMAP sweep — leads 30, 31, 32, 58, 59 + full cohort | fu precondition |
| 08:45 | fu_041 — Steve, Halifax Window Cleaning | IMAP clean + not sent 2026-04-23 |
| 08:55 | fu_042 — Pontefract Pharmacy | IMAP clean + not sent |
| 09:05 | fu_043 — Ann, Castleford Carpets | IMAP clean + not sent |
| 09:15 | fu_044 — Old Court Solicitors | IMAP clean + not sent |
| 09:25 | fu_045 — Tony, Scarborough Roofing | IMAP clean + not sent |
| 09:30 | Batch 5 data check — BRAIN decision | If data received: BRAIN personalises now |
| 10:00-11:30 | Batch 5 initial sends | If Ryedale data received by 09:30 |
| EOD | CHANGELOG.md update | ALL actions logged with timestamps — 39 days unlogged |

## Next BRAIN Run
- **If Batch 5 fires today:** Next mandatory BRAIN run is **Friday 2026-05-09** for Day-3 bump copy and send-date confirmation (Friday 09 May preferred over Monday 11 May).
- **If no data by 09:30 today:** Sends limited to fu_041-045 (5 sends). Next BRAIN run when Ryedale data arrives.
- **If Batch 5 data arrives today after 09:30:** BRAIN runs same session. Thursday 2026-05-07 initial sends.
- **Next mandatory BRAIN run: Friday 2026-05-09** (if Batch 5 fired today) or on data arrival (if not).
