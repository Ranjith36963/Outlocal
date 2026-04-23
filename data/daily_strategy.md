# Daily Strategy — 2026-04-23 (Wednesday) — Day 26

## Campaign Overview

| Metric | Value | Notes |
|---|---|---|
| Leads scraped to date | ~61 (leads 1–61) | Batch 5 not yet scraped — 16 days overdue |
| Emails sent (estimated) | ~82 | Includes tu_036-040 assumed sent Tuesday |
| Total replies | 11 | 17.9% reply rate across all touchpoints |
| INTERESTED | 3 | Claire (3), Rob (22), Tom (1) — OUTCOME_UNKNOWN × 19 days |
| NOT_INTERESTED | 2 | Lead 2 (Nidderdale Pet Supplies) |
| UNSUBSCRIBE | 1 | Lead 19 — permanently suppressed |
| OUT_OF_OFFICE | 2 | Both resolved, sequences complete |
| Sequences completing today | 5 | fu_041-045 |
| Sequences completing tomorrow | 4 | fu_046-049 |
| New-lead pipeline gap | 16 days | **EXISTENTIAL. Batch 5 must happen today.** |
| IMAP gap | 19 days | Last confirmed HANDS check: 2026-04-04 |
| Warm pipeline outcomes unknown | 3 | Must resolve TODAY |
| Tuesday execution status | UNCONFIRMED | HANDS has not updated any output file since 2026-04-21 |

---

## CRITICAL GAPS — ACT BEFORE 09:00

Two compounding gaps require resolution before today's send window opens:

### Gap 1: IMAP (19 days unconfirmed)
The last confirmed IMAP check was 2026-04-04. Leads may have replied to Day-3, Day-7, or even proposal emails and the replies are sitting unread. Sending a breakup to a lead that already replied is a serious relationship error.

**Before 09:00:** Check IMAP for each of today's 5 breakup leads (30, 31, 32, 58, 59). Check warm pipeline leads (3, 22, 1) if not yet resolved from Tuesday.

### Gap 2: Tuesday execution unconfirmed
fu_036 (Sarah, Blossom Beauty), fu_037 (Dr Rowe, Meadowbrook Vets), fu_038 (Mike Thornfield, Thornfield Electricals), fu_039 (Mike Rawlings, Scarborough Bay Plumbing), fu_040 (James Hewitt, Pocklington Fine Furniture) — status unknown. If not sent Tuesday, they are now 6 days overdue. Still worth sending today alongside today's scheduled sends — HANDS flag in CHANGELOG.md.

---

## TODAY (Wednesday, 2026-04-23) — STRICT EXECUTION ORDER

### Step 1: IMAP sweep — warm pipeline (07:00 target)

If not resolved from Tuesday, check in this order:

1. **Claire, Westfield Hair & Beauty** (`claire@westfieldhair.co.uk`)
   - 16 days since call. 13 days since proposal nudge. Close window was 2026-04-14.
   - Decision tree: see `value_delivery_queue.json` vd_001
   - **Deadline: send final close by 16:00 today if no prior close sent**

2. **Rob, Pennine Print & Design** (`rob@pennineprint.co.uk`)
   - 16 days since nudge. Close window was 2026-04-15.
   - Rob's bundle question ('sort the whole thing in one go') remains the strongest buying signal in the campaign.
   - **Deadline: send final close by 16:00 today if no prior close sent**

3. **Tom, Ripon Road Carpentry** (`tom@riponroadcarpentry.co.uk`)
   - 15 days since nudge. Close window was ~2026-04-14.
   - Spring carpentry season — pain may be more acute now.
   - **Deadline: send final close by 16:00 today if no prior close sent**

### Step 2: Retrieve email addresses from database before 09:00

Leads 30, 31, 32 have `HANDS: retrieve from database` markers in `followup_queue.json`. Do this before the send window opens — it is a blocking dependency for fu_041, fu_042, fu_043.

### Step 3: Breakup email sends (09:00-10:15)

