# OUTLOCAL Daily Strategy — Day 66 (Monday 2026-06-01 — Week 11 Start)

**Updated:** 2026-06-01 (BRAIN Day 66 run — Monday — Week 11 Start)  
**Replaces:** 2026-05-31 strategy (Day 65 — Sunday — Week 10 Close)  
**Key changes from Day 65:** Day advances to 66. Week 11 start. **Scenario A CONFIRMED CLOSED** (Sunday EOD deadline passed without file). **Scenario B last viable window: TODAY Monday EOD.** Scenario C introduced (Day-0 Tue 2026-06-16) if file not received today. IMAP gap 58 days. CHANGELOG 64+ days overdue.

---

## SITUATION

**Campaign day 66 of ongoing (Week 11 start — Monday 2026-06-01).**

Scenario A (Day-0 Tuesday 2026-06-02) is **CONFIRMED CLOSED**. Sunday EOD deadline passed without batch_6_leads.json. This is the 66th consecutive session without the file.

**TODAY IS THE FINAL DECISION POINT.** The Monday window determines whether Scenario B (Day-0 Tue 2026-06-09) is still achievable, or whether it defers to Scenario C (Day-0 Tue 2026-06-16):

- **Scenario B (Day-0 Tue 2026-06-09):** Requires batch_6_leads.json **by TODAY Monday EOD**. BRAIN generates per-lead copy tonight. HANDS executes IMAP + sends Tuesday Jun 9. LinkedIn Day 3 Fri Jun 12. Archive trigger Tue Jun 17 EOD.
- **Scenario C (Day-0 Tue 2026-06-16):** Activates if batch_6_leads.json not received today. All touchpoints shift +7 days. LinkedIn archive trigger Tue Jun 24 EOD.

No sends today. No IMAP today (Monday is not a send day). BRAIN run is a planning and template-generation session.

---

## SCENARIO A POST-MORTEM

Scenario A closed without execution. Causes:
1. batch_6_leads.json not written across 65+ consecutive sessions (HANDS failure)
2. Sunday EOD absolute deadline passed — no further reprieve
3. Day-0 Tue 2026-06-02 is not possible — insufficient time for per-lead IMAP before morning sends

**Result:** No revenue impact yet. Scenario B still viable if file received today.

---

## WEEK 10 CLOSE VERDICT

**Final results (Days 59-65):**
- Day-14 breakup assumed sent Tuesday 2026-05-26 — UNCONFIRMED (66-session HANDS pattern)
- Post-Day-14 reply window opened Wed 2026-05-27 (24h), peaked Thu (48h), closed Fri 2026-05-29 evening (72h)
- Zero confirmed replies in the window (58-day IMAP gap means sweep results unknown)
- Batch 5 formally closed Friday 2026-05-29 evening — 0 confirmed replies across full 4-touchpoint sequence
- batch_6_leads.json missed Wednesday, Friday, Saturday, Sunday, and now Monday morning deadlines

**Model performance:**
- SSL-PAS: 15% INTERESTED rate (Batches 1–3) — non-negotiable, unchanged for Batch 6
- Batch 5 0% = execution failure (58-day IMAP gap, LinkedIn 66-session failure, no per-lead data file)
- Do not adjust copy or signal mix — the playbook works when executed correctly

---

## SUBJECT LINE WINNERS

All 3 INTERESTED replies from identical subject structure:

> `[First name] — your [town] [business type] site is flagged 'Not Secure'`

**Confirmed rules:**
- First name in subject — 3/3 INTERESTED had known first names
- Town name — local credibility, confirmed trust signal
- `'Not Secure'` — Chrome's exact wording (not "unsecured" or "security issue")
- No question marks — statement of fact beats question hook every time
- Post-bank-holiday Tuesday AM — all 3 INTERESTED replied adjacent to bank holidays

**Batch 6 subject line examples (ready to use):**
- "Mark — your Knaresborough plumbing site is flagged 'Not Secure'"
- "Julie — your Skipton B&B website is flagged 'Not Secure'"
- "David — your Ripon estate agency site isn't secure"
- "Sarah — your Settle builder website is flagged 'Not Secure'"
- "Helen — your Boroughbridge joinery site is flagged 'Not Secure'"
- "James — your Grassington joinery site is flagged 'Not Secure'"
- "Karen — your Ripon solicitor website isn't secure"

---

## BATCH 6 STRATEGIC BRIEF

**Territory:** Harrogate District + Craven District  
**Day-0 date:** Scenario B — Tue 2026-06-09 (if batch_6_leads.json received TODAY EOD). Scenario C — Tue 2026-06-16 (if not).

**Why this territory:**
- North Yorkshire continuation — consistent with Batches 1–5 geographic focus
- Harrogate District: Knaresborough (market town, high trades density), Ripon (cathedral city, new leads only — do NOT reapproach lead 1), Boroughbridge (A1 corridor trades)
- Craven District: Skipton (largest market town, broadest sector mix), Settle (Dales gateway, hospitality + trades), Grassington (tourist village, strong no-website BAB angle), Gargrave (low competition)

**Signal priority for Batch 6:**
1. SSL-PAS (60%) — every HTTP site in target sectors. Non-negotiable.
2. Mobile-PAS (20%) — only if SSL is CLEAN AND mobile is clearly broken. Test personally. Document specific failure.
3. No-website BAB (15%) — 4★+ AND 20+ reviews, confirmed owner name. Grassington/Gargrave strongest candidates.
4. AIDA (5%) — 4.5★+ AND 100+ reviews ONLY. Verifiable keyword gap confirmed.

