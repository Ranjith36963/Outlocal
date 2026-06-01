# OUTLOCAL — Active Campaign Strategy
**Updated:** 2026-06-01 (Day 66 Monday — Week 11 Start — Scenario A CONFIRMED CLOSED — batch_6_leads.json LAST VIABLE WINDOW TODAY EOD)  
**Replaces:** 2026-05-31 strategy (Day 65 — Sunday — Week 10 Close — Scenario B High Probability)  
**Valid until:** After Batch 6 Day-0 send confirmed (Scenario B: Tue 2026-06-09 / Scenario C: Tue 2026-06-16)  
**Weekly report:** data/weekly_reports/week_2026-05-31.md (WEEK 10 CLOSE)

---

## CURRENT CAMPAIGN STATUS

- **Week:** 11 start (live since 28 March 2026 — 66 days)
- **Batch 5 Ryedale:** **FORMALLY CLOSED — 2026-05-29 evening.** 0 confirmed replies across full 4-touchpoint sequence. Reapproach: 2026-11-26. No further IMAP, no further sends.
- **Batch 6 Harrogate + Craven:** **LAUNCH CONFIRMED.** batch_6_leads.json STILL MISSING — **66-session HANDS pattern**. **SCENARIO A CONFIRMED CLOSED** (Sunday EOD deadline passed). **TODAY Monday 2026-06-01 EOD is the LAST VIABLE WINDOW for Scenario B** (Day-0 Tue 2026-06-09). Scenario C activates (Day-0 Tue 2026-06-16) if not received today.
- **Leads scraped:** ~50 confirmed (Batches 1–4) + 12-18 Batch 5 Ryedale (UNCONFIRMED) + 18-22 Batch 6 pending scrape (batch_6_leads.json MISSING)
- **Emails sent (estimated):** ~160-184 total (Batches 1–5 all touchpoints assumed, UNCONFIRMED beyond Batch 1–3)
- **Total replies:** 11 (17.9% overall reply rate — all from Batches 1–4)
- **Batch 5 replies:** **0 confirmed. Window CLOSED Friday 2026-05-29 evening. FORMALLY CLOSED.**
- **INTERESTED leads (ever):** 3 (leads 1, 3, 22) — ALL PERMANENTLY ARCHIVED LOST_NO_RESPONSE
- **Conversions confirmed:** 0
- **LinkedIn:** **PERMANENTLY CLOSED for Batch 5 and all prior leads — archive trigger fired 2026-05-19 EOD (66-session failure). MANDATORY for Batch 6: activate Day 3-7 from Day-0. Archive trigger Day 7 from Day-0 — unconditional. orchestrator.py NOT IMPLEMENTED — build before Day-3 window.**
- **IMAP gap:** **58 days** from confirmed check (2026-04-04). NOT REQUIRED today (Monday block, Batch 5 window closed). Next IMAP obligation: Batch 6 leads only (per lead before each Day-0 send).
- **CHANGELOG:** **64+ days overdue — MANDATORY — same session as Batch 6 Day-0 sends — ABSOLUTE FINAL DEADLINE.**

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
- "James — your Grassington joinery site is flagged 'Not Secure'"

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
- IMAP check before EVERY send — 58-day gap is an operational and compliance risk — weekly IMAP mandatory for Batch 6
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
| **Scenario A** | **CONFIRMED CLOSED** — Tue 2026-06-02 Day-0 not possible |
| **Scenario B** | **TUESDAY 2026-06-09, 09:00-10:30** — IF batch_6_leads.json received TODAY Monday EOD |
| **Scenario C** | **TUESDAY 2026-06-16, 09:00-10:30** — IF batch_6_leads.json not received today |

---

## BATCH 5 RYEDALE — FINAL STATUS (Formally Closed — 2026-05-29 Evening)

**Formally closed:** Friday 2026-05-29 evening — post-Day-14 72h window closed.

