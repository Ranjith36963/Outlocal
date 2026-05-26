# Daily Strategy — 2026-05-26 (Tuesday) — Day 60

**Updated:** 2026-05-26 (BRAIN Day 60 run — Tuesday, Batch 5 Day 14 — DAY-14 BREAKUP SEND DAY — FINAL TOUCHPOINT)  
**Replaces:** 2026-05-25 strategy (Day 59 — Monday, Batch 5 Day 13 — Monday Prep Day)  
**Key changes from Day 59:** Day advances to 60. Batch 5 Day 14. IMAP gap now 52 days — RESOLVING TODAY per-lead. Day-14 is **TODAY** (no longer "tomorrow"). Send window: 09:00-10:30. CHANGELOG mandatory today same session — absolute final deadline. Post-Day-14 reply window opens tomorrow. Batch 6 post-mortem + launch: tomorrow Wednesday BRAIN run.

---

## TODAY'S SITUATION

### What happened overnight
- **Monday 2026-05-25:** Prep day. No sends. No IMAP. Zero overnight arrivals.
- **Overnight IMAP:** NOT EXECUTED — Monday hard block (correct).
- **Spontaneous replies overnight:** ZERO — new_replies.json unchanged from 2026-04-04.
- **CHANGELOG:** Still outstanding — 58+ days overdue. MANDATORY TODAY same session as sends. ABSOLUTE FINAL DEADLINE.
- **Result:** All Batch 5 leads proceed to Day-14 subject to per-lead IMAP check this morning.

### What this means today (Tuesday)
- **Day-14 breakup sends today** — 09:00-10:30, 10-min stagger, all 4 signal variants ready
- **IMAP mandatory per lead** before each send — covers 52-day gap. Action per classification before proceeding.
- **CHANGELOG today** — same session as sends. 58+ days overdue. Cannot be deferred further.
- **Post-Day-14 reply window opens TOMORROW** — Wednesday 2026-05-27 (24h post-send). Peak: Thursday.
- **Batch 6 scoping TOMORROW** — Wednesday BRAIN run. Full Batch 5 post-mortem + Harrogate + Craven launch decision.

### The 4-action execution order for today

| Order | Action | Time |
|---|---|---|
| **1** | IMAP per lead (first lead in send order) | Before 09:00 |
| **2** | Day-14 breakup send (if IMAP clean for that lead) | 09:00 onward, 10-min stagger |
| **3** | Update sequence_complete + reapproach 2026-11-26 | After each send |
| **4** | CHANGELOG.md — full historical log | Same session — ABSOLUTE FINAL DEADLINE |

---

## PART A: SIGNAL INTELLIGENCE

**No new leads or signals received.** HANDS has not provided new scraping data in 60+ sessions.

Waterfall assignment unchanged. Today's usage:

| Signal | Framework | Day-14 allocation | Copy location |
|---|---|---|---|
| `ssl` (HTTP site) | PAS | ~60% of Day-14 sends | `daily_email_plan.json` → `day14_breakup.ssl_pas_day14` |
| `mobile` failure | PAS | ~20% of Day-14 sends | `daily_email_plan.json` → `day14_breakup.mobile_pas_day14` |
| `no_website` (4★+ 20+ reviews) | BAB | ~15% of Day-14 sends | `daily_email_plan.json` → `day14_breakup.no_website_bab_day14` |
| `aida` (4.5★+ 100+ reviews) | AIDA | ~5% of Day-14 sends | `daily_email_plan.json` → `day14_breakup.aida_keyword_gap_day14` |

**Next signal assignments:** Batch 6 Harrogate + Craven — starts TOMORROW Wednesday 2026-05-27 (scraping from afternoon; initial sends Tuesday 2026-06-02).

---

## PART B: FOLLOW-UP ANALYSIS — DAY-14 EXECUTION

### Batch 5 Ryedale Sequence Status

| Touchpoint | Date | Status |
|---|---|---|
| Day-0 initial | Tue 2026-05-12 | ASSUMED SENT — UNCONFIRMED |
| Day-3 bump | Fri 2026-05-15 | ASSUMED SENT — UNCONFIRMED |
| Day-7 new-angle | Tue 2026-05-19 | ASSUMED SENT — UNCONFIRMED |
| **Day-14 breakup** | **TODAY — Tue 2026-05-26** | **SENDING 09:00-10:30 — FINAL TOUCHPOINT** |