**Sector framing for Harrogate + Craven:**
- Trades (plumber, electrician, joiner, builder, roofer): "Customers search for you online before calling — the Not Secure warning stops them." Trust framing.
- B&B/hospitality: First-impression and booking angle.
- Estate agents: Trust and local SEO framing.
- Solicitors/accountants: Professional credibility framing. "HTTPS is the baseline expectation for any professional services firm in 2026."
- Beauty/salon (Skipton only): Lead with booking gap, NOT SSL deficit.

---

## THREE-SCENARIO CALENDAR

| Milestone | Scenario B (file received TODAY) | Scenario C (file not received today) |
|---|---|---|
| batch_6_leads.json deadline | **TODAY Mon 2026-06-01 EOD** | MISSED |
| BRAIN copy generation | Tonight/tomorrow | Thu 2026-06-11 (on receipt) |
| **Day-0 sends** | **Tue 2026-06-09, 09:00-10:30** | **Tue 2026-06-16, 09:00-10:30** |
| Day-3 bumps + LinkedIn | Fri 2026-06-12 | Fri 2026-06-19 |
| LinkedIn archive trigger | **Tue 2026-06-17 EOD** | **Tue 2026-06-24 EOD** |
| Day-7 new angle | Tue 2026-06-16 | Tue 2026-06-23 |
| Day-14 breakup | Tue 2026-06-23 | Tue 2026-06-30 |

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
- LinkedIn MANDATORY for Batch 6 — it was the primary conversion channel missed across all 66 sessions
- Execute within Day 3–7 from Day-0 — zero tolerance for deferral
- Write profiles.json same session — if not written, LinkedIn did not happen for BRAIN purposes
- Archive trigger fires Day 7 from Day-0 unconditionally — regardless of reason for non-execution
- **orchestrator.py still NOT IMPLEMENTED** — must be built before Fri Jun 12 (Scenario B) or Fri Jun 19 (Scenario C)
- Connection note: 200-char hard limit, start with name, mention specific business, end low-pressure

### 3. Per-lead data file
- BRAIN cannot personalise copy without: owner_name, business_name, URL, ssl_status, town, review_count, star_rating
- batch_6_leads.json minimum fields per lead: lead_id, business_name, owner_name, email, website_url, ssl_status, mobile_score, review_count, star_rating, signal_type, signal_notes, lead_score
- Without this file: only generic templates are possible — INTERESTED rate drops significantly

### 4. CHANGELOG (Write at every send day)
- Mandatory entry after: every Day-0, Day-3, Day-7, Day-14 send session
- CHANGELOG currently 64+ days overdue — MANDATORY same session as Batch 6 Day-0 sends — ABSOLUTE FINAL DEADLINE

---

## ANALYTICS PATTERNS — WINNING ANGLES FOR BATCH 6

**Body copy patterns that worked:**
- Opening with "I was looking up [trade] in [town] this morning" — shows local knowledge, specific research
- Including the specific URL with the 'Not Secure' label — credibility, shows you actually checked
- One pain point per email — never list multiple issues
- Soft close: "Would it be worth a quick chat?" — low commitment, low friction

**Body copy patterns that failed (0 replies):**
- Generic "your website could be better" framing — no specificity
- Multiple issues listed in one email — dilutes the single hook
- Question mark in subject line — weaker than statement every time
- Day-7 that reframes Day-0 instead of genuinely new angle — 0% response confirmed

**Day sequence dynamics:**
- Day-0: SSL-PAS primary. Tuesday AM. First-name subject. Specific URL.
- Day-3: Short thread bump. "Still showing the warning." Not a new pitch.
- Day-7: MUST be a genuinely different pain point. SSL → ranking penalty is the proven pivot.
- Day-14: 3 lines max. No pressure. "Leaving this with you." Door open.

---

## FORWARD DECISIONS

| Decision | Owner | Deadline | Status |
|---|---|---|---|
| Write batch_6_leads.json | HANDS | **TODAY Mon 2026-06-01 EOD — ABSOLUTE LAST VIABLE WINDOW FOR SCENARIO B** | MISSING — 66 sessions |
| BRAIN copy generation | BRAIN | Tonight/tomorrow (on file receipt) | Pending file |
| Update Batch 5 leads → sequence_complete | HANDS | Mon 2026-06-01 | OVERDUE |
| Build orchestrator.py | HANDS | Before Fri 2026-06-12 (B) or Fri 2026-06-19 (C) | NOT IMPLEMENTED |
| CHANGELOG | HANDS | Same session as Batch 6 Day-0 | 64+ DAYS OVERDUE — ABSOLUTE FINAL |
| Batch 6 Day-0 sends | HANDS | Tue 2026-06-09 (B) or Tue 2026-06-16 (C) | Upcoming |
| LinkedIn Day 3 + profiles.json | HANDS | Fri 2026-06-12 (B) or Fri 2026-06-19 (C) | Upcoming |

---

*Strategy maintained by OUTLOCAL BRAIN layer.*  
*Day 66 — Monday 2026-06-01 — Week 11 start.*  
*HANDS: TODAY is the LAST VIABLE WINDOW for batch_6_leads.json (Scenario B — Day-0 Tue 2026-06-09). Write the file TODAY EOD. If not received by today EOD: Day-0 defers to Tue 2026-06-16. CHANGELOG mandatory same session as Day-0 sends.*
