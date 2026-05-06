# Daily Strategy — 2026-05-06 (Wednesday — SEND DAY) — Day 39

**Updated:** 2026-05-06 (BRAIN Day 39 run — Wednesday execution day)
**Replaces:** 2026-05-05 strategy (Day 38 — bank holiday bridge)
**Key change from Day 38:** This is no longer planning. Today is the SEND DAY. Execute the locked sequence.

---

## TODAY — EXECUTE

**2026-05-06 is Wednesday — first working day after UK May Day bank holiday.**

| Window | Action | Status |
|---|---|---|
| 07:00-07:45 | IMAP sweep — leads 3, 22, 1 | EXECUTE — LinkedIn precondition |
| 07:45-08:20 | LinkedIn — leads 3, 22, 1 | EXECUTE — absolute last chance |
| 08:20 | Write linkedin_profiles.json | MANDATORY — same session |
| 08:20-08:40 | IMAP sweep — full cohort + fu leads | EXECUTE — fu precondition |
| 08:45-09:25 | fu_041-045 breakups | EXECUTE — IMAP conditional |
| 09:30 | Batch 5 data decision point | IF data: BRAIN personalises, sends 10:00 |
| 10:00-11:30 | Batch 5 initial sends | CONDITIONAL on data receipt |
| EOD | CHANGELOG.md | MANDATORY — 39 days unlogged |

---

## EXECUTIVE SUMMARY — DAY 39

**Three live actions today. Priority order is fixed. No deviations.**

1. **IMAP sweep from 07:00 — 32-day gap.** Leads 3, 22, 1 first (LinkedIn precondition). Full cohort before EOD.
2. **LinkedIn for leads 1, 3, 22 — 07:45-08:20.** 39 sessions without execution. Archive permanently if missed today.
3. **fu_041-045 breakups — 08:45-09:25.** 13 days overdue. Professionally closes the loop.
4. **Batch 5 initial sends — 10:00-11:30 if data arrives.** Post-bank-holiday premium window is NOW.

---

## CAMPAIGN STATUS — DAY 39

| Metric | Value | Delta | Notes |
|---|---|---|---|
| Leads scraped (Batches 1-4) | ~61 | — | Batch 5 Ryedale: NOT received |
| Estimated emails sent | ~91 | — | Batches 1-4 complete or assumed |
| Total replies confirmed | 11 | — | 17.9% overall reply rate |
| INTERESTED | 3 | — | Leads 1, 3, 22 — PRESUMED_LOST_NO_RESPONSE |
| Conversions confirmed | 0 | — | — |
| IMAP gap | **32 days** | +1 | Sweep from 07:00 TODAY |
| Campaign stall (no new leads) | **29 days** | +1 | Batch 5 Ryedale: 14 days overdue |
| fu_041-045 overdue | **13 days** | +1 | Send TODAY 08:45-09:25 |
| LinkedIn sessions without profiles.json | **39** | +1 | Execute TODAY 07:45-08:20 or archive |
| CHANGELOG updates since Session 1 | **0** | — | Update TODAY EOD |

---

## PART A: IMAP — CRITICAL FIRST ACTION

**32-day gap. Sweep in this priority order before any sends or LinkedIn.**

### Priority 1: Warm pipeline (LinkedIn precondition)
| Lead | Email | LinkedIn window | IMAP action |
|---|---|---|---|
| Claire, lead 3 | claire@westfieldhair.co.uk | 07:45-08:00 | Check for replies since 2026-04-04 |
| Rob, lead 22 | rob@pennineprint.co.uk | 08:00-08:10 | Check for replies since 2026-04-04 |
| Tom, lead 1 | tom@riponroadcarpentry.co.uk | 08:10-08:20 | Check for replies since 2026-04-04 |

**If reply found for any warm pipeline lead:** Act on reply immediately. Cancel LinkedIn for that lead. If conversion: CHANGELOG.md — Campaign Milestone #1 — first revenue. Invoice same day.

### Priority 2: fu cohort (fu_041-045 precondition)
Leads 30, 31, 32, 58, 59 — check before 08:45.

### Priority 3: Full remaining cohort
All other leads — sweep before EOD.

---

## PART B: LINKEDIN — EXECUTE NOW

**39 sessions without a single linkedin_profiles.json written. This ends today.**

### Why it still matters
All three leads showed genuine buying intent on 2026-04-04. The combined pipeline value is £800-1,175. LinkedIn is the only remaining channel. A 3-week conversion is still worth executing for.

### Today's protocol (07:45-08:20)

**For each lead, in this exact order:**

1. IMAP sweep result (already done in 07:00-07:45) — if reply: skip LinkedIn for this lead
2. Search LinkedIn for profile. Verify it's the right person.
3. Check recent posts (last 60 days). Post_reference note if post found — 3-4x higher acceptance.
4. Send connection note using approved text (linkedin_connection_notes.json).
5. Write linkedin_profiles.json after session — even if no note was sent.

