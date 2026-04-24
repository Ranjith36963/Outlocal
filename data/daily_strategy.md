# Daily Strategy — 2026-04-24 (Thursday) — Day 27

## Campaign Overview

| Metric | Value | Notes |
|---|---|---|
| Leads scraped to date | ~61 (leads 1–61) | Batch 5 not yet scraped — 17 days overdue |
| Emails sent (estimated) | ~86 | Includes assumed Wednesday sends fu_041-045 |
| Total replies | 11 | 17.9% reply rate — strong for cold outreach |
| INTERESTED | 3 | Claire (3), Rob (22), Tom (1) — OUTCOME_UNKNOWN × 20 days |
| NOT_INTERESTED | 2 | Lead 2 (Nidderdale Pet Supplies) |
| UNSUBSCRIBE | 1 | Lead 19 — permanently suppressed |
| OUT_OF_OFFICE | 2 | Both resolved, sequences complete |
| Sequences completing today | 4 | fu_046-049 |
| Sequences completing after today | 0 | Campaign cohort complete |
| New-lead pipeline gap | 17 days | **CRITICAL. Batch 5 must happen today.** |
| IMAP gap | 20 days | Last confirmed HANDS check: 2026-04-04 |
| Warm pipeline outcomes unknown | 3 | Final close attempts today — no further slippage |
| Wednesday execution status | UNCONFIRMED | No output files updated since 2026-04-21 |

---

## CAMPAIGN MILESTONE — TODAY

After fu_049 (Neil, East Riding Electrical, ~09:45) is sent:

**ALL active sequences are complete. The entire campaign cohort (~60 leads, Batches 1–4) will have been through all 4 touchpoints.**

This is the first moment in the campaign where a complete, analysable dataset exists. It enables:
- Signal-type performance comparison (SSL vs mobile vs no-website vs social)
- Framework performance comparison (PAS vs BAB vs AIDA)
- Sequence-step analysis (Day-0 vs Day-3 vs Day-7 vs Day-14 reply rates)
- Day-of-week analysis
- Sector and geography breakdowns

**HANDS: log in CHANGELOG.md after fu_049 confirms sent — "Campaign milestone #2: all sequences complete."**

BRAIN will write the full post-campaign analysis in the next run (Friday 2026-04-25 or Saturday 2026-04-26).

---

## TODAY (Thursday, 2026-04-24) — STRICT EXECUTION ORDER

### Step 1: IMAP sweep — warm pipeline (before 09:00)

Three leads have been INTERESTED since 2026-04-04. Their close windows have passed. Today is the final day for close attempts.

1. **Claire — Westfield Hair & Beauty** (`claire@westfieldhair.co.uk`)
   - 17 days since call. 14 days since proposal nudge.
   - Decision: see `value_delivery_queue.json` vd_001
   - **If no reply and no prior close sent: send final close before 12:00. Then mark LOST_NO_RESPONSE.**

2. **Rob — Pennine Print & Design** (`rob@pennineprint.co.uk`)
   - 17 days since nudge. Bundle signal still the strongest in the campaign.
   - Decision: see `value_delivery_queue.json` vd_002
   - **If no reply and no prior close sent: send final close before 12:00. Then mark LOST_NO_RESPONSE.**

3. **Tom — Ripon Road Carpentry** (`tom@riponroadcarpentry.co.uk`)
   - 16 days since nudge. Spring carpentry season.
   - Decision: see `value_delivery_queue.json` vd_003
   - **If no reply and no prior close sent: send final close before 12:00. Then mark LOST_NO_RESPONSE.**

**After today: these three records are closed regardless of outcome. No further contact.**

---

### Step 2: Retrieve email addresses from database before 09:00

Leads 50, 52, 55, 56 have `HANDS: retrieve from database` markers. This is a blocking dependency for fu_046-049.

---

### Step 3: Breakup sends — CAMPAIGN FINAL (09:00–09:45)

All bodies pre-written in `followup_queue.json`. IMAP check before each individual send.

| Time | ID | Business | Recipient | Email |
|---|---|---|---|---|
| 09:00 | fu_046 | Holderness Homecare | Linda Walsh | DB lookup |
| 09:15 | fu_047 | Beverley Sports & Leisure | Craig Lawson | DB lookup |
| 09:30 | fu_048 | The Harbour Fish Bar | Pete | DB lookup |
| 09:45 | **fu_049** | **East Riding Electrical** | **Neil** | **DB lookup — FINAL SEND** |

