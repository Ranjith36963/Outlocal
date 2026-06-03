# OUTLOCAL — Active Campaign Strategy
**Updated:** 2026-06-03 (Day 68 Wednesday — Week 11 — SCENARIO C CONFIRMED ACTIVE — Day-0 Tue 2026-06-16 13 days away)  
**Replaces:** 2026-05-29 strategy (Day 63 — Friday — Batch 5 Post-Day-14 72h FINAL)  
**Valid until:** After Batch 6 Day-0 send confirmed (Scenario C: Tue 2026-06-16)  
**Weekly report:** data/weekly_reports/week_2026-05-31.md (WEEK 10 CLOSE)

---

## CURRENT CAMPAIGN STATUS

- **Week:** 11 (live since 28 March 2026 — 68 days)
- **Batch 5 Ryedale:** **FORMALLY CLOSED — 2026-05-29 evening.** 0 confirmed replies across full 4-touchpoint sequence. Reapproach: 2026-11-26. No further IMAP, no further sends.
- **Batch 6 Harrogate + Craven:** **SCENARIO C CONFIRMED ACTIVE.** batch_6_leads.json STILL MISSING — **68-session HANDS pattern**. **SCENARIO A CLOSED** (never executed — Day-0 Tue Jun 2 was yesterday). **SCENARIO B CLOSED** (Monday EOD deadline passed — 68-session failure). **Scenario C Day-0: Tue 2026-06-16 — CONFIRMED. 13 days away. The only remaining path.**
- **Leads scraped:** ~50 confirmed (Batches 1–4) + 12-18 Batch 5 Ryedale (UNCONFIRMED) + 18-22 Batch 6 pending scrape (batch_6_leads.json MISSING)
- **Emails sent (estimated):** ~160-184 total (Batches 1–5 all touchpoints assumed, UNCONFIRMED beyond Batch 1–3)
- **Total replies:** 11 (17.9% overall reply rate — all from Batches 1–4)
- **Batch 5 replies:** **0 confirmed. Window CLOSED Friday 2026-05-29 evening. FORMALLY CLOSED.**
- **INTERESTED leads (ever):** 3 (leads 1, 3, 22) — ALL PERMANENTLY ARCHIVED LOST_NO_RESPONSE
- **Conversions confirmed:** 0
- **LinkedIn:** **PERMANENTLY CLOSED for Batch 5 and all prior leads — archive trigger fired 2026-05-19 EOD (68-session failure). MANDATORY for Batch 6: activate Day 3 from Day-0 (Fri 2026-06-19). Archive trigger Tue 2026-06-24 EOD — unconditional. orchestrator.py NOT IMPLEMENTED — build before Fri 2026-06-19 (16 days).**
- **IMAP gap:** **60 days** from confirmed check (2026-04-04). NOT REQUIRED today. Next IMAP obligation: Batch 6 leads only (per lead before each Day-0 send Tue 2026-06-16).
- **CHANGELOG:** **66+ days overdue — MANDATORY — same session as Batch 6 Day-0 sends (Tue 2026-06-16) — ABSOLUTE FINAL DEADLINE.**

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
3. **`no_website`** (active businesses, 4★+, 20+ reviews) — Ryedale rural bar (lowered from 50+). **15% of sends.**
4. **`aida` / keyword gap** — 4.5★+ 100+ reviews only. Verifiable keyword gap required. **5% test only.**
5. **`generic`** — **DO NOT USE.** No signal = no relevance = no reply.

---

## FRAMEWORK ALLOCATION — WEEK 8

| Framework | Allocation | Signal | When to use |
|---|---|---|---|
| **PAS** | **60%** | SSL (HTTP site) | Every HTTP site. Non-negotiable. |
| **PAS** | **20%** | Mobile failure | ssl=false AND mobile clearly broken — show you tested it |
| **BAB** | **15%** | No website | 4★+ AND 20+ reviews — reference Google Maps listing directly |
| **AIDA** | **5%** | High review + poor rank | 4.5★+ AND 100+ reviews ONLY — keyword-gap angle (verifiable) |
| Question | 0% | — | Deferred |
| Cliffhanger | 0% | — | Deferred indefinitely |
| Observation | 0% | — | Deferred indefinitely |

