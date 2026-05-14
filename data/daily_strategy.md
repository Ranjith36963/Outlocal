# Daily Strategy — 2026-05-14 (Thursday) — Day 47

**Updated:** 2026-05-14 (BRAIN Day 47 run — Thursday evening, eve of Day-3)  
**Replaces:** 2026-05-11 strategy (Day 44 — Monday cleanup day)  
**Key changes from Day 44:** Batch 5 Ryedale assumed sent Tuesday 2026-05-12. Day-3 is TOMORROW (Friday 2026-05-15). LinkedIn window opens tomorrow — hard deadline Tuesday 2026-05-19. IMAP gap: 40 days. CHANGELOG: 47 days overdue — mandatory Friday.

---

## TOMORROW — FRIDAY 2026-05-15 (BATCH 5 DAY 3)

**Day 3 of Batch 5 Ryedale. Email bumps + LinkedIn. This day defines whether Batch 5 produces revenue.**

| Priority | Action | Status |
|---|---|---|
| 1 | IMAP sweep — all Batch 5 Ryedale leads (NOT leads 1/3/22) | FIRST — 40-day gap. Precondition for bumps and LinkedIn. |
| 2 | Day-3 email bumps — thread reply per lead (signal-specific, 3-4 lines) | **SEND TOMORROW 09:00-10:30 — copy in daily_email_plan.json** |
| 3 | LinkedIn connection requests — all Batch 5 leads where profile confirmed | **EXECUTE TOMORROW — after bumps. 1-hour gap. Hard deadline Tue 2026-05-19.** |
| 4 | Write data/linkedin_profiles.json | **MANDATORY — same session as LinkedIn. No exceptions.** |
| 5 | CHANGELOG.md update | **MANDATORY — 47 days overdue. Log all sends, IMAP results, LinkedIn outcomes.** |

---

## EXECUTIVE SUMMARY — DAY 47

Tomorrow is the most operationally important day since the campaign started. Five things must happen in sequence.

**1. IMAP sweep first.** 40-day gap — inbox state is unknown. Sweep every Batch 5 Ryedale lead before sending their bump. If INTERESTED reply found: use the interested variant (daily_email_plan.json), write to new_replies.json, prepare proposal within 24 hours. If NOT_INTERESTED: cancel bump, block LinkedIn, log CHANGELOG. If UNSUBSCRIBE: suppress within 24h (GDPR Article 21).

**2. Day-3 bumps 09:00-10:30.** Thread reply to original Day-0 email. 3-4 lines. Reference the exact signal from Day-0 (URL for SSL leads; business name for mobile leads; trade + town for no-website). Not a restatement of the full pitch. No new angles. 10-minute stagger. Copy is ready in daily_email_plan.json — HANDS fills placeholders from send records.

**3. LinkedIn connection requests — after bumps, 1-hour gap.** Check each profile for posts from the last 60 days BEFORE writing the note. Post-reference note has 3-4x higher acceptance rate. 200-character hard limit. Do NOT reference email, SSL, mobile, or any audit finding in the note. See linkedin_connection_notes.json for sector templates and note strategy.

**4. Write linkedin_profiles.json same session.** One entry per lead searched. If not written: LinkedIn execution is unconfirmed (same failure mode as warm pipeline). This step is non-negotiable.

**5. CHANGELOG.md before close of Friday session.** 47 days unlogged. All Batch 5 Day-0 sends, fu_041-045 outcomes, archive decisions, today's IMAP results, today's bump sends, today's LinkedIn outcomes. If not done Friday: absolute latest is Monday 2026-05-18 (must be complete before Day-7 sends on Tuesday 2026-05-19).

---

## CAMPAIGN STATUS — DAY 47

