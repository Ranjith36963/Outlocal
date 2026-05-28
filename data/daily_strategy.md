# Daily Strategy — 2026-05-28 (Thursday) — Day 62

**Updated:** 2026-05-28 (BRAIN Day 62 run — Thursday, Batch 5 Day 16 — Post-Day-14 48h Reply Peak)
**Replaces:** 2026-05-27 strategy (Day 61 — Wednesday, Batch 5 Day 15 — Post-Day-14 24h peak)
**Key changes from Day 61:** Day advances to 62. Batch 5 Day 16. IMAP gap now 54 days. 48h post-Day-14 peak TODAY (primary window). 72h FINAL sweep TOMORROW Friday — reply window closes Friday evening. batch_6_leads.json STILL MISSING (62-session HANDS pattern — was due Wednesday). CHANGELOG 60+ days overdue.

---

## TODAY AT A GLANCE

| Item | Status |
|---|---|
| Post-Day-14 reply window | **OPEN — 48h peak TODAY (primary window)** |
| IMAP obligation | **MANDATORY per Batch 5 lead (NOT 1/3/22) — 54-day gap** |
| Sends today | **NONE** |
| batch_6_leads.json | **MISSING — was due Wed 2026-05-27 — absolute deadline FRIDAY 2026-05-29** |
| CHANGELOG | **60+ days overdue — MANDATORY THIS SESSION** |
| Wednesday 24h IMAP | UNCONFIRMED (62-session pattern) — today's sweep covers full gap |

---

## PART A: TODAY'S EXECUTION BRIEF

### 1. IMAP — Post-Day-14 48h Peak (MANDATORY FIRST)
- Today is the **primary post-Day-14 reply peak** (48h from assumed Tuesday 2026-05-26 send)
- Wednesday 24h sweep assumed NOT executed — today's sweep covers the full 54-day gap
- Sweep each Batch 5 Ryedale lead in Day-0 send order (highest score first)
- **DO NOT sweep leads 1, 3, 22** — archive is unconditionally final
- **If INTERESTED found:** Prepare bespoke 3-option proposal within **24h from IMAP time** (NON-NEGOTIABLE — 24/7). Sequence complete — no further email sends. Write to `new_replies.json`, classify in `reply_classifications.json`, update `value_delivery_queue.json`. Log CHANGELOG same session.
- **If NOT_INTERESTED:** Log. No further action. Sequence complete.
- **If UNSUBSCRIBE:** Suppress ALL channels within 24h (GDPR Art. 21). Log `audit_log` + CHANGELOG.
- **If OOO:** Note return date. Sequence complete — no further emails.
- **If clean:** No action — FINAL sweep TOMORROW Friday (72h — reply window closes).

### 2. Batch 6 Scraping — batch_6_leads.json OVERDUE (absolute deadline Friday)
- Was due to start **Wednesday 2026-05-27** — assumed NOT started (62-session HANDS pattern)
- **Absolute deadline for batch_6_leads.json: FRIDAY 2026-05-29**
- If HANDS does not write batch_6_leads.json by Friday: BRAIN cannot assign signals. Batch 6 Day-0 sends (Tuesday 2026-06-02) will be at risk — only 3 days left for BRAIN review + copy on Monday.
- Territory: Harrogate District (Knaresborough, Ripon new leads, Boroughbridge) + Craven District (Skipton, Settle, Grassington, Gargrave)
- Target: 18-22 leads. See `daily_signals.json` → `batch_6_scrape_plan` for full sector + town list
- Use `src/outlocal/scrapers/` Google Maps scraper — output to `data/batch_6_leads.json`

### 3. CHANGELOG.md — 60+ DAYS OVERDUE
- Was the ABSOLUTE FINAL DEADLINE Tuesday 2026-05-26. Not completed.
- Not completed Wednesday. Now 60+ days.
- Zero further tolerance — mandatory this session before ending.

### 4. Database update — Batch 5 sequence_complete (if not already done)
- All Batch 5 Ryedale leads → `status: sequence_complete` in database
- Reapproach date: `2026-11-26` minimum

---

## PART B: POST-DAY-14 REPLY WINDOW STATUS

### Window Timeline

| Time | Date | Status |
|---|---|---|
| 24h peak | Wednesday 2026-05-27 | PASSED — IMAP sweep UNCONFIRMED |
| **48h peak** | **Thursday 2026-05-28 (TODAY)** | **PRIMARY ACTIVE WINDOW** |
| 72h peak | Friday 2026-05-29 | FINAL SWEEP — reply window closes Friday evening |
| Post-window | Saturday+ | No further IMAP required (Batch 5) |

### Why Wednesday Sweep Still Counts As Missed
- 62-session HANDS pattern: new_replies.json unchanged from 2026-04-04
- Wednesday IMAP sweep is assumed NOT executed
- Today's Thursday sweep covers the full 54-day gap plus any Wednesday-received replies
- This does not add risk — email timestamps allow retrospective classification regardless of sweep timing