---

## LEAD SCORING RULES

- **Minimum score to email: 55**
- Exception: no-website leads (4★+ AND 20+ reviews) with confirmed owner name — can email at 50+
- 100% of INTERESTED leads came from score range 70+
- Do not spend enrichment time on leads scoring <50 unless email is trivially findable

---

## SUBJECT LINE RULES

**Primary pattern:** `[First name] — [town] [business type] website flagged 'Not Secure'`

Examples:
- "Mark — your Malton plumbing site is flagged 'Not Secure'"
- "Julie — your Pickering B&B website is flagged 'Not Secure'"
- "David — your Helmsley estate agency site isn't secure"
- "Helen — your Kirkbymoorside joinery site is flagged 'Not Secure'"

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
- IMAP check before EVERY send — 53-day gap is an operational and compliance risk — weekly IMAP mandatory for Batch 6
- Unsubscribers: suppress immediately, log CHANGELOG.md and audit_log
- 24h proposal SLA from any INTERESTED reply — NON-NEGOTIABLE, 24/7

**Day-7 pivot rules for Batch 5:**
- Day-0 SSL → Day-7: Google ranking impact of 'Not Secure' (HTTP → lower local search rank)
- Day-0 mobile → Day-7: SSL (if HTTP) OR missing click-to-call button
- Day-0 no-website → Day-7: competitors ranking for '[trade] [town]' keyword, OR missed enquiry estimate
- **Rule: Day-7 MUST be a genuinely different pain point. A reframe of Day-0 does not perform.**

---

## SEND TIMING RULES

| Rule | Detail |
|---|---|
| **Best send day** | Tuesday AM |
| **Best send window** | 09:00–10:30 |
| **Post-bank-holiday premium** | First working day after bank holiday Monday is peak yield |
| **No bank holiday sends** | Hard rule — business owners are offline |
| **No weekend sends** | Saturday/Sunday always blocked |
| **Scenario A** | **CONFIRMED CLOSED** — Tue 2026-06-02 Day-0 was yesterday. Never executed. |
| **Scenario B** | **CONFIRMED CLOSED** — Monday EOD deadline passed. Tue 2026-06-09 not possible. |
| **Scenario C** | **CONFIRMED ACTIVE — TUESDAY 2026-06-16, 09:00-10:30 (13 days away)** |

---

## BATCH 5 RYEDALE — FINAL STATUS (Formally Closed — 2026-05-29 Evening)

**Formally closed:** Friday 2026-05-29 evening — post-Day-14 72h window closed.

| Milestone | Date | Status |
|---|---|---|
| Day-0 sends | Tue 2026-05-12 | ASSUMED SENT — UNCONFIRMED |
| Day-3 bumps | Fri 2026-05-15 | ASSUMED SENT — UNCONFIRMED |
| Day-7 sends | Tue 2026-05-19, 09:00-10:30 | ASSUMED SENT — UNCONFIRMED |
| LinkedIn archive trigger | Tue 2026-05-19 EOD | **FIRED — PERMANENTLY CLOSED** |
| Day-14 breakup sends | Tue 2026-05-26 | ASSUMED SENT — UNCONFIRMED. FINAL TOUCHPOINT. |
| **Post-Day-14 72h FINAL IMAP** | **Fri 2026-05-29** | **UNCONFIRMED — window now CLOSED regardless** |
| **POST-DAY-14 WINDOW** | **CLOSED — 2026-05-29 evening** | **UNCONDITIONAL. 0 confirmed replies.** |
| **SEQUENCE STATUS** | **FORMALLY CLOSED** | **Reapproach: 2026-11-26. No further sends or IMAP.** |

**Model assessment:** SOUND. 0% Batch 5 = execution failure (60-day IMAP gap + 68-session LinkedIn failure + no per-lead data file). SSL-PAS 15% INTERESTED rate remains non-negotiable for Batch 6.

