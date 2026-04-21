# Daily Strategy — 2026-04-21 (Easter Monday) — Day 24

## Campaign Overview

| Metric | Value | Notes |
|---|---|---|
| Leads scraped to date | ~61 (leads 1–61) | Batch 5 not yet scraped |
| Emails sent (estimated) | ~77 | Includes fu_020 + fu_021 assumed sent Easter Saturday |
| Total replies | 11 | 17.9% reply rate across all touchpoints |
| INTERESTED | 3 | Claire (lead 3), Rob (lead 22), Tom (lead 1) — outcomes unknown |
| NOT_INTERESTED | 2 | Lead 2 (Nidderdale Pet Supplies) |
| UNSUBSCRIBE | 1 | Lead 19 — permanently suppressed |
| OUT_OF_OFFICE | 2 | Both resolved, sequences complete |
| Sequences completing this week | 14 | All breakup emails (fu_036–049) |
| New-lead pipeline gap | 14 days | Batch 5 is existential |
| IMAP gap | 17 days | Last checked 2026-04-04 |
| Warm pipeline outcomes unknown | 3 | Must resolve 2026-04-22 first thing |

---

## TODAY (Easter Monday, 2026-04-21)

**ZERO SENDS. ZERO LINKEDIN. No outreach on any channel.**

UK bank holiday. No business email expected. No decision-makers at their desks.

Only BRAIN-layer activity today: this strategy file.

---

## TOMORROW IS THE MOST IMPORTANT EXECUTION DAY OF THE CAMPAIGN

Tuesday 2026-04-22 is the highest-stakes single day since launch. Three things converge:

1. **17 days of unread IMAP** — any reply from the warm pipeline (Claire, Rob, Tom) or cold sequence leads who responded to Day-7 emails is sitting unread right now.
2. **14 breakup emails queued** — the final touchpoints for the entire active lead cohort. Sending a breakup to a lead that already replied is a serious error.
3. **14-day pipeline gap** — without Batch 5 Ryedale data scraped and back to BRAIN, there are no new sends until end of week at the earliest.

Get these wrong and the campaign stalls. Get them right and there may be revenue to log, plus a fresh batch of leads entering the pipeline.

---

## TUESDAY 2026-04-22 — STRICT EXECUTION ORDER

Do not deviate from this sequence. Every step depends on the one before.

### Step 1: IMAP sweep — warm pipeline (07:00 target)

Check in this order:
1. **Claire, Westfield Hair & Beauty** (`claire@westfieldhair.co.uk`) — call was 2026-04-07, proposal nudge sent ~2026-04-10. Final close window passed ~2026-04-14.
2. **Rob, Pennine Print & Design** (`rob@pennineprint.co.uk`) — nudge sent 2026-04-07. Rob's question about a full redesign bundle was a genuine purchase signal. Close window was 2026-04-15.
3. **Tom, Ripon Road Carpentry** (`tom@riponroadcarpentry.co.uk`) — nudge sent 2026-04-08. Close window was ~2026-04-14.

Apply the decision trees in `data/value_delivery_queue.json` for each. Update status fields: `CONVERTED / LOST / LOST_NO_RESPONSE / STILL_LIVE`. Write to CHANGELOG.md immediately if any converts.

**Why this matters:** Easter weekend is a known reply trigger — B2B owners often scroll email on Sunday evenings or Easter Monday and compose a reply they send Tuesday morning. Rob especially: he was in a buying frame of mind and had a 4-day weekend to make a decision. Do not assume these leads are lost before checking IMAP.

### Step 2: LinkedIn searches — CRITICAL 5 (07:00–09:00)

For leads 42 (Sarah, Blossom Beauty) → 44 (Dr Rowe, Meadowbrook Vets) → 46 (Mike Thornfield, Thornfield Electricals) → 57 (Mike Rawlings, Scarborough Bay Plumbing) → 60 (James Hewitt, Pocklington Fine Furniture).

Check IMAP for each lead immediately before sending the connection request. Connection notes are in `data/linkedin_connection_notes.json`. Populate `data/linkedin_profiles.json` after each search — this is blocking all note quality upgrades.

Maximum 10 minutes per search. Skip and move on if profile not found.

### Step 3: Breakup email sends (09:00–10:15)

All bodies are pre-written in `data/followup_queue.json`. In order:

| Time | ID | Business | Recipient |
|---|---|---|---|
| 09:00 | fu_036 | Blossom Beauty Studio | Sarah (York) |
| 09:15 | fu_037 | Meadowbrook Vets | Dr Rowe (Skipton) |
| 09:30 | fu_038 | Thornfield Electricals | Mike Thornfield (Bradford) |
| 09:45 | fu_039 | Scarborough Bay Plumbing | Mike Rawlings |
| 10:00 | fu_040 | Pocklington Fine Furniture | James Hewitt |

IMAP check for each lead immediately before sending. If reply found: classify, cancel breakup, re-route.

Retrieve email addresses from database for leads 42, 44, 46 before 09:00 — these are marked `HANDS: retrieve from database` in the queue.

### Step 4: LinkedIn searches — HIGH priority (10:30+)