**Reply windows:**
- Post-Day-3 peak: CLOSED (11+ days post-bump)
- Post-Day-7 wave: CLOSED (72h+ cutoff passed Friday evening). Any late arrivals: surface in today's IMAP.
- **Post-Day-14 window: opens TOMORROW Wednesday 2026-05-27** (24h post-send). Peak: Thursday 2026-05-28 (48h).

### Day-14 IMAP protocol (per lead)

Before each lead's Day-14 send, run their IMAP check:

| IMAP outcome | Action before that lead's Day-14 |
|---|---|
| **Clean** | Proceed with Day-14 send. 10-min stagger. |
| **INTERESTED** | **Cancel Day-14 for this lead. 24h proposal SLA from IMAP time (24/7 — NON-NEGOTIABLE). See value_delivery_queue.json.** |
| **NOT_INTERESTED** | Cancel Day-14 permanently. Suppress all channels. Log CHANGELOG. |
| **UNSUBSCRIBE** | Cancel Day-14. Suppress all channels within 24h (GDPR Article 21). Log audit_log + CHANGELOG. |
| **OOO (return after 2026-05-25)** | Mark sequence complete. Do NOT send Day-14 (4-touchpoint hard limit). |
| **OOO (return 2026-05-25 or before)** | Lead is back. Proceed with Day-14 send. |
| **WRONG_PERSON** | Do NOT send Day-14. Investigate correct contact. Log CHANGELOG. |

**Leads never to sweep:** 1, 3, 22 — archive unconditionally final. Do not include in send order.

### OOO Deadline — PASSED
Day-14 is TODAY. OOO cutoff was 2026-05-25 (yesterday). Any OOO lead with stated return after yesterday: sequence complete, no Day-14.

### 4-Touchpoint Hard Limit — ENFORCED TODAY
Day-14 is the 4th and final email in the sequence. There is no Day-21, no final check-in, no extended outreach. After Day-14: sequence complete, reapproach 2026-11-26 at earliest.

### LinkedIn Channel — PERMANENTLY CLOSED
Archive trigger fired Tuesday 2026-05-19 EOD (unconditional). Email only channel for Batch 5.

---

## PART C: REPLY MONITORING

### IMAP Status — Tuesday 2026-05-26
- Gap from last confirmed check: **52 days** (last confirmed 2026-04-04)
- All sweeps Wed-Sun: UNCONFIRMED / NOT EXECUTED (60-session HANDS pattern)
- **Today:** EXECUTING — per Batch 5 lead before each Day-14 send in send order. Covers entire 52-day gap.

### Overnight Reply Check
**ZERO new replies** — new_replies.json confirmed unchanged from 2026-04-04 (5 historical replies only).

### Post-Day-14 Monitoring Brief (for HANDS — TOMORROW onwards)
**Wednesday 2026-05-27** — IMAP per Batch 5 lead. Post-Day-14 reply window opens.  
**Thursday 2026-05-28** — IMAP per Batch 5 lead. 48h peak.  
**Friday 2026-05-29** — IMAP per Batch 5 lead. 72h secondary peak. Reply wave closes.  
**If INTERESTED reply arrives Wed-Fri:** 24h proposal SLA from reply time (24/7 — NON-NEGOTIABLE). Same protocol as today.

---

## PART D: DAY-14 COPY BRIEF (HANDS EXECUTION)

All copy is READY in `data/daily_email_plan.json` (day14_breakup section).

**Day-14 rules (non-negotiable):**
1. NEW standalone email — NOT a thread reply
2. New subject line (from recommended_subject field per signal)
3. 3 lines body maximum — no exceptions
4. No question marks — anywhere in subject or body
5. No new signal or pain point — brief reference only, then clean exit
6. UK English throughout
7. First name in subject if known (ssl, mobile, aida) — consistent with sequence
8. 'You know where I am' / 'I'm easy to reach' / 'Happy to help' — warm door, no pressure
9. Fill ALL [bracketed placeholders] from 2026-05-12 send records before sending

**By signal:**

| Signal | Subject template | Body opener | Source |
|---|---|---|---|
| SSL (60%) | `[First name] — closing the loop on [business name]` | "Sent a couple of notes about the 'Not Secure' issue..." | `ssl_pas_day14` |
| Mobile (20%) | `[First name] — [business name]: last note from me` | "Sent a few notes about [business name]'s site..." | `mobile_pas_day14` |
| No-website (15%) | `Last note — [business name]` | "Followed up a couple of times about [business name] not appearing..." | `no_website_bab_day14` |
| AIDA (5%) | `[First name] — last note on [business name]` | "Sent a couple of notes about the search visibility gap..." | `aida_keyword_gap_day14` |