### Connection notes (generic — use ONLY if no recent post found)

| Lead | Note | Chars |
|---|---|---|
| Claire (3) | "Claire — Westfield Hair & Beauty came up when I was looking at independent salons in Leeds. Noticed something about the online presence worth a quick mention. Connecting in case it's useful." | 191 |
| Rob (22) | "Rob — Pennine Print & Design stood out when I was looking at print businesses in Sowerby Bridge. Noticed something about the website worth a quick mention. Connecting in case it's relevant." | 188 |
| Tom (1) | "Tom — Ripon Road Carpentry came up when I was looking at trades businesses around Ripon. Something about the online presence caught my attention. Connecting in case it's worth a conversation." | 193 |

**Post-reference upgrade topics to check:**
- Claire: wedding hair, prom, bank holiday, spring colour, summer bookings, new treatment
- Rob: wedding stationery, graduation, summer print, event programme, rebrand, new client
- Tom: spring builds, garden structures, bespoke furniture, decking (low probability — trades)

### Non-negotiable rules
- Zero reference to prior email, website audit, call, SSL, booking system, quote form, or any prior contact
- Under 200 characters — hard LinkedIn limit
- Do not send a message at connection — wait for acceptance
- Do NOT reference the call Claire booked 2026-04-07

### If LinkedIn not done by 08:20
Archive leads 1, 3, 22 immediately as LOST_NO_RESPONSE. Log in CHANGELOG.md:
> *"Warm pipeline permanently closed — LinkedIn never executed across 39 sessions. Leads 1/3/22 archived LOST_NO_RESPONSE 2026-05-06 EOD."*

---

## PART C: fu_041-045 BREAKUP SENDS

**Five Day-14 breakups, 13 days overdue. Execute 08:45-09:25 after IMAP sweep.**

| Time | ID | Lead | Business | Town | Subject |
|---|---|---|---|---|---|
| 08:45 | fu_041 | 30 | Steve | Halifax Window Cleaning | "Closing the loop — Halifax Window Cleaning" |
| 08:55 | fu_042 | 31 | — | Pontefract Pharmacy | "Closing the loop — Pontefract Pharmacy" |
| 09:05 | fu_043 | 32 | Ann | Castleford Carpets | "Closing the loop — Castleford Carpets" |
| 09:15 | fu_044 | 58 | — | The Old Court Solicitors | "Closing the loop — The Old Court Solicitors" |
| 09:25 | fu_045 | 59 | Tony | Scarborough Roofing Specialists | "Closing the loop — Scarborough Roofing Specialists" |

**Condition for each send:** IMAP clean (no prior reply for that lead) + not already sent on 2026-04-23.

Full email bodies in followup_queue.json.

**Seasonal notes:**
- fu_043 (Ann, Castleford Carpets): May home-improvement season — minor upside
- fu_045 (Tony, Scarborough Roofing): Peak roofing season May-August — well-timed close

---

## PART D: BATCH 5 RYEDALE — DECISION POINT 09:30

**Status: 14 days overdue. Campaign stall: 29 days.**

| Scenario | Action |
|---|---|
| Data arrives before 09:30 today | BRAIN personalises same session. Sends 10:00-11:30 (post-bank-holiday premium). |
| Data arrives after 09:30 today | Thursday 2026-05-07 sends valid (premium partially lost). |
| No data today | Sends today: fu_041-045 only (5 sends). Batch 5 waits. |

**If sending today (10:00-11:30):**
- 10-15 initial sends
- 8-10 minute stagger
- Domain safety limit: 40/day — max 20 today (5 fu + 15 Batch 5). No risk.
- Post-bank-holiday premium: same mechanism that delivered all 3 INTERESTED replies. Do NOT defer to Thursday if data arrives before 09:30.

**Data format required (HANDS delivers):**
```
business_name, url_or_no_website_flag, review_count, rating, town, category, phone, ssl (true/false), mobile (pass/fail), owner_name (if known)
```

**Signal waterfall on receipt:**
1. ssl (HTTP) → PAS → 60% → First name if known + town + 'Not Secure'
2. mobile fail → PAS → 20% → First name + mobile issue specific
3. no_website + 20+ reviews + 4★+ → BAB → 15%
4. 4.5★+ + 100+ reviews → AIDA keyword-gap → 5% (test only)

**Blocked leads (final attempt today):**
- Lead 49 (East Riding Builders): Companies House director name — archive by EOD if unresolved
- Lead 51 (Driffield Garden Centre): phone after 09:30 — archive if no answer
- Lead 53 (Bridlington Bay Lettings): Rightmove/Zoopla or info@ fallback
- Lead 54 (The Wolds Inn): try info@thewoldsinn.co.uk

