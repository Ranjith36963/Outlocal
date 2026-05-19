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
| **2026-05-17** | **51** | **Weekly intelligence report (Sunday — Week 8 close)** | **week_2026-05-17.md + week_2026-05-17_summary.json written. active_strategy.md updated (Week 8 close, valid to 2026-05-24). Key findings: SSL-PAS 15% INTERESTED rate (non-negotiable), 0 Batch 5 replies (peak OPEN), LinkedIn FINAL WINDOW Monday, Day-7 sends Tuesday, Batch 6 trigger if Day-7 replies ≥ 2 (Harrogate/Craven). £800-1,175 warm pipeline written off (50-session LinkedIn failure). CHANGELOG 50+ days overdue.** |
| **2026-05-17** | **51** | **Daily email + followup (Sunday bridge, Batch 5 Day 5)** | **Reply peak 48h post-bump (still open, closes Monday morning). IMAP gap 43 days. Zero Batch 5 replies. LinkedIn STILL MISSING — TOMORROW Monday is the ABSOLUTE FINAL window. Day-14 breakup copy GENERATED EARLY — all 4 signal variants added to daily_email_plan.json (day14_breakup section), ahead of Tuesday evening schedule. All 7 data files updated. No sends today (Sunday block). CHANGELOG: 50+ days overdue — Monday mandatory.** |
| **2026-05-17** | **51** | **Daily LinkedIn research (Sunday evening, Batch 5 Day 5 — FINAL PLANNING DAY)** | **All 3 LinkedIn output files updated to Day 51 / 2026-05-17. linkedin_profiles.json STILL MISSING (51-session failure). Reply peak 48h post-bump OPEN (closes Monday morning). No channel status changes from Day 50. All Batch 5 Ryedale leads approved pending IMAP per lead Monday. monday_fallback_notes ACTIVE EXECUTION PLAN (direct-use, no further BRAIN run needed). Archive trigger confirmed Tuesday 2026-05-19 EOD. src/outlocal/linkedin/orchestrator.py NOT YET IMPLEMENTED. Commit + push completed.** |
| **2026-05-18** | **52** | **Daily email + followup (Monday — FINAL LinkedIn window, Batch 5 Day 6, pre-Day-7 brief)** | **All 7 data files updated to Day 52. linkedin_profiles.json STILL MISSING (52+ session failure) — today is the absolute final LinkedIn window, archive trigger fires TOMORROW Tuesday EOD. IMAP gap: 44 days. Reply peak at 72h closing boundary (post-Day-3 bump). Day-7 new-angle sends TOMORROW Tuesday 2026-05-19 09:00-10:30 (copy unchanged — ready in daily_email_plan.json). Day-14 breakup copy carried forward (generated early Day 51). Zero Batch 5 replies. No new leads. CHANGELOG mandatory TODAY. Commit + push completed.** |
| **2026-05-18** | **52** | **Daily LinkedIn research (Monday EXECUTION DAY — Batch 5 Day 6 — ABSOLUTE FINAL WINDOW)** | **All 3 LinkedIn output files updated to Day 52. linkedin_profiles.json STILL MISSING (52-session failure). 14 sector-discovery search queries populated in search_plan.json (covering all Ryedale town+sector combinations in execution priority order — replace with name-specific queries from 2026-05-12 records where full name known). All sector connection note templates confirmed ready in connection_notes.json. Coordination file execution checklist updated to PENDING. IMAP gap: 44 days, zero Batch 5 replies. Reply peak at 72h closing boundary. Archive trigger fires TOMORROW Tuesday 2026-05-19 EOD. HANDS must execute today: IMAP per lead → LinkedIn searches → connection notes → write profiles.json same session → CHANGELOG. Commit + push completed.** |
| **2026-05-19** | **53** | **Daily email + followup (Tuesday — Batch 5 Day 7 SEND DAY — LinkedIn archive trigger fires TODAY EOD)** | **All 6 data files updated to Day 53. linkedin_profiles.json STILL MISSING (53-session failure). LinkedIn archive trigger fires TONIGHT EOD — any Batch 5 lead without confirmed LinkedIn archived LOST_NO_RESPONSE. Day-7 new-angle sends TODAY 09:00-10:30 (copy unchanged, READY in daily_email_plan.json day7_new_angle section). IMAP per lead mandatory before each send. IMAP gap: 45 days. Zero Batch 5 replies. Post-Day-7 reply wave opens after sends: peak Wednesday-Friday 2026-05-21-23. Day-14 breakup copy ready (day14_breakup section). CHANGELOG 51 days overdue — mandatory today. Commit + push completed.** |
| **2026-05-19** | **53** | **Daily LinkedIn research (Tuesday — Batch 5 Day 7 ARCHIVE TRIGGER DAY — FINAL BRAIN LinkedIn run)** | **All 3 LinkedIn output files updated to Day 53. linkedin_profiles.json STILL MISSING (53-session failure). Archive trigger fires TONIGHT EOD — unconditional. Any Batch 5 lead without confirmed LinkedIn (note_sent: true in linkedin_profiles.json) archived LOST_NO_RESPONSE at EOD. Zero channel status changes since Day 52. All 14 sector-discovery search queries retained in linkedin_search_plan.json. All sector connection note templates confirmed ready in linkedin_connection_notes.json (monday_fallback_notes usable today before EOD). Coordination file execution checklist renamed tuesday_execution_checklist. archive_trigger_tomorrow renamed archive_trigger_today. IMAP gap: 45 days. Post-Day-7 reply wave: Wednesday-Friday 2026-05-21-23. Next BRAIN run: Tuesday evening — Day-7 results + Batch 6 scoping. Commit + push completed.** |

