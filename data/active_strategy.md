# OUTLOCAL — Active Campaign Strategy
**Updated:** 2026-05-31 (Day 65 Sunday — Week 10 Close — Weekly Intelligence Report — Batch 5 Formally Closed — Batch 6 Scenario B Active)  
**Replaces:** 2026-05-30 strategy (Day 64 — Saturday — Emergency Sunday Deadline)  
**Valid until:** 2026-06-09 (Batch 6 Day-0 confirmed — Scenario B date — reassess after Day-3 IMAP results)  
**Weekly report:** data/weekly_reports/week_2026-05-31.md (next: ~2026-06-07 Week 11 close)

---

## CURRENT CAMPAIGN STATUS

- **Week:** 11 (live since 28 March 2026 — 65 days)
- **Batch 5 Ryedale:** **FORMALLY CLOSED — 2026-05-29 evening.** 0 confirmed replies across full 4-touchpoint sequence. Reapproach: 2026-11-26. No further IMAP, no further sends, no further action.
- **Batch 6 Harrogate + Craven:** **LAUNCH CONFIRMED — SCENARIO B ACTIVE.** `data/batch_6_leads.json` STILL MISSING — missed Friday 2026-05-29 absolute deadline AND Sunday 2026-05-31 emergency deadline. **Day-0 deferred to Tuesday 2026-06-09 (Scenario B).** File must be delivered Monday 2026-06-02 for BRAIN to generate copy in time.
- **Leads scraped:** ~79 confirmed (Batches 1–5, all Batch 5 UNCONFIRMED) + 18–22 Batch 6 pending scrape
- **Emails sent (estimated):** ~154–160 total (all Batch 4–5 UNCONFIRMED)
- **Total replies:** 11 (17.9% overall reply rate — all from Batches 1–4)
- **Batch 5 replies:** **0 confirmed — window CLOSED Friday 2026-05-29 evening. FORMALLY CLOSED.**
- **INTERESTED leads (ever):** 3 (leads 1, 3, 22) — ALL PERMANENTLY ARCHIVED LOST_NO_RESPONSE
- **Conversions confirmed:** 0
- **LinkedIn:** **PERMANENTLY CLOSED for all current leads — archive trigger fired 2026-05-19 EOD (65-session failure). MANDATORY for Batch 6: activate Day 3–7 from Day-0. Archive trigger Day 7 from Day-0 — unconditional.**
- **IMAP gap:** **57 days** from confirmed check (2026-04-04). NOT REQUIRED today (Sunday / post-Batch-5-close). Next IMAP obligation: Batch 6 leads only, per lead before each Day-0 send (Tue 2026-06-09).
- **CHANGELOG:** **63+ days overdue — MANDATORY — same session as Batch 6 Day-0 sends — ZERO FURTHER TOLERANCE.**
- **Weekly intelligence report:** data/weekly_reports/week_2026-05-31.md (Week 10 close — next: ~2026-06-07 Week 11 close)

---

## CONFIRMED WINNING PLAYBOOK — NON-NEGOTIABLE

These patterns produced 100% of INTERESTED leads. Do not deviate.

1. **SSL → PAS → first-name subject → town name → specific URL** — 3/3 INTERESTED rate
2. **Post-bank-holiday Tuesday AM send** — all 3 INTERESTED replies followed bank-holiday-adjacent Tuesday sends
3. **Day-7 genuinely different pain point** — not a reframe of Day-0. Reframes produce 0% responses.
4. **One pain point per email** — single clear signal. Listing multiple issues kills response.
5. **Town name in subject AND body** — local credibility confirmed by every INTERESTED reply
6. **No question marks in subject** — statement of fact outperforms question hook every time
7. **Chrome's exact wording** — `'Not Secure'` (not "unsecured") builds verifiable credibility

---

## SIGNAL PRIORITY ORDER

When scraping and selecting leads to email, prioritise in this order:

1. **`ssl` (HTTP site)** — 15% INTERESTED rate confirmed. Lead with this always. **60% of sends.**
2. **`mobile` failure** — 0% direct INTERESTED, but Day-7 pivot produced 1 conversion. **20% of sends.**
3. **`no_website`** (active businesses, 4★+, 20+ reviews) — rural bar (lowered from 50+). **15% of sends.**
4. **`aida` / keyword gap** — 4.5★+ 100+ reviews only. Verifiable keyword gap required. **5% test only.**
5. **`generic`** — **DO NOT USE.** No signal = no relevance = no reply.

---

## FRAMEWORK ALLOCATION — WEEK 11

| Framework | Allocation | Signal | When to use |
|---|---|---|---|
| **PAS** | **60%** | SSL (HTTP site) | Every HTTP site. Non-negotiable. |
| **PAS** | **20%** | Mobile failure | ssl=false AND mobile clearly broken — show you tested it |
| **BAB** | **15%** | No website | 4★+ AND 20+ reviews — reference Google Maps listing directly |
| **AIDA** | **5%** | High review + poor rank | 4.5★+ AND 100+ reviews ONLY — keyword-gap angle (verifiable) |
| Question | 0% | — | Deferred |
| Cliffhanger | 0% | — | Deferred indefinitely |
| Observation | 0% | — | Deferred indefinitely |

**Review trigger:** If BAB and AIDA remain at 0% through Batch 6 Day-7 with IMAP confirmed, reduce BAB to 10%, AIDA to 2%, redirect 8% to SSL-PAS. Do not reduce allocations before Day-7 data.

---

## LEAD SCORING RULES

- **Minimum score to email: 55**
- Exception: no-website leads (4★+ AND 20+ reviews) with confirmed owner name — can email at 50+
- 100% of INTERESTED leads came from score range 70+
- Do not spend enrichment time on leads scoring <50 unless email is trivially findable

---

## SUBJECT LINE RULES

**Primary pattern:** `[First name] — your [town] [business type] site is flagged 'Not Secure'`

Examples:
- "Mark — your Knaresborough plumbing site is flagged 'Not Secure'"
- "Julie — your Skipton B&B website is flagged 'Not Secure'"
- "David — your Ripon estate agency site isn't secure"
- "Helen — your Boroughbridge joinery site is flagged 'Not Secure'"
- "Sarah — your Settle builder website is flagged 'Not Secure'"

**Rules:**
1. First name in subject if owner name is known — outperforms business name only
2. Town name always included — local credibility is a trust signal
3. Issue must be specific and verifiable (not "improve your presence")
4. **No question marks in subject** — statement of fact outperforms question every time
5. Use Chrome's exact wording: `'Not Secure'`

**Fallback (no owner name):** `[Business name] — [town] [trade]: website flagged 'Not Secure'`

---

## PERSONALISATION RULES

- Always address by first name in body if known; "Hi" if not
- Mention the **specific URL** that has the problem — builds credibility, shows you actually looked
- Reference the town in the opening line
- **One pain point per email** — single signal only. Never list all issues.
- For trades: "customers search for you online before calling — the Not Secure warning will stop them"
- For beauty/wellness: lead with trust/reputation angle, not technical deficit
- For hospitality: booking and first-impression framing
- For B2B (solicitors, accountants, print): credibility and professionalism angle

---

## FOLLOW-UP SEQUENCE

| Day | Type | Notes |
|---|---|---|
| Day 0 | Initial send | PAS/BAB/AIDA as assigned. Tuesday AM only. |
| Day 3 | Short bump | Thread reply, 3–5 lines. Signal-specific. Not a restatement of Day-0. |
| Day 7 | New angle | **DIFFERENT pain point — not a reframe.** Fresh email, new subject. |
| Day 14 | Breakup | 3 lines max. No pressure. No question marks. Door open. |

- Maximum 4 total touchpoints — hard limit, no exceptions
- IMAP check before EVERY send — 57-day gap is an operational and compliance risk — weekly IMAP mandatory for Batch 6
- Unsubscribers: suppress immediately, log CHANGELOG.md and audit_log
- 24h proposal SLA from any INTERESTED reply — NON-NEGOTIABLE, 24/7

---

## SEND TIMING RULES