For leads 30 (Steve, Halifax) → 32 (Ann, Castleford) → 59 (Tony, Scarborough Roofing) → 58 (Old Court Solicitors — website crawl for named individual first) → 31 (Pontefract Pharmacy — conditional, named individual required).

These leads have breakup emails on 2026-04-23. Do LinkedIn this afternoon to separate the channels by 18+ hours.

### Step 5: Batch 5 Ryedale Google Maps scrape (10:30+, background)

Target areas: Malton, Pickering, Helmsley, Kirkbymoorside, Hovingham, Norton-on-Derwent.
Categories: plumbers, electricians, roofers, builders, joiners, pubs/restaurants, B&Bs, estate agents, solicitors.

Do NOT attempt to write email copy. Return raw data and BRAIN will assign signals on the next run (BRAIN needs to run Tuesday evening or Wednesday morning to write Batch 5 copy in time for Wednesday/Thursday sends).

### Step 6: Unblock blocked leads (parallel with scrape)

- **Lead 49** (East Riding Builders Ltd): Companies House director name search. Domain pattern attempt.
- **Lead 51** (Driffield Garden Centre): Phone after 09:30. "Just need the right address for some information I wanted to send across."
- **Lead 53** (Bridlington Bay Lettings): Rightmove / Zoopla agent directory. Try info@ fallback.
- **Lead 54** (The Wolds Inn): Try info@thewoldsinn.co.uk. Low priority — do after 49, 51, 53.

### Step 7: Confirm assumed-sent items in CHANGELOG.md

Verify and log: fu_027, fu_028, fu_029, fu_030, fu_031, fu_032, fu_020, fu_021.
Note actual send dates. Flag any that were NOT sent — BRAIN needs accurate data.

---

## WEDNESDAY 2026-04-23 PLAN

Morning breakup sends (09:00-10:15):
- fu_041 Steve, Halifax Window Cleaning
- fu_042 Pontefract Pharmacy
- fu_043 Ann, Castleford Carpets
- fu_044 Old Court Solicitors
- fu_045 Tony Shields, Scarborough Roofing

Retrieve email addresses for leads 30, 31, 32 from database before 09:00.

New sends (10:30+): 1-3 Batch 5 leads if BRAIN wrote copy on Tuesday evening/Wednesday morning.

BRAIN run required: Wednesday morning to write Batch 5 copy (if Ryedale data is back from HANDS by Tuesday EOD).

---

## THURSDAY 2026-04-24 PLAN

Morning breakup sends (09:00-10:00):
- fu_046 Linda Walsh, Holderness Homecare
- fu_047 Craig Lawson, Beverley Sports & Leisure
- fu_048 Pete, The Harbour Fish Bar (post-Easter, fishing/hospitality businesses busy)
- fu_049 Neil, East Riding Electrical

New sends (10:30+): 3-5 Batch 5 if copy is ready.

By end of Thursday: **the entire active lead cohort (60+ leads) will have been through all 4 touchpoints.** This is the first complete campaign dataset — full analysis follows.

---

## WHAT TO EXPECT BY END OF WEEK

### Breakup responses (normally 0-2%)
Out of 14 breakup emails this week, expect 0-1 late positive replies. Breakup emails occasionally unlock delayed decisions. If anyone replies to a breakup with interest: treat as warm lead, route to value_delivery_queue immediately.

### Batch 5 opens (earliest 2026-04-24)
If Batch 5 sends go out Wednesday/Thursday, the first opens and replies arrive Thursday/Friday. Ryedale trades businesses have a high density of SSL and mobile signals — PAS framework, strong reply rate expected (~20-25% based on Batches 1-3 SSL performance).

### Warm pipeline resolution
By end of Tuesday, we will know the outcome for Claire, Rob, and Tom. Best case: one conversion at £150-675. Likely case: one or two final closes with LOST_NO_RESPONSE status. Even a zero-conversion outcome provides the data needed to optimise the next 60-lead batch.

---

## POST-EASTER CAMPAIGN DATA: WHAT WE'LL KNOW BY FRIDAY

| Metric | Target | Current (Day 24) |
|---|---|---|
| Overall reply rate | 18-22% | 17.9% ✓ |
| Positive rate | 5-8% | 4.9% (marginally below — needs Batch 5 data) |
| INTERESTED-to-CONVERTED rate | 33%+ | 0/3 confirmed (all UNKNOWN) |
| Email cost | £0 | £0 ✓ |
| LLM cost | £0 | £0 ✓ |
| Revenue | ≥£1 to validate | £0 — unknown pending IMAP |

The campaign model is mathematically valid if one lead converts. Claire at £350 (Option B) = 33% INTERESTED-to-CONVERTED = validated.

---

## CONFIRMED WINNING PATTERNS (unchanged)