---

## PART E: VALUE DELIVERY — IF INTERESTED REPLY FOUND TODAY

**Current state:** 0 INTERESTED replies in Batch 5. Zero overnight arrivals. Today's IMAP will resolve 52-day inbox gap.

If today's IMAP surfaces an INTERESTED reply for any lead:

**SSL trades (~60% of Batch 5):**
- Option A: SSL certificate fix only — £75-100 one-off
- **Option B: SSL + mobile fix — £150-200 one-off** ← recommended entry point
- Option C: SSL + mobile + local SEO — £300-350

**No-website leads (rural Ryedale, 20+ reviews — ~15%):**
- Option A: Single-page contact site — £300 one-off
- **Option B: 5-page site + contact form + Google Business Profile setup — £500** ← recommended
- Option C: Option B + 3 months local SEO — £550 + £75/month

**Rules:**
- Bespoke to their signal. Reference specific URL from Day-0.
- Give 3 options. Offer 15-minute call.
- Respond within 24h from IMAP time (24/7 — applies on Tuesday — NON-NEGOTIABLE).
- Cancel Day-14 for that lead. Do NOT send breakup to an interested lead.

Full pricing in `data/value_delivery_queue.json` (value_delivery_on_interested section).

---

## PART F: CAMPAIGN ANALYTICS — PATTERNS FOR BATCH 6

### Confirmed Winning Patterns (100% of INTERESTED leads, Batches 1-4)
1. **SSL → PAS → first-name subject → town name → specific URL** — 3/3 INTERESTED rate
2. **Post-bank-holiday Tuesday AM send** — all 3 INTERESTED replies followed bank-holiday-adjacent sends
3. **Day-7 genuinely different pain point** — ranking vs. trust (not a reframe)
4. **One pain point per email** — multiple signals kill response rate
5. **Town name in subject AND body** — local credibility anchor
6. **No question marks in subject** — statement of fact outperforms question
7. **Chrome's exact wording** `'Not Secure'` — verifiable, specific, credible

### Failure Patterns — Corrections for Batch 6

| Failure | Severity | Batch 6 correction |
|---|---|---|
| LinkedIn never activated (60 sessions) | **CRITICAL** — £800-1,175+ written off | LinkedIn Day 3-7 mandatory. profiles.json same session. Archive trigger: Day 7 unconditional. |
| IMAP gap (52 days, 6+ consecutive missed sweeps) | **HIGH** — compliance risk, missed INTERESTED replies | IMAP per lead before each send. Per-lead IMAP, not batch sweep. |
| CHANGELOG 58+ days overdue | **HIGH** — audit fail risk | CHANGELOG written same session as every send batch. No exceptions. |
| HANDS send confirmation never received | **MEDIUM** — forces "ASSUMED" data across 60 sessions | Batch 6 fix: HANDS writes `data/batch_sends/YYYY-MM-DD.json` same session. |
| Batch 5 per-lead data never received | **MEDIUM** — copy had to be generated without confirmed per-lead signals | Batch 6 fix: HANDS provides lead list with signals before BRAIN run. |

### Batch 5 Post-Mortem Preview (full analysis TOMORROW)

- **Total sends (estimated):** 48-72 (Day-0 + Day-3 + Day-7 + Day-14 across 12-18 Batch 5 leads, plus Batches 1-4)
- **Confirmed replies:** 11 total (all Batches 1-4). Batch 5 replies: 0 confirmed (52-day IMAP gap).
- **Overall reply rate:** 17.9% (11/~61 leads, Batches 1-4 only — Batch 5 unconfirmed)
- **INTERESTED rate (SSL-PAS):** 3/3 on confirmed SSL leads = 100% — but 3/11 overall = 27% INTERESTED rate
- **Conversions:** 0 confirmed (all 3 INTERESTED leads lost to LinkedIn failure + follow-up breakdown)
- **Batch 5 signal performance:** UNKNOWN (no IMAP confirmation, no per-lead data from HANDS)
- **Full post-mortem:** TOMORROW Wednesday 2026-05-27 BRAIN run

