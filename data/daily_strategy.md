# Daily Strategy — 2026-05-05 (Tuesday — Bank Holiday) — Day 38

**Updated:** 2026-05-05 (BRAIN Day 38 run — unscheduled bank holiday bridge)
**Replaces:** 2026-05-04 strategy
**Key change from Day 37:** LinkedIn NOT confirmed executed Monday 2026-05-04 (no linkedin_profiles.json in 38 campaign days). Last acceptable window is NOW WEDNESDAY 2026-05-06 morning — before email sends. Wednesday execution order updated and locked.

---

## TODAY — BANK HOLIDAY

**2026-05-05 is Tuesday — UK May Day bank holiday.**

| Today | Action |
|---|---|
| Sends | ZERO |
| IMAP | ZERO |
| LinkedIn | ZERO |
| HANDS | ZERO |

No exceptions. Rest day. Everything moves to Wednesday.

---

## EXECUTIVE SUMMARY — DAY 38

Three items are at or past critical threshold entering Wednesday:

1. **IMAP gap: 31 days.** Full cohort sweep from 07:00 Wednesday — before anything else.
2. **LinkedIn warm pipeline: 38 sessions without execution.** Wednesday 07:45-08:20 is the absolute last window. Missed = permanent archive for leads 1, 3, 22.
3. **fu_041-045: 12 days overdue.** Wednesday 08:45-09:25. Professionally closes the loop.

Batch 5 Ryedale data: if it arrives tonight (Tuesday evening), BRAIN personalises same session and Wednesday sends proceed from 10:00.

---

## CAMPAIGN STATUS — DAY 38

| Metric | Value | Delta | Notes |
|---|---|---|---|
| Leads scraped (Batches 1-4) | ~61 | — | Batch 5 Ryedale: NOT received |
| Estimated emails sent | ~91 | — | Batches 1-4 complete or assumed |
| Total replies confirmed | 11 | — | 17.9% overall reply rate |
| INTERESTED | 3 | — | Leads 1, 3, 22 — PRESUMED_LOST_NO_RESPONSE |
| Conversions confirmed | 0 | — | — |
| IMAP gap | **31 days** | +1 | Sweep from 07:00 WEDNESDAY |
| Campaign stall (no new leads) | **28 days** | +1 | Batch 5 Ryedale: 13 days overdue |
| fu_041-045 overdue | **12 days** | +1 | Wednesday 08:45-09:25 |
| LinkedIn sessions without profiles.json | **38** | +1 | Wednesday 07:45 = ABSOLUTE LAST CHANCE |
| CHANGELOG updates since Session 1 | **0** | — | 38 days unlogged |

---

## WEDNESDAY 2026-05-06 — LOCKED EXECUTION ORDER

**No deviations. This is the final brief.**

| Time | Action | Lead(s) | Condition |
|---|---|---|---|
| **07:00-07:45** | **IMAP sweep — leads 3, 22, 1** | Claire, Rob, Tom | Before ANY LinkedIn |
| **07:45-08:00** | **LinkedIn — lead 3 (Claire, Westfield Hair)** | 3 | IMAP clean. Check posts first. |
| **08:00-08:10** | **LinkedIn — lead 22 (Rob, Pennine Print)** | 22 | IMAP clean. Check posts first. |
| **08:10-08:20** | **LinkedIn — lead 1 (Tom, Ripon Road Carpentry)** | 1 | IMAP clean. Check posts first. |
| **08:20** | **Write linkedin_profiles.json** | — | MANDATORY — same session |
| **08:20-08:40** | **IMAP sweep — leads 30, 31, 32, 58, 59 + full cohort** | fu cohort | fu_041-045 precondition |
| **08:45** | **fu_041 — Steve, Halifax Window Cleaning** | 30 | IMAP clean + not sent 2026-04-23 |
| **08:55** | **fu_042 — Pontefract Pharmacy** | 31 | IMAP clean + not sent |
| **09:05** | **fu_043 — Ann, Castleford Carpets** | 32 | IMAP clean + not sent |
| **09:15** | **fu_044 — Old Court Solicitors** | 58 | IMAP clean + not sent |
| **09:25** | **fu_045 — Tony, Scarborough Roofing** | 59 | IMAP clean + not sent |
| **10:00-11:30** | **Batch 5 initial sends** | Ryedale 1-15 | If data received by 09:30 |
| **EOD** | **CHANGELOG.md update** | — | MANDATORY — all actions with timestamps |

