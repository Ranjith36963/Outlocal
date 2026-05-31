# OUTLOCAL Daily Strategy — Day 65 (Sunday 2026-05-31 — Week 10 Close)

**Updated:** 2026-05-31 (BRAIN Day 65 run — Sunday — Week 10 Close)  
**Replaces:** 2026-05-30 strategy (Day 64 — Saturday — Weekend Bridge — Batch 5 Formally Closed)  
**Key changes from Day 64:** Day advances to 65. Week 10 close. batch_6_leads.json STILL MISSING (emergency final deadline TODAY EOD). IMAP gap 57 days. Batch 5 FORMALLY CLOSED (0 confirmed replies, window closed Fri 2026-05-29 evening). Weekly intelligence report generated (week_2026-05-31.md).

---

## SITUATION

**Campaign day 65 of 65 (Week 10 close).**

Batch 5 Ryedale is formally closed as of Friday 2026-05-29 evening. Zero confirmed replies across a full 4-touchpoint sequence. The model is sound — the 0% result is an execution failure, not a copy or signal failure.

The singular blocker for Batch 6 is **batch_6_leads.json**, which has now missed its Wednesday, Friday, and Saturday deadlines across 65 consecutive unwritten sessions. TODAY SUNDAY EOD is the absolute final window for **Scenario A** (Day-0 Tuesday 2026-06-02). If the file is not received by tonight, **Scenario B is confirmed**: Day-0 deferred to Tuesday 2026-06-09, with all subsequent dates shifting 7 days.

No sends today. No IMAP today (Sunday block). This is a planning and reporting session only.

---

## WEEK 10 VERDICT

**What happened this week:**
1. Day-14 breakup assumed sent Tuesday 2026-05-26 — final Batch 5 touchpoint
2. Post-Day-14 reply window opened Wednesday (24h), peaked Thursday (48h), closed Friday evening (72h)
3. Zero confirmed replies in the window (57-day IMAP gap means this may be incomplete)
4. Batch 5 formally closed Friday 2026-05-29 evening
5. batch_6_leads.json missed its Wednesday, Friday, and Saturday deadlines
6. CHANGELOG remained at 63+ days with no new entries

**Model performance review:**
- SSL-PAS: 15% INTERESTED rate across Batches 1–3 — remains the strongest signal in the campaign
- The three INTERESTED leads (Tom, Claire, Rob) all came from SSL-PAS Day-0 emails — confirmed playbook
- Batch 5 0% is consistent with 65-session execution failure (IMAP gap, LinkedIn failure, no per-lead data)
- Do not adjust copy or signal mix for Batch 6 — the playbook works when executed correctly

---

## SUBJECT LINE WINNERS

All 3 INTERESTED replies from identical subject structure:

> `[First name] — your [town] [business type] site is flagged 'Not Secure'`

**Confirmed rules:**
- First name in subject — outperforms business name only (3/3 INTERESTED had known first names)
- Town name — local credibility, confirmed trust signal
- `'Not Secure'` — Chrome's exact wording, not "unsecured" or "security issue"
- No question marks — statement of fact beats question hook every time
- Post-bank-holiday Tuesday AM — all 3 INTERESTED replied to sends adjacent to bank holidays

**Batch 6 subject line examples (ready to use):**
- "Mark — your Knaresborough plumbing site is flagged 'Not Secure'"
- "Julie — your Skipton B&B website is flagged 'Not Secure'"
- "David — your Ripon estate agency site isn't secure"
- "Sarah — your Settle builder website is flagged 'Not Secure'"
- "Helen — your Boroughbridge joinery site is flagged 'Not Secure'"

---

## BATCH 6 STRATEGIC BRIEF

**Territory:** Harrogate District + Craven District  
**Why this territory:**
- North Yorkshire continuation — consistent with Batches 1–5 geographic focus
- Harrogate District: Knaresborough (market town, high trades density), Ripon (cathedral city heritage), Boroughbridge (A1 corridor)
- Craven District: Skipton (largest market town, broadest sector mix), Settle (Dales gateway, hospitality), Grassington (tourist village, no-website angle), Gargrave (low competition)
- Both districts have strong trades economies with expected high SSL site density (small businesses, built mid-2000s to mid-2010s, rarely updated)

**Signal priority for Batch 6:**
1. SSL-PAS (60%) — lead with this. Non-negotiable. Every HTTP site in target sectors.
2. Mobile-PAS (20%) — only if SSL is clean AND mobile is clearly broken (test it personally, document specific failure)
3. No-website BAB (15%) — 4★+ AND 20+ reviews, confirmed owner name. Grassington and Gargrave are the strongest candidates.
4. AIDA (5%) — 4.5★+ AND 100+ reviews only, verifiable keyword gap confirmed

**Sector framing for Harrogate + Craven:**
- Trades (plumber, electrician, joiner, builder, roofer): "Customers search for you online before calling — the Not Secure warning stops them." Trust framing.
- B&B/hospitality: First-impression and booking angle. "Booking sites charge 15–18% per night. A site with a direct booking form captures that back."
- Estate agents: Trust and local SEO framing. "Buyers and sellers both check your credibility online before they call."
- Solicitors/accountants: Professional credibility framing. "HTTPS is the baseline expectation for any professional services firm in 2026."
- Beauty/salon (Skipton): Trust + booking gap. Lead with booking, not SSL deficit.

---