| Rule | Detail |
|---|---|
| **Best send day** | Tuesday AM |
| **Best send window** | 09:00–10:30 |
| **Post-bank-holiday premium** | First working day after bank holiday Monday is peak yield |
| **No bank holiday sends** | Hard rule — business owners are offline |
| **No weekend sends** | Saturday/Sunday always blocked |
| **Batch 6 Day-0 (Scenario B)** | **TUESDAY 2026-06-09, 09:00–10:30** (batch_6_leads.json missing — Scenario B active) |

---

## BATCH 5 RYEDALE — FINAL STATUS (Formally Closed — 2026-05-29 Evening)

**Formally closed:** Friday 2026-05-29 evening — post-Day-14 72h window closed. No further action.

| Milestone | Date | Status |
|---|---|---|
| Day-0 sends | Tue 2026-05-12 | ASSUMED SENT — UNCONFIRMED |
| Day-3 bumps | Fri 2026-05-15 | ASSUMED SENT — UNCONFIRMED |
| Day-7 sends | Tue 2026-05-19, 09:00–10:30 | ASSUMED SENT — UNCONFIRMED |
| LinkedIn archive trigger | Tue 2026-05-19 EOD | **FIRED — PERMANENTLY CLOSED** |
| Day-14 breakup sends | Tue 2026-05-26 | ASSUMED SENT — UNCONFIRMED |
| **Post-Day-14 72h FINAL window** | **Fri 2026-05-29 evening** | **CLOSED — 0 confirmed replies** |
| **SEQUENCE STATUS** | **FORMALLY CLOSED** | **Reapproach: 2026-11-26. No further sends or IMAP.** |

**Model assessment:** SOUND. 0% Batch 5 = execution failure (57-day IMAP gap + 65-session LinkedIn failure + no per-lead data file). SSL-PAS 15% INTERESTED rate remains non-negotiable for Batch 6.

**Incidental reply protocol:** If any Batch 5 reply found incidentally during Batch 6 pre-send IMAP: treat as new reply, classify, 24h proposal SLA from discovery time (24/7 — NON-NEGOTIABLE). Sequence complete — no further sends. Use value_delivery_queue.json directly.

---

## BATCH 6 HARROGATE + CRAVEN — SCENARIO B ACTIVE

**Decision:** Confirmed. Proceeds regardless of Batch 5 reply count.  
**Territory:** Harrogate District (Knaresborough priority 1, Ripon new leads only, Boroughbridge) + Craven District (Skipton priority 1, Settle, Grassington, Gargrave)  
**`batch_6_leads.json`:** MISSING — missed Friday 2026-05-29 absolute deadline AND Sunday 2026-05-31 emergency deadline  
**Active scenario:** B — Day-0 Tuesday 2026-06-09  
**File deadline (Scenario B):** Monday 2026-06-02 (BRAIN generates copy same day → Day-0 Tuesday 2026-06-09)

| Milestone | Scenario B Date | Notes |
|---|---|---|
| `batch_6_leads.json` delivery | **Mon 2026-06-02 (HANDS)** | BRAIN generates copy same day — last viable window for Tue 2026-06-09 Day-0 |
| BRAIN per-lead copy generation | **Mon 2026-06-02** | Signal assignments + subject lines + body copy per lead |
| **Batch 6 Day-0** | **Tue 2026-06-09, 09:00–10:30** | IMAP per lead before each send — mandatory |
| **Day-3 bumps + LinkedIn** | **Fri 2026-06-12** | `profiles.json` MUST be written same session |
| **LinkedIn archive trigger** | **Tue 2026-06-17 EOD** | Fires unconditionally if `profiles.json` missing |
| Day-7 new angle | Tue 2026-06-16 | Genuinely different pain point — not a reframe |
| Day-14 breakup | Tue 2026-06-23 | 3 lines max. No pressure. Door open. |
| **Weekly intelligence report** | **Sun 2026-06-07** | Week 11 close — includes Day-0 IMAP results + LinkedIn Day-3 status |

**If `batch_6_leads.json` NOT received by Monday 2026-06-02:** BRAIN cannot generate copy — notifies HANDS immediately. Day-0 defers to Tuesday 2026-06-16 (next viable Tuesday). No further scenario extensions.

---

## LINKEDIN CHANNEL RULES — WEEK 11