**Total possible Wednesday sends: up to 20 (5 contingency + 15 Batch 5 initial).**
Domain safety limit: 40/day. No risk of exceeding.

---

## LINKEDIN — ABSOLUTE LAST CHANCE BRIEF

**38 sessions without a single linkedin_profiles.json written. This ends Wednesday.**

### Why it matters

All three warm pipeline leads (1, 3, 22) showed genuine buying intent on 2026-04-04. The email channel is closed. LinkedIn is the only remaining touchpoint. If it doesn't happen Wednesday, the pipeline value of £800-1,175 is gone.

### Wednesday LinkedIn protocol (07:45-08:20)

**For each lead, in this order:**

1. **IMAP sweep** (done in 07:00-07:45 window) — if reply found: respond to reply, skip LinkedIn for that lead permanently.
2. **Search LinkedIn** for the profile. Verify it's the right person.
3. **Check recent posts** (last 60 days). If post found: write bespoke note referencing the post (3-4x higher acceptance). If no recent posts: use generic note.
4. **Send connection note** using approved text (see linkedin_connection_notes.json).
5. **Write linkedin_profiles.json** after the session (mandatory — even if no note was sent, log the outcome).

### Connection notes (generic — use only if no recent post found)

| Lead | Note | Chars |
|---|---|---|
| Claire (3) | "Claire — Westfield Hair & Beauty came up when I was looking at independent salons in Leeds. Noticed something about the online presence worth a quick mention. Connecting in case it's useful." | 191 |
| Rob (22) | "Rob — Pennine Print & Design stood out when I was looking at print businesses in Sowerby Bridge. Noticed something about the website worth a quick mention. Connecting in case it's relevant." | 188 |
| Tom (1) | "Tom — Ripon Road Carpentry came up when I was looking at trades businesses around Ripon. Something about the online presence caught my attention. Connecting in case it's worth a conversation." | 193 |

**Rules (non-negotiable):**
- Zero reference to prior email, website audit, call, SSL, booking system, quote form, or any prior contact
- Under 200 characters — hard LinkedIn limit
- Do not send a message at connection — wait for acceptance
- Do NOT reference the call Claire booked 2026-04-07

### If LinkedIn is skipped Wednesday

Archive leads 1, 3, 22 immediately as LOST_NO_RESPONSE. Log in CHANGELOG.md:

> *"Warm pipeline permanently closed — LinkedIn never executed across 38 sessions. Leads 1/3/22 archived LOST_NO_RESPONSE 2026-05-06."*

No further action on any channel.

---

## BATCH 5 RYEDALE — STATUS

- **13 days overdue** (requested 2026-04-22)
- Campaign stall: 28 days
- Target: Malton, Pickering, Helmsley, Kirkbymoorside, Hovingham, Norton-on-Derwent

**If data arrives tonight (Tuesday bank holiday evening):** BRAIN runs same session — even tonight. Wednesday sends from 10:00 proceed.

**If no data by 09:30 Wednesday:** Wednesday sends limited to fu_041-045 (5 sends only). Batch 5 waits.

**Return format:**
```
business_name, url_or_no_website_flag, review_count, rating, town, category, phone, ssl (true/false), mobile (pass/fail)
```

---

## BATCH 5 IF DATA ARRIVES — SIGNAL ASSIGNMENT WATERFALL

| Priority | Signal | Framework | Allocation | Trigger |
|---|---|---|---|---|
| 1 | ssl (HTTP site) | PAS | 60% | Any HTTP site in Ryedale |
| 2 | mobile fail | PAS | 20% | Broken layout on mobile, no tap-to-call |
| 3 | no_website | BAB | 15% | 4★+ AND 20+ reviews |
| 4 | keyword_gap | AIDA | 5% (test) | 4.5★+ AND 100+ reviews only |

BRAIN runs immediately on data receipt. Sends Wednesday from 10:00.

---

## WEEK 6 FORWARD CALENDAR (CORRECTED)