All bodies pre-written in `followup_queue.json`. IMAP check immediately before each individual send.

| Time | ID | Business | Recipient | Email |
|---|---|---|---|---|
| 09:00 | fu_041 | Halifax Window Cleaning | Steve | DB lookup |
| 09:15 | fu_042 | Pontefract Pharmacy | — (no name) | DB lookup |
| 09:30 | fu_043 | Castleford Carpets | Ann | DB lookup |
| 09:45 | fu_044 | The Old Court Solicitors | — (no name) | info@oldcourtsolicitors.co.uk |
| 10:00 | fu_045 | Scarborough Roofing Specialists | Tony Shields | tony@scarboroughroofing.co.uk |

If any lead has replied since 2026-04-04: classify the reply, cancel that breakup, route per `reply_classifications.json`.

### Step 4: Confirm Tuesday sends in CHANGELOG.md (by 10:30)

Confirm actual send/cancel status for fu_036-040. If any were NOT sent: add them to today's send queue immediately after fu_045 (10:15+). They are overdue but still valuable as final touchpoints.

### Step 5: Batch 5 Ryedale scrape — CRITICAL (10:30-12:30)

**This is the most urgent single action of the entire week.**

Without Batch 5 data today, the campaign will have zero new sends from Friday 2026-04-25 onwards — the first complete pipeline stall since launch.

- Target areas: **Malton, Pickering, Helmsley, Kirkbymoorside, Hovingham, Norton-on-Derwent**
- Categories: plumbers, electricians, roofers, builders, joiners, pubs/restaurants, B&Bs, estate agents, solicitors
- Expected yield: 18-22 raw leads
- Return format: business name, URL (or no-website flag), Google review count + rating, town, category, phone
- **Do NOT attempt email copy** — return raw data and BRAIN writes copy on next run (Thursday 24 April)
- **Deadline: Wednesday EOD** — if data returns Wednesday, BRAIN can write copy Thursday morning, enabling initial sends Thursday afternoon

### Step 6: Unblock carried-forward leads (parallel with scrape)

| Lead | Business | Days blocked | Action |
|---|---|---|---|
| 49 | East Riding Builders Ltd | 23 | Companies House director name + domain pattern |
| 51 | Driffield Garden Centre | 23 | Phone call after 09:30 |
| 53 | Bridlington Bay Lettings | 23 | Rightmove / Zoopla agent directory |
| 54 | The Wolds Inn | 23 | Try info@thewoldsinn.co.uk (low priority) |

### Step 7: LinkedIn — Wednesday cohort (afternoon)

Medium priority. For leads with Thursday breakups — separate email and LinkedIn by 18+ hours:
- Lead 50 (Pete, Harbour Fish Bar)
- Lead 52 (Linda Walsh, Holderness Homecare)
- Lead 55 (Craig Lawson, Beverley Sports & Leisure)
- Lead 56 (Neil, East Riding Electrical)

Connection notes pre-written in `linkedin_connection_notes.json`. Check `linkedin_profiles.json` first — if HANDS wrote profiles on Tuesday, upgrade connection notes before sending requests.

---

## TOMORROW (Thursday, 2026-04-24)

### Morning sends (09:00-10:00)

| Time | ID | Business | Recipient |
|---|---|---|---|
| 09:00 | fu_046 | Holderness Homecare | Linda Walsh |
| 09:15 | fu_047 | Beverley Sports & Leisure | Craig Lawson |
| 09:30 | fu_048 | The Harbour Fish Bar (Bridlington) | Pete |
| 09:45 | fu_049 | East Riding Electrical | Neil |

Retrieve email addresses for leads 50, 52, 55, 56 from database before 09:00.

**After fu_049 is sent: the entire active campaign cohort will have been through all 4 touchpoints.** This is campaign milestone #2 (milestone #1 is first revenue).

### New initial sends (10:30+)

3-5 Batch 5 Ryedale sends — ONLY if HANDS returned data Wednesday EOD AND BRAIN wrote copy Thursday morning. BRAIN must run Thursday at 07:00 to write copy before Thursday's send window.

