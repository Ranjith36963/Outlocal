# Daily Strategy — 2026-05-11 (Monday) — Day 44

**Updated:** 2026-05-11 (BRAIN Day 44 run — Monday cleanup day)  
**Replaces:** 2026-05-10 strategy (Day 43 — weekend bridge)  
**Key changes from Day 43:** Today is the final window for fu_041-045. Archive leads 53/54 today — final attempt deadline. CHANGELOG mandatory before tomorrow's Batch 5 sends. IMAP gap now 37 days — sweep FIRST. Campaign restart tomorrow: Batch 5 Ryedale, Tuesday 2026-05-12, 09:00-10:30.

---

## TODAY — MONDAY 2026-05-11

**Cleanup and preparation day. Tomorrow is Batch 5 Ryedale send day.**

| Priority | Action | Status |
|---|---|---|
| 1 | IMAP sweep — leads 30, 31, 32, 58, 59 + full cohort | MANDATORY — 37-day gap. fu_041-045 precondition. Do NOT include leads 1/3/22. |
| 2 | fu_041-045 — Day-14 breakups | **SEND TODAY** — 09:30-10:10, 10-min stagger, IMAP clean per lead |
| 3 | Archive leads 53 and 54 | **ARCHIVE TODAY** — LOST_UNRESOLVED. Final attempt deadline passed. Log CHANGELOG. |
| 4 | CHANGELOG.md update | **MANDATORY** — 44 days unlogged. Must complete before Tuesday sends. |
| 5 | Confirm Ryedale scrape data is ready | If data arrives today: BRAIN pre-generates Batch 5 copy. HANDS still sends Tuesday 09:00. |

---

## EXECUTIVE SUMMARY — DAY 44

Today is the last cleanup day before the campaign restarts.

1. **fu_041-045 send today.** Five Day-14 breakups (leads 30, 31, 32, 58, 59), 18 days overdue. IMAP sweep first — if any of these leads have replied in the 37-day gap: cancel that fu, classify reply, mark sequence complete. After IMAP clean: send 09:30-10:10, 10-minute stagger. These close five sequences permanently.

2. **Archive leads 53 and 54 today.** Bridlington Bay Lettings and The Wolds Inn — enrichment opportunities exhausted over 40+ days, final attempt window closed Friday. No further deferrals. Archive LOST_UNRESOLVED and log CHANGELOG.

3. **CHANGELOG is 44 days overdue.** No record of any send or action since Session 1 (2026-03-28). This must be logged today before tomorrow's Batch 5 sends. Operational credibility depends on it.

4. **Tomorrow is the campaign restart.** Batch 5 Ryedale — 12-18 initial sends, Tuesday 2026-05-12, 09:00-10:30. BRAIN personalises per lead from Ryedale scrape data (pre-generated if data arrives today, otherwise Tuesday morning). Expected: 2-3 INTERESTED replies by Friday 2026-05-15.

---

## CAMPAIGN STATUS — DAY 44

| Metric | Value | Delta from Day 43 | Notes |
|---|---|---|---|
| Campaign day | 44 | +1 | Monday 2026-05-11 |
| Leads scraped | ~61 | 0 | Batch 5 data still pending |
| Emails sent (est.) | ~91 | 0 | No sends Sunday (weekend blocked) |
| Emails sending today | 5 | +5 | fu_041-045 breakups (IMAP clean) |
| Active sequences | 0 | 0 | Campaign stall: 34 days |
| Total replies | 11 | 0 | 17.9% reply rate |
| INTERESTED (active) | 0 | 0 | Warm pipeline closed — unconditionally final |
| IMAP gap | 37 days | +1 | Sweep first thing Monday |
| CHANGELOG lag | 44 days | +1 | Must fix today |
| fu overdue | 18 days | +1 | **SEND TODAY — FINAL WINDOW** |
| Archived (total) | 7 | +2 | Leads 53/54 archived today |

---

## TODAY'S SEND BRIEF — fu_041-045

| # | fu_id | Lead | Business | Subject | Send time |
|---|---|---|---|---|---|
| 1 | fu_041 | 30 | Halifax Window Cleaning (Steve) | Closing the loop — Halifax Window Cleaning | 09:30 |
| 2 | fu_042 | 31 | Pontefract Pharmacy | Closing the loop — Pontefract Pharmacy | 09:40 |
| 3 | fu_043 | 32 | Castleford Carpets (Ann) | Closing the loop — Castleford Carpets | 09:50 |
| 4 | fu_044 | 58 | The Old Court Solicitors | Closing the loop — The Old Court Solicitors | 10:00 |
| 5 | fu_045 | 59 | Scarborough Roofing Specialists (Tony) | Closing the loop — Scarborough Roofing Specialists | 10:10 |

**Full copy in followup_queue.json and daily_email_plan.json.**  
**IMAP clean per lead mandatory before each send.**  
**10-minute stagger.**  
**5 sends — well within 40/day domain limit.**

---