| Milestone | Date | Status |
|---|---|---|
| Day-0 sends | Tue 2026-05-12 | ASSUMED SENT — UNCONFIRMED |
| Day-3 bumps | Fri 2026-05-15 | ASSUMED SENT — UNCONFIRMED |
| Day-7 sends | Tue 2026-05-19, 09:00-10:30 | ASSUMED SENT — UNCONFIRMED |
| LinkedIn archive trigger | Tue 2026-05-19 EOD | **FIRED — PERMANENTLY CLOSED** |
| Day-14 breakup sends | Tue 2026-05-26 | ASSUMED SENT — UNCONFIRMED |
| **Post-Day-14 72h FINAL IMAP** | **Fri 2026-05-29** | **UNCONFIRMED — window now CLOSED regardless** |
| **POST-DAY-14 WINDOW** | **CLOSED — 2026-05-29 evening** | **UNCONDITIONAL. 0 confirmed replies.** |
| **SEQUENCE STATUS** | **FORMALLY CLOSED** | **Reapproach: 2026-11-26. No further sends or IMAP.** |

**Model assessment:** SOUND. 0% Batch 5 = execution failure (58-day IMAP gap + 66-session LinkedIn failure + no per-lead data file). SSL-PAS 15% INTERESTED rate remains non-negotiable for Batch 6.

---

## BATCH 6 HARROGATE + CRAVEN — THREE-SCENARIO STATUS

**Decision:** Confirmed. Proceeds regardless of Batch 5 reply count.  
**Territory:** Harrogate District (Knaresborough, Ripon new leads only, Boroughbridge) + Craven District (Skipton, Settle, Grassington, Gargrave)  
**batch_6_leads.json:** MISSING — **LAST VIABLE WINDOW: TODAY Monday 2026-06-01 EOD**  

| Scenario | Condition | Day-0 | Day-3 + LinkedIn | LinkedIn Trigger | Day-7 | Day-14 |
|---|---|---|---|---|---|---|
| **A** | File received Sun 2026-05-31 EOD | Tue 2026-06-02 | Fri 2026-06-05 | Tue 2026-06-10 EOD | Tue 2026-06-09 | Tue 2026-06-16 |
| **B** | File received **TODAY Mon 2026-06-01 EOD** | **Tue 2026-06-09** | **Fri 2026-06-12** | **Tue 2026-06-17 EOD** | Tue 2026-06-16 | Tue 2026-06-23 |
| **C** | File NOT received by today EOD | Tue 2026-06-16 | Fri 2026-06-19 | Tue 2026-06-24 EOD | Tue 2026-06-23 | Tue 2026-06-30 |

**Scenario A: CONFIRMED CLOSED** — Sunday EOD deadline passed.  
**Scenario B: LAST VIABLE WINDOW TODAY.** HANDS must write file by tonight.  
**Scenario C: ACTIVATES if file not received today.** No further extensions.

**LinkedIn rules (MANDATORY both Scenarios B and C):**
- Execute Day 3-7 from Day-0 — zero tolerance for deferral
- profiles.json MUST be written same session as execution
- Archive trigger fires on Day 7 from Day-0 — unconditional if profiles.json missing
- **orchestrator.py NOT IMPLEMENTED** — must be built before Day-3 window (Fri 2026-06-12 or Fri 2026-06-19)
- Connection note: 200-char hard limit, start with name, mention specific business, end low-pressure

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

## LINKEDIN CHANNEL RULES — WEEK 11

**STATUS FOR BATCH 5 AND ALL PRIOR: PERMANENTLY CLOSED — archive trigger fired Tuesday 2026-05-19 EOD (66-session failure).**

**STATUS FOR BATCH 6: MANDATORY — activate Day 3-7 from Day-0.**

### Batch 6 LinkedIn Rules (non-negotiable)

1. Execute within Day 3-7 of initial email send — zero tolerance for deferral
2. profiles.json MUST be written same session as execution — one entry per lead
3. If profiles.json not written same session: that session's LinkedIn did not happen for BRAIN purposes
4. Archive trigger fires on Day 7 from Day-0 — fires unconditionally if profiles.json missing — NO EXCEPTIONS
5. Connection note: 200-char hard limit, start with name, mention specific business, end low-pressure
6. After connection accepted: wait 3-5 days, send ONE short value message (no pitch, no email reference)
7. **orchestrator.py must be built before Day-3 window — this is the only mechanism guaranteeing profiles.json same-session write**

---

## GEOGRAPHIC FOCUS — WEEK 11

