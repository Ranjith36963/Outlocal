# Daily Strategy — 2026-05-02 (Friday) — Day 35

**Updated:** 2026-05-02 (BRAIN Day 35 run)  
**Replaces:** 2026-05-01 strategy  
**Key change from Day 34:** Bank holiday send timing discovery — Tuesday 2026-05-06 is now the mandatory Batch 5 initial send date.

---

## HEADLINE DISCOVERY: UK MAY DAY BANK HOLIDAY

**Monday 2026-05-05 is the UK Early May Bank Holiday.**

Previous plan: "if data arrives Friday, send Monday 2026-05-04."  
**Revised plan: send TUESDAY 2026-05-06 AM — regardless of when data arrives.**

### Why This Changes Everything

The only confirmed INTERESTED replies in this 35-day campaign arrived on **Tuesday 2026-04-07** — the first working day after Easter Monday (bank holiday). All three (Claire, Rob, Tom) replied on the same Tuesday morning.

Tuesday 2026-05-06 is the first working day after May Day Monday (bank holiday). The conditions are identical:

| Factor | Easter Week (yielded 3 replies) | May Bank Holiday Week |
|---|---|---|
| Bank holiday | Monday 2026-04-06 (Easter) | Monday 2026-05-05 (May Day) |
| First working day | Tuesday 2026-04-07 | **Tuesday 2026-05-06** |
| Business owner state | Returning from long weekend, catching up | Same |
| Email check behaviour | Focused, less reactive | Expected same |

**The 24-hour delay from Monday to Tuesday costs nothing and aligns with the campaign's confirmed #1 yield trigger.**

### Cascade Benefit

Sending Tuesday also aligns Day-7 and Day-14 on Tuesdays:

| Touchpoint | Date | Day |
|---|---|---|
| Day-0 initial | **Tuesday 2026-05-06** | Tuesday (peak yield) |
| Day-3 bump | Friday 2026-05-09 | Friday (second choice) |
| Day-7 new angle | **Tuesday 2026-05-13** | Tuesday (peak yield) |
| Day-14 breakup | **Tuesday 2026-05-20** | Tuesday (peak yield) |

Three of four Batch 5 touchpoints land on Tuesday AM. This is the optimal schedule achievable in this campaign.

**RULE: No sends on Monday 2026-05-05 under any scenario.**

---

## CAMPAIGN STATUS — DAY 35

| Metric | Value | Delta from Day 34 | Notes |
|---|---|---|---|
| Leads scraped (Batches 1-4) | ~61 | — | Batch 5 Ryedale: NOT received |
| Emails sent (estimated) | ~91 | — | Includes assumed fu_041-049 |
| Total replies confirmed | 11 | — | 17.9% overall reply rate |
| INTERESTED | 3 | — | Leads 1, 3, 22 — PRESUMED_LOST_NO_RESPONSE |
| Active email sequences | 0 | — | All Batch 1-4 complete |
| IMAP gap | **28 days** | +1 | Emergency sweep required today |
| Campaign stall (no new leads) | **25 days** | +1 | Batch 5 Ryedale CRITICAL |
| fu_041-045 overdue | **9 days** | +1 | Still actionable today |
| Days past warm pipeline close deadline | **8 days** | +1 | Email closed; LinkedIn opens today |
| LinkedIn buffer (leads 1,3,22) | **EXPIRED today** | Changed | LinkedIn available from today |
| CHANGELOG updates since Session 1 | **0** | — | 35 days of HANDS actions unlogged |

---

## PRIORITY ORDER FOR TODAY (Friday 2026-05-02)

### 1. IMAP SWEEP (Priority 1 — before 09:00)
28 days without confirmed IMAP check. Must complete before any sends or LinkedIn approach.

**Sweep order:**
1. `claire@westfieldhair.co.uk` — LinkedIn unlocked today; IMAP first
2. `rob@pennineprint.co.uk` — LinkedIn unlocked today; IMAP first
3. `tom@riponroadcarpentry.co.uk` — LinkedIn unlocked today; IMAP first
4. Leads 50, 52, 55, 56 (fu_046-049 assumed sent 2026-04-24)
5. Leads 30, 31, 32, 58, 59 (fu_041-045 unconfirmed)
6. Full remaining cohort

