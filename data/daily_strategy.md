# Daily Strategy — 2026-04-20 (Easter Sunday) — Day 23

## Campaign Overview

| Metric | Value | Notes |
|---|---|---|
| Leads scraped to date | ~61 (leads 1–61) | Batch 5 not yet scraped |
| Emails sent (estimated) | ~77 | Includes fu_020 + fu_021 assumed sent yesterday |
| Total replies | 11 | 17.9% reply rate across all touchpoints |
| INTERESTED | 3 | Claire, Rob, Tom — outcomes unknown |
| NOT_INTERESTED | 2 | — |
| UNSUBSCRIBE | 1 | Lead 19 permanently suppressed |
| OUT_OF_OFFICE | 2 | Both resolved, sequences complete |
| Sequences completing this week | 14 | All breakup emails (fu_036–049) |
| New-lead pipeline gap | 13 days | Batch 5 is existential |
| Warm pipeline outcomes unknown | 3 | Must resolve 2026-04-22 morning |

---

## TODAY (Easter Sunday, 2026-04-20)

**ZERO SENDS. No outreach on any channel.**

fu_020 (Rachel, Skipton Garden Design) and fu_021 (Boroughbridge Plumbing) are assumed sent yesterday. If HANDS did not send them: they are now 1 day overdue but still worth sending — send both on Tuesday 2026-04-22 as the first two items before the breakup window.

---

## TOMORROW (Easter Monday, 2026-04-21)

**ZERO SENDS. UK bank holiday. No outreach on any channel.**

---

## MOST IMPORTANT ACTIONS ON 2026-04-22 (Tuesday — first business day)

Priority order is strict. Do not deviate.

### 1. Full IMAP sweep — warm pipeline first (09:00 target)
Check Claire (lead 3) → Rob (lead 22) → Tom (lead 1).
Apply decision tree from value_delivery_queue.json for each.
Log outcomes immediately — update value_delivery_queue.json status fields.
Even one CONVERTED entry transforms the campaign narrative.

### 2. Retrieve DB email addresses before 09:00
Before starting breakup sends, pull from database:
- Lead 42 (Blossom Beauty Studio)
- Lead 44 (Meadowbrook Vets)
- Lead 46 (Thornfield Electricals)
- Lead 30 (Halifax Window Cleaning) — for Wed sends
- Lead 31 (Pontefract Pharmacy) — for Wed
- Lead 32 (Castleford Carpets) — for Wed
- Leads 50, 52, 55, 56 — for Thu sends

### 3. Send 5 breakup emails (09:00–10:15)
fu_036 → fu_037 → fu_038 → fu_039 → fu_040
IMAP check before each individual send. If reply found: classify, cancel breakup, re-route.

### 4. Run Batch 5 Ryedale Google Maps scrape (after 10:30)
Target: Malton, Pickering, Helmsley, Kirkbymoorside, Hovingham, Norton-on-Derwent.
Categories: plumbers, electricians, roofers, builders, joiners, pubs/restaurants, B&Bs, estate agents, solicitors.
Return raw data to BRAIN. Do not attempt to write email copy — BRAIN will do this.

### 5. Unblock blocked leads (parallel with scrape)
- Lead 49 (East Riding Builders): Companies House director search
- Lead 51 (Driffield Garden Centre): phone for direct email
- Lead 53 (Bridlington Bay Lettings): Rightmove/Zoopla + info@ fallback
- Lead 54 (The Wolds Inn): try info@thewoldsinn.co.uk

### 6. Confirm assumed-sent items in CHANGELOG.md
Verify and log: fu_027, fu_028, fu_029, fu_030, fu_031, fu_032, fu_020, fu_021.
Note actual send dates for any that are confirmed. Flag any that were NOT sent.

---

## Post-Easter Send Calendar (confirmed)

