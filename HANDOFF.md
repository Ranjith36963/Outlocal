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
| **2026-05-06** | **39** | **Daily LinkedIn research (FINAL RUN)** | **All 3 output files updated; archive trigger live; HANDS execute 07:45-08:20 or archive leads 1/3/22 EOD** |
| **2026-05-07** | **40** | **Daily email + followup (archive + carry-forward)** | **Leads 1/3/22 formally archived LOST_NO_RESPONSE (LinkedIn never executed, 40 sessions). fu_041-045 carry forward (14 days overdue). Batch 5: last Thursday send window. IMAP gap 33 days.** |
| **2026-05-08** | **41** | **Daily email + followup (Friday bridge)** | **Batch 5 deferred to Tuesday 2026-05-12 (confirmed). fu_041-045 carry forward (15 days overdue — sendable Friday or Monday). Final IMAP override window for leads 1/3/22. Leads 49/51 archived LOST_UNRESOLVED. IMAP gap 34 days.** |
| **2026-05-10** | **43** | **Daily email + followup (Sunday weekend bridge)** | **Archive of leads 1/3/22 UNCONDITIONALLY FINAL (Friday override window closed). fu_041-045 carry to Monday (17 days overdue). active_strategy.md validity extended to 2026-05-17. Leads 53/54 archive Monday. Batch 5 confirmed Tuesday 2026-05-12. IMAP gap 36 days.** |
| **2026-05-11** | **44** | **Daily email + followup (Monday cleanup day)** | **fu_041-045 SEND TODAY (18 days overdue — final window). Leads 53/54 archive LOST_UNRESOLVED. CHANGELOG mandatory today. IMAP gap 37 days. Batch 5 Ryedale confirmed Tuesday 2026-05-12, 09:00-10:30.** |
| **2026-05-12** | **45** | **Daily LinkedIn research (Tuesday evening, Batch 5 Day-0)** | **Batch 5 Ryedale assumed sent today 09:00-10:30 (unconfirmed). Zero legacy LinkedIn candidates (all windows expired). Day-3 LinkedIn window opens Friday 2026-05-15. Hard deadline Day 7 = Tuesday 2026-05-19. All 3 output files updated. HANDS populates search_queries[] from morning send list and executes Friday.** |
| **2026-05-14** | **47** | **Daily email + followup (Thursday evening, eve of Day-3)** | **Day-3 email bump copy ready (per-signal templates, daily_email_plan.json). Day-3 LinkedIn templates ready (linkedin_search_plan.json + linkedin_connection_notes.json). IMAP gap: 40 days — sweep FIRST Friday. Batch 5 per-lead data still unconfirmed by HANDS. Day-3 send window: Friday 2026-05-15, 09:00-10:30. LinkedIn hard deadline: Tuesday 2026-05-19. CHANGELOG: 47 days overdue — MANDATORY Friday.** |
| **2026-05-15** | **48** | **Daily email + followup (Friday evening, Batch 5 Day 3)** | **Day-3 bumps assumed sent (UNCONFIRMED). LinkedIn UNCONFIRMED — profiles.json missing (48-session pattern). Monday 2026-05-18 is last LinkedIn window before Tuesday archive trigger. Day-7 new-angle copy generated (all 4 signal variants ready in daily_email_plan.json). Monday fallback LinkedIn templates added to linkedin_connection_notes.json (direct-use, no BRAIN run needed). Reply peak window open: Saturday-Monday post-bump. IMAP gap: 41 days confirmed check. CHANGELOG: 48 days overdue — absolute deadline before Tuesday Day-7 sends.** |
| **2026-05-18** | **49** | **Daily LinkedIn research (Monday morning, Batch 5 Day 6 — LAST WINDOW)** | **linkedin_profiles.json STILL MISSING (49-session failure). Today is the absolute last LinkedIn window — archive trigger fires Tuesday 2026-05-19 EOD. All 3 output files updated. IMAP gap: 42 days, zero Batch 5 replies. Sector-prioritised discovery queries added to search_plan for all Ryedale towns. monday_fallback_notes marked as ACTIVE EXECUTION PLAN (not backup). Coordination file updated — all Batch 5 Ryedale leads approved pending per-lead IMAP. HANDS must execute today: IMAP → LinkedIn search → connection note → write profiles.json → CHANGELOG.** |
| **2026-05-16** | **50** | **Daily email + followup (Saturday bridge, Batch 5 Day 4 — full weekly review)** | **Reply peak window OPEN (24-72h post-bump). LinkedIn STILL MISSING (49+ sessions). active_strategy.md full weekly review completed — valid to 2026-05-24. All 6 data files updated. Monday = FINAL LinkedIn window. Tuesday = Day-7 sends + LinkedIn archive trigger EOD. IMAP gap: 42 days. No new replies or signals. CHANGELOG: 49+ days overdue — mandatory before Tuesday sends.** |
| **2026-05-16** | **50** | **Daily LinkedIn research (Saturday evening, Batch 5 Day 4 — weekend bridge)** | **50-session LinkedIn failure. All 3 LinkedIn files updated to Day 50 / 2026-05-16. linkedin_profiles.json STILL MISSING. Day-3 bumps assumed sent yesterday — reply peak OPEN NOW (Saturday-Monday). monday_fallback_notes marked ACTIVE EXECUTION PLAN. All Batch 5 Ryedale leads approved pending IMAP per lead Monday. Archive trigger confirmed Tuesday 2026-05-19 EOD. Weekend IMAP monitoring recommended. src/outlocal/linkedin/orchestrator.py NOT FOUND — LinkedIn module not yet implemented.** |

