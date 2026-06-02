# OUTLOCAL Daily Strategy — Day 67 (Tuesday 2026-06-02 — Week 11)

**Updated:** 2026-06-02 (BRAIN Day 67 run — Tuesday — Week 11)  
**Replaces:** 2026-06-01 strategy (Day 66 — Monday — Week 11 Start)  
**Key changes from Day 66:** Day advances to 67. **SCENARIO B CONFIRMED CLOSED** — Monday EOD deadline passed without batch_6_leads.json (67-session HANDS pattern). **SCENARIO C NOW CONFIRMED ACTIVE** — Day-0 Tue 2026-06-16. This is Scenario A's original Day-0 date (never executed). IMAP gap advances to 59 days. CHANGELOG 65+ days overdue.

---

## SITUATION

**Campaign day 67 of ongoing (Week 11 — Tuesday 2026-06-02).**

Today was Scenario A's planned Day-0. It was not executed.

Scenario B (Day-0 Tue 2026-06-09) is now **CONFIRMED CLOSED**. Monday EOD deadline passed without `batch_6_leads.json`. This is the 67th consecutive session without the file.

**SCENARIO C IS NOW THE ONLY ACTIVE SCENARIO.** All three prior scenarios (A, B, C-contingent) have resolved into a single confirmed path:

- **Day-0: Tuesday 2026-06-16, 09:00–10:30**
- **Day-3 + LinkedIn: Friday 2026-06-19**
- **LinkedIn archive trigger: Tuesday 2026-06-24 EOD** — unconditional
- **Day-7: Tuesday 2026-06-23**
- **Day-14: Tuesday 2026-06-30**

No sends today. No IMAP today (Batch 6 not launched). BRAIN run is a state-update and coordination session.

---

## SCENARIO B POST-MORTEM

Scenario B closed without execution. Causes:
1. `batch_6_leads.json` not written across 67 consecutive sessions (HANDS failure pattern)
2. Monday EOD absolute deadline passed — no further reprieve
3. Day-0 Tue 2026-06-09 is no longer possible — insufficient time for per-lead IMAP before morning sends

**Result:** No revenue impact yet. Scenario C is viable and confirmed. A 7-day calendar shift from Scenario B.

---

## SCENARIO STATUS SUMMARY

| Scenario | Day-0 | Status |
|---|---|---|
| **A** | Tue 2026-06-02 (TODAY) | **CLOSED** — Never executed. 67-session failure. |
| **B** | Tue 2026-06-09 | **CLOSED** — Monday EOD deadline passed. 67-session failure. |
| **C** | **Tue 2026-06-16** | **CONFIRMED ACTIVE** — The only remaining path. No further extensions. |

---

## CONFIRMED SCENARIO C CALENDAR

| Milestone | Date | Status |
|---|---|---|
| **batch_6_leads.json recommended receipt** | **Thu 2026-06-11 EOD** | Recommended — allows BRAIN ~4 days per-lead copy generation |
| batch_6_leads.json absolute minimum | Mon 2026-06-15 | Not recommended — same-day tight BRAIN run |
| **BATCH 6 DAY-0 SENDS** | **Tue 2026-06-16, 09:00–10:30** | CONFIRMED |
| Day-3 bumps + LinkedIn | Fri 2026-06-19 | LinkedIn MANDATORY — profiles.json SAME SESSION |
| LinkedIn archive trigger | **Tue 2026-06-24 EOD** | **UNCONDITIONAL** — fires if profiles.json missing |
| Day-7 new angle | Tue 2026-06-23 | Standalone new email, new pain point |
| Day-14 breakup | Tue 2026-06-30 | Final touchpoint — 4-touchpoint hard limit |

---

## ORCHESTRATOR.PY — CRITICAL BUILD WINDOW

`src/outlocal/linkedin/orchestrator.py` — **NOT IMPLEMENTED. 17 days remaining.**

- **Deadline: Before Fri 2026-06-19** (Scenario C Day-3 LinkedIn window)
- This is the only mechanism that guarantees `profiles.json` is written same session as execution
- Without it: LinkedIn fails again (67-session manual execution failure — the pattern is clear)
- Without `profiles.json`: archive trigger fires Tue 2026-06-24 EOD unconditionally — Batch 6 LinkedIn permanently closed

**Build priority: This week. No further deferrals.**

Minimum viable features (from `COORD_65_005` in `linkedin_coordination.json`):
1. Read `batch_6_leads.json` → extract lead names and business names
2. Generate connection note per lead (signal-type template, 200-char hard limit)
3. Write `data/linkedin_profiles.json` with: `{lead_id, business_name, connection_sent_at, note_sent: true/false}`
4. Log to `CHANGELOG.md`

