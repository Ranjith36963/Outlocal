# OUTLOCAL — Active Campaign Strategy
**Updated:** 2026-05-17 (Day 51 Sunday — weekly intelligence report, Week 8 close)  
**Replaces:** 2026-05-16 strategy (valid to 2026-05-24)  
**Valid until:** 2026-05-24 (after Batch 5 Day-7 + Day-14 results and Batch 6 scoping decision)  
**Weekly report:** data/weekly_reports/week_2026-05-17.md

---

## CURRENT CAMPAIGN STATUS

- **Week:** 9 (live since 28 March 2026 — 51 days)
- **Batch 5 Ryedale:** Day 5 (Sunday). Day-0: Tue 2026-05-12 (assumed). Day-3 bump: Fri 2026-05-15 (assumed). Day-7: Tue 2026-05-19 (copy READY).
- **Leads scraped:** ~61 confirmed (Batches 1–4) + 12-18 Batch 5 Ryedale (UNCONFIRMED)
- **Emails sent (estimated):** ~115-127 total (Batches 1–5 Day-0 + Day-3 + all follow-ups, all UNCONFIRMED beyond Batch 1–3)
- **Total replies:** 11 (17.9% overall reply rate — all from Batches 1–4)
- **Batch 5 replies:** 0 confirmed. Reply peak window OPEN Saturday-Tuesday post-bump.
- **INTERESTED leads (ever):** 3 (leads 1, 3, 22) — ALL PERMANENTLY ARCHIVED LOST_NO_RESPONSE
- **Conversions confirmed:** 0
- **LinkedIn:** Never activated (0 connections in 50 sessions) — **FINAL WINDOW MONDAY 2026-05-18, ARCHIVE TRIGGER TUESDAY 2026-05-19 EOD**
- **IMAP gap:** 42 days from confirmed check (2026-04-04) — SWEEP MANDATORY before every send (Monday before LinkedIn, Tuesday before each Day-7 send, per lead)
- **CHANGELOG:** 50+ days overdue — **MANDATORY before Tuesday 2026-05-19 Day-7 sends**
- **Weekly intelligence report:** data/weekly_reports/week_2026-05-17.md (generated 2026-05-17)

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
- IMAP check before EVERY send — 42-day gap is an operational and compliance risk
- Unsubscribers: suppress immediately, log CHANGELOG.md and audit_log

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
| **Batch 5 Day-7 send** | **TUESDAY 2026-05-19, 09:00-10:30** |
| **Batch 5 Day-14 send** | **TUESDAY 2026-05-26, 09:00-10:30** |

---

## BATCH 5 RYEDALE — CURRENT STATUS (Week 8, Day 4)

**Target towns:** Malton, Pickering, Helmsley, Kirkbymoorside, Hovingham, Norton-on-Derwent  
**Minimum review bar for no-website leads:** 4★+ AND 20+ reviews (rural offline economy adjustment)

| Milestone | Date | Status |
|---|---|---|
| Day-0 sends | Tue 2026-05-12 | ASSUMED SENT — UNCONFIRMED |
| Day-3 bumps | Fri 2026-05-15 | ASSUMED SENT — UNCONFIRMED |
| Reply peak | Sat 2026-05-16 — Mon 2026-05-18 | OPEN NOW — 24-72h post-bump |
| LinkedIn execution | Mon 2026-05-18 | **FINAL WINDOW** — profiles.json MISSING (49+ sessions) |
| LinkedIn archive trigger | Tue 2026-05-19 EOD | Fires for any lead without confirmed LinkedIn |
| Day-7 sends | Tue 2026-05-19, 09:00-10:30 | Copy READY in data/daily_email_plan.json |
| Day-14 sends | Tue 2026-05-26, 09:00-10:30 | BRAIN generates copy Tue morning |

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

## LINKEDIN CHANNEL RULES — WEEK 8

**STATUS: NEVER ACTIVATED (0 notes sent in 49+ sessions). HARD DEADLINE: Tuesday 2026-05-19 EOD.**

### Batch 5 LinkedIn — Monday 2026-05-18 (FINAL WINDOW)

1. IMAP sweep per lead first (mandatory)
2. LinkedIn profile searches — sector priority queries in linkedin_search_plan.json
3. Open profile, scroll posts from last 60 days
4. If post found: write bespoke post_reference note (3–4x higher acceptance — always check first)
5. If no post: use monday_fallback_notes from linkedin_connection_notes.json (sector templates — direct-use)
6. Send connection request (200-char hard limit — count in plain-text editor)
7. **Write linkedin_profiles.json IMMEDIATELY after each search — one entry per lead. No batching.**

### LinkedIn Note Rules (non-negotiable)

- 200 character HARD LIMIT — count every character including spaces and punctuation
- Start with their name — never start with "I"
- Mention the specific business name — shows you looked
- One specific observation — not vague, not flattering, just real
- End with low-pressure framing ("in case it's useful")
- Do NOT mention: email outreach, the website, SSL, any prior contact, 'Not Secure'
- Do NOT use: "I came across your profile", "I was impressed by", "synergies", "reach out"
- Do NOT use exclamation marks

