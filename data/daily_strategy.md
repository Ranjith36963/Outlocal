# Daily Strategy — 2026-05-15 (Friday) — Day 48

**Updated:** 2026-05-15 (BRAIN Day 48 run — Friday evening, Batch 5 Day 3)  
**Replaces:** 2026-05-14 strategy (Day 47 — Thursday evening)  
**Key changes from Day 47:** Day-3 bumps assumed sent today (UNCONFIRMED). LinkedIn UNCONFIRMED (profiles.json missing) — Monday 2026-05-18 is last window. Day-7 new-angle copy now ready. Reply peak opens now (Saturday-Monday post-bump). CHANGELOG: 48 days overdue — absolute deadline before Tuesday Day-7 sends.

---

## 🚨 CRITICAL ALERTS — DAY 48

### ALERT 1: LinkedIn Execution Unconfirmed (48 Sessions)
`data/linkedin_profiles.json` was NOT written by HANDS today. LinkedIn execution is UNCONFIRMED.  
This is the same failure mode that cost £800-1,175 in the warm pipeline.

**Monday 2026-05-18 is the last window. Archive trigger fires Tuesday 2026-05-19 EOD. No deferrals.**

### ALERT 2: CHANGELOG 48 Days Overdue
Must be completed **before Tuesday 2026-05-19 Day-7 sends**. Absolute deadline. Not optional.

### ALERT 3: active_strategy.md Expires Sunday
Full strategy review due Sunday/Monday 2026-05-17-18 with first Batch 5 results.

---

## MONDAY EXECUTION ORDER — 2026-05-18 (LAST LINKEDIN WINDOW)

| Priority | Action | Condition |
|---|---|---|
| 1 | Check linkedin_profiles.json — does it exist? | If YES: LinkedIn done Friday. Skip to priority 4. If NO: execute LinkedIn today. |
| 2 | IMAP sweep — each Batch 5 lead before LinkedIn | Per lead before note send |
| 3 | LinkedIn connection requests — all Batch 5 leads | Last window. Archive trigger fires Tuesday EOD. See linkedin_connection_notes.json (monday_fallback_notes section). |
| 4 | Write data/linkedin_profiles.json | MANDATORY same session. One entry per lead searched. |
| 5 | CHANGELOG.md update | Must be done before Tuesday Day-7 sends. 48 days overdue. |

---

## EXECUTIVE SUMMARY — DAY 48

Day-3 bumps assumed sent today (09:00-10:30 — UNCONFIRMED). LinkedIn execution unconfirmed. Reply peak opens now.

**The critical path for the next 96 hours:**

**Weekend (Sat-Mon):** Monitor inbox. Day-3 bump peak reply window is 24-72 hours post-send. If INTERESTED reply arrives over the weekend: prepare proposal immediately (24h SLA runs from reply time). Do not wait for Monday.

**Monday morning:** If linkedin_profiles.json is missing — execute LinkedIn immediately. Write profiles.json same session. Update CHANGELOG.

**Tuesday 09:00:** IMAP per lead → Day-7 new-angle sends → LinkedIn archive trigger fires EOD for any leads without confirmed LinkedIn.

The Day-7 new-angle email copy is ready in `data/daily_email_plan.json` (day7_new_angle section). HANDS fills placeholders from send records.

---

## CAMPAIGN STATUS — DAY 48

| Metric | Value | Delta from Day 47 | Notes |
|---|---|---|---|
| Campaign day | 48 | +1 | Friday 2026-05-15 |
| Leads scraped | ~61+ Batch 5 | 0 confirmed | Batch 5 Ryedale assumed — HANDS confirmation not received |
| Emails sent (est.) | ~91 + 12-18 Batch 5 Day-0 + 12-18 Day-3 bumps | +12-18 assumed today | Day-3 bumps assumed sent — UNCONFIRMED |
| Batch 5 Day-3 bumps | 12-18 (assumed sent today) | — | UNCONFIRMED. If not sent: send Monday. |
| Active sequences | Batch 5 Day-3 assumed complete | — | Day-7 sends Tuesday 2026-05-19 |
| Batch 5 replies | 0 confirmed | 0 | Reply peak window now open (post-bump) |
| INTERESTED (active) | 0 | — | Warm pipeline permanently closed |
| IMAP gap (from confirmed) | 41 days | +1 | Friday sweep assumed clean — UNCONFIRMED |
| CHANGELOG lag | 48 days | +1 | **MANDATORY before Tuesday** |
| LinkedIn executed | 0 in 48 sessions | 0 | **MONDAY IS LAST WINDOW — ARCHIVE TRIGGER FIRES TUESDAY EOD** |

---

## DAY-7 SEND BRIEF — TUESDAY 2026-05-19

**Send window:** 09:00-10:30  
**Stagger:** 10 minutes between sends  
**Type:** Standalone NEW email — NOT a thread reply. New subject. New pain point.  
**IMAP precondition:** Per lead before each send