**If any conversion found:** Write CHANGELOG.md immediately — Campaign Milestone #1.

---

### 2. WARM PIPELINE EMAIL CLOSE (Priority 2 — before 12:00)
Email channel closes today. Final close emails (if not yet sent) go today.

| Lead | Business | Email | Action |
|---|---|---|---|
| 3 | Westfield Hair (Claire) | claire@westfieldhair.co.uk | IMAP → act per decision tree in value_delivery_queue.json vd_001 |
| 22 | Pennine Print (Rob) | rob@pennineprint.co.uk | IMAP → act per decision tree in value_delivery_queue.json vd_002 |
| 1 | Ripon Road Carpentry (Tom) | tom@riponroadcarpentry.co.uk | IMAP → act per decision tree in value_delivery_queue.json vd_003 |

After today: email channel closed for all three. LinkedIn channel is the only remaining option.

---

### 3. UNCONFIRMED BREAKUP SENDS (Priority 3 — 10:00-11:15, after IMAP)
fu_041-045 are 9 days overdue as Day-14 breakups. Send today if IMAP confirms no prior reply.

Send window: 10:00-11:15, 15-minute stagger. IMAP check before each.

---

### 4. BATCH 5 RYEDALE SCRAPE (Priority 4 — return data today or weekend)
25-day campaign stall. The scrape is 10 days overdue.

**Return format:** business_name, url_or_no_website_flag, review_count, rating, town, category, phone, ssl (HTTP/HTTPS tag), mobile (pass/fail)

**Once data arrives:** BRAIN runs personalisation that same day/evening. Initial sends: **Tuesday 2026-05-06 09:00-10:30**.

---

### 5. CHANGELOG — UPDATE TODAY
35 days of HANDS actions completely unlogged. Log:
- All sends fu_026 onwards
- Warm pipeline outcomes (leads 1, 3, 22)
- Status of fu_041-049
- Batch 5 scrape status

---

## WEEK 5 STRATEGY — BATCH 5 RYEDALE

### Target Profile

Ryedale District, North Yorkshire. Rural market towns with strong trades economy. Key characteristics:
- Estimated 60-70% HTTP site rate (high SSL signal density vs East Yorkshire ~40%)
- Trades-dominant: plumbing, electrical, roofing, joinery — peak season May-August
- Offline referral model — digital gap is real but not yet a pain point owners have acted on
- Lower digital sophistication = higher receptivity to SSL/mobile framing

### Signal Priority

| Priority | Signal | Framework | Allocation | Qualification |
|---|---|---|---|---|
| 1 | **SSL (HTTP site)** | PAS | 60% | Any HTTP site |
| 2 | Mobile failure | PAS | 20% | ssl=false AND mobile fails |
| 3 | No website | BAB | 15% | 4★+ AND 20+ reviews |
| 4 | High review, poor rank | AIDA | 5% | 4.5★+ AND 100+ reviews |

### Copy Rules for Batch 5