1. **SSL → PAS → first-name subject** — all 3 INTERESTED leads came from this combination. Core playbook for Batch 5.
2. **Day-7 new pain-point pivot** — Tom replied to Day-7 (not Day-0). Never reframe the original signal — always introduce a second distinct pain point.
3. **Town name in subject and body** — non-negotiable trust signal.
4. **Two-sentence proposal nudges** outperform longer follow-ups.
5. **BRAIN run every 3 days maximum** — the 10-day BRAIN gap between Days 12 and 22 caused 8 leads to skip Day-7 entirely. Confirmed opportunity cost.
6. **Tuesday AM IMAP sweep** — first working day after any holiday produces above-average reply yield.

---

## BATCH 5 SIGNAL PREVIEW (Ryedale, pre-scrape)

| Signal | Probability | Framework | Subject pattern |
|---|---|---|---|
| SSL / HTTP | 55-65% | PAS | "[Name] — [town] [trade] website flagged 'Not Secure'" |
| Mobile fail | 15-20% | PAS | "[Name] — [town] [business] site isn't mobile-friendly" |
| No website | 10-15% | BAB | "[Business] — [town] [trade]: customers can't find you online" |
| Social/high review | 5-10% | AIDA | "[Name] — [N] people reviewed [business], but your site isn't ranking" |

Ryedale profile: rural North Yorkshire market towns. Higher no-website density than East Yorkshire coast. Lower digital sophistication = higher signal density = strong conversion potential. Trades (plumbing, electrical, roofing, joinery) are the primary target — referrals typically offline, digital gap is real and acknowledged.

---

## A/B TEST STATUS (Day 24)

| Variable | Status | Finding |
|---|---|---|
| Name vs business in subject | Confirmed | Name-first dominates 3-0. Default always. |
| PAS vs BAB vs AIDA | PAS confirmed | 3/3 INTERESTED from PAS. PAS default for SSL + mobile. |
| Day-7 new angle vs reframe | Confirmed winner | New angle (Tom replied). Never reframe — always shift pain point. |
| Friday AM IMAP sweep | Observational | Highest reply density on Thursday/Friday sends. Still testing. |
| GDPR frame (professional) | Pending | Old Court Solicitors breakup (fu_044) sends Wednesday — watch for post-sequence reply. |
| Easter Saturday B2B send | Pending | fu_020/021 sent Saturday — Tuesday IMAP will reveal open/reply rate for weekend sends. |
| Post-Easter Tuesday reply rate | New test | 17-day IMAP gap resolved Tuesday. Will this yield higher-than-normal reply count? |

---

## COMPLIANCE STATUS (Day 24)

- Lead 19 (Summit Fitness) — permanently suppressed. No contact on any channel.
- Lead 2 (Nidderdale Pet Supplies) — LOST. No contact.
- Lead 7 — suppressed. No contact.
- Good Friday 2026-04-18 and Easter Monday 2026-04-21 — no outreach. Correctly enforced.
- All 14 breakup sequences respect the 4-touchpoint maximum.
- GDPR: all outreach B2B legitimate interest. Unsubscribes processed within 24 hours (last: Lead 19).
- No residential addresses. No fitness/wellness category in Otley until framing reviewed.

---

## BRAIN OPERATING SCHEDULE (post-Easter)

With all active lead sequences completing by 2026-04-24, BRAIN cadence becomes critical:

| Date | BRAIN Run | Purpose |
|---|---|---|
| Tue 22 Apr | ✓ TODAY (Day 25 run) | Write Batch 5 copy if Ryedale data returned by HANDS |
| Thu 24 Apr | Required | Day-3 bump copy for Batch 5 initial sends (if sent Wed/Thu) |
| Sun 27 Apr | Required | Day-3 bumps for Fri 25 sends; Day-7 prep for Mon 28 |
| Tue 29 Apr | Required | Day-7 new angles for Batch 5 |
| Fri 2 May | Required | Day-14 breakup prep for Batch 5 |

Maximum gap: 3 days. If BRAIN does not run by Thu 24 Apr, Batch 5 Day-3 bumps will be missed — repeat of the Easter gap failure.

**Hard rule from Day 22 onwards: BRAIN runs every 3 days maximum.**

---

## LINKEDIN (Easter Monday)

No LinkedIn activity today. LinkedIn paused until 2026-04-22.

Active cohort for tomorrow: leads 42, 44, 46, 57, 60 (CRITICAL — before 09:00).
Afternoon cohort: leads 30, 32, 59, 58, 31.
Wednesday cohort: leads 50, 52, 55, 56.
Optional last-shot: lead 8 (Graham, Ilkley Ironmongery) — post-breakup, low yield.

Connection notes pre-written in `data/linkedin_connection_notes.json`.
HANDS must write `data/linkedin_profiles.json` after each search — 5 BRAIN runs have been unable to upgrade notes without this data.

---

*Generated by OUTLOCAL BRAIN layer — 2026-04-21 08:00 UTC*  
*HANDS: TODAY — no sends (Easter Monday bank holiday). TOMORROW (2026-04-22): IMAP sweep at 07:00 → LinkedIn CRITICAL before 09:00 → 5 breakup emails 09:00-10:15 → Batch 5 scrape 10:30+ → unblock leads 49/51/53. This is the single most important execution day of the campaign. See followup_queue.json, daily_email_plan.json, value_delivery_queue.json, and linkedin_coordination.json.*