| Metric | Value | Delta from Day 44 | Notes |
|---|---|---|---|
| Campaign day | 47 | +3 | Thursday 2026-05-14 |
| Leads scraped | ~61+ Batch 5 | 0 confirmed | Batch 5 Ryedale assumed added — pending HANDS confirmation |
| Emails sent (est.) | ~91 + 12-18 Batch 5 Day-0 | +12-18 assumed | Batch 5 Day-0 assumed Tuesday — unconfirmed |
| Day-3 bumps sending tomorrow | 12-18 | — | Friday 2026-05-15, 09:00-10:30 |
| Active sequences | 0 legacy + Batch 5 | — | Batch 5 Day-3 tomorrow |
| Total replies | 11 legacy + 0 Batch 5 | 0 confirmed | IMAP gap 40 days — batch 5 replies may exist unread |
| INTERESTED (active) | 0 legacy (closed) | — | Warm pipeline permanently closed |
| IMAP gap | 40 days | +3 | Sweep tomorrow FIRST |
| CHANGELOG lag | 47 days | +3 | **MANDATORY Friday** |
| LinkedIn executed | 0 in 47 sessions | 0 | **TOMORROW OR ARCHIVE TRIGGER FIRES Tuesday** |

---

## DAY-3 SEND BRIEF — FRIDAY 2026-05-15

**Send window:** 09:00-10:30  
**Stagger:** 10 minutes between sends  
**Type:** Thread reply to original Day-0 email  
**IMAP precondition:** Sweep per lead before each send

| Signal | Template | % of sends | Personalise |
|---|---|---|---|
| **SSL** | "'Not Secure' warning on [URL] is still showing." | ~60% | First name + exact URL from Day-0 |
| **Mobile** | "[business name]'s site is still not loading properly on a mobile screen." | ~20% | First name + business name |
| **No-website** | "[trade] [town] still isn't surfacing [business name] on Google." | ~15% | Trade keyword + town + business name |
| **AIDA** | "[business name] has [N] reviews but '[keyword] [town]' still isn't surfacing the website." | ~5% | First name + business name + N + keyword + town |

**Full copy in data/daily_email_plan.json → copy_by_signal section.**

---

## LINKEDIN BRIEF — FRIDAY 2026-05-15

**Window:** Opens today (Day 3) → HARD DEADLINE Tuesday 2026-05-19 (Day 7)  
**Order of operations:** Email bumps first → 1-hour gap → LinkedIn connection requests

| Step | Action |
|---|---|
| 1 | Open each Batch 5 lead's LinkedIn profile (use queries from linkedin_search_plan.json) |
| 2 | Check posts from last 60 days BEFORE writing note |
| 3 | If post found: write bespoke post_reference note (3-4x higher acceptance) |
| 4 | If no post: use sector-specific generic note from linkedin_connection_notes.json |
| 5 | Send connection request with note — 200-char hard limit |
| 6 | Write entry to data/linkedin_profiles.json immediately — mandatory |

**Sector priority:** Solicitors → Estate agents → Hotels/B&Bs → Restaurants → Boutique retail → Trades  
**Town priority:** Malton → Helmsley → Pickering → Kirkbymoorside → Norton-on-Derwent → Hovingham