### What Happens If a Reply Is Found Today
- **INTERESTED:** Prepare bespoke 3-option proposal within **24h from IMAP discovery time** (NON-NEGOTIABLE, 24/7). Sequence already complete (Day-14 assumed sent 2026-05-26). Write proposal email per `value_delivery_queue.json` template. Prepare Option 1/2/3 per signal type. Log CHANGELOG same session.
- **NOT_INTERESTED:** Log. No reapproach before 2026-11-26.
- **UNSUBSCRIBE:** Suppress all channels within 24h. GDPR Art. 21. Log audit_log + CHANGELOG.
- **OOO:** Note return date. No further email sends (4-touchpoint limit reached). Phone if number available and OOO return within 2 weeks.
- **Clean (no reply):** One more sweep Friday (72h) then window closes.

---

## PART C: BATCH 6 LAUNCH STATUS

### Critical Path — Days Remaining

| Date | Action | Risk if missed |
|---|---|---|
| **Thu 2026-05-28 (TODAY)** | HANDS writes batch_6_leads.json | BRAIN cannot review Friday — cuts Mon review time |
| **Fri 2026-05-29** | HANDS writes batch_6_leads.json (ABSOLUTE DEADLINE) | No file = no email copy = no sends Tue |
| **Mon 2026-06-01** | BRAIN reviews leads, assigns signals, writes email copy | Critical — Day-0 prep day |
| **Tue 2026-06-02** | **BATCH 6 DAY-0 SENDS — 18-22 leads, 09:00-10:30** | Slip = one week delay (next Tuesday) |
| **Fri 2026-06-05** | Day-3 bumps + LinkedIn MANDATORY | LinkedIn archive trigger Tue 2026-06-10 EOD |
| **Tue 2026-06-10 EOD** | LinkedIn archive trigger fires unconditionally | Repeating Batch 5 failure |

### Signal Mix (unchanged — confirmed winning playbook)
- **60% SSL-PAS** — HTTP sites, any sector. Town in subject. Chrome's 'Not Secure' wording.
- **20% Mobile-PAS** — SSL clean but mobile broken. Show you tested it.
- **15% No-website BAB** — 4★+ AND 20+ reviews. Reference Google Maps listing.
- **5% AIDA** — 4.5★+ AND 100+ reviews only. Verifiable keyword gap.

### Geography Notes for Batch 6 Scraping
- **Knaresborough priority 1** — older market town sites likely to have SSL failures. Trades and estate agents.
- **Skipton priority 1** — biggest Craven town, broadest sector mix.
- **Ripon: new leads ONLY** — do not reapproach lead 1 (Ripon Road Carpentry). That lead is permanently archived.
- **Grassington + Gargrave** — BAB angle strongest here (tourist/no-website businesses).
- **LinkedIn mandatory for all Batch 6 leads** — Fri 2026-06-05 (Day 3). profiles.json same session.

---

## PART D: WINNING PATTERNS (UNCHANGED)

### Subject Line Performance (Batches 1-4 confirmed)
- `[First name] — [town] [trade]: flagged 'Not Secure'` → 3/3 INTERESTED leads
- Statement > question — no question marks in subjects
- Town name in subject — local credibility confirmed by every INTERESTED reply
- Chrome's exact wording: `'Not Secure'` (not "unsecured") — verifiable credibility
- First name outperforms business name in subject (confirmed)

### Copy Performance
- **One pain point per email** — single clear signal. Multiple issues kill response.
- SSL signal: **15% INTERESTED rate** (confirmed Batches 1-4)
- Day-7 pivot must be a **genuinely different** pain point — reframes produce 0% responses
- BAB framing for no-website — lead with strength (reviews), then reveal the gap
- For trades: "customers search for you online before calling" framing

### Timing
- **Tuesday AM (09:00-10:30)** — all 3 INTERESTED replies came from Tuesday sends
- **Post-bank-holiday premium** — first working Tuesday after a bank holiday peaks
- **10-minute stagger** between sends
- No weekend or bank holiday sends — hard block

---

## FORWARD CALENDAR

| Date | Action |
|---|---|
| **Thu 2026-05-28 (TODAY)** | IMAP per Batch 5 lead (48h peak, NOT 1/3/22). batch_6_leads.json — HANDS scrape TODAY. CHANGELOG MANDATORY. |
| **Fri 2026-05-29** | IMAP per Batch 5 lead (72h FINAL — reply window CLOSES). batch_6_leads.json ABSOLUTE DEADLINE (HANDS). |
| Sat 2026-05-30 | No sends, no IMAP. Post-Day-14 window closed. Weekend bridge. |
| **Sun 2026-05-31** | **Weekly intelligence report — Week 10 close.** Batch 5 full close summary. Batch 6 scrape results. |
| **Mon 2026-06-01** | **BRAIN reviews batch_6_leads.json → signal assignments → per-lead email copy in daily_email_plan.json.** MANDATORY before Tuesday sends. |
| **Tue 2026-06-02** | **BATCH 6 DAY-0 SENDS. 09:00-10:30. IMAP per lead before each send.** 18-22 leads. SSL-PAS 60%. |
| Fri 2026-06-05 | **Day-3 bumps + LinkedIn MANDATORY same session. profiles.json same session. Archive trigger Tue 2026-06-10 EOD.** |
| Tue 2026-06-09 | Batch 6 Day-7 new angle. |
| **Tue 2026-06-10 EOD** | **LinkedIn archive trigger fires unconditionally if profiles.json missing.** |
| Tue 2026-06-16 | Batch 6 Day-14 breakup. |