| Date | Sends | IDs | Notes |
|---|---|---|---|
| Sun 20 Apr | 0 | — | TODAY — Easter Sunday |
| Mon 21 Apr | 0 | — | Easter Monday — bank holiday |
| **Tue 22 Apr** | **5 breakups** | fu_036–040 | + IMAP sweep + Batch 5 scrape |
| **Wed 23 Apr** | **5 breakups** + 1-3 new | fu_041–045 | Batch 5 new sends if copy ready |
| **Thu 24 Apr** | **4 breakups** + 3-5 new | fu_046–049 | Batch 5 new sends |
| **Fri 25 Apr** | 5-8 new sends | Batch 5 | Full Batch 5 send day |
| Mon 28 Apr | Day-3 bumps | Batch 5 | For sends made 22-23 Apr |
| Tue 29 Apr | Day-3 bumps | Batch 5 | For sends made 24-25 Apr |

---

## Strategy Update: What Easter Week Has Clarified

### The BRAIN gap was costly in one specific way
Between 2026-04-10 and today (10 days), 8 leads missed their Day-7 new-angle window and went straight to breakup. Day-7 is confirmed as the highest-conversion touchpoint (Tom/lead 1 replied to Day-7, not Day-0). We will never know how many of the 8 skipped leads might have converted with a well-crafted new angle. This is an opportunity cost, not a model failure. Going forward: **BRAIN must run every 3 days maximum** — this is now a firm operating rule.