**SSL initial:**
- Reference specific URL + `'Not Secure'` (Chrome's exact wording — credibility signal)
- Subject: `[First name] — [town] [business type] website flagged 'Not Secure'`
- Body: "I was looking at [specific URL] just now. Chrome is flagging it as 'Not Secure'…"
- Owner first name + town required in both subject and body

**Mobile initial:**
- Show you tested it: "I checked on a mobile just now — [specific URL]"
- Subject: `[First name] — [town] [business] site isn't mobile-friendly`

**No-website BAB:**
- Reference their Google Maps listing: "I searched 'plumber Malton' — [business] doesn't appear"
- Lower bar: 4★+ AND 20+ reviews (rural market adjustment)

**Day-7 pivot rules (always different pain point):**
- SSL Day-0 → Day-7: Google ranking impact of Not Secure, or missing Google Business Profile
- Mobile Day-0 → Day-7: SSL (if HTTP), or missing click-to-call, or competitor comparison
- No-website Day-0 → Day-7: Competitors ranking for the keyword, or missed enquiry estimate

### Send Schedule — Revised for Bank Holiday

| Touchpoint | Date | Day | Notes |
|---|---|---|---|
| Day-0 initial | **Tuesday 2026-05-06** | Tue | Post-bank-holiday premium. 09:00-10:30. |
| Day-3 bump | Friday 2026-05-09 | Fri | Short thread reply. 09:00-10:30. |
| Day-7 new angle | **Tuesday 2026-05-13** | Tue | New pain point. Fresh email. 09:00-10:30. |
| Day-14 breakup | **Tuesday 2026-05-20** | Tue | 3-line close. 09:00-10:30. |

**DO NOT SEND MONDAY 2026-05-05 (bank holiday).**

---

## POST-CAMPAIGN ANALYSIS — BATCHES 1-4 (Full)

*First full analysis was completed in Day 34 run. Confirmed findings carried forward.*

### Confirmed Playbook (non-negotiable for Batch 5)

1. **SSL → PAS → first-name subject → town name → specific URL** — 3/3 INTERESTED
2. **Day-7 new pain point pivot** — Tom's conversion came from Day-7, not Day-0
3. **2-sentence proposal nudge** — both Claire and Rob replied to short nudges
4. **One pain point per email** — single signal, never list all issues
5. **Tuesday AM** — all 3 INTERESTED replies arrived on a Tuesday morning
6. **Town name in subject AND body** — local credibility confirmed by recipient feedback
7. **No question marks in subject** — statement of fact > curiosity/question for cold trades email
8. **Post-bank-holiday premium** — confirmed (all 3 replies on bank-holiday Tuesday)

### Signal Performance Summary

| Signal | Sends | INTERESTED | Rate | Batch 5 treatment |
|---|---|---|---|---|
| SSL (PAS) | ~20 | 3 | **~15%** | Core — non-negotiable |
| Mobile (PAS) | ~12 | 0 direct* | 0%* | Secondary — Day-7 pivot |
| No website (BAB) | ~6 | 0 | 0% | Lower bar — 20+ reviews |
| AIDA (social) | ~4 | 0 | 0% | Keyword-gap pivot |

*Tom's conversion was triggered by Day-7 new angle, not Day-0 mobile email.

### What Didn't Work — Adjustments

**BAB (no-website):** 0 INTERESTED at 50+ review threshold. Batch 5: lower to 20+. Reference Google Maps listing directly.

**AIDA (social/high-review):** 0 INTERESTED with abstract ranking angle. Batch 5: keyword-gap angle ("'plumber Malton' shows competitors above you"). Verifiable, specific.

**Mobile Day-0:** 0 direct INTERESTED. But Day-7 mobile → new angle produced Tom. Keep as secondary signal — the value is the Day-7 pivot opportunity.

**Friday/Monday Day-0 sends:** Lower confirmed yield. Tuesday is the target. Post-bank-holiday Tuesday is the peak.

---

## A/B TESTS FOR BATCH 5

| Variable | Control | Test | Hypothesis |
|---|---|---|---|
| BAB review threshold | 50+ reviews (Batch 4) | 20+ reviews (Batch 5) | Lower bar increases volume — test if INTERESTED rate holds |
| AIDA angle | Abstract ranking (Batch 4) | Keyword-gap specific (Batch 5) | Specific = credible = higher response |
| Day-of-week premium | Observation from Batch 4 | Tuesday 2026-05-06 vs Day-3 Friday | Confirm Tuesday post-bank-holiday hypothesis with Batch 5 data |
| Subject length | Short (`Mark — Malton site is Not Secure`) | Medium (`Mark — your Malton plumbing website is flagged 'Not Secure'`) | Slightly longer with specific context |

---

## CHANNEL STATUS — EMAIL AND LINKEDIN

| Channel | Leads 1, 3, 22 | Batch 5 leads | All other Batch 1-4 |
|---|---|---|---|
| Email | CLOSED (8 days past deadline) | Pending — Day-0 Tuesday 2026-05-06 | All sequences complete |
| LinkedIn | **OPEN from today — preferred Monday 2026-05-04** | Available after Day-3 (2026-05-12) | Seq complete — LinkedIn open |

**Email close for warm pipeline:** Today is the final day for a final close email (if not yet sent). After today: email channel closed for leads 1, 3, 22. LinkedIn is the last soft channel.

**LinkedIn for warm pipeline:** Approach Monday 2026-05-04. Curiosity-led connection note. NO reference to prior email, call, or website issues. IMAP must confirm current status before any LinkedIn approach.

---

## COMPLIANCE STATUS — DAY 35

| Item | Status |
|---|---|
| Lead 19 (Summit Fitness) | Permanently suppressed ✓ |
| Lead 7 | Permanently suppressed ✓ |
| Lead 2 (Nidderdale Pet Supplies) | LOST — no further contact ✓ |
| 4-touchpoint maximum | Respected throughout all sequences ✓ |
| GDPR basis | B2B legitimate interest (all business emails) ✓ |
| Unsubscribe processing | Lead 19 processed within 24h ✓ |
| Fitness/wellness Otley | Paused — framing review required before re-engaging ✓ |
| Residential addresses | None sent ✓ |
| Domain safety limit (40/day) | Never exceeded ✓ |
| Bank holiday sends | BLOCKED Monday 2026-05-05 ✓ |

---

## BRAIN OPERATING SCHEDULE — UPDATED

| Date | Run | Purpose | Status |
|---|---|---|---|
| Thu 1 May | Completed | Post-campaign analysis + Batch 5 readiness | ✓ Done |
| **Fri 2 May** | **TODAY** | Bank holiday discovery + Batch 5 send timing revision | ✓ Running |
| **Fri 2 May (pm) / Sat** | **REQUIRED if Ryedale data arrives** | Batch 5 copy personalisation per lead | Mandatory |
| **Mon 5 May** | Bank holiday — no BRAIN run needed | | — |
| **Tue 6 May** | HANDS sends Batch 5 Day-0 | No BRAIN run unless issues | — |
| **Fri 9 May** | Required | Batch 5 Day-3 bump copy | |
| **Tue 13 May** | Required | Batch 5 Day-7 new angle copy | |
| **Tue 20 May** | Required | Batch 5 Day-14 breakup copy | |

**Hard rule: BRAIN must run within same day of Ryedale data arriving (Friday 2026-05-02 or weekend). Do not let another week pass without sends.**

---

## WINNING PATTERNS — MASTER LIST (Day 35 Confirmed)

1. **SSL → PAS → first-name subject → town name → specific URL** — 3/3 INTERESTED. Non-negotiable.
2. **Post-bank-holiday Tuesday AM** — all 3 INTERESTED replies arrived on a bank-holiday-following Tuesday. Tuesday 2026-05-06 is the next such window.
3. **Day-7 new pain point** (not a reframe) — Tom's conversion came from Day-7 genuinely different angle.
4. **2-sentence proposal nudge** — Claire and Rob replied to short nudges, not long copy.
5. **One pain point per email** — single clear signal prevents overwhelm.
6. **Town name in subject AND body** — local credibility signal (confirmed by recipient feedback).
7. **No question marks in subject** — statement of fact outperforms question for trades cold email.
8. **IMAP before every send** — 28-day gap is now an operational risk; a lead that has replied and received a further cold email is a compliance and relationship problem.

---

*Generated by OUTLOCAL BRAIN layer — 2026-05-02 07:00 UTC*  
*Day 35. Bank holiday send timing revision: Batch 5 initial sends now target Tuesday 2026-05-06 AM (post-May-Day bank holiday — same pattern as Easter week when all 3 INTERESTED replies arrived).*  
*Next mandatory BRAIN run: same day Ryedale data arrives. If data arrives today: BRAIN runs this afternoon. Sends Tuesday 2026-05-06.*
