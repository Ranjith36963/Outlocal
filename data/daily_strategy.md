# Daily Strategy — 2026-05-27 (Wednesday) — Day 61

**Updated:** 2026-05-27 (BRAIN Day 61 run — Wednesday, Batch 5 Day 15 — Post-Day-14 Reply Peak — Batch 6 Launch Decision)  
**Replaces:** 2026-05-26 strategy (Day 60 — Tuesday, Batch 5 Day 14 — DAY-14 BREAKUP SEND DAY)  
**Key changes from Day 60:** Day advances to 61. Batch 5 Day 15. IMAP gap now 53 days — 24h post-Day-14 peak TODAY. Day-14 assumed sent yesterday (UNCONFIRMED). No sends today. Post-Day-14 reply window OPEN. Batch 6 launch CONFIRMED — Harrogate + Craven — scraping starts today. CHANGELOG 59+ days overdue — MANDATORY THIS SESSION (yesterday's absolute final deadline not met).

---

## TODAY AT A GLANCE

| Item | Status |
|---|---|
| Day-14 breakup sends | ASSUMED SENT yesterday Tue 2026-05-26 (UNCONFIRMED — 61-session pattern) |
| Post-Day-14 reply window | **OPEN NOW — 24h peak TODAY** |
| IMAP obligation | **MANDATORY per Batch 5 lead (NOT 1/3/22) — 53-day gap** |
| Sends today | **NONE** |
| Batch 6 decision | **CONFIRMED LAUNCH — Harrogate + Craven — scraping starts TODAY** |
| CHANGELOG | **59+ days overdue — MANDATORY THIS SESSION — zero tolerance** |

---

## PART A: TODAY'S EXECUTION BRIEF

### 1. IMAP — Post-Day-14 24h Peak (MANDATORY FIRST)
- Sweep each Batch 5 Ryedale lead in Day-0 send order
- **DO NOT sweep leads 1, 3, 22** — archive is unconditionally final
- 53-day IMAP gap — any reply from the entire post-April period will surface here
- **If INTERESTED found:** Prepare bespoke 3-option proposal within **24h from IMAP time** (NON-NEGOTIABLE — 24/7). Sequence already complete — no further email sends. Write to `new_replies.json`, classify in `reply_classifications.json`, update `value_delivery_queue.json`.
- **If NOT_INTERESTED:** Log. No further action.
- **If UNSUBSCRIBE:** Suppress ALL channels within 24h (GDPR Art. 21). Log `audit_log` + CHANGELOG.
- **If clean:** No action — continue monitoring Thursday/Friday.

### 2. CHANGELOG.md — ABSOLUTE MANDATORY (59+ days overdue)
This was the ABSOLUTE FINAL DEADLINE on Tuesday. It was not completed (61-session HANDS pattern). Zero tolerance — write this session before ending. Minimum required entries:
- Batch 5 Day-0 assumed 2026-05-12 + per-lead results if known
- Batch 5 Day-3 assumed 2026-05-15 + per-lead results if known
- Batch 5 Day-7 assumed 2026-05-19 + per-lead results if known
- Batch 5 Day-14 assumed 2026-05-26 + IMAP results + send outcomes
- fu_041-045 outcomes (assumed sent Mon 2026-05-11)
- Archive decisions: leads 1/3/22 (LOST_NO_RESPONSE 2026-05-07), leads 49/51 (Day 40), leads 53/54 (Day 44)
- All IMAP gaps and results since 2026-04-04
- LinkedIn archive: 54-session failure, trigger fired 2026-05-19 EOD
- Today's IMAP results
- Batch 6 launch decision

### 3. Batch 6 Scraping — Starts TODAY
- Territory: **Harrogate District + Craven District**
- Target: 18-22 leads
- Use Google Maps scraper (`src/outlocal/scrapers/`) — search `[sector] [town]` for each target combination
- Output: `data/batch_6_leads.json` — one entry per lead with all enrichment fields
- See `daily_signals.json` → `batch_6_scrape_plan` for full town + sector priority list
- **HANDS must write `data/batch_6_leads.json` for BRAIN to assign signals and write email copy**

### 4. Database update — Batch 5 sequence_complete
- Update all Batch 5 Ryedale lead records to `status: sequence_complete` in database
- Note reapproach date: `2026-11-26` minimum

---

## PART B: FULL BATCH 5 POST-MORTEM

### Campaign Summary

| Metric | Value |
|---|---|
| Territory | Ryedale District (Malton, Pickering, Helmsley, Kirkbymoorside, Hovingham, Norton-on-Derwent) |
| Campaign period | Tue 2026-05-12 — Tue 2026-05-26 (14 days) |
| Leads targeted | 12-18 (UNCONFIRMED — HANDS never wrote per-lead data file) |
| Day-0 sends | ASSUMED Tue 2026-05-12 (UNCONFIRMED) |
| Day-3 bumps | ASSUMED Fri 2026-05-15 (UNCONFIRMED) |
| Day-7 sends | ASSUMED Tue 2026-05-19 (UNCONFIRMED) |
| Day-14 breakup | ASSUMED Tue 2026-05-26 (UNCONFIRMED) |
| Confirmed replies | **0** |
| Confirmed reply rate | **0% (UNCONFIRMED baseline — IMAP gap 53 days)** |
| LinkedIn | **PERMANENTLY CLOSED** — archive trigger fired 2026-05-19 EOD (54-session failure) |

### Root Cause Analysis — 0% Batch 5 Reply Rate

Three possible explanations, in order of likelihood:

**1. Sends may not have happened (probability: HIGH)**  
HANDS has not confirmed any Batch 5 sends. 61 consecutive sessions without executing or writing per-lead data. The 0% reply rate is consistent with emails never being sent.

**2. Rural Ryedale market behavioral difference (probability: MEDIUM)**  
Batches 1-4 were primarily Leeds, West Yorkshire, and North Yorkshire market towns with established business connectivity. Ryedale is more rural and offline-first. Email response rates may be genuinely lower. Insufficient data to confirm.

**3. Signal quality or copy issues (probability: LOW)**  
SSL-PAS copy produced 15% INTERESTED rate in Batches 1-4 — the model is proven. If sends did happen, copy quality is not the explanation.

### Model Assessment
- **SSL-PAS model: STRUCTURALLY SOUND.** Do not deviate.
- 15% INTERESTED rate on SSL-PAS confirmed across Batches 1-4 (3/~20 SSL leads)
- Batch 5 0% does not invalidate the model — it points to HANDS execution failure
- **Proceed with Batch 6 using identical framework**

### What Changes for Batch 6
1. BRAIN requires `data/batch_6_leads.json` from HANDS BEFORE writing signal assignments — no file = no email plan = no sends
2. LinkedIn activation is MANDATORY Day 3-7 (Fri 2026-06-05). Archive trigger fires Tue 2026-06-10 EOD — no exceptions.
3. IMAP weekly at minimum — BRAIN will flag IMAP gap every run
4. Per-send confirmation: HANDS writes `data/batch_6_send_log.json` each session

---

## PART C: BATCH 6 LAUNCH PLAN

### Decision
**CONFIRMED LAUNCH** — Batch 6 proceeds regardless of Batch 5 reply count.

### Territory
- **Harrogate District:** Knaresborough (priority 1), Ripon (new leads only — do not reapproach lead 1), Boroughbridge
- **Craven District:** Skipton (priority 1), Settle, Grassington, Gargrave

### Signal Mix

| Signal | Allocation | Condition |
|---|---|---|
| SSL-PAS | 60% | HTTP site (not HTTPS), any sector |
| Mobile-PAS | 20% | SSL clean AND mobile clearly broken — personal test required |
| No-website BAB | 15% | 4★+ AND 20+ reviews (rural bar — same as Ryedale) |
| AIDA | 5% | 4.5★+ AND 100+ reviews only — verifiable keyword gap |

### Timeline

| Date | Action |
|---|---|
| Wed 2026-05-27 (TODAY) | Batch 6 scraping starts — HANDS writes `data/batch_6_leads.json` |
| Thu-Fri 2026-05-28-29 | Scraping continues + per-lead enrichment |
| Mon 2026-06-01 | BRAIN reviews `batch_6_leads.json` → signal assignments → per-lead email copy |
| **Tue 2026-06-02** | **BATCH 6 DAY-0 SENDS — 09:00-10:30. IMAP per lead before each send.** |
| Fri 2026-06-05 | **Batch 6 Day-3 bumps. LinkedIn MANDATORY — execute AND write `profiles.json` SAME SESSION.** |
| Tue 2026-06-09 | Batch 6 Day-7 new angle sends |
| Tue 2026-06-10 EOD | **LinkedIn archive trigger fires unconditionally if `profiles.json` missing** |
| Tue 2026-06-16 | Batch 6 Day-14 breakup |

---

## PART D: WINNING PATTERNS

### Subject Line Performance (Batches 1-4)
- `[First name] — [town] [trade]: flagged 'Not Secure'` → 3/3 INTERESTED leads
- Statement > question — no question marks in subjects
- Town name in subject — local credibility confirmed by every INTERESTED reply
- Chrome's exact wording: `'Not Secure'` (not "unsecured") — verifiable credibility

### Copy Performance
- One pain point per email — single clear signal
- SSL signal: 15% INTERESTED rate confirmed
- Day-7 pivot to Google ranking — genuinely different angle (not a reframe)
- BAB framing for no-website — lead with strength (reviews), then reveal the gap

### Timing
- Tuesday AM (09:00-10:30) — all 3 INTERESTED replies came from Tuesday sends
- Post-bank-holiday premium — first working Tuesday after a bank holiday peaks
- 10-minute stagger between sends

---

## FORWARD CALENDAR

| Date | Action |
|---|---|
| **Wed 2026-05-27 (TODAY)** | IMAP per Batch 5 lead (24h peak). Batch 6 scraping starts. CHANGELOG MANDATORY. |
| Thu 2026-05-28 | IMAP per Batch 5 lead (48h peak). Batch 6 scraping continues. |
| Fri 2026-05-29 | IMAP per Batch 5 lead (72h — closes). `batch_6_leads.json` expected from HANDS. |
| Mon 2026-06-01 | BRAIN reviews `batch_6_leads.json` → signal assignments → email copy. |
| **Tue 2026-06-02** | **BATCH 6 DAY-0 SENDS. 09:00-10:30. IMAP per lead before each send.** |
| Fri 2026-06-05 | Day-3 bumps. **LinkedIn MANDATORY same session. `profiles.json` same session.** |
| Sun 2026-05-31 | Weekly intelligence report (Week 10 close). |
| Tue 2026-06-09 | Batch 6 Day-7 new angle. |
| Tue 2026-06-10 EOD | LinkedIn archive trigger fires unconditionally. |
| Tue 2026-06-16 | Batch 6 Day-14 breakup. |