---

## CRITICAL STATE — 2026-05-16 (Day 50 — BATCH 5 DAY-4 SATURDAY EVENING — REPLY PEAK OPEN — MONDAY FINAL LINKEDIN WINDOW — ALL 3 LINKEDIN FILES UPDATED)

### WARM PIPELINE — PERMANENTLY CLOSED (UNCONDITIONALLY FINAL)
- **Archive trigger fired 2026-05-06** — LinkedIn deadline missed for 47 consecutive sessions
- **Leads 1 (Tom), 3 (Claire), 22 (Rob): LOST_NO_RESPONSE — UNCONDITIONALLY FINAL**
- Friday 2026-05-08 EOD override window has closed. No further action, no further IMAP checks for leads 1/3/22.
- Email channel: CLOSED. LinkedIn channel: PERMANENTLY CLOSED (never activated).
- Combined pipeline value written off: £800-1,175

### Active Data Files
- `data/daily_signals.json` — **Day 50 (2026-05-16 SATURDAY) — UPDATED. Reply peak OPEN. Monday/Tuesday execution orders. IMAP gap 42 days.**
- `data/daily_email_plan.json` — **Day 50 (2026-05-16 SATURDAY) — HEADER UPDATED. Day-7 new-angle copy READY — all 4 signal variants. Tuesday 2026-05-19, 09:00-10:30.**
- `data/daily_strategy.md` — **Day 50 (2026-05-16 SATURDAY) — UPDATED. Saturday bridge. Monday FINAL LinkedIn window. Tuesday Day-7 sends. Archive trigger brief.**
- `data/followup_queue.json` — **Day 50 (2026-05-16 SATURDAY) — UPDATED. Day-3 assumed. Day-7 schedule LIVE. Day-14 pending. No sends today.**
- `data/reply_classifications.json` — **Day 50 (2026-05-16 SATURDAY) — UPDATED. IMAP gap 42 days. Weekend monitoring recommended. No new replies.**
- `data/value_delivery_queue.json` — **Day 50 (2026-05-16 SATURDAY) — UPDATED. Reply peak open. 24h SLA live. Monday LinkedIn FINAL alert.**
- `data/active_strategy.md` — **Day 50 (2026-05-16 SATURDAY) — FULL WEEKLY REVIEW COMPLETE. Valid to 2026-05-24. Batch 6 triggers added. Week 8 operational priorities.**
- `data/linkedin_connection_notes.json` — **Day 50 (2026-05-16 SATURDAY EVENING) — UPDATED. monday_fallback_notes ACTIVE EXECUTION PLAN. Sector templates for all Ryedale towns. 200-char hard limit. Post-reference priority. 50-session failure noted.**
- `data/linkedin_search_plan.json` — **Day 50 (2026-05-16 SATURDAY EVENING) — UPDATED. Sector discovery queries for all Ryedale towns. search_queries[] still empty (HANDS to populate from send records Monday). FINAL WINDOW — archive trigger Tuesday EOD.**
- `data/linkedin_coordination.json` — **Day 50 (2026-05-16 SATURDAY EVENING) — UPDATED. All Batch 5 leads approved pending per-lead IMAP Monday. Archive trigger fires Tuesday 2026-05-19 EOD. Weekend monitoring recommended.**

### IMAP Status
- **42 days overdue** (last confirmed check: 2026-04-04)
- Friday 2026-05-15 sweep ASSUMED — UNCONFIRMED (new_replies.json unchanged — consistent with clean sweep)
- Zero Batch 5 replies to date. **Reply peak window OPEN NOW — 24-72h post-bump (Saturday-Monday)**
- **Do NOT sweep leads 1/3/22 — archive is unconditionally final**
- **RECOMMENDED: Weekend sweep today Saturday or Sunday — post-bump reply peak is highest now**
- **MANDATORY per lead before each LinkedIn note Monday 2026-05-18**
- **MANDATORY per lead before each Day-7 send Tuesday 2026-05-19**

### Batch 5 Status
- **Day-0 sends assumed completed Tuesday 2026-05-12, 09:00-10:30 — UNCONFIRMED**
- **Day-3 bumps assumed sent Friday 2026-05-15, 09:00-10:30 — UNCONFIRMED**
- No per-lead data file received from HANDS (49+ consecutive sessions)
- Ryedale targets: Malton, Pickering, Helmsley, Kirkbymoorside, Hovingham, Norton-on-Derwent
- Signal: SSL-primary (PAS, 60%), mobile-secondary (PAS, 20%), no-website BAB (15%), AIDA keyword-gap (5%)
- **Day 4 = TODAY SATURDAY 2026-05-16 — Reply peak OPEN. Weekend monitoring recommended. No sends.**
- **Day 6 = MONDAY 2026-05-18 — FINAL LINKEDIN WINDOW. Execute immediately Monday morning.**
- **Day 7 = TUESDAY 2026-05-19 — Day-7 new-angle sends (09:00-10:30) + LinkedIn archive trigger EOD.**