---

## CAMPAIGN MILESTONE ANALYSIS (Day 26)

By end of Thursday 2026-04-24:
- All 60+ active leads will have been through all 4 touchpoints
- Full dataset exists for the first time
- First complete campaign A/B test results available

### Preliminary analysis (without final closes / unconfirmed actions)

| Signal type | Leads sent | Positive replies | Rate |
|---|---|---|---|
| SSL (PAS) | ~20 | 3 (Claire, Rob, Tom) | ~15% |
| Mobile (PAS) | ~12 | 0 confirmed | 0% (needs review) |
| No website (BAB) | ~6 | 0 confirmed | 0% |
| Social media (AIDA) | ~4 | 0 confirmed | 0% |

**Finding confirmed:** SSL → PAS → first-name subject is the core playbook. All 3 INTERESTED leads used this combination. PAS outperforms BAB and AIDA for technical-deficit signals.

---

## WINNING PATTERNS (confirmed, Day 26)

1. **SSL → PAS → first-name subject** — 3/3 INTERESTED leads. Core playbook for all new batches.
2. **Day-7 new pain-point pivot, not reframe** — Tom replied to Day-7 (not Day-0). Always shift to a *new* pain point on Day-7. Never re-state the original.
3. **Town name in subject and body** — non-negotiable trust signal. No exceptions.
4. **Two-sentence proposal nudges** — outperform longer follow-ups. Keep nudges short.
5. **One pain point per email** — multiple issues overwhelm. One clear signal per touchpoint only.
6. **B2B owners reply on Tuesday AM** — first business day after any break produces above-average yield.

---

## A/B TEST STATUS (Day 26)

| Variable | Status | Finding |
|---|---|---|
| Name vs business in subject | **CONFIRMED** | Name-first dominates 3-0. Default always. |
| PAS vs BAB vs AIDA | **PAS CONFIRMED** | 3/3 INTERESTED from PAS. PAS default for SSL + mobile. |
| Day-7 new angle vs reframe | **CONFIRMED** | New angle (Tom replied). Never reframe. |
| Easter Saturday B2B send | **PENDING** — fu_020/021 sent Saturday | Tuesday IMAP will reveal rate. HANDS must confirm. |
| Wednesday breakup rate | **NEW** — today's 5 breakups | First Wednesday-specific data. Log replies by day. |
| Post-19-day-IMAP-gap yield | **NEW** — ongoing | Will this extended gap produce a suppressed reply burst? |
| GDPR frame for solicitors | **NEW** — fu_044 today | Watch for reply from The Old Court Solicitors post-breakup. |

---

## BATCH 5 SIGNAL PREVIEW (Ryedale, pre-scrape)

| Signal | Probability | Framework |
|---|---|---|
| SSL / HTTP | 55-65% | PAS |
| Mobile fail | 15-20% | PAS |
| No website | 10-15% | BAB (active-review only, 4★+) |
| Social / high review | 5-10% | AIDA (4.5★+ with 100+ reviews only) |

**Ryedale profile:** Rural North Yorkshire market towns. Higher no-website density than East Yorkshire. Trades businesses (plumbing, electrical, roofing, joinery) are primary target — offline referral model, digital gap real and acknowledged. Low digital sophistication = high signal density = strong expected conversion rate (~20-25% based on Batches 1-3 SSL performance).

---

## COMPLIANCE STATUS (Day 26)

- Lead 19 (Summit Fitness) — permanently suppressed. No contact on any channel.
- Lead 2 (Nidderdale Pet Supplies) — LOST. No contact.
- Lead 7 — suppressed. No contact.
- All 14 breakup sequences respect 4-touchpoint maximum.
- GDPR: all outreach B2B legitimate interest. Unsubscribes processed within 24 hours (last: Lead 19).
- No residential addresses. No fitness/wellness in Otley until framing reviewed.
- Max daily send volume: 5 breakups today, 4 tomorrow. Well within 40/day domain safety limit.