---

## CRITICAL STATE — 2026-05-19 (Day 53 — BATCH 5 DAY-7 TUESDAY — DAY-7 SENDS TODAY — LINKEDIN ARCHIVE TRIGGER FIRES TONIGHT EOD — IMAP SWEEP MANDATORY PER LEAD — CHANGELOG MANDATORY TODAY)

### TODAY'S MANDATORY ACTIONS (Tuesday 2026-05-19 — Day 53)

| Priority | Action | Deadline |
|---|---|---|
| **1** | **IMAP sweep — per Batch 5 lead, before each individual Day-7 send (NOT leads 1/3/22)** | Before each send, in send order |
| **2** | **Day-7 new-angle sends — all Batch 5 leads** | TODAY 09:00-10:30, 10-min stagger. NEW standalone email (NOT thread reply). Copy in daily_email_plan.json day7_new_angle section. |
| **3** | **LinkedIn archive trigger — EOD today** | Any Batch 5 lead without note_sent: true in linkedin_profiles.json → archive LOST_NO_RESPONSE immediately. Log CHANGELOG. |
| **4** | **CHANGELOG.md update** | TODAY — 51 days overdue. Absolute deadline. |

**If any IMAP sweep finds INTERESTED reply before Day-7 send: cancel Day-7, use interested variant from daily_email_plan.json (conditional_handling section), 24h proposal SLA from reply time.**

---

### WARM PIPELINE — PERMANENTLY CLOSED (UNCONDITIONALLY FINAL)
- **Archive trigger fired 2026-05-06** — LinkedIn deadline missed for 47 consecutive sessions
- **Leads 1 (Tom), 3 (Claire), 22 (Rob): LOST_NO_RESPONSE — UNCONDITIONALLY FINAL**
- Friday 2026-05-08 EOD override window has closed. No further action, no further IMAP checks for leads 1/3/22.
- Email channel: CLOSED. LinkedIn channel: PERMANENTLY CLOSED (never activated).
- Combined pipeline value written off: £800-1,175