| Signal | Day-7 Angle | Subject pattern | Key phrase |
|---|---|---|---|
| **SSL** | Google local ranking penalty | "[First name] — the 'Not Secure' warning is also a Google ranking issue for [business name]" | 'ranking lower when someone searches for [trade] in [town]' |
| **Mobile** | SSL for ALL visitors (or click-to-call gap) | "[First name] — [business name]: one more issue I noticed on the website" | 'not just mobile users — every visitor' |
| **No-website** | Named competitor ranking / missed enquiries | "Following up — who's getting the [trade] calls in [town]" | 'those are enquiries that could be going to [business name]' |
| **AIDA** | Reviews not converting to ranking | "[First name] — [business name] has [N] great reviews but low search visibility in [town]" | 'not ranking for [keyword] in [town]' |

**Full copy with body text in data/daily_email_plan.json → day7_new_angle section.**

---

## LINKEDIN BRIEF — MONDAY 2026-05-18 (FALLBACK — LAST WINDOW)

**Status:** Friday execution UNCONFIRMED (linkedin_profiles.json missing)  
**Monday IS the last window. Archive trigger fires Tuesday 2026-05-19 EOD.**  
**Order of operations:** IMAP sweep per lead → LinkedIn searches → Connection requests → Write profiles.json

| Step | Action |
|---|---|
| 1 | Check if linkedin_profiles.json exists — if YES, LinkedIn done Friday. Skip to step 5. |
| 2 | IMAP sweep each Batch 5 lead before their note |
| 3 | Open LinkedIn profile (queries in linkedin_search_plan.json) |
| 4 | Check posts from last 60 days BEFORE writing note |
| 5 | Post found: write bespoke post_reference note (3-4x acceptance). No post: use sector note from linkedin_connection_notes.json (monday_fallback_notes section) |
| 6 | Send connection request — 200-char hard limit |
| 7 | Write entry to data/linkedin_profiles.json immediately — mandatory |

**Sector priority:** Solicitors → Estate agents → Hotels/B&Bs → Restaurants → Boutique retail → Trades  
**Town priority:** Malton → Helmsley → Pickering → Kirkbymoorside → Norton-on-Derwent → Hovingham

**Rules (non-negotiable):**
- Do NOT mention email outreach, SSL, mobile, 'Not Secure', or any technical finding
- Start with their name. Never start with 'I'.
- No exclamation marks. No 'reach out', 'synergies', 'I came across your profile'.
- Post-reference is strongly preferred. Check posts FIRST.
- End with low-pressure framing: 'in case it's useful' or 'connecting in case relevant'

---

## LINKEDIN HARD DEADLINE — NON-NEGOTIABLE

**Tuesday 2026-05-19 is Day 7. Archive trigger fires EOD for any Batch 5 lead without confirmed LinkedIn.**

The warm pipeline failure (48 sessions, £800-1,175) must not repeat. Hard deadlines are enforced with zero tolerance.

- Day 3 (Friday 2026-05-15) — assumed. UNCONFIRMED.
- Day 6 (Monday 2026-05-18) — **LAST WINDOW. MANDATORY if Friday missed.**
- Day 7 (Tuesday 2026-05-19) — archive trigger. No deferral. No extensions.

---

## IMAP STATUS — DAY 48

**41-day gap from confirmed check (2026-04-04).** Friday sweep assumed clean (new_replies.json unchanged). This is consistent with either (a) clean sweep — no Batch 5 replies in first 3 days (normal) or (b) sweep not run. Weekend monitoring recommended.

**Post-bump reply peak:** Day-3 bumps assumed sent today. 24-72 hours post-bump is the peak window. Most first replies from cold email arrive in this window after a bump.

**Weekend IMAP monitoring:** If HANDS has IMAP access Saturday or Sunday: sweep Batch 5 leads. An INTERESTED reply over the weekend enables a Monday morning proposal.

**Handling rules (all IMAP checks):**
- INTERESTED reply found: use interested variant (daily_email_plan.json), write to new_replies.json, classify, prepare proposal within 24 hours (from reply time — 24/7 SLA)
- NOT_INTERESTED: cancel remaining sends, block all channels, log CHANGELOG
- UNSUBSCRIBE: suppress within 24h (GDPR Article 21), log audit_log and CHANGELOG
- OOO: note return date, pause sequence, resume Day-7 day after return (within 14-day window)
- WRONG_PERSON: pause, investigate, log CHANGELOG

---

## WINNING ANALYTICS — WHAT THE DATA SAYS

| Pattern | Performance | Status |
|---|---|---|
| SSL-PAS with first-name subject | 3/3 INTERESTED (campaign-best) | Non-negotiable for Batch 5 |
| Tuesday AM send window | All 3 INTERESTED replies followed Tuesday sends | Confirmed — hard rule (Batch 5 Day-0 executed Tuesday) |
| Day-7 new angle (not reframe) | 1 conversion (Tom) from fresh pain point | READY — Day-7 copy in daily_email_plan.json. Tuesday 2026-05-19. |
| Town name in subject | All INTERESTED leads referenced local angle in replies | Non-negotiable |
| One pain point per email | 100% of replies engaged with the specific signal used | Non-negotiable |
| LinkedIn (warm pipeline) | 0 connections sent in 48 sessions — £800-1,175 written off | HARD DEADLINE: Tuesday EOD. Zero tolerance. |
| Generic signal | 0% reply rate | DO NOT USE |
| 24-hour proposal SLA | Tom asked for pricing — never received it (lost) | MANDATORY for Batch 5 INTERESTED replies |
| Day-3 bump effect | Not yet measured for Batch 5 | First data point: post-bump replies Saturday-Monday |