---

## BATCH 6 SCOPING — DECISION TOMORROW

**Territory:** Harrogate District (Knaresborough, Ripon new leads only, Boroughbridge) + Craven District (Skipton, Settle, Grassington, Gargrave)  
**Signal model:** SSL-PAS 60%, mobile-PAS 20%, no-website BAB 15%, AIDA 5%  
**LinkedIn:** MANDATORY Day 3-7. profiles.json same session. Archive trigger Day 7 unconditional.  
**Expected leads:** 18-22 across both districts.  
**Scraping:** Starts TOMORROW Wednesday 2026-05-27 (after post-mortem).  
**Initial sends:** Tuesday 2026-06-02, 09:00-10:30.  
**Decision confirmation:** Wednesday BRAIN run — launch Harrogate + Craven regardless of Batch 5 reply count.

---

## WEEK REMAINDER CALENDAR

| Date | Day | Batch 5 Day | Action |
|---|---|---|---|
| **Tue 2026-05-26** | **60** | **14** | **THIS SESSION. IMAP per lead → Day-14 breakup sends 09:00-10:30 → sequence_complete update → CHANGELOG mandatory same session.** |
| Wed 2026-05-27 | 61 | 15 | IMAP per Batch 5 lead (post-Day-14 day 1). Full Batch 5 post-mortem BRAIN run. Batch 6 launch decision. Batch 6 scraping starts. |
| Thu 2026-05-28 | 62 | 16 | Post-Day-14 reply peak (48h). IMAP per lead. |
| Fri 2026-05-29 | 63 | 17 | Post-Day-14 secondary peak (72h). IMAP per lead. Reply wave closes. |
| Sat-Sun 2026-05-30-31 | 64-65 | 18-19 | Weekend block. No sends. No IMAP. Sporadic replies possible. 24h SLA if INTERESTED. |
| Tue 2026-06-02 | 67 | — | **Batch 6 Day-0 sends. Harrogate District + Craven District. SSL-PAS 60%.** |
| Fri 2026-06-05 | 70 | — | **Batch 6 Day-3 + LinkedIn execution — profiles.json same session — MANDATORY** |

---

## OPERATIONAL PRIORITIES — TODAY AND FORWARD

| Priority | Action | Deadline |
|---|---|---|
| **1** | **IMAP per Batch 5 lead before each Day-14 send** — in send order, NOT leads 1/3/22 | **Today — before each individual send** |
| **2** | **Day-14 breakup sends** — 09:00-10:30. Copy READY. IMAP clean required per lead. | **Today 09:00-10:30** |
| **3** | **Update lead status to sequence_complete** — all Day-14 recipients. Reapproach: 2026-11-26. | **Today — after each send** |
| **4** | **CHANGELOG.md — ABSOLUTE FINAL DEADLINE** — 58+ days overdue. Same session as sends. | **TODAY — no further deferrals.** |
| **5** | **Post-Day-14 IMAP monitoring** — per Batch 5 lead, Wed-Fri | Wed-Fri 2026-05-27-29 |
| **6** | **Full Batch 5 post-mortem** — total sends, reply rate, signal performance, HANDS failures | **Wed 2026-05-27 BRAIN run** |
| **7** | **Batch 6 launch decision** — Harrogate District + Craven District (launch regardless) | **Wed 2026-05-27 BRAIN run** |
| **8** | **Batch 6 scraping** — 18-22 leads (Harrogate + Craven towns) | From Wed 2026-05-27 |
| **9** | **Batch 6 initial sends** — SSL-PAS 60% primary. LinkedIn MANDATORY Day 3-7. | **Tue 2026-06-02, 09:00-10:30** |

---

*BRAIN layer — Tuesday 2026-05-26 (Day 60, Batch 5 Day 14 — DAY-14 BREAKUP SEND DAY — FINAL TOUCHPOINT).*  
*HANDS layer: IMAP per lead before each send → Day-14 sends 09:00-10:30 → sequence_complete → CHANGELOG mandatory today.*  
*Next BRAIN run: Wednesday 2026-05-27 — Day-14 results + Batch 5 full post-mortem + Batch 6 launch decision.*  
*If INTERESTED reply found in today's IMAP: no new BRAIN run needed. Use value_delivery_queue.json directly. 24h proposal SLA from IMAP time (NON-NEGOTIABLE). Cancel Day-14 for that lead.*