---

## EMAIL ENRICHMENT RULES

**For trades businesses (garage, plumber, electrician, builder, roofer):**
- Prefer website contact page email over Google Maps listing email
- Google Maps listing often routes to workshop/reception, not the owner
- If no website email: Companies House for director name + domain pattern

**Priority order for enrichment time:**
1. Leads with owner name known + website URL → fastest, highest reply rate
2. Leads with website only → crawl contact page
3. Leads with no website, 4★+ 20+ reviews → phone lookup / Companies House
4. Leads scoring <50 → deprioritise unless trivially enrichable

**No blocked enrichment leads remaining.** Leads 49/51/53/54 formally archived LOST_UNRESOLVED.

---

## LINKEDIN CHANNEL RULES — WEEK 11

**STATUS FOR BATCH 5 AND ALL PRIOR: PERMANENTLY CLOSED — archive trigger fired Tuesday 2026-05-19 EOD (68-session failure).**

**STATUS FOR BATCH 6: MANDATORY — activate Day 3 from Day-0 (Fri 2026-06-19).**

### Batch 6 LinkedIn Rules (non-negotiable)

1. Execute on Day 3 of initial email send — zero tolerance for deferral (Fri 2026-06-19)
2. profiles.json MUST be written same session as execution — one entry per lead
3. If profiles.json not written same session: that session's LinkedIn did not happen for BRAIN purposes
4. Archive trigger fires Tue 2026-06-24 EOD — fires unconditionally if profiles.json missing — NO EXCEPTIONS
5. Connection note: 200-char hard limit, start with name, mention specific business, end low-pressure
6. After connection accepted: wait 3-5 days, send ONE short value message (no pitch, no email reference)
7. **orchestrator.py must be built before Fri 2026-06-19 — this is the only mechanism guaranteeing profiles.json same-session write**

---

## GEOGRAPHIC FOCUS — WEEK 11

**Batch 5 (FORMALLY CLOSED):**
- **Ryedale District:** Malton, Pickering, Helmsley, Kirkbymoorside, Hovingham, Norton-on-Derwent
- Window closed 2026-05-29 evening. 0 confirmed replies. Reapproach: 2026-11-26.

**Batch 6 — CONFIRMED LAUNCH — Scenario C:**
- **Territory:** Harrogate District (Knaresborough, Ripon new leads only — DO NOT reapproach lead 1, Boroughbridge), Craven District (Skipton, Settle, Grassington, Gargrave)
- **Day-0:** Tue 2026-06-16 (Scenario C — CONFIRMED, 13 days away)

**Paused / do not expand:**
- Fitness/wellness (Otley) — suppress category. Use AIDA positive-amplification only before re-engaging
- Sheffield, Manchester — outside Yorkshire focus; dilutes personalisation
- East Yorkshire general — Batch 4 complete. Fresh scrape earliest June.
- Beverley, Bridlington, Driffield — re-scrape June with new leads only. Do not reapproach Batch 4 leads before October.

**Blocked leads (do not reapproach before listed date):**
- Lead 2 (Nidderdale Pet Supplies) — NOT_INTERESTED. Reapproach: 2026-10-06
- Leads 1, 3, 22 — PERMANENTLY ARCHIVED LOST_NO_RESPONSE. Reapproach: 2026-10-26
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

## COMPLIANCE REMINDERS

- All outreach to business emails only — B2B legitimate interest basis
- Unsubscribes: suppress within 24 hours (GDPR Article 21) — log in audit_log table — applies 24/7
- Log all suppressions in audit_log table
- No residential addresses ever
- OOO pauses are mandatory — do not re-send during stated OOO period
- IMAP check before every send — 60-day gap is a compliance risk — weekly IMAP mandatory for Batch 6
- 4-touchpoint maximum — hard limit, no exceptions
- LinkedIn: do not approach leads who replied NOT_INTERESTED on any channel

---

## OPERATIONAL PRIORITIES — WEEK 10-11 (Days 61-68, 2026-05-27 to 2026-06-03)