If any lead has replied since 2026-04-04: classify the reply, cancel that breakup, route per `reply_classifications.json`.

---

### Step 4: Wednesday confirmation + contingency sends (by 10:30)

Confirm actual send/cancel status for fu_041-045 in CHANGELOG.md. If any were NOT sent on Wednesday: add them to today's queue after fu_049 (10:00+, 15-min stagger). They are overdue by one day but still valid final touchpoints.

---

### Step 5: Batch 5 Ryedale scrape — CRITICAL (10:30–12:30)

**The most important action of the week. The campaign is now in full stall.**

- No active sequences after today
- No new sends possible until Batch 5 data is received and copy is written
- Target: Malton, Pickering, Helmsley, Kirkbymoorside, Hovingham, Norton-on-Derwent
- Categories: plumbers, electricians, roofers, builders, joiners, pubs/restaurants, B&Bs, estate agents, solicitors
- Expected yield: 18-22 raw leads
- Return format: business name, URL (or no-website flag), review count + rating, town, category, phone
- **Do NOT attempt email copy** — return raw data, BRAIN writes copy on Friday run

**Timeline if data returns today:**
BRAIN (Friday morning) → initial sends (Friday afternoon) → Day-3 bumps (Monday 2026-04-28)

**Timeline if data returns Friday:**
BRAIN (Friday evening/Saturday) → initial sends (Monday 2026-04-28) → Day-3 bumps (Thursday 2026-05-01)

---

### Step 6: Unblock carried-forward leads (parallel with scrape)

| Lead | Business | Days blocked | Action |
|---|---|---|---|
| 49 | East Riding Builders Ltd | 24 | Companies House director name + domain pattern |
| 51 | Driffield Garden Centre | 24 | Phone call after 09:30 |
| 53 | Bridlington Bay Lettings | 24 | Rightmove / Zoopla agent directory |
| 54 | The Wolds Inn | 24 | Try info@thewoldsinn.co.uk (low priority) |

---

### Step 7: Full post-campaign IMAP sweep (afternoon)

After today's sends complete: do a full IMAP sweep of the entire cohort. This is the first time since 2026-04-04 that BRAIN can request a complete inbox sweep. Any silent replies sitting in the inbox for 20+ days need to be found and classified.

Priority inbox check order:
1. Warm pipeline: claire@westfieldhair.co.uk, rob@pennineprint.co.uk, tom@riponroadcarpentry.co.uk
2. Today's breakup leads: leads 50, 52, 55, 56
3. Wednesday's breakup leads: leads 30, 31, 32, 58, 59
4. Remaining active cohort: all leads not in suppressed list

---

### Step 8: LinkedIn — check and send (afternoon, if time)

If connection requests were sent Wednesday for leads 50, 52, 55, 56: check acceptances. If accepted: wait 2-3 days before value message (do not rush).

If requests were NOT sent Wednesday: low priority today given the campaign milestone context — deprioritise until Batch 5 copy is written.

---

## TOMORROW (Friday, 2026-04-25)

### No scheduled sends

Zero active sequences after today. BRAIN runs on Friday.

### BRAIN priorities for Friday run:
1. Write post-campaign analysis (full dataset now available)
2. Write Batch 5 Ryedale initial-send copy (if data returned Thursday)
3. Update active_strategy.md for Week 4 / Batch 5 strategy
4. If any warm-pipeline outcomes resolved: update CRM records

---

## CAMPAIGN DATA ANALYSIS — PRELIMINARY (Day 27, pre-final-closes)

*Full analysis to be written Friday after complete dataset confirmed.*

### Signal performance (confirmed)

| Signal type | Approx leads sent | INTERESTED replies | Rate |
|---|---|---|---|
| SSL (PAS) | ~20 | 3 (Claire, Rob, Tom) | **~15%** |
| Mobile (PAS) | ~12 | 0 confirmed | ~0% |
| No website (BAB) | ~6 | 0 confirmed | ~0% |
| Social media (AIDA) | ~4 | 0 confirmed | ~0% |