**Rules (non-negotiable):**
- Do NOT mention email outreach, SSL, mobile, 'Not Secure', or any technical finding
- Do NOT start note with 'I'
- No exclamation marks
- No 'I came across your profile', 'synergies', 'reach out'
- Start with their name — personal, cuts through noise
- One specific observation — not vague, not flattering, just real
- End with low-pressure framing ('in case it's useful', 'connecting in case relevant')

---

## LINKEDIN HARD DEADLINE — NON-NEGOTIABLE

**Tuesday 2026-05-19 is Day 7. Archive trigger fires immediately for any Batch 5 lead where LinkedIn has not been executed.**

This is the rule that failed for 47 sessions with leads 1, 3, and 22. The cost was £800-1,175. That failure mode must not repeat.

- Day 3 (Friday 2026-05-15) — preferred. Execute all LinkedIn today if possible.
- Day 6 (Monday 2026-05-18) — fallback for any leads not done Friday.
- Day 7 (Tuesday 2026-05-19) — archive trigger. If LinkedIn not executed by EOD Tuesday: archive remaining Batch 5 leads as LOST_NO_RESPONSE. Log CHANGELOG immediately. No deferral.

---

## IMAP STATUS

**40-day gap (last confirmed check: 2026-04-04).** Any Batch 5 leads who replied to the Day-0 email (sent Tuesday 2026-05-12) will be in the inbox unchecked. Friday morning is the first window to catch early replies.

**Handling rules:**
- INTERESTED reply found: use interested variant (daily_email_plan.json), write to new_replies.json, classify, prepare proposal within 24 hours
- NOT_INTERESTED: cancel bump, block all channels, log CHANGELOG
- UNSUBSCRIBE: suppress within 24h (GDPR Article 21), log audit_log and CHANGELOG
- OOO: note return date, pause sequence, resume bump day after return
- WRONG_PERSON: investigate, log CHANGELOG

---

## WINNING ANALYTICS — WHAT THE DATA SAYS

| Pattern | Performance | Status |
|---|---|---|
| SSL-PAS with first-name subject | 3/3 INTERESTED (campaign-best) | Non-negotiable for Batch 5 |
| Tuesday AM send window | All 3 INTERESTED replies followed Tuesday sends | Confirmed — hard rule (Batch 5 Day-0 executed Tuesday) |
| Day-7 new angle (not reframe) | 1 conversion (Tom) from fresh pain point | Required — BRAIN generates per lead for Tuesday 2026-05-19 |
| Town name in subject | All INTERESTED leads referenced local angle in replies | Non-negotiable |
| One pain point per email | 100% of replies engaged with the specific signal used | Non-negotiable |
| LinkedIn (warm pipeline) | 0 connections sent — £800-1,175 written off | HARD DEADLINE: Day 7 enforced. Zero tolerance. |
| Generic signal | 0% reply rate | DO NOT USE |
| 24-hour proposal SLA | Tom asked for pricing — never received it (lost) | MANDATORY for Batch 5 INTERESTED replies |

---

## FORWARD CALENDAR

| Date | Day | Action | Type |
|---|---|---|---|
| **Thu 2026-05-14** | **47** | **BRAIN: Day-3 copy + LinkedIn templates. No sends.** | **TODAY (BRAIN only)** |
| **Fri 2026-05-15** | **48** | **HANDS: IMAP sweep. Day-3 bumps 09:00-10:30. LinkedIn. linkedin_profiles.json. CHANGELOG.** | **DAY 3 — CRITICAL** |
| Fri 2026-05-15 eve | 48 | BRAIN: Day-7 copy generation from linkedin_profiles.json (if HANDS returns data) | After HANDS session |
| Mon 2026-05-18 | 51 | LinkedIn fallback if any leads not done Friday | Day 6 |
| **Tue 2026-05-19** | **52** | **Day-7 new angle sends 09:00-10:30. LinkedIn HARD DEADLINE — archive trigger fires EOD.** | **DAY 7** |
| Tue 2026-05-19 eve | 52 | BRAIN: Day-14 breakup copy generation | After sends |
| **Tue 2026-05-26** | **59** | **Day-14 breakup sends 09:00-10:30.** | **DAY 14** |
| 2026-05-17 | — | active_strategy.md weekly review (due — first Batch 5 week data) | Weekly strategy |

---

## BATCH 5 RYEDALE — STATUS

**Assumed sent:** Tuesday 2026-05-12, 09:00-10:30 (unconfirmed — HANDS confirmation not received)  
**Sends assumed:** 12-18 leads across Malton, Pickering, Helmsley, Kirkbymoorside, Hovingham, Norton-on-Derwent  
**Signal mix:** SSL-PAS (60%), mobile-PAS (20%), no-website-BAB (15%), AIDA keyword-gap (5%)  
**Expected interested:** 2-3 (15% SSL-PAS historical rate)  
**Day-3 bumps:** TOMORROW (Friday 2026-05-15)  
**LinkedIn:** TOMORROW and hard deadline Tuesday 2026-05-19

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

`data/active_strategy.md` is valid until 2026-05-17. Full weekly review due this Sunday/Monday with first Batch 5 results. If Day-3 bump reply data is available by Monday: update strategy accordingly, extend to 2026-05-24.

---

*Strategy maintained by OUTLOCAL BRAIN layer.*  
*Day 47 — Thursday 2026-05-14. Eve of Batch 5 Day-3.*  
*Tomorrow is the most operationally important day since the campaign started.*  
*active_strategy.md valid to 2026-05-17. Next full review: Sunday/Monday with Batch 5 first-week data.*