### Archive Trigger — Tuesday 2026-05-19 EOD

**Any Batch 5 lead without confirmed LinkedIn (note_sent: true in linkedin_profiles.json) by EOD Tuesday: archive immediately as LOST_NO_RESPONSE. Log CHANGELOG same session. No extensions. No deferrals.**

The warm pipeline failure (49+ sessions, £800-1,175 written off) does not repeat. This trigger is unconditional.

### After LinkedIn Connection Accepted

Wait 3-5 days. Send ONE short value message — a specific observation. Not a pitch. Do not reference the email unless they mention it first.

---

## GEOGRAPHIC FOCUS — WEEK 8

**Primary (Batch 5 — active):**
- **Ryedale District:** Malton, Pickering, Helmsley, Kirkbymoorside, Hovingham, Norton-on-Derwent
- Rural North Yorkshire trades economy — confirmed high SSL signal density

**Batch 6 — planning trigger (fire after Tuesday Day-7 results):**
- **Condition:** Batch 5 Day-7 replies ≥ 2 → confirms Ryedale rural model. Start Batch 6 immediately.
- **Territory:** Harrogate District (Knaresborough, Ripon new leads only, Boroughbridge), Craven District (Skipton, Settle, Grassington, Gargrave)
- **Start:** Data collection from Wed 2026-05-20. Initial sends: Tue 2026-05-26 or Tue 2026-06-02.
- **If Batch 5 Day-7 replies = 0:** Review signal mix and sector targeting before expanding. Do not scrape Batch 6 until Batch 5 full sequence analysis complete.

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
- IMAP check before every send — 42-day gap is a compliance risk
- 4-touchpoint maximum — hard limit, no exceptions
- LinkedIn: do not approach leads who replied NOT_INTERESTED on any channel

---

## OPERATIONAL PRIORITIES — WEEK 9 (Days 51-57)

| Priority | Action | Deadline | Blocker if missed |
|---|---|---|---|
| **1** | **IMAP sweep per Batch 5 lead** — before LinkedIn (Mon) and before each Day-7 send (Tue) | Mon 2026-05-18 + Tue 2026-05-19 | Compliance risk, missed INTERESTED replies |
| **2** | **LinkedIn execution — ALL Batch 5 leads** (FINAL WINDOW) | Mon 2026-05-18 | Archive trigger fires Tue EOD — same outcome as warm pipeline (£800-1,175 written off) |
| **3** | **Write data/linkedin_profiles.json** — same session as execution | Mon 2026-05-18 same session | Archive trigger cannot confirm exceptions |
| **4** | **CHANGELOG.md update** — 50+ days overdue | Before Tue 2026-05-19 Day-7 sends | Compliance audit risk |
| **5** | **Day-7 new-angle sends** — 12-18 Batch 5 leads, 09:00-10:30 | Tue 2026-05-19 | Sequence expires, Day-14 becomes irrelevant |
| **6** | **LinkedIn archive trigger** — archive any Batch 5 lead without confirmed LinkedIn | Tue 2026-05-19 EOD | Warm pipeline repeat failure |
| **7** | **Batch 6 scoping decision** — if Day-7 replies ≥ 2, scrape Harrogate/Craven | From Wed 2026-05-20 | Campaign stall without next batch |
| **8** | **BRAIN: Day-14 breakup copy** generation | Tue 2026-05-26 morning | Day-14 sends miss Tuesday window |
| **9** | **HANDS: Day-14 breakup sends** | Tue 2026-05-26, 09:00-10:30 | 4-touchpoint sequence incomplete |

---

## WEEK 9 VOLUME TARGETS

| Activity | Target |
|---|---|
| Batch 5 Day-7 sends | 12-18 (Tuesday 2026-05-19) |
| LinkedIn connection requests | 12-18 Batch 5 leads (Monday — FINAL WINDOW) |
| Expected INTERESTED (Batch 5, Day-7) | 2-3 (15% SSL-PAS rate on 12-18 sends) |
| IMAP checks | Per Batch 5 lead (Monday before LinkedIn + before each Tuesday send) |
| CHANGELOG entries | All historical (50 days) + Batch 5 Day-0 + Day-3 + LinkedIn outcomes |
| Batch 6 scrape (if triggered) | 18-22 leads (Harrogate District + Craven District) |
| Batch 6 trigger condition | Batch 5 Day-7 replies ≥ 2 by Wednesday 2026-05-20 |

---

*Active strategy maintained by OUTLOCAL BRAIN layer.*  
*Updated: 2026-05-17 (Day 51 — Sunday, weekly intelligence report, Week 8 close).*  
*HANDS layer agents must read this file before starting any daily run.*  
*Next review: 2026-05-24 after Batch 5 Day-7 + Day-14 results and Batch 6 scoping decision.*  
*Weekly intelligence report: data/weekly_reports/week_2026-05-17.md*