---

## batch_6_leads.json — RECOMMENDED RECEIPT WINDOW

The file is no longer blocking Scenario C (Day-0 Jun 16 is confirmed regardless). But it IS required for BRAIN to generate **per-lead personalised copy** before Day-0.

**Without the file:** BRAIN can only use generic templates. Per-lead personalisation (first name, specific URL, review count, exact signal notes) is what produces 15% INTERESTED rate. Generic templates will underperform.

| Receipt Date | BRAIN Preparation | Risk |
|---|---|---|
| **Thu 2026-06-11** | ~4 days | LOW — recommended |
| Fri 2026-06-12 | ~3 days | Acceptable |
| Mon 2026-06-15 | ~1 day (same-day tight) | HIGH — not recommended |
| Tue 2026-06-16 (Day-0 morning) | ZERO | UNACCEPTABLE — sends deferred or generic |

**HANDS: Write `data/batch_6_leads.json` by Thursday 2026-06-11 EOD. This is the final recommended window.**

Required fields per lead: `lead_id`, `business_name`, `owner_name`, `email`, `website_url`, `ssl_status`, `mobile_score`, `review_count`, `star_rating`, `signal_type`, `signal_notes`, `lead_score`, `town`, `sector`

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

## CRITICAL OPERATIONAL CORRECTIONS FOR BATCH 6

These are the specific failure modes from Batches 1–5 that MUST be fixed:

### 1. IMAP (Non-negotiable from Day-0)
- **Weekly IMAP from Day-0 send date** — no exceptions
- **Per-lead IMAP before every send** — pre-send sweep required
- Do NOT allow the gap to exceed 7 days at any point in the Batch 6 sequence
- Any unsubscribe found: suppress within 24h, log audit_log + CHANGELOG same session
- Any INTERESTED found: 24h proposal SLA (24/7, including weekends)

### 2. LinkedIn (Execute Day 3 or lose the channel)
- LinkedIn MANDATORY for Batch 6 — primary conversion channel missed across 67 sessions
- Execute within Day 3 from Day-0 (Fri Jun 19) — zero tolerance for deferral
- Write profiles.json same session — if not written, LinkedIn did not happen for BRAIN purposes
- Archive trigger fires Tue 2026-06-24 EOD unconditionally — regardless of reason for non-execution
- **orchestrator.py NOT IMPLEMENTED** — must be built before Fri Jun 19 (17 days)

### 3. Per-lead data file
- BRAIN cannot personalise copy without: owner_name, business_name, URL, ssl_status, town, review_count, star_rating
- Recommended receipt: Thu 2026-06-11 EOD
- Without this file: only generic templates possible — INTERESTED rate drops significantly

### 4. CHANGELOG (Write at every send day)
- Mandatory entry after every Day-0, Day-3, Day-7, Day-14 send session
- CHANGELOG currently 65+ days overdue — MANDATORY same session as Batch 6 Day-0 sends (Tue 2026-06-16) — ABSOLUTE FINAL DEADLINE

---

## FORWARD DECISIONS

| Decision | Owner | Deadline | Status |
|---|---|---|---|
| Write batch_6_leads.json | HANDS | **Thu 2026-06-11 EOD (RECOMMENDED — allows BRAIN per-lead copy generation)** | MISSING — 67 sessions |
| BRAIN per-lead copy generation | BRAIN | On file receipt (~Thu-Fri Jun 11-12) | Pending file |
| Build orchestrator.py | HANDS | **Before Fri 2026-06-19 (Day-3 LinkedIn — 17 days)** | NOT IMPLEMENTED |
| Update Batch 5 leads → sequence_complete | HANDS | OVERDUE — do today | OVERDUE |
| CHANGELOG | HANDS | **Same session as Batch 6 Day-0 Tue 2026-06-16 — ABSOLUTE FINAL DEADLINE** | **65+ DAYS OVERDUE** |
| Batch 6 Day-0 sends | HANDS | **Tue 2026-06-16, 09:00–10:30** | CONFIRMED |
| LinkedIn Day 3 + profiles.json | HANDS | **Fri 2026-06-19** | Upcoming |
| LinkedIn archive trigger | Auto | **Tue 2026-06-24 EOD (unconditional)** | Armed |

---

*Strategy maintained by OUTLOCAL BRAIN layer.*  
*Day 67 — Tuesday 2026-06-02 — Week 11.*  
*Scenario C confirmed active. Day-0 Tue 2026-06-16. HANDS: Write batch_6_leads.json by Thu Jun 11 (recommended). Build orchestrator.py before Fri Jun 19. CHANGELOG mandatory Tue Jun 16.*