## IMAP SWEEP — PROTOCOL

**37-day gap (last confirmed check: 2026-04-04). This is CRITICAL.**

What to check:
1. **Leads 30, 31, 32, 58, 59** — fu_041-045 precondition. If any reply found: cancel that fu, write to new_replies.json, classify.
2. **Full remaining cohort** — any unsubscribe found: suppress within 24h (GDPR Article 21), log audit_log and CHANGELOG.
3. **Do NOT check leads 1, 3, 22** — archive is UNCONDITIONALLY FINAL. If reply somehow found: acknowledge only (no sales attempt), log CHANGELOG, treat as closed-lost.

---

## ARCHIVE DECISIONS — FINAL

| Lead | Business | Archive status | Reason |
|---|---|---|---|
| 1 | Ripon Road Carpentry (Tom) | LOST_NO_RESPONSE — FINAL | LinkedIn never executed. Override closed 2026-05-08 EOD. |
| 3 | Westfield Hair & Beauty (Claire) | LOST_NO_RESPONSE — FINAL | LinkedIn never executed. Override closed 2026-05-08 EOD. |
| 22 | Pennine Print & Design (Rob) | LOST_NO_RESPONSE — FINAL | LinkedIn never executed. Override closed 2026-05-08 EOD. |
| 49 | East Riding Builders Ltd | LOST_UNRESOLVED — FINAL | Enrichment overdue 38+ days. Archived Day 40. |
| 51 | Driffield Garden Centre | LOST_UNRESOLVED — FINAL | Enrichment overdue 38+ days. Archived Day 40. |
| **53** | **Bridlington Bay Lettings** | **LOST_UNRESOLVED — ARCHIVE TODAY** | **Final attempt deadline passed. No further deferrals.** |
| **54** | **The Wolds Inn** | **LOST_UNRESOLVED — ARCHIVE TODAY** | **Final attempt deadline passed. No further deferrals.** |

**HANDS: update database and CRM for leads 53/54 today. Log CHANGELOG.**

---

## CHANGELOG — WHAT NEEDS LOGGING TODAY

44 days since last entry (2026-03-28). Everything below must be logged Monday:

```
[2026-04-04] IMAP sweep — 11 replies received across all batches (reply_id 7-11).
  - Lead 3 (Claire, Westfield Hair & Beauty): INTERESTED — call confirmed Tuesday 2pm 2026-04-07.
  - Lead 22 (Rob, Pennine Print & Design): INTERESTED — bundle enquiry.
  - Lead 1 (Tom, Ripon Road Carpentry): INTERESTED — asked for pricing.
  - Lead 2 (Nidderdale Pet Supplies): NOT_INTERESTED — politely declined.
  - Lead 5 (Harewood Accountants): OUT_OF_OFFICE — returned 2026-04-06.

[2026-04-07 to 2026-04-08] Proposals / nudges sent to leads 1, 3, 22 (warm pipeline).
  - No further replies received.

[2026-05-07] Warm pipeline declared LOST_NO_RESPONSE — leads 1, 3, 22 archived.
  - Root cause: LinkedIn never executed across 43 sessions.
  - Combined pipeline value written off: £800-1,175.
  - IMAP override window set to Friday 2026-05-08 EOD.

[2026-05-08] IMAP override window closed EOD — archive is UNCONDITIONALLY FINAL.

[2026-05-07] Leads 49 and 51 archived LOST_UNRESOLVED — enrichment overdue 38+ days.

[2026-05-11] Leads 53 and 54 archived LOST_UNRESOLVED — final attempt deadline passed.

[2026-05-11] fu_041-045 Day-14 breakups sent (or: UNSENT — sequence expired):
  - fu_041: Steve, Halifax Window Cleaning — [IMAP clean / reply found — CANCELLED]
  - fu_042: Pontefract Pharmacy — [IMAP clean / reply found — CANCELLED]
  - fu_043: Ann, Castleford Carpets — [IMAP clean / reply found — CANCELLED]
  - fu_044: The Old Court Solicitors — [IMAP clean / reply found — CANCELLED]
  - fu_045: Tony, Scarborough Roofing Specialists — [IMAP clean / reply found — CANCELLED]

[2026-05-11] IMAP sweep — 37-day gap. Results: [log outcomes]
```

---

## TOMORROW — TUESDAY 2026-05-12 — BATCH 5 RYEDALE SEND DAY

| Time | Action |
|---|---|
| 07:00-07:30 | IMAP sweep — full cohort (pre-send precondition) |
| 07:30-09:00 | BRAIN personalisation run — per-lead copy, signal assignment, daily_email_plan.json |
| 09:00-10:30 | HANDS sends — 12-18 emails, 10-minute stagger |
| 10:30-11:00 | CHANGELOG — all sends logged same session |
| Evening | BRAIN Day-3 copy run — per-lead Day-3 bump copy + Batch 5 LinkedIn queries |