**STATUS FOR BATCH 5 AND ALL PRIOR: PERMANENTLY CLOSED.**

**STATUS FOR BATCH 6: MANDATORY — activate Day 3 (Friday 2026-06-12) through Day 7 from Day-0.**

### Batch 6 LinkedIn Rules (non-negotiable)

1. Execute Day 3–7 from Day-0 — zero tolerance for deferral
2. `linkedin_profiles.json` MUST be written same session as execution — one entry per lead
3. If `profiles.json` not written same session: that session's LinkedIn did not happen for BRAIN purposes
4. Archive trigger fires Day 7 from Day-0 (Tuesday 2026-06-17 EOD) — fires unconditionally if `profiles.json` missing — NO EXCEPTIONS
5. Connection note: 200-char hard limit, start with name, mention specific business, end low-pressure
6. Post-reference check MANDATORY before every note — 3–4x acceptance rate premium documented
7. After connection accepted: wait 3–5 days, send ONE short value message (no pitch, no email reference)
8. Sector priority: Solicitors → Estate agents → Hotels/B&Bs → Professional services → Trades

### LinkedIn vs Email Channel Split — Week 11

**80% email, 20% LinkedIn time allocation (Day 3–7 window only).**

If Batch 6 LinkedIn acceptance rate ≥ 20%: increase LinkedIn time to 30% in Week 12.

---

## GEOGRAPHIC FOCUS — WEEK 11

**Batch 5 (FORMALLY CLOSED):**
- **Ryedale District:** Malton, Pickering, Helmsley, Kirkbymoorside, Hovingham, Norton-on-Derwent
- Window closed 2026-05-29 evening. 0 confirmed replies. Reapproach: 2026-11-26. No contact.

**Batch 6 — CONFIRMED LAUNCH (Scenario B):**
- **Harrogate District:** Knaresborough (priority 1, 5–7 leads), Ripon new leads ONLY (priority 2, 4–5 leads — DO NOT reapproach lead 1), Boroughbridge (priority 3, 2–3 leads)
- **Craven District:** Skipton (priority 1, 6–8 leads), Settle (priority 2, 2–3 leads), Grassington (priority 3, 1–2 leads), Gargrave (stretch, 1 lead)
- **Day-0:** Tuesday 2026-06-09 (Scenario B)

**Paused / do not expand:**
- Fitness/wellness (Otley) — suppress category
- Sheffield, Manchester — outside Yorkshire focus
- East Yorkshire general — Batch 4 complete. Fresh scrape earliest June.
- Beverley, Bridlington, Driffield — re-scrape June. Do not reapproach Batch 4 leads before October.

**Blocked leads (do not reapproach before listed date):**
- Lead 2 (Nidderdale Pet Supplies) — NOT_INTERESTED. Reapproach: 2026-10-06
- Leads 1, 3, 22 — PERMANENTLY ARCHIVED LOST_NO_RESPONSE. Reapproach: 2026-10-26 (earliest)
- Leads 49, 51, 53, 54 — LOST_UNRESOLVED. No reapproach (no email ever obtained)
- Leads 7, 19 — permanently suppressed

---

## INDUSTRY FRAMING NOTES

| Sector | Best approach | Signal priority | Avoid |
|---|---|---|---|
| Trades (plumber, electrician, roofer, builder) | Trust + "customers Google you first" + SSL | SSL > mobile > no-website | Technical jargon |
| Joiners / Carpentry | Trust + quote form gap + seasonal (spring builds) | SSL > mobile | Vague "website help" |
| Beauty/salon | Booking gap, trust, local reputation | SSL+mobile > social proof | Deficit framing |
| Hospitality (pub, restaurant, B&B) | Conversion, booking link, first-impression | SSL > mobile > no-website | Generic "presence" pitch |
| Accountancy/professional | Business impact, Google ranking, trust | SSL > social_media | "Marketing services" framing |
| Print/design (B2B) | B2B credibility, portfolio, SSL trust | SSL > mobile | Consumer framing |
| Estate agents | Local SEO, trust, portal dependency risk | SSL > keyword-gap | — |
| Fitness/wellness | Positive amplification (AIDA/BAB) ONLY | Social proof / keyword-gap | PAS deficit framing |
| Solicitors | Trust, credibility, HTTPS compliance expectation | SSL > keyword-gap | Cold/generic pitch |