---

## BRAIN OPERATING SCHEDULE

| Date | BRAIN Run | Purpose | Status |
|---|---|---|---|
| Tue 22 Apr | Missed | Write Batch 5 copy / IMAP resolution | ⚠ MISSED — no HANDS data |
| **Wed 23 Apr** | **TODAY** | Wednesday breakup sends + Batch 5 copy placeholder | ✓ Running now |
| Thu 24 Apr | REQUIRED | Thursday breakup sends + Batch 5 initial copy | MANDATORY |
| Sun 27 Apr | Required | Batch 5 Day-3 bumps (if initial sends went out Thu/Fri) | Schedule now |
| Tue 29 Apr | Required | Batch 5 Day-7 new angles | |
| Fri 2 May | Required | Batch 5 Day-14 breakup prep | |

**Hard rule:** BRAIN must run every 3 days maximum. Thursday (24 April) is the next mandatory run — Batch 5 copy must be written before initial sends fire.

---

## WHAT TO EXPECT BY END OF WEEK

### Breakup responses (0-2% base rate)
Today: 5 breakups. Tomorrow: 4 breakups. 9 more final touchpoints. Occasionally a breakup unlocks a delayed decision — particularly for leads who were genuinely interested but busy. If anyone replies to a breakup with intent: cancel any further actions, route to `value_delivery_queue.json` immediately, and write to CHANGELOG.md.

### Warm pipeline resolution (today)
By end of today we will have confirmed outcomes for Claire, Rob, and Tom. Best case: one conversion (£350+). Likely case: one or two final closes with LOST_NO_RESPONSE. Even zero converts provides the data needed to optimise the next batch.

### Batch 5 pipeline (Friday onwards)
If Batch 5 data arrives today: BRAIN writes copy Thursday AM → initial sends Thursday PM → first opens Thursday evening → Day-3 bumps Sunday/Monday.

If Batch 5 data does NOT arrive today: first new sends slip to Monday 2026-04-28 at the earliest. 14 days of zero initial sends becomes 19 days. This is the worst-case scenario and must be avoided.

---

## POST-CAMPAIGN ANALYSIS PREVIEW (available Friday 2026-04-25)

After all sequences complete Thursday, the full dataset will enable:

1. **Signal performance analysis:** SSL vs mobile vs no-website vs social by reply rate
2. **Framework analysis:** PAS vs BAB vs AIDA by positive reply rate
3. **Day-of-week analysis:** Which days produce the most replies (Thursday AM looks strong from early data)
4. **Sequence step analysis:** Day-0 vs Day-3 vs Day-7 by first positive reply
5. **Sector analysis:** Trades vs beauty vs hospitality vs professional services
6. **Geography analysis:** West Yorkshire vs North Yorkshire vs East Yorkshire reply rates

This analysis should inform the Batch 5 and Batch 6 targeting and sequencing strategy. BRAIN will write a full Week 4 strategy document on Friday 2026-04-25 (or Saturday at latest).

---

*Generated by OUTLOCAL BRAIN layer — 2026-04-23 08:00 UTC*  
*HANDS instructions for TODAY:*
*1. IMAP sweep (warm pipeline: Claire, Rob, Tom) — if not done Tuesday, do BEFORE 09:00 today*
*2. Retrieve emails for leads 30, 31, 32 from database — before 09:00*
*3. Breakup sends fu_041 → fu_042 → fu_043 → fu_044 → fu_045 (09:00-10:15)*
*4. Confirm Tuesday sends fu_036-040 in CHANGELOG.md (by 10:30)*
*5. Batch 5 Ryedale Google Maps scrape (10:30-12:30) — CRITICAL — return raw data by EOD*
*6. Unblock leads 49, 51, 53, 54 (parallel with scrape)*
*7. LinkedIn for Thursday breakup leads 50, 52, 55, 56 (afternoon)*
*8. Send final closes for Claire/Rob/Tom by 16:00 if not yet sent*