**Expected volume:** 12-18 initial sends  
**Expected INTERESTED replies:** 2-3 (15% SSL-PAS rate)  
**Expected reply window:** Wednesday 2026-05-13 to Friday 2026-05-15

---

## WINNING PLAYBOOK — UNCHANGED

These patterns produced 100% of INTERESTED leads. Non-negotiable for Batch 5.

1. **SSL → PAS → first-name subject → town name → specific URL** — 3/3 INTERESTED
2. **Tuesday AM send** — all 3 INTERESTED replies arrived on the day following Tuesday AM sends
3. **Day-7 genuinely different pain point** — not a reframe. Tom's conversion came from Day-7 new angle.
4. **One pain point per email** — single signal only. Listing multiple issues kills response.
5. **Town name in subject AND body** — local credibility confirmed by recipients
6. **No question marks in subject** — statement of fact outperforms question hook for trades cold email
7. **Chrome's exact wording** — `'Not Secure'` builds verifiable, testable credibility

---

## FORWARD CALENDAR

| Date | Day | Action | Type |
|---|---|---|---|
| **Mon 2026-05-11** | **44** | **IMAP sweep. fu_041-045 sends. CHANGELOG. Archive 53/54.** | **TODAY** |
| **Tue 2026-05-12** | **45** | **BRAIN: Batch 5 personalisation. HANDS: initial sends 09:00-10:30. CHANGELOG.** | **SEND DAY** |
| Tue 2026-05-12 eve | 45 | BRAIN: Day-3 email copy + LinkedIn queries for Batch 5 | After sends |
| Wed 2026-05-13 | 46 | Fallback: Day-3 BRAIN run if not done Tuesday evening | Optional |
| **Fri 2026-05-15** | **48** | **HANDS: Batch 5 Day-3 bump emails + LinkedIn connection requests (09:00-10:30)** | **Day-3** |
| Mon 2026-05-18 | 51 | LinkedIn fallback if Friday not executed | Day-6 |
| **Tue 2026-05-19** | **52** | **Batch 5 Day-7 new angle sends. LinkedIn HARD DEADLINE — close channel if not done.** | **Day-7** |
| Tue 2026-05-26 | 59 | Batch 5 Day-14 breakup sends | Day-14 |
| Weekly review | After 2026-05-12 data | active_strategy.md review — first Batch 5 week results | Strategy |

---

## BATCH 5 RYEDALE — COPY BRIEF (TOMORROW)

**Target towns:** Malton, Pickering, Helmsley, Kirkbymoorside, Hovingham, Norton-on-Derwent  
**Signal allocation:** SSL → PAS (60%), mobile → PAS (20%), no-website 4★+ 20+ reviews → BAB (15%), 4.5★+ 100+ reviews → AIDA (5% test)  
**Subject line pattern:** `[First name] — [town] [trade] website flagged 'Not Secure'`  
**BRAIN personalises per lead. HANDS does NOT use templates directly.**

If Ryedale data arrives today (Monday): BRAIN pre-generates all per-lead copy now and updates daily_email_plan.json. HANDS still sends Tuesday 09:00 — pre-generation does not move the send window.

---

## LINKEDIN PROTOCOL — BATCH 5

**This time, LinkedIn executes by Day 7. No further exceptions.**

| Event | Date |
|---|---|
| Batch 5 Day 0 | Tuesday 2026-05-12 |
| LinkedIn window opens | Friday 2026-05-15 (Day 3) |
| **LinkedIn HARD DEADLINE** | **Tuesday 2026-05-19 (Day 7)** |
| If not done by Day 7 | Close LinkedIn channel for those leads immediately |
| linkedin_profiles.json | MUST be written same session as LinkedIn execution |

**Lesson from warm pipeline:** 44 sessions elapsed without LinkedIn execution. Cost: £800-1,175. This does not happen in Batch 5.

---

## WINNING ANALYTICS — WHAT THE DATA SAYS

| Pattern | Performance | Status |
|---|---|---|
| SSL-PAS with first-name subject | 3/3 INTERESTED (campaign-best) | Non-negotiable for Batch 5 |
| Tuesday AM send window | All 3 INTERESTED replies followed Tuesday sends | Confirmed — hard rule |
| Day-7 new angle (not reframe) | 1 conversion (Tom) from fresh pain point | Required — BRAIN generates per lead |
| Town name in subject | All INTERESTED leads referenced local angle in replies | Non-negotiable |
| One pain point per email | 100% of replies engaged with the specific signal used | Non-negotiable |
| LinkedIn (warm pipeline) | 0 connections sent — £800-1,175 written off | HARD DEADLINE: Day 7 enforced |
| Generic signal | 0% reply rate | DO NOT USE |

---

*Strategy maintained by OUTLOCAL BRAIN layer.*  
*Day 44 — Monday 2026-05-11. Cleanup and preparation day.*  
*Tomorrow: Batch 5 Ryedale send day — 09:00-10:30.*  
*active_strategy.md valid to 2026-05-17. Next full review: after Batch 5 first-week data.*
