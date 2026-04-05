# OUTLOCAL — Active Campaign Strategy
**Updated:** 2026-04-05 (Week 2 strategy)  
**Replaces:** N/A (first active_strategy.md)  
**Valid until:** 2026-04-12 (next weekly review)

---

## CURRENT CAMPAIGN STATUS

- **Week:** 2 (live since 28 March 2026)
- **Leads scraped:** ~48
- **Emails sent:** ~30
- **In pipeline:** 2 INTERESTED (leads 3, 22), ~28 no-reply or pending
- **Overall reply rate:** 20% | Positive rate: 6.7%
- **LinkedIn:** Launching this week (Day 7+ cohort now qualifies)

---

## SIGNAL PRIORITY ORDER

When scraping and selecting leads to email, prioritise in this order:

1. **`ssl` / `ssl_mobile`** — highest reply rate (~25%). Lead with this always.
2. **`no_website`** (businesses with phone + active reviews) — promising, needs Day 7 data
3. **`mobile`** — valid pain, use BAB framework, softer opener
4. **`social_media`** — AIDA only, requires 4.5★+ / 100+ reviews
5. **`generic`** — do not email until deep crawl finds specific angle

---

## FRAMEWORK ALLOCATION (Week 2 targets)

| Framework | Allocation | When to use |
|---|---|---|
| **PAS** | 55% | SSL, mobile, no-website — any visible technical deficit |
| **BAB** | 25% | No-website + active social; mobile failures |
| **AIDA** | 10% | High-reputation leads (4.5★+, 100+ reviews) missing one channel |
| **Question** | 10% | Trades with no owner name — curiosity-led opener |
| Cliffhanger | 0% | Deferred — insufficient signal |
| Observation | 0% | Deferred — insufficient signal |

---

## LEAD SCORING RULES

- **Minimum score to email: 55**
- Exception: no-website leads in active businesses with confirmed owner name — can email at 50+
- Do not spend enrichment time on leads scoring <50 unless email is trivially findable
- Both Week 1 positive replies came from leads scoring 70+

---

## SUBJECT LINE RULES

**Use this pattern:** `[First name] — [town] [business type] [specific concrete issue]`  
Examples:
- "Sarah — your York salon website is flagged 'Not Secure'"
- "Tom — your Ripon carpentry site isn't mobile-friendly"

**Rules:**
1. First name in subject if owner name is known (outperforms business name only)
2. Town name always included — local relevance is a trust signal
3. Issue must be specific and verifiable (not "improve your presence")
4. No question marks in subject — statement of fact performs better for cold email

**Fallback (no owner name):** `[Business name] — [specific concrete issue]`

---

## PERSONALISATION RULES

- Always address by first name in body if known, "Hi" if not
- Mention the specific URL that has the problem (builds credibility — shows you looked)
- Reference the town in the opening line
- One pain point per email — do not list all issues (overwhelm kills response)
- For trades: mention "customers search for you online before calling"
- For beauty/wellness: lead with trust/reputation angle, not technical deficit

---

## FOLLOW-UP SEQUENCE

| Day | Type | Notes |
|---|---|---|
| Day 0 | Initial send | PAS/BAB/AIDA as assigned |
| Day 3 | Short bump | Thread reply, 3–5 lines, no new content |
| Day 7 | New angle | Different pain point, fresh email |
| Day 14 | Breakup | Short, no pressure, leaves door open |

- Maximum 3 follow-ups (4 total touchpoints)
- Always suppress unsubscribers immediately
- Pause OOO leads — resume day after return date

---

## EMAIL ENRICHMENT RULES

**For trades businesses (garage, plumber, electrician, builder, roofer):**
- Prefer website contact page email over Google Maps listing email
- Google Maps listing often routes to workshop/reception, not the owner
- If no website email found, try Companies House for director name + domain pattern

**Priority order for enrichment time:**
1. Leads with owner name known + website URL → fastest to enrich
2. Leads with website only → crawl contact page
3. Leads with no website → phone lookup / Companies House / social media DM
4. Leads scoring <50 → deprioritise

---

## LINKEDIN CHANNEL RULES

**Qualification criteria:**
- Emailed 3+ days ago with no reply
- Not replied, not unsubscribed, not converted
- Do not target if already replied on email

**Connection note priorities:**
1. `post_reference` — reference a specific post they made (highest acceptance)
2. `headline` — comment on their role/headline naturally
3. `local_interest` — shared local business topic
4. `generic` — fallback only

**Anti-patterns (never use):**
- "I came across your profile"
- "I was impressed by"
- Any mention of AI or automation
- No pitching in the connection note — curiosity only

**After connection accepted:** Wait 2–3 days, then send a short value message (not a pitch). Reference the email if it was sent.

**Channel split:** 80% email / 20% LinkedIn in Week 2.

---

## GEOGRAPHIC FOCUS

**Active:**
- West Yorkshire (Leeds, Bradford, Halifax, Calderdale corridor, Keighley, Dewsbury, Sowerby Bridge, Hebden Bridge, Todmorden, Cleckheaton, Batley)
- North Yorkshire (York, Harrogate, Ripon, Skipton, Pateley Bridge)
- Derbyshire (Bakewell — light coverage)

**Expanding Week 2:**
- East Yorkshire: Beverley, Bridlington, Driffield — fresh territory, high trades density
- Ilkley corridor deeper coverage

**Paused/deprioritised:**
- Fitness/wellness category in Otley — 1 unsubscribe; reconsider framing before re-engaging
- Sheffield, Manchester — too early to expand outside Yorkshire

---

## INDUSTRY FRAMING NOTES

| Sector | Best approach | Avoid |
|---|---|---|
| Trades (plumber, electrician, roofer) | Trust + "customers Google you first" | Technical jargon |
| Beauty/salon | Reputation, booking, trust signal | Deficit framing |
| Hospitality/restaurant | Conversion, booking link, social proof | Generic "website" pitch |
| Accountancy/professional | Business impact, Google ranking | "Marketing services" framing |
| Fitness/wellness | Positive amplification (AIDA) | PAS deficit framing |
| Vets/healthcare | Reputation amplification | Cold, transactional tone |
| Retail/flooring/carpets | Trust, showroom pre-visit research | — |

---

## IMMEDIATE PRIORITIES THIS WEEK

1. Convert **lead 3 (Claire, Westfield Hair, Leeds)** → run audit, reply with PDF + call availability
2. Convert **lead 22 (Rob, Pennine Print, Sowerby Bridge)** → reply with pricing + audit today
3. Resume **lead 12 (Bronte Country Cottages)** from 8 April — use info@brontecottages.co.uk
4. Re-enrich **lead 15 (Valley View Garage, Todmorden)** → find owner via website/phone
5. Launch **LinkedIn** for 28–31 March no-reply cohort
6. **Batch 4 scrape** — East Yorkshire
7. Send **Day 3 and Day 7 follow-ups** from followup_queue.json
8. Domain auth check before scaling beyond 40 sends/day

---

## COMPLIANCE REMINDERS

- All outreach to business emails only — B2B legitimate interest basis
- Process unsubscribes within 24 hours (GDPR Article 21)
- Log all suppressions in audit_log table
- No residential addresses ever
- OOO pauses are mandatory — do not re-send during stated OOO period

---

*Active strategy maintained by OUTLOCAL BRAIN layer.*  
*Updated weekly. HANDS layer agents read this file before starting any daily run.*  
*Next review: 2026-04-12 after Week 2 data collected.*