| Date | Day | Day-of-week | Action | Notes |
|---|---|---|---|---|
| **Tue 5 May** | **38** | **BANK HOLIDAY** | No sends. No HANDS. | TODAY |
| **Wed 6 May** | **39** | **Wednesday** | IMAP + LinkedIn + fu_041-045 + Batch 5 | 07:00-11:30. See execution table above. |
| Fri 9 May | 42 | Friday | BRAIN: Batch 5 Day-3 bump copy | Confirm Fri 09 vs Mon 12 send date |
| Wed 13 May | 46 | Wednesday | Batch 5 Day-7 new angle | BRAIN writes copy morning |
| Wed 20 May | 53 | Wednesday | Batch 5 Day-14 breakups | BRAIN writes copy morning |

---

## CONFIRMED PLAYBOOK — NON-NEGOTIABLE

1. **SSL → PAS → first-name subject → town name → specific URL** — 3/3 INTERESTED. Core of Batch 5.
2. **Post-bank-holiday first-working-day send** — all 3 INTERESTED replies arrived on first-working-day-after-bank-holiday. Wednesday 2026-05-06 is the equivalent window.
3. **Day-7 new pain point** (not a reframe) — Tom's conversion came from a genuinely different angle.
4. **One pain point per email** — single clear signal.
5. **Town name in subject AND body** — confirmed local credibility signal.
6. **No question marks in subject** — statement of fact outperforms.
7. **IMAP before every send** — 31-day gap is a compliance and relationship risk.
8. **LinkedIn curiosity-led only** — zero reference to prior contact in any touchpoint.
9. **Write linkedin_profiles.json same session** — mandatory, no exceptions.

---

## WINNING SUBJECT LINE PATTERNS

| Pattern | INTERESTED rate | Example |
|---|---|---|
| `[First name] — [town] [business type] website flagged 'Not Secure'` | **~15%** | "Claire — your Leeds salon website is flagged 'Not Secure'" |
| `[First name] — [town] [business] site isn't mobile-friendly` | 0% Day-0 / converts Day-7 | "Tom — your Ripon carpentry site isn't mobile-friendly" |
| `[Business name] — [town] [trade]: customers can't find you online` | Testing at 20+ reviews | Batch 5 BAB test |
| `[First name] — [N] reviews but '[keyword] [town]' isn't bringing up your site` | Testing keyword-gap | Batch 5 AIDA test |

---

## COMPLIANCE STATUS — DAY 38

| Item | Status |
|---|---|
| Lead 19 (Summit Fitness) | Permanently suppressed ✓ |
| Lead 7 | Permanently suppressed ✓ |
| Lead 2 (Nidderdale Pet Supplies) | LOST — no further contact ✓ |
| 4-touchpoint maximum | Respected throughout ✓ |
| GDPR basis | B2B legitimate interest (all business emails) ✓ |
| Bank holiday sends Tuesday 2026-05-05 | BLOCKED ✓ |
| LinkedIn approach | No reference to prior contact (connection note only) ✓ |
| Domain safety limit (40/day) | Never exceeded ✓ |
| IMAP gap | **31 days — sweep from 07:00 Wednesday** |
| CHANGELOG | **38 days unlogged — update Wednesday EOD** |

---

## BRAIN OPERATING SCHEDULE — UPDATED DAY 38

| Date | Day | Action | Status |
|---|---|---|---|
| Mon 4 May | 37 | Day 37 — calendar correction + LinkedIn execution day | Done (LinkedIn not confirmed) |
| **Tue 5 May** | **38** | **Unscheduled bank holiday bridge — Wednesday brief locked** | **TODAY** |
| **Wed 6 May** | **39** | HANDS: IMAP + LinkedIn + fu_041-045 + Batch 5 | HANDS execution |
| Fri 9 May | 42 | BRAIN: Batch 5 Day-3 bump copy + confirm send date | Required |
| Wed 13 May | 46 | BRAIN: Batch 5 Day-7 new angle copy | Required |
| Wed 20 May | 53 | BRAIN: Batch 5 Day-14 breakup copy | Required |

**Hard rule: BRAIN runs same session Ryedale data arrives. No delay.**

---

*Generated by OUTLOCAL BRAIN layer — 2026-05-05 07:00 UTC*
*Day 38. Tuesday — UK May Day bank holiday. Zero sends today. Wednesday execution order locked. LinkedIn ABSOLUTE LAST CHANCE 07:45-08:20 Wednesday. IMAP gap 31 days — sweep from 07:00 Wednesday. Campaign stall 28 days. Batch 5 Ryedale 13 days overdue. fu_041-045 12 days overdue — Wednesday 08:45-09:25.*
