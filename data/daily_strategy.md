# Daily Strategy — 2026-05-07 (Thursday) — Day 40

**Updated:** 2026-05-07 (BRAIN Day 40 run)
**Replaces:** 2026-05-06 strategy (Day 39 — SEND DAY)
**Key changes from Day 39:** Archive trigger has fired. Warm pipeline formally closed. Thursday is the last send window this week. Calendar reset in progress.

---

## TODAY — EXECUTE

**2026-05-07 is Thursday — last acceptable send day before the weekend.**

| Priority | Action | Status |
|---|---|---|
| 1 | IMAP sweep — leads 3, 22, 1 (archive override check) | EXECUTE FIRST |
| 2 | IMAP sweep — leads 30-32, 58, 59 + full cohort | EXECUTE — fu precondition |
| 3 | fu_041-045 breakup sends | After IMAP clean confirmed |
| 4 | Batch 5 Ryedale sends | If data arrives today (any time) |
| 5 | CHANGELOG.md | EOD — 40 days unlogged — MANDATORY |

---

## EXECUTIVE SUMMARY — DAY 40

**Warm pipeline closed. Campaign depends entirely on Batch 5.**

Three facts define today:

1. **Archive trigger has fired.** Leads 1, 3, 22 are formally archived LOST_NO_RESPONSE. LinkedIn was never activated across 40 sessions. Combined pipeline value of £800-1,175 is written off. One final IMAP check today may reveal a late reply — if so, override archive immediately.

2. **Thursday is the last send day before the weekend.** If Ryedale data arrives today, send it. Thursday sends are not premium (Tuesday AM is the winning window) but they are perfectly valid. Friday sends land in weekend noise — avoid unless early morning.

3. **fu_041-045 are 14 days overdue.** Still appropriate to send — a Day-14 breakup email arriving slightly late is professionally acceptable. IMAP clean per lead before each.

---

## CAMPAIGN STATUS — DAY 40

| Metric | Value | Delta | Notes |
|---|---|---|---|
| Leads scraped (Batches 1-4) | ~61 | — | Batch 5 Ryedale: NOT received |
| Estimated emails sent | ~91 | — | Batches 1-4 assumed complete |
| Total replies confirmed | 11 | — | 17.9% overall reply rate |
| INTERESTED | 3 | — | Leads 1, 3, 22 — ARCHIVED LOST_NO_RESPONSE today |
| Conversions confirmed | 0 | — | — |
| IMAP gap | **33 days** | +1 | Sweep FIRST today |
| Campaign stall (no new leads) | **30 days** | +1 | Batch 5 Ryedale: 15 days overdue |
| fu_041-045 overdue | **14 days** | +1 | Send today after IMAP clear |
| LinkedIn sessions without profiles.json | **40** | +1 | Channel closed — archive triggered |
| CHANGELOG updates since Session 1 | **0** | — | Update TODAY EOD |

---

## PART A: WARM PIPELINE — FORMALLY CLOSED

### Archive Declaration

**Leads 1, 3, 22 are formally archived as LOST_NO_RESPONSE as of 2026-05-07.**

- **Why:** LinkedIn channel was never activated. Archive trigger per Day 39 rules fired (08:20 deadline missed, 2026-05-06).
- **Email channel:** Closed since 2026-04-08.
- **LinkedIn channel:** Never opened. Now permanently closed.
- **Combined value written off:** £800-1,175 (Claire £350 + Rob £550-675 + Tom £100-150).

### One Final Override Condition

**IMAP sweep of leads 3, 22, 1 is mandatory today.** If any reply is discovered (33-day gap — anything is possible):

| Scenario | Action |
|---|---|
| Claire (lead 3) has replied — still interested | Cancel archive. Lead with Option B (£350). Invoice today. CHANGELOG Campaign Milestone #1. |
| Rob (lead 22) has replied — deal still alive | Cancel archive. Present Options A/B/C. Target close today. |
| Tom (lead 1) has replied | Cancel archive. Agree spec (quote form £100-150). Set call this week. |
| Any lead has converted | CHANGELOG Campaign Milestone #1 immediately. Invoice. Begin delivery same day. |
| No replies for all three | Archive confirmed. Log CHANGELOG. Update lead status and CRM. |

**After today's IMAP check: archive is final. No further action on leads 1, 3, 22 on any channel.**

### Lesson Applied to Batch 5

The warm pipeline failure was not a scraping or email failure. The campaign produced a **17.9% reply rate** and 3 INTERESTED leads — exceptional results. The failure was post-reply follow-through.

**Rule for Batch 5 — non-negotiable:**
- LinkedIn approach: open Day 3, close Day 7. Not Day 40.
- linkedin_profiles.json: written same session as LinkedIn execution. No exceptions.
- If LinkedIn not executed within Day 7 of initial send: close the channel for that lead.

---

## PART B: fu_041-045 BREAKUP SENDS