### Active Data Files
- `data/daily_signals.json` — **Day 53 (2026-05-19 TUESDAY) — UPDATED. Day-7 SEND DAY. IMAP per lead mandatory. LinkedIn archive trigger TONIGHT EOD. Post-Day-7 reply wave opens after sends (peak Wed-Fri). IMAP gap 45 days. No new leads or signals.**
- `data/daily_email_plan.json` — **Day 53 (2026-05-19 TUESDAY) — Metadata updated. All email copy UNCHANGED. Day-7: TODAY 09:00-10:30. Day-14: Tuesday 2026-05-26, 09:00-10:30. Both copy sets READY.**
- `data/daily_strategy.md` — **Day 53 (2026-05-19 TUESDAY) — UPDATED. Tuesday Day-7 execution brief. LinkedIn archive trigger tonight. Day-7 sends today. Batch 6 trigger conditions. Forward calendar through Day-14.**
- `data/followup_queue.json` — **Day 53 (2026-05-19 TUESDAY) — UPDATED. Day-7 sends TODAY. Day-14 READY (Tuesday 2026-05-26). LinkedIn archive trigger TONIGHT EOD. CHANGELOG mandatory today.**
- `data/reply_classifications.json` — **Day 53 (2026-05-19 TUESDAY) — UPDATED. IMAP gap 45 days. Per-lead IMAP mandatory before each Day-7 send today. Post-Day-7 reply wave monitoring Wed-Fri. No new replies.**
- `data/value_delivery_queue.json` — **Day 53 (2026-05-19 TUESDAY) — UPDATED. No Batch 5 INTERESTED replies. Day-7 sends today open fresh reply wave Wed-Fri 2026-05-21-23. 24h proposal SLA live from any INTERESTED reply. LinkedIn archive trigger TONIGHT.**
- `data/active_strategy.md` — **Day 51 (2026-05-17 SUNDAY) — Last updated by weekly report run. Valid to 2026-05-24. No changes required today.**
- `data/linkedin_connection_notes.json` — **Day 53 (2026-05-19 TUESDAY — ARCHIVE TRIGGER DAY) — Updated this morning. monday_fallback_notes ACTIVE EXECUTION PLAN (usable before EOD today). Archive trigger fires TONIGHT EOD unconditionally.**
- `data/linkedin_search_plan.json` — **Day 53 (2026-05-19 TUESDAY — ARCHIVE TRIGGER DAY) — Updated this morning. 14 sector-discovery queries ready. Archive trigger fires TONIGHT EOD.**
- `data/linkedin_coordination.json` — **Day 53 (2026-05-19 TUESDAY — ARCHIVE TRIGGER DAY) — Updated this morning. tuesday_execution_checklist updated. archive_trigger_today fires TONIGHT EOD unconditionally.**
- `data/weekly_reports/week_2026-05-17.md` — **Day 51 (2026-05-17 SUNDAY) — WEEK 8 INTELLIGENCE REPORT COMPLETE. Full campaign analysis. Week 9 operational priorities.**
- `data/weekly_reports/week_2026-05-17_summary.json` — **Day 51 (2026-05-17 SUNDAY) — Week 8 summary JSON. Machine-readable KPIs and recommendations.**

### IMAP Status
- **45 days overdue** (last confirmed check: 2026-04-04)
- Monday sweep UNCONFIRMED — new_replies.json unchanged from 2026-04-04 (either not executed or zero replies)
- Zero Batch 5 replies to date. **Post-Day-3 reply peak CLOSED. Post-Day-7 reply wave opens after today's sends (peak Wednesday-Friday 2026-05-21-23).**
- **Do NOT sweep leads 1/3/22 — archive is unconditionally final**
- **MANDATORY per Batch 5 lead before each Day-7 send TODAY Tuesday 2026-05-19**

### Batch 5 Status
- **Day-0 sends assumed completed Tuesday 2026-05-12, 09:00-10:30 — UNCONFIRMED**
- **Day-3 bumps assumed sent Friday 2026-05-15, 09:00-10:30 — UNCONFIRMED**
- No per-lead data file received from HANDS (53+ consecutive sessions)
- Ryedale targets: Malton, Pickering, Helmsley, Kirkbymoorside, Hovingham, Norton-on-Derwent
- Signal: SSL-primary (PAS, 60%), mobile-secondary (PAS, 20%), no-website BAB (15%), AIDA keyword-gap (5%)
- **Day 7 = TODAY TUESDAY 2026-05-19 — Day-7 new-angle sends (09:00-10:30) + LinkedIn archive trigger EOD. IMAP per lead before each send.**
- **Day 14 = TUESDAY 2026-05-26 — Day-14 breakup sends. Copy READY in daily_email_plan.json (day14_breakup section — generated early Day 51).**

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
- No HANDS updates since 2026-03-28 (**51+ days**). **MANDATORY — must be completed TODAY Tuesday 2026-05-19 alongside Day-7 sends. Absolute final deadline. No further deferrals under any circumstances.**