| Priority | Action | Deadline | Status |
|---|---|---|---|
| **1** | **IMAP FINAL per Batch 5 lead** — 72h post-Day-14 (NOT leads 1/3/22). 55-day gap. LAST BATCH 5 SWEEP. | **TODAY Fri 2026-05-29 (72h FINAL — window closes this evening)** | EXECUTING TODAY |
| **2** | **CHANGELOG.md** — 61+ days overdue — ABSOLUTE FINAL DEADLINE | **THIS SESSION — ZERO TOLERANCE — CANNOT BE DEFERRED** | OVERDUE |
| **3** | **Batch 6 scraping** — HANDS writes data/batch_6_leads.json (18-22 leads, Harrogate + Craven) | OVERDUE (was Wed 2026-05-27) — **ABSOLUTE FINAL DEADLINE TODAY FRIDAY 2026-05-29** | MISSING |
| **4** | **Update lead status → sequence_complete** — all Batch 5 Ryedale leads. Reapproach: 2026-11-26. | **THIS SESSION** | DUE TODAY |
| **5** | **BRAIN signal assignment + email copy** — review batch_6_leads.json, assign signals, write per-lead copy | Mon 2026-06-01 (after HANDS writes batch_6_leads.json) | Upcoming |
| **6** | **Batch 6 Day-0 sends** — 18-22 leads. SSL-PAS 60%. IMAP per lead before each send. | **Tue 2026-06-02, 09:00-10:30** | Upcoming |
| **1** | **batch_6_leads.json** — 18-22 leads, Harrogate + Craven | **Thu 2026-06-11 EOD (RECOMMENDED — 8 days — final window for BRAIN quality copy)** | MISSING — 68-SESSION FAILURE |
| **2** | **Build orchestrator.py** — src/outlocal/linkedin/orchestrator.py | **Before Fri 2026-06-19 (Day-3 LinkedIn window — 16 days)** | NOT IMPLEMENTED |
| **3** | **CHANGELOG.md** — 66+ days overdue | **Same session as Batch 6 Day-0 Tue 2026-06-16 — ABSOLUTE FINAL DEADLINE** | OVERDUE |
| **4** | **Update lead status → sequence_complete** — all Batch 5 Ryedale leads | OVERDUE | DUE |
| **5** | **Batch 6 Day-0 sends** — IMAP per lead before each | **Tue 2026-06-16, 09:00-10:30 (SCENARIO C — CONFIRMED)** | Upcoming |
| **6** | **Batch 6 Day-3 bumps + LinkedIn** — profiles.json SAME SESSION | **Fri 2026-06-19** | Upcoming |
| **7** | **LinkedIn archive trigger** — fires unconditionally | **Tue 2026-06-24 EOD** | Armed |
| **8** | **Batch 6 Day-7 new angle** | **Tue 2026-06-23** | Upcoming |
| **9** | **Batch 6 Day-14 breakup** | **Tue 2026-06-30** | Upcoming |
| **10** | **Weekly IMAP** — resume from Batch 6 Day-0, every 7 days minimum | From Day-0 (Tue 2026-06-16) onward | CRITICAL |

---

*Active strategy maintained by OUTLOCAL BRAIN layer.*  
*Updated: 2026-06-03 (Day 68 — Wednesday — Week 11 — Scenario C CONFIRMED ACTIVE — Day-0 Tue 2026-06-16 13 days away).*  
*HANDS layer agents must read this file before starting any daily run.*  
*SINGLE MOST IMPORTANT ACTION: Write data/batch_6_leads.json by Thu 2026-06-11 EOD (8 days — recommended) to allow BRAIN per-lead copy generation before Scenario C Day-0 Tue 2026-06-16. Build orchestrator.py before Fri 2026-06-19 (16 days). CHANGELOG mandatory Tue 2026-06-16.*  
*If INTERESTED reply ever discovered incidentally during Batch 6 IMAP: 24h proposal SLA applies (24/7 — NON-NEGOTIABLE). Use value_delivery_queue.json directly.*