---

## FORWARD CALENDAR

| Date | Day | Action | Notes |
|---|---|---|---|
| **Wed 6 May** | **39** | **IMAP + LinkedIn + fu_041-045 + Batch 5 (conditional)** | **TODAY** |
| Fri 9 May | 42 | BRAIN: Batch 5 Day-3 bump copy + confirm send date | Fri 09 May send (before weekend) or Mon 11 May |
| Wed 13 May | 46 | BRAIN: Batch 5 Day-7 new angle copy | HANDS sends Wednesday AM |
| Wed 20 May | 53 | BRAIN: Batch 5 Day-14 breakup copy | HANDS sends Wednesday AM |

**BRAIN schedule note:**
- No mandatory BRAIN run Thursday or Friday unless Batch 5 fires today (then Friday 2026-05-09 run is required for Day-3 bumps)
- If Batch 5 fires today: Day 3 = Saturday 2026-05-09 (weekend, no send). BRAIN confirms on Friday 09 May: Friday 09 May send preferred over Monday 11 May (avoids weekend cold gap).
- If Batch 5 does NOT fire today: next BRAIN run when data arrives.

---

## WINNING PLAYBOOK — NON-NEGOTIABLE

1. **SSL → PAS → first-name subject → town name → specific URL** — 3/3 INTERESTED. Non-negotiable for Batch 5.
2. **Post-bank-holiday first-working-day send** — all 3 INTERESTED replies arrived on first-working-day-after-bank-holiday. Window is NOW.
3. **Day-7 new pain point** (not a reframe) — Tom's conversion came from a genuinely different angle.
4. **One pain point per email** — single clear signal only.
5. **Town name in subject AND body** — confirmed local credibility signal.
6. **No question marks in subject** — statement of fact outperforms.
7. **IMAP before every send** — 32-day gap is a compliance and relationship risk.
8. **LinkedIn curiosity-led only** — zero reference to prior contact.
9. **Write linkedin_profiles.json same session** — mandatory, 39 sessions without.

---

## WINNING SUBJECT LINE PATTERNS

| Pattern | INTERESTED rate | Example |
|---|---|---|
| `[First name] — [town] [business type] website flagged 'Not Secure'` | **~15%** | "Mark — your Malton plumbing site is flagged 'Not Secure'" |
| `[First name] — [town] [business] site isn't mobile-friendly` | 0% Day-0 / converts Day-7 | — |
| `[Business name] — [town] [trade]: customers can't find you online` | Testing at 20+ reviews (BAB) | — |
| `[First name] — [N] reviews but '[keyword] [town]' isn't bringing up your site` | Testing keyword-gap (AIDA) | — |

---

## COMPLIANCE STATUS — DAY 39

| Item | Status |
|---|---|
| Lead 19 (Summit Fitness) | Permanently suppressed ✓ |
| Lead 7 | Permanently suppressed ✓ |
| Lead 2 (Nidderdale Pet Supplies) | LOST — no further contact ✓ |
| 4-touchpoint maximum | Respected throughout ✓ |
| GDPR basis | B2B legitimate interest (all business emails) ✓ |
| Bank holiday sends Tuesday 2026-05-05 | BLOCKED ✓ |
| LinkedIn approach | No reference to prior contact (connection note only) ✓ |
| Domain safety limit (40/day) | Max 20 today — no risk ✓ |
| IMAP gap | **32 days — sweep from 07:00 TODAY** |
| CHANGELOG | **39 days unlogged — UPDATE TODAY EOD** |

---

## BRAIN OPERATING SCHEDULE

| Date | Day | Action | Status |
|---|---|---|---|
| Mon 4 May | 37 | Day 37 — calendar correction | Done |
| Tue 5 May | 38 | Bank holiday bridge — Wednesday brief locked | Done |
| **Wed 6 May** | **39** | **SEND DAY — IMAP + LinkedIn + fu_041-045 + Batch 5** | **TODAY** |
| Fri 9 May | 42 | BRAIN: Batch 5 Day-3 bump copy + confirm send date | Required if Batch 5 fires today |
| Wed 13 May | 46 | BRAIN: Batch 5 Day-7 new angle copy | Required |
| Wed 20 May | 53 | BRAIN: Batch 5 Day-14 breakup copy | Required |

---

*Generated by OUTLOCAL BRAIN layer — 2026-05-06 06:30 UTC*
*Day 39. Wednesday — SEND DAY. Post-bank-holiday premium window active. IMAP gap 32 days — sweep from 07:00. LinkedIn ABSOLUTE LAST CHANCE 07:45-08:20 — execute or archive leads 1/3/22 permanently. fu_041-045 13 days overdue — 08:45-09:25. Batch 5 Ryedale 14 days overdue — sends if data received by 09:30. CHANGELOG.md EOD — 39 days unlogged.*