## CRITICAL OPERATIONAL CORRECTIONS FOR BATCH 6

These are the specific failure modes from Batches 1–5 that MUST be fixed:

### 1. IMAP (Non-negotiable from Day-0)
- **Weekly IMAP from Day-0 send date** — no exceptions
- **Per-lead IMAP before every send** — pre-send sweep required
- Do NOT allow the gap to exceed 7 days at any point in the Batch 6 sequence
- Any unsubscribe found: suppress within 24h, log audit_log + CHANGELOG same session
- Any INTERESTED found: 24h proposal SLA (24/7, including weekends)

### 2. LinkedIn (Execute Day 3–7 or lose the channel)
- LinkedIn is MANDATORY for Batch 6 — it was the primary conversion channel missed across all 65 sessions
- **Execute within Day 3–7 from Day-0 — zero tolerance for deferral**
- **Write profiles.json same session** — if not written, LinkedIn did not happen for BRAIN purposes
- **Archive trigger fires Day 7 from Day-0 unconditionally** — regardless of reason for non-execution
- Connection note: 200-char hard limit, start with name, mention specific business, end low-pressure
- After acceptance: 3–5 day wait, ONE short value message (no pitch, no email reference)

### 3. Per-lead data (HANDS must write file before BRAIN can run copy)
- BRAIN cannot personalise copy without knowing: owner_name, business_name, URL, ssl_status, town, review_count, star_rating
- batch_6_leads.json MUST be written by HANDS before BRAIN's Monday copy run
- Minimum fields per lead: lead_id, business_name, owner_name (if findable), email, website_url, ssl_status, mobile_score, review_count, star_rating, signal_type, signal_notes, lead_score
- Without this file: BRAIN writes generic templates. Personalisation is lost. INTERESTED rate drops.

### 4. CHANGELOG (Write after every send day)
- Mandatory entry after: every Day-0, Day-3, Day-7, Day-14 send session
- Minimum per entry: date, sends completed (with lead IDs), IMAP results, LinkedIn status, any replies found
- This is a compliance audit trail, not optional

---

## ANALYTICS PATTERNS — WINNING ANGLES FOR BATCH 6

Based on all confirmed INTERESTED replies and observed patterns:

**Body copy patterns that worked:**
- Opening with "I was looking up [trade] in [town] this morning" — shows local knowledge, specific research
- Including the specific URL with the 'Not Secure' label — builds credibility, shows you actually checked
- One pain point per email — never list multiple issues in a single email
- Soft close: "Would it be worth a quick chat?" — low commitment, low friction

**Body copy patterns that failed (0 replies):**
- Generic "your website could be better" framing — no specificity, no signal
- Multiple issues listed in one email — dilutes the single hook
- Question mark in subject line — weaker than a statement every time
- Day-7 that reframes Day-0 instead of introducing a genuinely new angle — 0% response confirmed

**Day sequence dynamics:**
- Day-0: SSL-PAS primary. Tuesday AM. First-name subject. Specific URL.
- Day-3: Short thread bump. "Still showing the warning." Not a new pitch.
- Day-7: MUST be a genuinely different pain point. SSL → ranking penalty is the proven pivot.
- Day-14: 3 lines max. No pressure. "Leaving this with you." Door open.

---

## SCENARIO PLANNING

### If batch_6_leads.json received TODAY Sunday EOD:
1. BRAIN runs Monday 2026-06-01 — reads file, assigns signals, generates per-lead copy
2. HANDS confirms copy Monday afternoon
3. Tuesday 2026-06-02, 09:00: IMAP per lead (pre-send sweep)
4. Tuesday 2026-06-02, 09:00–10:30: Batch 6 Day-0 sends (18–22 leads, stagger 10 min)
5. Friday 2026-06-05: Day-3 bumps + LinkedIn execution + profiles.json same session
6. Tuesday 2026-06-10 EOD: LinkedIn archive trigger fires unconditionally

### If batch_6_leads.json NOT received by Monday morning BRAIN run:
1. BRAIN Monday confirms Scenario B
2. BRAIN generates framework copy for deferred Day-0 (awaiting per-lead population)
3. HANDS writes file Monday → Tuesday 2026-06-09 Day-0 is the new target
4. 7-day schedule shift across all touchpoints and LinkedIn trigger

---

## FORWARD DECISIONS

| Decision | Owner | Deadline | Status |
|---|---|---|---|
| Write batch_6_leads.json | HANDS | TODAY Sunday EOD | PENDING — 65-session failure |
| BRAIN copy generation | BRAIN | Monday 2026-06-01 | Upcoming |
| Update Batch 5 leads → sequence_complete | HANDS | Monday | DUE |
| CHANGELOG | HANDS | Monday | 63+ days overdue |
| Batch 6 Day-0 sends | HANDS | Tue 2026-06-02 (A) or Tue 2026-06-09 (B) | Upcoming |
| LinkedIn Day 3 execution + profiles.json | HANDS | Fri 2026-06-05 (A) or Fri 2026-06-12 (B) | Upcoming |

---

*Strategy maintained by OUTLOCAL BRAIN layer.*  
*Day 65 — Sunday 2026-05-31 — Week 10 close.*  
*HANDS: Read the Week 10 intelligence report (data/weekly_reports/week_2026-05-31.md) before your Monday session.*  
*Single most important action: write data/batch_6_leads.json TODAY Sunday EOD.*