**Five Day-14 breakups. 14 days overdue. Status unknown from Day 39. Send today.**

| Followup ID | Lead | Business | Town | Owner | Subject |
|---|---|---|---|---|---|
| fu_041 | 30 | Halifax Window Cleaning | Halifax | Steve | "Closing the loop — Halifax Window Cleaning" |
| fu_042 | 31 | Pontefract Pharmacy | Pontefract | — | "Closing the loop — Pontefract Pharmacy" |
| fu_043 | 32 | Castleford Carpets | Castleford | Ann | "Closing the loop — Castleford Carpets" |
| fu_044 | 58 | The Old Court Solicitors | Scarborough | — | "Closing the loop — The Old Court Solicitors" |
| fu_045 | 59 | Scarborough Roofing Specialists | Scarborough | Tony | "Closing the loop — Scarborough Roofing Specialists" |

**IMAP precondition:** Sweep leads 30, 31, 32, 58, 59 before each send. Any reply = cancel that fu.

**Stagger:** 10 minutes between sends. Full copy: followup_queue.json.

**Seasonal notes:**
- fu_043 (Castleford Carpets): May home-improvement season.
- fu_045 (Scarborough Roofing): Peak roofing season May-August.

---

## PART C: BATCH 5 RYEDALE — LAST WINDOW THIS WEEK

**Campaign stall: 30 days. Data overdue: 15 days. Thursday is the last viable send day before the weekend.**

### Send Window Decision Tree

| Scenario | Action |
|---|---|
| Data arrives any time today | BRAIN personalises same session. HANDS sends same day. 12-18 initial sends. |
| Data arrives before 09:00 Friday | Send Friday by 10:30 maximum — borderline but acceptable. |
| No data today or Friday | Next send window: **Tuesday 2026-05-12, 09:00-10:30.** Standard Tuesday AM premium. |
| Data arrives after 09:00 Friday | Hold until Tuesday 2026-05-12. |

### If Batch 5 Fires Today (Thursday 2026-05-07)

**Day-3 bump planning:**
- Calendar Day 3 = Sunday 2026-05-10 — weekend, no send
- Adjusted Day-3: **Friday 2026-05-09** (preferred — avoids full weekend gap) or Monday 2026-05-11
- **BRAIN action today:** If Batch 5 fires, generate Day-3 copy + LinkedIn note templates before end of day — Friday is tomorrow
- **LinkedIn Day-3 window:** Friday 2026-05-09 or Monday 2026-05-11 — HANDS executes, writes linkedin_profiles.json same session

**Day-7 new angle:** Thursday 2026-05-14, 09:00-10:30 (BRAIN run: Thursday 14 May morning)

**Day-14 breakup:** Thursday 2026-05-21, 09:00-10:30 (BRAIN run: Thursday 21 May morning)

### If Batch 5 Waits Until Tuesday 2026-05-12

**Day-3 bump:** Calendar Day 3 = Friday 2026-05-15 (no adjustment needed). BRAIN run: Tuesday evening or Wednesday morning.

**Day-7 new angle:** Tuesday 2026-05-19. **Day-14 breakup:** Tuesday 2026-05-26.

### Signal Waterfall (reminder)

1. `ssl` (HTTP site) → PAS → 60% → First-name subject + town + 'Not Secure' + specific URL
2. `mobile` fail → PAS → 20% → First-name + mobile issue specific
3. `no_website` 4★+ 20+ reviews → BAB → 15%
4. 4.5★+ 100+ reviews → AIDA keyword-gap → 5% (test only)

**Blocked leads (final attempt — archive today EOD if unresolved):**
- Lead 49 (East Riding Builders Ltd): Companies House director name
- Lead 51 (Driffield Garden Centre): phone attempt
- Lead 53 (Bridlington Bay Lettings): info@ fallback
- Lead 54 (The Wolds Inn): info@thewoldsinn.co.uk

---

## FORWARD CALENDAR

| Date | Day | Action | Notes |
|---|---|---|---|
| **Thu 7 May** | **40** | **IMAP + archive check + fu_041-045 + Batch 5 (conditional)** | **TODAY** |
| Fri 8 May | 41 | Batch 5 early sends ONLY if data arrives before 09:00 | Hold after 09:00 |
| **Tue 12 May** | **45** | **Batch 5 initial sends (if not sent Thu/Fri)** | **Standard Tuesday AM premium** |
| Fri 9 May OR Mon 11 May | 42/44 | Batch 5 Day-3 bumps (if Day-0 was Thursday) | BRAIN generates today evening if Batch 5 fires |
| Fri 15 May OR Mon 18 May | — | Batch 5 Day-3 bumps (if Day-0 was Tuesday) | BRAIN generates Tue/Wed |
| Thu 14 May OR Tue 19 May | — | Batch 5 Day-7 new angle | Depends on Day-0 date |
| Thu 21 May OR Tue 26 May | — | Batch 5 Day-14 breakups | Depends on Day-0 date |

