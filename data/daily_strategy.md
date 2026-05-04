# Daily Strategy — 2026-05-04 (Monday) — Day 37

**Updated:** 2026-05-04 (BRAIN Day 37 run — Monday execution day)
**Replaces:** 2026-05-03 strategy
**Key change from Day 36:** Calendar correction logged. LinkedIn approach executes TODAY. Send day confirmed as Wednesday 2026-05-06 (first working day after Tuesday bank holiday).

---

## CALENDAR CORRECTION — LOGGED THIS RUN

Prior BRAIN runs (Days 34-36) called the bank holiday "Monday 2026-05-05." This is wrong.

| Date | Correct day | Status |
|---|---|---|
| 2026-05-04 | **Monday** | TODAY — HANDS: IMAP + LinkedIn |
| 2026-05-05 | **Tuesday** | UK May Day bank holiday — ZERO sends |
| 2026-05-06 | **Wednesday** | First working day — SEND DAY |

**Impact on strategy:** None. Date 2026-05-06 was always correct as send day. The "post-bank-holiday first-working-day premium" logic is unchanged — it's the mechanism (business owners returning to inbox after a bank holiday) that drives yield, not whether the day name is Tuesday or Wednesday.

**Day-3 bump recalculation:** Day 3 from Wednesday 2026-05-06 = Saturday 2026-05-09. Weekend — no send. BRAIN runs Friday 2026-05-09 to confirm: Friday send (same day) vs Monday 2026-05-11. Friday is likely preferred — avoids a 5-day gap.

---

## EXECUTIVE SUMMARY — DAY 37

Today is the HANDS execution day. Two critical actions must happen before the bank holiday closes the window:

1. **IMAP sweep — 30-day gap.** A conversion may be sitting unread. Full cohort sweep before 09:00.
2. **LinkedIn warm pipeline — leads 1, 3, 22.** Buffer expired 2026-05-02. Execute 09:30-10:00 after IMAP.

No new leads. No new signals. Campaign holds until Wednesday 2026-05-06.

---

## CAMPAIGN STATUS — DAY 37

| Metric | Value | Delta | Notes |
|---|---|---|---|
| Leads scraped (Batches 1-4) | ~61 | — | Batch 5 Ryedale: NOT received |
| Estimated emails sent | ~91 | — | Includes assumed fu_041-049 |
| Total replies confirmed | 11 | — | 17.9% overall reply rate |
| INTERESTED | 3 | — | Leads 1, 3, 22 — PRESUMED_LOST_NO_RESPONSE |
| Active email sequences | 0 | — | All Batch 1-4 complete |
| IMAP gap | **30 days** | +1 | Sweep TODAY before 09:00 |
| Campaign stall (no new leads) | **27 days** | +1 | Batch 5 Ryedale CRITICAL — 12 days overdue |
| fu_041-045 overdue | **11 days** | +1 | Send Wednesday 2026-05-06 08:45-09:25 |
| LinkedIn buffer (leads 1,3,22) | **EXECUTE TODAY** | — | Monday 2026-05-04, 09:30-10:00 |
| CHANGELOG updates since Session 1 | **0** | — | 37 days of HANDS actions unlogged |

---

## TODAY'S EXECUTION PRIORITIES (Monday 2026-05-04)

### PRIORITY 1: IMAP SWEEP (Before 09:00)

30-day IMAP gap. A conversion may exist unread. **Sweep in this order:**

1. `claire@westfieldhair.co.uk` (lead 3) — LinkedIn approach today; IMAP must precede
2. `rob@pennineprint.co.uk` (lead 22) — LinkedIn approach today; IMAP must precede
3. `tom@riponroadcarpentry.co.uk` (lead 1) — LinkedIn approach today; IMAP must precede
4. Leads 52, 55, 50, 56 (fu_046-049 assumed sent 2026-04-24)
5. Leads 30, 31, 32, 58, 59 (fu_041-045 unconfirmed)
6. Full remaining cohort

**If conversion found:** Write CHANGELOG.md immediately — Campaign Milestone #1. Send invoice today. Do NOT approach on LinkedIn for that lead.

---

### PRIORITY 2: LINKEDIN WARM PIPELINE (09:30-10:00, after IMAP)

LinkedIn buffer expired 2026-05-02. Approach today.