### fu_041-045 Status
- **ASSUMED SEQUENCE COMPLETE** — breakups for leads 30/31/32/58/59 assumed sent Monday 2026-05-11
- LinkedIn window for all 5 leads: EXPIRED. No LinkedIn approach ever.
- Reapproach date: 2026-10-23

### Blocked Leads — Final Decisions
- Lead 49 (East Riding Builders Ltd): ARCHIVED LOST_UNRESOLVED (Day 40).
- Lead 51 (Driffield Garden Centre): ARCHIVED LOST_UNRESOLVED (Day 40).
- Lead 53 (Bridlington Bay Lettings): ASSUMED ARCHIVED Monday 2026-05-11 (LOST_UNRESOLVED).
- Lead 54 (The Wolds Inn): ASSUMED ARCHIVED Monday 2026-05-11 (LOST_UNRESOLVED).

### CHANGELOG
- No HANDS updates since 2026-03-28 (**49+ days**). **MANDATORY — must be completed Monday 2026-05-18. Absolute deadline: before Day-7 sends on Tuesday 2026-05-19. No further deferrals.**

---

## HANDS Execution Order for TODAY SATURDAY 2026-05-16 (Weekend — Reply Peak Open)

No sends today (Saturday block). Weekend IMAP monitoring recommended.

| Priority | Action | Condition |
|---|---|---|
| 1 | Weekend IMAP sweep — all Batch 5 leads (NOT leads 1/3/22) | RECOMMENDED (not mandatory today). Per lead. If INTERESTED reply found: write new_replies.json immediately, classify, begin proposal draft. 24h SLA from reply time. If NOT_INTERESTED: block all channels. If UNSUBSCRIBE: suppress within 24h (GDPR Article 21 — applies weekends). |

## HANDS Execution Order for MONDAY 2026-05-18 (LinkedIn FINAL Last Window)

linkedin_profiles.json is STILL MISSING — LinkedIn was NOT executed. Monday is the absolute last window.

| Priority | Action | Condition |
|---|---|---|
| 1 | IMAP sweep — all Batch 5 leads (NOT leads 1/3/22) | Per lead, not bulk. If NOT_INTERESTED: block LinkedIn + Day-7 send permanently. If UNSUBSCRIBE: suppress all channels, GDPR 24h. |
| 2 | LinkedIn profile searches — all Batch 5 leads, sector priority order | Solicitors → Estate agents → Hotels/B&Bs → Restaurants → Retail → Trades. Primary query: `site:linkedin.com/in "[Full Name]" "[Business Name]"`. Fallback: sector_discovery_fallback_queries in linkedin_search_plan.json. |
| 3 | Check posts from last 60 days on each confirmed profile | Post-reference note has 3-4x higher acceptance. Essential step — do not skip. |
| 4 | LinkedIn connection requests — confirmed profiles only | **Use monday_fallback_notes in linkedin_connection_notes.json — active execution plan, direct-use.** 200-char hard limit. Count in plain-text editor before sending. |
| 5 | Write data/linkedin_profiles.json — MANDATORY | One entry per lead searched (including PROFILE_NOT_FOUND entries). Write immediately after each search — do not batch. This is the only confirmation mechanism. |
| 6 | CHANGELOG.md update | **MANDATORY — 49+ days unlogged. Must complete before Tuesday Day-7 sends. Absolute deadline.** |

## HANDS Execution Order for TUESDAY 2026-05-19 (Batch 5 Day 7)

| Priority | Action | Condition |
|---|---|---|
| 1 | IMAP sweep — each Batch 5 lead before their individual Day-7 send | Per lead. NOT leads 1/3/22. |
| 2 | Day-7 new-angle sends — all Batch 5 leads (IMAP clean per lead) | **NEW standalone email — not thread reply. New subject. Different pain point. 09:00-10:30, 10-min stagger. Copy in daily_email_plan.json (day7_new_angle section).** |
| 3 | LinkedIn archive trigger — EOD Tuesday | Any Batch 5 lead without confirmed LinkedIn: archive LOST_NO_RESPONSE immediately. Log CHANGELOG. |

## Next BRAIN Runs
- **MONDAY 2026-05-18 EVENING** — If HANDS writes linkedin_profiles.json from Monday's execution: BRAIN generates per-lead personalised LinkedIn notes (post-reference preferred).
- **TUESDAY 2026-05-19 EVENING** — Day-14 breakup copy generation (for sends Tuesday 2026-05-26).
- **TUESDAY 2026-05-26 (Day 14)** — HANDS: Day-14 breakup sends 09:00-10:30 (copy from Tuesday evening BRAIN run).