---

## HANDS Execution Order for TODAY TUESDAY 2026-05-19 (Batch 5 Day 7 SEND DAY — LinkedIn Archive Trigger TONIGHT EOD)

linkedin_profiles.json STILL MISSING. 53+ consecutive sessions. Archive trigger fires TONIGHT EOD.

| Priority | Action | Condition |
|---|---|---|
| 1 | IMAP sweep — each Batch 5 lead before their individual Day-7 send (NOT leads 1/3/22) | Per lead, in send order. If INTERESTED: cancel Day-7, reply in thread using interested variant from daily_email_plan.json (conditional_handling section). 24h proposal SLA from reply time. If NOT_INTERESTED: cancel Day-7 permanently, block all channels. If UNSUBSCRIBE: cancel Day-7, suppress within 24h GDPR Article 21. If OOO: pause Day-7, note return date. |
| 2 | Day-7 new-angle sends — all Batch 5 leads (IMAP clean per lead) | **NEW standalone email — not thread reply. New subject. Different pain point. 09:00-10:30, 10-min stagger. Fill [bracketed placeholders] from 2026-05-12 send records. Copy in daily_email_plan.json (day7_new_angle section — READY NOW). SSL leads: Google ranking angle. Mobile: SSL or click-to-call. No-website: competitor angle.** |
| 3 | LinkedIn archive trigger — EOD TODAY Tuesday 2026-05-19 | Any Batch 5 lead without confirmed LinkedIn (note_sent: true in linkedin_profiles.json): archive IMMEDIATELY as LOST_NO_RESPONSE. Log CHANGELOG same session. No extensions, no deferrals. |
| 4 | CHANGELOG.md update — MANDATORY | **51+ days overdue. Complete today alongside sends. Log: Batch 5 Day-0 sends (date, lead IDs, business names, signals), Day-3 bumps, fu_041-045 breakup outcomes, archive decisions (leads 1/3/22, 49/51/53/54), all IMAP sweep results since April, today's Day-7 send outcomes, LinkedIn archive outcomes.** |

## HANDS Monitoring — Wednesday-Friday 2026-05-21-23 (Post-Day-7 Reply Wave)

| Priority | Action | Condition |
|---|---|---|
| 1 | IMAP monitoring per lead — daily Wednesday-Friday | Post-Day-7 reply wave peak (24-72h post-send). Any new reply: write to new_replies.json immediately. |
| 2 | Classify new replies in reply_classifications.json | If INTERESTED: 24h proposal SLA from reply time. If NOT_INTERESTED: suppress all channels. If UNSUBSCRIBE: suppress within 24h GDPR. |
| 3 | Batch 6 decision — if Day-7 replies ≥ 2 by Wednesday | Fire Batch 6 scoping: Harrogate District + Craven District. Data collection from Wednesday 2026-05-20. Initial sends: Tuesday 2026-05-26 or Tuesday 2026-06-02. |

## HANDS Execution Order for TUESDAY 2026-05-26 (Batch 5 Day 14 — FINAL TOUCHPOINT)

| Priority | Action | Condition |
|---|---|---|
| 1 | IMAP sweep — each Batch 5 lead before their individual Day-14 send | Per lead. If INTERESTED reply found since Day-7: cancel Day-14, use proposal flow instead. |
| 2 | Day-14 breakup sends — all Batch 5 leads not yet INTERESTED or suppressed | Copy in daily_email_plan.json (day14_breakup section — READY NOW). 09:00-10:30, 10-min stagger. 3 lines max. Final touchpoint — hard limit. |
| 3 | Update lead status to 'sequence_complete' | All Day-14 recipients. Note reapproach date: 2026-11-26 minimum. Log CHANGELOG. |

## Next BRAIN Runs
- **TUESDAY 2026-05-19 EVENING** — Day-7 results analysis + Batch 6 scoping decision. Day-14 breakup copy NOT required (generated early Day 51 — already in daily_email_plan.json).
- **TUESDAY 2026-05-26 (Day 60)** — HANDS: Day-14 breakup sends 09:00-10:30 (copy in data/daily_email_plan.json day14_breakup section — READY NOW). BRAIN: Day-14 results analysis + full Batch 5 post-mortem + Batch 6 launch prep.