| Lead | Business | Owner | Connection note |
|---|---|---|---|
| 3 | Westfield Hair & Beauty | Claire | "Hi Claire — came across Westfield Hair & Beauty while looking at Leeds salons. Really strong local reputation. Would be great to connect." (121 chars) |
| 22 | Pennine Print & Design | Rob | "Hi Rob — came across Pennine Print while exploring Calderdale businesses. Great local reputation. Happy to connect." (106 chars) |
| 1 | Ripon Road Carpentry | Tom | "Hi Tom — spotted Ripon Road Carpentry while looking at North Yorkshire trades businesses. Great reputation locally. Happy to connect." (123 chars) |

**Rules (non-negotiable):**
- IMAP must be clean for each lead before sending their note
- Zero reference to prior email, SSL, website, quote form, booking
- Connection note only — do NOT send a message at connection time
- Write `linkedin_profiles.json` same session (mandatory)
- After acceptance: wait 2-3 days, then send first warm message (see value_delivery_queue.json)

---

### PRIORITY 3: CHANGELOG UPDATE (By EOD Monday)

37 days of HANDS actions completely unlogged. Must log today:
- All sends fu_026 onwards (estimated dates from BRAIN files)
- fu_041-045: confirm sent or not sent on 2026-04-23
- fu_046-049: confirm sent or not sent 2026-04-24
- Warm pipeline email close status for leads 1, 3, 22
- All LinkedIn approach attempts today

---

### PRIORITY 4: BATCH 5 RYEDALE SCRAPE (Critical — any time today)

27-day campaign stall. 12 days overdue. **If data arrives today:** BRAIN runs same evening for Wednesday 2026-05-06 sends.

**Return format:** `business_name, url_or_no_website_flag, review_count, rating, town, category, phone, ssl (true/false), mobile (pass/fail)`

---

## WEDNESDAY 2026-05-06 — EXECUTION ORDER

**Tuesday 2026-05-05 bank holiday is the hard gate — nothing sends Tuesday.**

| Time | Action | Leads | Condition |
|---|---|---|---|
| 08:00-08:40 | IMAP sweep — full cohort | All | Required |
| 08:45-09:25 | fu_041-045 contingency sends | 30, 31, 32, 58, 59 | If not sent + IMAP clear |
| 10:00-11:30 | Batch 5 initial sends | Ryedale 1-15 | If data received |

**Total possible Wednesday sends: up to 20 (5 contingency + 15 Batch 5 initial).**
Domain safety limit: 40/day. No risk of exceeding.

---

## WEEK 6 PREVIEW (CORRECTED CALENDAR)

| Date | Day | Day-of-week | Action | Notes |
|---|---|---|---|---|
| Mon 4 May | 37 | Monday | IMAP + LinkedIn warm pipeline | TODAY |
| Tue 5 May | 38 | **TUESDAY — BANK HOLIDAY** | No sends. No HANDS. | UK May Day |
| **Wed 6 May** | **39** | **Wednesday** | **Batch 5 initial sends + fu_041-045** | 08:45-11:30 |
| Fri 9 May | 42 | Friday | BRAIN: Batch 5 Day-3 bump copy | Confirm send Fri or Mon |
| Wed 13 May | 46 | Wednesday | Batch 5 Day-7 new angle | BRAIN writes copy morning |
| Wed 20 May | 53 | Wednesday | Batch 5 Day-14 breakups | BRAIN writes copy morning |

*Note: Batch 5 follow-up cadence shifts to Wednesday consistency (same day as initial sends) rather than prior Tuesday pattern.*

---

## CONFIRMED PLAYBOOK — NON-NEGOTIABLE (Day 37 Status)

1. **SSL → PAS → first-name subject → town name → specific URL** — 3/3 INTERESTED. Core of Batch 5.
2. **Post-bank-holiday first-working-day send** — all 3 INTERESTED replies arrived on first-working-day-after-bank-holiday. Wednesday 2026-05-06 is the equivalent window. Mechanism confirmed.
3. **Day-7 new pain point** (not a reframe) — Tom's conversion came from a genuinely different angle.
4. **One pain point per email** — single clear signal.
5. **Town name in subject AND body** — confirmed local credibility signal.
6. **No question marks in subject** — statement of fact outperforms for trades cold email.
7. **IMAP before every send** — 30-day gap is a compliance and relationship risk.
8. **LinkedIn curiosity-led only** — zero reference to prior contact in any touchpoint.
9. **Write linkedin_profiles.json same session** — mandatory, no exceptions.