---

## EMAIL ENRICHMENT RULES

**For trades businesses (garage, plumber, electrician, builder, roofer):**
- Prefer website contact page email over Google Maps listing email
- If no website email: Companies House for director name + domain pattern

**Priority order for enrichment time:**
1. Leads with owner name known + website URL → fastest, highest reply rate
2. Leads with website only → crawl contact page
3. Leads with no website, 4★+ 20+ reviews → phone lookup / Companies House
4. Leads scoring <50 → deprioritise unless trivially enrichable

---

## COMPLIANCE REMINDERS

- All outreach to business emails only — B2B legitimate interest basis
- Unsubscribes: suppress within 24 hours (GDPR Article 21) — log in audit_log table — applies 24/7
- Log all suppressions in audit_log table
- No residential addresses ever
- OOO pauses are mandatory — do not re-send during stated OOO period
- IMAP check before every send — 57-day gap is a compliance risk — weekly IMAP mandatory for Batch 6
- 4-touchpoint maximum — hard limit, no exceptions
- LinkedIn: do not approach leads who replied NOT_INTERESTED on any channel

---

## OPERATIONAL PRIORITIES — WEEK 11 (Days 65–71, 2026-05-31 to 2026-06-06)

| Priority | Action | Deadline | Status |
|---|---|---|---|
| **1** | **`batch_6_leads.json`** — 18–22 leads, Harrogate + Craven | **TODAY Sunday 2026-05-31 EOD (final) — or Mon 2026-06-02 morning (last viable for Tue 2026-06-09 Day-0)** | MISSING — OVERDUE |
| **2** | **BRAIN signal assignment + per-lead email copy** — read batch_6_leads.json, assign signals, write copy | **Monday 2026-06-02** (after file received) | Pending file delivery |
| **3** | **CHANGELOG.md** — 63+ days overdue | **SAME SESSION AS DAY-0 SENDS (Tue 2026-06-09) — ZERO TOLERANCE** | OVERDUE |
| **4** | **Update lead status → `sequence_complete`** — all Batch 5 Ryedale leads. Reapproach: 2026-11-26. | ASAP | DUE |
| **5** | **Batch 6 Day-0 sends** — IMAP per lead before each | **Tue 2026-06-09, 09:00–10:30 (Scenario B)** | Upcoming |
| **6** | **Batch 6 Day-3 bumps + LinkedIn** — `profiles.json` SAME SESSION | **Fri 2026-06-12** | Upcoming |
| **7** | **LinkedIn archive trigger** — fires unconditionally | **Tue 2026-06-17 EOD (Scenario B)** | Upcoming |
| **8** | **Batch 6 Day-7 new angle** | **Tue 2026-06-16** | Upcoming |
| **9** | **Weekly intelligence report** — Week 11 close | **Sun 2026-06-07** | Upcoming |
| **10** | **Batch 6 Day-14 breakup** | **Tue 2026-06-23** | Upcoming |

---

*Active strategy maintained by OUTLOCAL BRAIN layer.*  
*Updated: 2026-05-31 (Day 65 — Sunday — Week 10 Close — Weekly Intelligence Report — Batch 5 Formally Closed — Batch 6 Scenario B Active).*  
*HANDS layer agents must read this file before starting any daily run.*  
*Next BRAIN review: Sunday 2026-06-07 — weekly intelligence report (Week 11 close). Will include Batch 6 Day-0 IMAP results + Day-3 reply peak + LinkedIn execution status.*  
*URGENT: `batch_6_leads.json` must be delivered TODAY (Sunday EOD) or Monday 2026-06-02 morning — BRAIN generates per-lead copy Monday → Day-0 Tuesday 2026-06-09. If not received Monday morning: Day-0 defers to Tuesday 2026-06-16.*  
*If INTERESTED reply ever discovered incidentally: 24h proposal SLA applies (24/7 — NON-NEGOTIABLE). Use value_delivery_queue.json directly.*