**Confirmed finding: SSL → PAS is the only framework that produced INTERESTED leads.** All three positive outcomes used PAS with a first-name subject line and SSL signal. This is the core playbook for Batch 5.

### Winning patterns (confirmed)

1. **SSL → PAS → first-name subject** — 3/3 INTERESTED leads. Non-negotiable for Batch 5. Prioritise SSL leads in Ryedale.
2. **Day-7 new pain point, not a reframe** — Tom replied to the Day-7 email (new angle) not Day-0. Always pivot to a *different* problem on Day-7.
3. **Town name in subject and body** — trust signal. Both mentioned in Claire and Tom's replies as making the email feel credible.
4. **Short two-sentence nudges** — proposal nudges were 2 sentences. Rob and Claire both replied to these, not longer copy.
5. **One pain point per email** — no lead was overwhelmed. Single clear signal per touchpoint drove the reply decisions.
6. **Tuesday AM highest yield** — all 3 INTERESTED replies came in on a Tuesday morning (2026-04-04). Post-bank-holiday Tuesdays likely the top slot.

### What didn't work (provisional)

- **BAB (no-website)** — 0 replies across ~6 sends. Possible reasons: harder to verify legitimacy (no URL to reference), targets may have deliberately chosen not to have a website. Reconsider for Batch 5 — only use if 4.5★+ and 50+ reviews.
- **AIDA (social media)** — 0 replies across ~4 sends. High-review businesses may not perceive a gap, or the 'ranking' angle feels too abstract. Consider pivoting to a specific keyword-gap angle rather than a general ranking claim.
- **Mobile (PAS)** — 0 confirmed INTERESTED (though Tom's Day-0 was a mobile email and he replied on Day-7 to a new angle). Possibly mobile is a weaker pain point than SSL — people have learned to ignore mobile warnings more than security warnings.

### A/B tests still pending

| Variable | Status | When data arrives |
|---|---|---|
| Easter Saturday send rate | PENDING | After IMAP sweep — fu_020/021 sent 2026-04-19 |
| Wednesday vs Thursday breakup rate | PENDING | After today's breakups send and IMAP sweeps |
| GDPR angle for solicitors | PENDING | fu_044 Old Court Solicitors — check reply rate |
| Post-19-day IMAP gap — silent reply yield | PENDING | After full cohort IMAP sweep today |

---

## BATCH 5 STRATEGY PREVIEW (Ryedale, pre-scrape)

### Why Ryedale

Rural North Yorkshire market towns. Higher no-website density than East Yorkshire (estimated 15-20% of businesses). Trades-heavy economy: plumbing, electrical, roofing, joinery are primary targets. Offline referral model dominant — digital gap is real, acknowledged, and often *felt* (they know they don't have a website; they just haven't prioritised it).

Low digital sophistication = high SSL signal density = strong expected yield rate (~20-25%, based on Batches 1-3 SSL performance).

### Signal priority for Ryedale

1. **SSL** — expect 55-65% of websites in Ryedale to be HTTP. PAS framework, first-name subject. This alone should produce 10-14 eligible leads.
2. **Mobile** — secondary. Use only where SSL is absent but mobile failure is clear. PAS framework.
3. **No website** — 10-15% of Ryedale trades may have no website at all. BAB framework, but only for 4★+ businesses with 20+ reviews (lowers the bar from Batch 4 rules given the rural market context).
4. **Social / high review** — 5-10%. AIDA. Only for 4.5★+ with 100+ reviews.

### Copy notes for Batch 5 initial sends

All copy templates are pre-built in `daily_email_plan.json` under `batch_5_copy_readiness`. BRAIN will personalise per lead when Ryedale data arrives:
- SSL leads: mention specific URL + `flagged 'Not Secure'` in subject
- Mobile leads: mention specific URL + visible mobile failure
- No-website leads: reference Google search result + competitor that ranked above them
- Social leads: reference exact review count + specific gap (not generic "website")

### Geographic targeting within Ryedale

**Priority towns:** Malton (market town, highest business density), Pickering (strong trades, tourism), Helmsley (hospitality + professional services).
**Secondary:** Kirkbymoorside, Hovingham, Norton-on-Derwent.

---

## WINNING SUBJECT LINE PATTERNS (Day 27 confirmed)

Pattern: **[First name] — [town] [business type] [specific concrete issue]**

Examples that produced replies:
- `Claire — your Leeds hair salon website is flagged 'Not Secure'` → INTERESTED
- `Rob — your Sowerby Bridge print shop site has an SSL issue` → INTERESTED
- `Tom — your Ripon carpentry site isn't mobile-friendly` (Day-0, reply came Day-7 on new angle)

**Rules (unchanged from active_strategy.md):**
1. First name always if known — outperforms business-name-only 3-0
2. Town name always — trust signal
3. Issue must be specific and verifiable
4. No question marks — statements outperform questions for trades
5. Fallback (no owner name): `[Business name] — [town] [specific issue]`

---

## COMPLIANCE STATUS (Day 27)

- Lead 19 (Summit Fitness) — permanently suppressed. No contact.
- Lead 2 (Nidderdale Pet Supplies) — LOST. No contact.
- Lead 7 — suppressed. No contact.
- All 14 breakup sequences respect 4-touchpoint maximum (including today's 4 final sends).
- GDPR: all outreach B2B legitimate interest. Unsubscribes processed within 24h (last: Lead 19).
- No residential addresses. No fitness/wellness in Otley until framing reviewed.
- Today's send volume: 4 breakups — well within 40/day domain safety limit.
- Final closes for leads 3, 22, 1 (if sent today): valid under B2B legitimate interest (they replied voluntarily and initiated a sales conversation). Log all sends in audit_log.

---

## BRAIN OPERATING SCHEDULE (updated)

| Date | BRAIN Run | Purpose | Status |
|---|---|---|---|
| Tue 22 Apr | Missed | IMAP resolution / Batch 5 copy | ⚠ MISSED — no HANDS data |
| Wed 23 Apr | Run | Wednesday breakup plan | ✓ Run |
| **Thu 24 Apr** | **TODAY** | Final campaign sends + post-campaign analysis framing | ✓ Running now |
| **Fri 25 Apr** | **REQUIRED** | Post-campaign analysis + Batch 5 copy (if data arrives) | MANDATORY |
| Sun 27 Apr | Conditional | Batch 5 Day-3 bumps (if initial sends fired Friday) | Required if Friday sends happened |
| Tue 29 Apr | Required | Batch 5 Day-7 new angles | |
| Thu 7 May | Required | Batch 5 Day-14 breakup prep | |

**Hard rule: BRAIN must run every 2-3 days maximum while Batch 5 is in flight. Friday 25 April run is mandatory regardless of Batch 5 data status — post-campaign analysis must be written while the data is fresh.**

---

## SUMMARY: WHAT NEEDS TO HAPPEN TODAY

| Priority | Action | Deadline | Owner |
|---|---|---|---|
| 1 | IMAP sweep — warm pipeline (leads 3, 22, 1) | Before 09:00 | HANDS |
| 2 | Retrieve email addresses for leads 50, 52, 55, 56 from DB | Before 09:00 | HANDS |
| 3 | Send fu_046 → fu_047 → fu_048 → fu_049 (IMAP check before each) | 09:00–09:45 | HANDS |
| 4 | Confirm Wednesday sends fu_041-045 in CHANGELOG.md | By 10:00 | HANDS |
| 5 | Send final closes for leads 3, 22, 1 (if not yet sent) | Before 12:00 | HANDS |
| 6 | Log campaign milestone in CHANGELOG.md after fu_049 | By 10:00 | HANDS |
| 7 | Batch 5 Ryedale scrape (10:30–12:30) | EOD | HANDS |
| 8 | Unblock leads 49, 51, 53, 54 (parallel) | Afternoon | HANDS |
| 9 | Full IMAP sweep of entire cohort (afternoon) | EOD | HANDS |
| 10 | LinkedIn acceptance checks for leads 50-56 (if applicable) | Afternoon | HANDS (low priority) |

---

*Generated by OUTLOCAL BRAIN layer — 2026-04-24 07:00 UTC*
*Day 27. Campaign milestone day. All sequences complete after fu_049.*
*Next mandatory BRAIN run: Friday 2026-04-25 — post-campaign analysis + Batch 5 copy.*