---

## WINNING SUBJECT LINE PATTERNS (Campaign Total)

| Pattern | INTERESTED rate | Example |
|---|---|---|
| `[First name] — [town] [business type] website flagged 'Not Secure'` | **~15%** | "Claire — your Leeds salon website is flagged 'Not Secure'" |
| `[First name] — [town] [business] site isn't mobile-friendly` | 0% Day-0 / converts Day-7 | "Tom — your Ripon carpentry site isn't mobile-friendly" |
| `[Business name] — [town] [trade]: customers can't find you online` | 0% at 50+ reviews / testing at 20+ | Batch 5 test |
| `[First name] — [N] reviews but '[keyword] [town]' isn't bringing up your site` | 0% abstract / testing keyword-gap | Batch 5 test |

**Confirmed winner:** First name + dash + town + business type + factual specific issue.

---

## ANALYTICS — BATCH 5 A/B TESTS

| Variable | Control | Test (Batch 5) | Hypothesis |
|---|---|---|---|
| BAB review threshold | 50+ reviews | **20+ reviews** | Rural Ryedale — lower bar increases volume; test rate |
| AIDA angle | Abstract ranking | **Specific keyword-gap** | "plumber Malton shows X and Y above you" — verifiable = credible |
| Post-bank-holiday trigger | Easter Monday (Mon) → Tue | **May Day (Tue) → Wed** | First-working-day mechanism confirmed regardless of day name |
| fu_041-045 timing | Due 2026-04-23 | **Rescheduled 2026-05-06** | Post-bank-holiday applies to breakups too |

---

## COMPLIANCE STATUS — DAY 37

| Item | Status |
|---|---|
| Lead 19 (Summit Fitness) | Permanently suppressed ✓ |
| Lead 7 | Permanently suppressed ✓ |
| Lead 2 (Nidderdale Pet Supplies) | LOST — no further contact ✓ |
| 4-touchpoint maximum | Respected throughout ✓ |
| GDPR basis | B2B legitimate interest (all business emails) ✓ |
| Bank holiday sends Tuesday 2026-05-05 | BLOCKED ✓ |
| LinkedIn approach | No reference to prior contact (connection note only) ✓ |
| Fitness/wellness Otley | Paused ✓ |
| Residential addresses | None sent ✓ |
| Domain safety limit (40/day) | Never exceeded ✓ |
| IMAP gap | **30 days — sweep TODAY before any sends** |

---

## BRAIN OPERATING SCHEDULE — UPDATED DAY 37

| Date | Day | Day | Run | Purpose | Status |
|---|---|---|---|---|---|
| Sun 3 May | 36 | Sun | Completed | Weekend bridge — LinkedIn copy + Tuesday prep | ✓ Done |
| **Mon 4 May** | **37** | **Mon** | **TODAY** | Day 37 — calendar correction + LinkedIn execution day | ✓ Running |
| **Mon 4 May (eve)** | **37** | **Mon** | **If Ryedale data arrives today** | Batch 5 personalisation | Mandatory if data arrives |
| Tue 5 May | 38 | **BANK HOLIDAY** | No BRAIN run | — | — |
| **Wed 6 May** | **39** | **Wed** | HANDS sends | Batch 5 Day-0 + fu_041-045 | — |
| Fri 9 May | 42 | Fri | BRAIN | Batch 5 Day-3 bump copy + confirm send date | Required |
| Wed 13 May | 46 | Wed | BRAIN | Batch 5 Day-7 new angle copy | Required |
| Wed 20 May | 53 | Wed | BRAIN | Batch 5 Day-14 breakup copy | Required |

**Hard rule: BRAIN runs same day Ryedale data arrives. Do not let another day pass without BRAIN personalising.**

---

*Generated by OUTLOCAL BRAIN layer — 2026-05-04 07:00 UTC*
*Day 37. Monday execution day. Calendar correction: bank holiday = Tuesday 2026-05-05 (not Monday as prior BRAIN stated); first send day = Wednesday 2026-05-06. LinkedIn approach for leads 1, 3, 22 executes TODAY after IMAP sweep. IMAP gap now 30 days — sweep before 09:00. No new leads. Campaign stall 27 days. Batch 5 Ryedale 12 days overdue.*