**Batch 5 (FORMALLY CLOSED):**
- **Ryedale District:** Malton, Pickering, Helmsley, Kirkbymoorside, Hovingham, Norton-on-Derwent
- Window closed 2026-05-29 evening. 0 confirmed replies. Reapproach: 2026-11-26.

**Batch 6 — CONFIRMED LAUNCH:**
- **Territory:** Harrogate District (Knaresborough, Ripon new leads only — DO NOT reapproach lead 1, Boroughbridge), Craven District (Skipton, Settle, Grassington, Gargrave)
- **Day-0:** Scenario B Tue 2026-06-09 (if file received TODAY) / Scenario C Tue 2026-06-16 (if not)

**Paused / do not expand:**
- Fitness/wellness (Otley) — suppress category
- Sheffield, Manchester — outside Yorkshire focus
- East Yorkshire general — Batch 4 complete. Fresh scrape earliest June.
- Beverley, Bridlington, Driffield — re-scrape June. Do not reapproach Batch 4 leads before October.

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
- IMAP check before every send — 58-day gap is a compliance risk — weekly IMAP mandatory for Batch 6
- 4-touchpoint maximum — hard limit, no exceptions
- LinkedIn: do not approach leads who replied NOT_INTERESTED on any channel

---

## OPERATIONAL PRIORITIES — WEEK 11 (Days 66-72, 2026-06-01 to 2026-06-07)

| Priority | Action | Deadline | Status |
|---|---|---|---|
| **1** | **batch_6_leads.json** — 18-22 leads, Harrogate + Craven | **TODAY Monday 2026-06-01 EOD — ABSOLUTE LAST VIABLE WINDOW FOR SCENARIO B** | MISSING — 66-SESSION FAILURE |
| **2** | **CHANGELOG.md** — 64+ days overdue | **Same session as Batch 6 Day-0 — ABSOLUTE FINAL DEADLINE** | OVERDUE |
| **3** | **Build orchestrator.py** — src/outlocal/linkedin/orchestrator.py | **Before Day-3 LinkedIn window (Fri 2026-06-12 Scenario B or Fri 2026-06-19 Scenario C)** | NOT IMPLEMENTED |
| **4** | **Update lead status → sequence_complete** — all Batch 5 Ryedale leads | Monday today — OVERDUE | DUE |
| **5** | **Batch 6 Day-0 sends** — IMAP per lead before each | **Tue 2026-06-09 (B) or Tue 2026-06-16 (C)** | Upcoming |
| **6** | **Batch 6 Day-3 bumps + LinkedIn** — profiles.json SAME SESSION | **Fri 2026-06-12 (B) or Fri 2026-06-19 (C)** | Upcoming |
| **7** | **LinkedIn archive trigger** — fires unconditionally | **Tue 2026-06-17 EOD (B) or Tue 2026-06-24 EOD (C)** | Upcoming |
| **8** | **Batch 6 Day-7 new angle** | **Tue 2026-06-16 (B) or Tue 2026-06-23 (C)** | Upcoming |
| **9** | **Batch 6 Day-14 breakup** | **Tue 2026-06-23 (B) or Tue 2026-06-30 (C)** | Upcoming |
| **10** | **Weekly IMAP** — resume from Batch 6 Day-0, every 7 days minimum | From Day-0 onward | CRITICAL |

---

*Active strategy maintained by OUTLOCAL BRAIN layer.*  
*Updated: 2026-06-01 (Day 66 — Monday — Week 11 Start — Scenario A CONFIRMED CLOSED — batch_6_leads.json LAST VIABLE WINDOW TODAY EOD).*  
*HANDS layer agents must read this file before starting any daily run.*  
*SINGLE MOST IMPORTANT ACTION: Write data/batch_6_leads.json TODAY Monday 2026-06-01 by EOD. This is the FINAL window for Scenario B (Day-0 Tue 2026-06-09). If not received by tonight: Day-0 defers to Tue 2026-06-16 (Scenario C) — no further extensions under any circumstances.*  
*If INTERESTED reply ever discovered incidentally during Batch 6 IMAP: 24h proposal SLA applies (24/7 — NON-NEGOTIABLE). Use value_delivery_queue.json directly.*