### Easter Monday return = warm inbox opportunity
UK B2B decision-makers returning from a 4-day bank holiday weekend will typically:
1. Clear urgent emails Monday morning (bank holiday — most won't do this)
2. Do a proper inbox clear on Tuesday morning
3. Action deferred items Wednesday/Thursday

This means Tuesday IMAP sweep is higher-yield than a normal Tuesday — there may be replies to pre-Easter follow-ups that were read over the weekend and are now awaiting action. Do the IMAP sweep before 09:00 on Tuesday.

### Breakup timing post-Easter is acceptable
Breakup emails sent Tuesday/Wednesday after a bank holiday are commercially fine:
- Leads are returning to work and clearing backlogs
- A brief, final 'closing the loop' message will be noticed rather than buried
- The hospitality cohort (Pete/Harbour Fish Bar, East Riding) are at peak seasonal motivation post-Easter
- Dr Rowe (Meadowbrook Vets) operates a professional practice — Tuesday post-Easter is a normal working day

### Batch 5 urgency is now maximal
13 days without new leads entering the pipeline. With April ending on April 30, there are 8 business days remaining in the month. Working backwards:
- Day-14 breakups for Batch 5 leads would fall in mid-May
- Day-7 new angles fall in early May
- Day-3 bumps fall in late April / early May
- Initial sends: **must begin 2026-04-23 at the very latest** for a workable April sequence

If Batch 5 sends begin Wednesday 2026-04-23: the campaign will have ~6 active sequences running through May. This is the minimum viable pipeline to maintain momentum.

### The complete campaign dataset arrives this week
By end of Thursday 2026-04-24, all 60+ leads will have been through all 4 touchpoints. This is the first time BRAIN will have a complete performance dataset. Target benchmarks:
- **Reply rate (all touchpoints):** 18-22% — current ~17.9%, on track
- **Positive (INTERESTED) rate:** 5-8% — current 4.9%, marginally below target
- **INTERESTED-to-CONVERTED rate:** 33%+ — 0/3 confirmed, all unknown
- **Campaign validation:** one conversion at any price point validates the model

If we reach Thursday with zero confirmed conversions (even from Claire/Rob/Tom), the BRAIN layer should write a campaign model assessment note. If Claire converts at £350, converted rate = 33% — campaign validated.

---

## A/B Test Status (Day 23)

| Variable | Result | Action |
|---|---|---|
| Name vs business in subject | Name dominant: 3/3 INTERESTED came from name-first subjects | Rule confirmed. Default: name-first always. |
| PAS vs BAB framework | PAS dominant: 3/3 INTERESTED from PAS | PAS default confirmed for SSL and mobile signals. |
| Day-7 new angle vs reframe | New angle wins (Tom) | Always shift pain point on Day-7. Never reframe original. |
| Friday morning IMAP sweep | Observational: highest reply day appears to be Thursday/Friday | Schedule IMAP sweeps Friday AM. |
| GDPR frame for professional leads | Insufficient data (fu_028/fu_044 pending) | Watch for post-Easter reply to Old Court Solicitors before Wednesday breakup. |
| Easter Saturday B2B outreach | No data yet (fu_020/021 sent Saturday, no IMAP since) | Tuesday IMAP will confirm whether Easter Saturday sends get opens/replies. |

---

## Batch 5 Ryedale — Pre-BRAIN Signal Preview

Before HANDS returns the scrape data, BRAIN can pre-assign expected signal distribution for Ryedale:

**Ryedale profile:**
- Rural North Yorkshire market towns
- High density of trades (plumbers, electricians, joiners, roofers) and hospitality (pubs, B&Bs, restaurants)
- Many businesses have legacy websites or no website — built 10+ years ago, often not SSL, rarely mobile-optimised
- Lower digital sophistication than urban areas — higher proportion of no-website leads expected vs Batch 4 (East Yorkshire coast)

**Expected signal breakdown:**
| Signal | Expected % | Framework | Subject pattern |
|---|---|---|---|
| SSL / HTTP | 55-65% | PAS | "[Name] — [town] [trade] website is flagged 'Not Secure'" |
| Mobile fail | 15-20% | PAS | "[Name] — [town] [business] site isn't mobile-friendly" |
| No website | 10-15% | BAB | "[Business name] — [town] [trade]: customers can't find you online" |
| Social media / high reviews | 5-10% | AIDA | "[Name] — [number] people reviewed [business], but your site isn't ranking" |

**Prioritisation rule for Ryedale:**
1. Trades with owner name + SSL signal → email immediately (highest conversion rate)
2. Trades with owner name + mobile signal → email second wave
3. Hospitality with high reviews + no website → BAB framework, strong seasonal angle (spring/summer)
4. Professional services (solicitors, accountants) → PAS + GDPR trust angle, as per Old Court Solicitors pattern

---

## Winning Patterns — Confirmed to Day 23

1. **SSL → PAS → first-name subject** = all 3 INTERESTED leads. Core playbook.
2. **Day-7 new pain-point pivot** = confirmed winner (Tom). Never reframe — always shift.
3. **Town name in subject and body** = trust signal. Non-negotiable.
4. **Two-sentence proposal nudges** outperform longer follow-ups.
5. **IMAP sweep on Friday AM** = highest yield window.
6. **BRAIN run every 3 days maximum** = new hard rule. 10-day gaps destroy sequence value.

---

## Compliance Notes

- Lead 19 (Summit Fitness) — permanently suppressed. No contact on any channel.
- Lead 2 (Nidderdale Pet Supplies) — LOST. No contact.
- Lead 7 — suppressed. No contact.
- Good Friday 2026-04-18 and Easter Monday 2026-04-21 — no outreach. Correctly enforced.
- All 14 breakup sequences respect the 4-touchpoint maximum (Day 0 + Day 3 + Day 7 + Day 14).
- GDPR: any unsubscribe processed within 24 hours. None pending.
- Warm pipeline (leads 1, 3, 22): continued contact valid under B2B legitimate interest (they replied voluntarily).

---

## LinkedIn — Easter Period Update

LinkedIn activity is paused for all current sequences. All active leads are at Day 14 (breakup stage). LinkedIn connection at breakup stage has near-zero ROI. No LinkedIn outreach until Batch 5 leads reach Day 3 (earliest 2026-04-26).

**Exception:** If any Batch 5 lead has a highly active LinkedIn profile with recent posts, a targeted connection note on Day 3 remains a valid secondary channel. BRAIN will flag in the Batch 5 signal assignment.

---

*Generated by OUTLOCAL BRAIN layer — 2026-04-20 09:00 UTC*  
*HANDS: TODAY — no sends (Easter Sunday). TOMORROW — no sends (Easter Monday bank holiday). TUESDAY 2026-04-22: IMAP sweep + warm pipeline resolution FIRST, then 5 breakup emails, then Batch 5 scrape. See followup_queue.json and daily_email_plan.json.*