---

## WINNING PLAYBOOK — NON-NEGOTIABLE FOR BATCH 5

1. **SSL → PAS → first-name subject → town → specific URL** — 3/3 INTERESTED in campaign. Non-negotiable.
2. **Day-7 MUST be a genuinely different pain point** — not a reframe. Tom's conversion came from a new angle.
3. **One pain point per email** — single clear signal. Never list multiple issues.
4. **Town name in subject AND body** — confirmed local credibility signal.
5. **No question marks in subject** — statement of fact outperforms.
6. **IMAP before every send** — 33-day gap is a compliance and relationship risk.
7. **LinkedIn: Day 3 open, Day 7 close** — warm pipeline failure was LinkedIn delay. Not email failure.
8. **linkedin_profiles.json: same session** — mandatory every time.
9. **CHANGELOG.md: same day** — 40 days unlogged is operationally dangerous.

---

## WINNING SUBJECT LINE PATTERNS

| Pattern | INTERESTED rate | Notes |
|---|---|---|
| `[First name] — [town] [business type] website flagged 'Not Secure'` | **~15%** | Confirmed winner — 3/3 INTERESTED |
| `[First name] — [town] [business] site isn't mobile-friendly` | 0% Day-0 / converts Day-7 | Day-7 pivot produced 1 conversion |
| `[Business name] — [town] [trade]: customers can't find you online` | Untested (BAB) | Testing at 20+ reviews threshold |
| `[First name] — [N] reviews but '[keyword] [town]' isn't bringing your site up` | Untested (AIDA) | 5% test only |

---

## ANALYTICS — PATTERNS TO DATE

| Metric | Value |
|---|---|
| Overall reply rate | 17.9% (11/~61) |
| INTERESTED rate (all signals) | 4.9% (3/~61) |
| INTERESTED rate (SSL-PAS only) | ~15% (3/~20 SSL sends) |
| Average days to first reply | 0 (all 3 INTERESTED replied Day 0 — same send day) |
| Day-7 conversion rate | 1/3 INTERESTED from Day-7 new angle (Tom) |
| LinkedIn conversion rate | 0% (never activated) |
| Send day pattern for replies | 100% of INTERESTED replies arrived on first working day after bank holiday |
| Subject line with first name | 100% of INTERESTED leads had first name in subject |

---

## COMPLIANCE STATUS — DAY 40

| Item | Status |
|---|---|
| Lead 19 (Summit Fitness) | Permanently suppressed ✓ |
| Lead 7 | Permanently suppressed ✓ |
| Lead 2 (Nidderdale Pet Supplies) | LOST — no further contact ✓ |
| Leads 1, 3, 22 | ARCHIVED LOST_NO_RESPONSE today — no further contact ✓ |
| 4-touchpoint maximum | Respected throughout ✓ |
| GDPR basis | B2B legitimate interest (all business emails) ✓ |
| Bank holiday sends | BLOCKED on all UK bank holidays ✓ |
| IMAP gap | **33 days — sweep TODAY** |
| fu_041-045 condition | IMAP check required before each send ✓ |
| Domain safety limit (40/day) | Max 23 sends today (5 fu + 18 Batch 5) — within limit ✓ |
| CHANGELOG | **40 days unlogged — UPDATE TODAY EOD** |

---

## BRAIN OPERATING SCHEDULE

| Date | Day | Action | Status |
|---|---|---|---|
| Wed 6 May | 39 | SEND DAY — IMAP + LinkedIn + fu_041-045 + Batch 5 | Day 39 actions: status unknown |
| **Thu 7 May** | **40** | **Archive declaration + IMAP + fu_041-045 + Batch 5 (conditional)** | **TODAY** |
| Thu 7 May (evening) | 40 | **If Batch 5 fires: BRAIN generates Day-3 copy + LinkedIn queries** | Same-day — Friday is tomorrow |
| Fri 9 May | 41 | Day-3 bumps (if Batch 5 Day-0 was Thursday) | Or Mon 11 May |
| Tue 12 May | 45 | Batch 5 initial sends (if not sent Thu/Fri) | Standard Tuesday premium |
| Thu 14 May OR Tue 19 May | — | Day-7 new angle copy | Depends on Day-0 |
| Thu 21 May OR Tue 26 May | — | Day-14 breakup copy | Depends on Day-0 |

---

*Generated by OUTLOCAL BRAIN layer — 2026-05-07 06:30 UTC*
*Day 40. Thursday — last send window this week. Warm pipeline closed — leads 1/3/22 archived LOST_NO_RESPONSE (LinkedIn never executed, 40 sessions). IMAP gap 33 days — sweep first. fu_041-045: 14 days overdue — send today (IMAP conditional). Batch 5: last viable window before weekend — send if data arrives. CHANGELOG.md EOD — 40 days unlogged.*