## BATCH 5 PERFORMANCE EXPECTATIONS

Based on Batches 1-4 (11 replies / ~61 leads, 17.9% overall):

| Metric | Expected | Basis |
|---|---|---|
| Day-3 reply rate (post-bump) | 8-12% | Historical: bumps lift total reply rate by ~50% |
| Total interested (full sequence) | 2-3 | 15% SSL-PAS rate on 12-18 sends |
| Expected revenue if converted | £300-1,050 | Option B pricing: SSL+mobile (£150-200), no-website (£500) |
| Reply window post-bump | Saturday-Monday | 24-72h peak consistently observed |

First Batch 5 data signal arrives this weekend. Full strategy review Sunday/Monday 2026-05-17-18.

---

## FORWARD CALENDAR

| Date | Day | Action | Type |
|---|---|---|---|
| **Fri 2026-05-15** | **48** | **BRAIN: Day-7 copy ready. HANDS: Day-3 bumps assumed sent. LinkedIn UNCONFIRMED.** | **TODAY (BRAIN complete)** |
| Sat-Sun 2026-05-16-17 | 49-50 | HANDS: Weekend IMAP monitoring recommended (post-bump reply peak) | Monitoring |
| **Sun/Mon 2026-05-17-18** | **50-51** | **active_strategy.md full weekly review — due Sunday or Monday** | **Strategy** |
| **Mon 2026-05-18** | **51** | **HANDS: LinkedIn LAST WINDOW if Friday missed. CHANGELOG mandatory. profiles.json required.** | **CRITICAL — Day 6** |
| Mon 2026-05-18 eve | 51 | BRAIN: Per-lead LinkedIn note generation (IF linkedin_profiles.json received) | After HANDS session |
| **Tue 2026-05-19** | **52** | **HANDS: IMAP per lead → Day-7 sends 09:00-10:30. LinkedIn archive trigger fires EOD.** | **DAY 7 — CRITICAL** |
| Tue 2026-05-19 eve | 52 | BRAIN: Day-14 breakup copy generation | After sends |
| **Tue 2026-05-26** | **59** | **HANDS: Day-14 breakup sends 09:00-10:30.** | **DAY 14** |

---

## BATCH 5 RYEDALE — STATUS

**Assumed sent (Day-0):** Tuesday 2026-05-12, 09:00-10:30 (UNCONFIRMED — HANDS confirmation not received)  
**Day-3 bumps:** Assumed sent Friday 2026-05-15, 09:00-10:30 (UNCONFIRMED)  
**Sends assumed:** 12-18 leads across Malton, Pickering, Helmsley, Kirkbymoorside, Hovingham, Norton-on-Derwent  
**Signal mix:** SSL-PAS (60%), mobile-PAS (20%), no-website-BAB (15%), AIDA keyword-gap (5%)  
**Expected interested:** 2-3 (15% SSL-PAS historical rate)  
**Reply peak:** Saturday 2026-05-16 — Monday 2026-05-18 (post-bump)  
**Day-7 sends:** Tuesday 2026-05-19 — copy READY in daily_email_plan.json  
**LinkedIn:** UNCONFIRMED — Monday fallback mandatory if Friday missed. Hard deadline Tuesday EOD.

---

## COMPLIANCE REMINDERS

- IMAP sweep before every send — 40-day gap is a compliance risk
- Unsubscribes: suppress within 24 hours (GDPR Article 21), log audit_log
- 4-touchpoint maximum — hard limit, no exceptions
- LinkedIn: do not approach leads who replied NOT_INTERESTED on any channel
- B2B only — business emails, legitimate interest basis
- OOO pauses are mandatory — never re-send during stated OOO period

---

## ACTIVE STRATEGY VALIDITY

`data/active_strategy.md` is valid until 2026-05-17. Full weekly review is due **Sunday or Monday** with first Batch 5 results.

If Day-3 bump reply data is available by Monday: update strategy based on actual Batch 5 response patterns. Extend validity to 2026-05-24. Update geographic focus for Batch 6 based on Ryedale sector performance.

---

*Strategy maintained by OUTLOCAL BRAIN layer.*  
*Day 48 — Friday 2026-05-15. Batch 5 Day 3 evening.*  
*Day-7 new-angle copy is ready. LinkedIn Monday is the last window.*  
*Reply peak opens now. Monitor inbox Saturday-Monday.*  
*active_strategy.md valid to 2026-05-17. Next full review: Sunday/Monday 2026-05-17-18.*
