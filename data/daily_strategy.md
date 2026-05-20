# Daily Strategy — 2026-05-20 (Wednesday) — Day 54

**Updated:** 2026-05-20 (BRAIN Day 54 run — Wednesday, Batch 5 Day 8 — Post-Day-7 Monitoring)  
**Replaces:** 2026-05-19 strategy (Day 53 — Tuesday, Batch 5 Day 7 Send Day)  
**Key changes from Day 53:** Day advances to 54. Batch 5 Day 8. No sends today — monitoring only. LinkedIn archive trigger ASSUMED FIRED yesterday EOD (unconditional). LinkedIn channel PERMANENTLY CLOSED for all Batch 5 leads. Post-Day-7 reply wave OPEN NOW (peak TODAY 24-48h). IMAP mandatory TODAY. Day-14 breakup: Tuesday 2026-05-26 (6 days, copy READY).

---

## TODAY'S SITUATION

### What happened Tuesday (assumed)
- Day-7 new-angle sends assumed sent Tuesday 2026-05-19, 09:00-10:30 (UNCONFIRMED — 54-session pattern)
- LinkedIn archive trigger fired Tuesday 2026-05-19 EOD **unconditionally** — linkedin_profiles.json was never written (54-session failure)
- All Batch 5 Ryedale leads are now archived LOST_NO_RESPONSE on the LinkedIn channel effective Tuesday EOD
- IMAP per-lead sweep: UNCONFIRMED (no new entries in new_replies.json)
- CHANGELOG: still not updated (52+ days overdue)

### What this means today
- **Email is the only remaining channel for Batch 5**
- Post-Day-7 reply wave is OPEN — peak is RIGHT NOW (24-48h post-send)
- Day-14 breakup is the final touchpoint (Tuesday 2026-05-26)
- Batch 6 trigger cannot fire until IMAP confirms replies ≥ 2

---

## PART A: SIGNAL INTELLIGENCE

**No new leads or signals received.** HANDS has not provided new scraping data in 54+ sessions.

Waterfall assignment unchanged:

| Signal | Framework | Allocation | Rules |
|---|---|---|---|
| `ssl` (HTTP site) | PAS | 60% | SSL → Google ranking angle confirmed winning |
| `mobile` failure | PAS | 20% | Day-7 pivot: SSL or click-to-call |
| `no_website` (4★+ 20+ reviews) | BAB | 15% | Rural Ryedale bar (lowered from 50+) |
| `aida` (4.5★+ 100+ reviews) | AIDA | 5% | Keyword gap verifiable only |

---

## PART B: FOLLOW-UP ANALYSIS

### Batch 5 Ryedale Sequence Status

| Touchpoint | Date | Status |
|---|---|---|
| Day-0 initial | Tue 2026-05-12 | ASSUMED SENT — UNCONFIRMED |
| Day-3 bump | Fri 2026-05-15 | ASSUMED SENT — UNCONFIRMED |
| Day-7 new-angle | Tue 2026-05-19 | ASSUMED SENT — UNCONFIRMED |
| Day-14 breakup | **Tue 2026-05-26** | **UPCOMING — copy READY** |

**Reply windows:**
- Post-Day-3 peak: CLOSED (5+ days post-bump)
- Post-Day-7 wave: **OPEN NOW** — peak TODAY Wednesday (24-48h) and Thursday (48-72h)
- Post-Day-14 window: opens 2026-05-27

### LinkedIn Channel — PERMANENTLY CLOSED

The LinkedIn archive trigger fired Tuesday 2026-05-19 EOD, matching the outcome of the warm pipeline failure (leads 1/3/22 — £800-1,175 written off). This is the **second consecutive LinkedIn failure**:

- Warm pipeline: 49-session failure → archive 2026-05-08 EOD → £800-1,175 written off
- Batch 5 Ryedale: 54-session failure → archive 2026-05-19 EOD → pipeline value TBD

**Email is the only remaining channel for all active leads.**

### Legacy Sequences
- fu_041-045 (leads 30/31/32/58/59): assumed complete 2026-05-11. Reapproach 2026-10-23.
- All Batch 1-4 sequences: complete. Reapproach dates tracked in active_strategy.md.

---

## PART C: REPLY MONITORING

### IMAP Status
- Gap from last confirmed check: **46 days** (last confirmed 2026-04-04)
- Post-Day-7 reply wave: **OPEN — peak TODAY**
- Zero Batch 5 replies confirmed in new_replies.json

### Classification Protocol (on any new reply)

| Classification | Action |
|---|---|
| **INTERESTED** | Write new_replies.json immediately → classify → cancel Day-14 → **24h proposal SLA** (24/7) → update value_delivery_queue.json |
| **NOT_INTERESTED** | Classify → cancel Day-14 permanently → suppress all channels → log CHANGELOG |
| **UNSUBSCRIBE** | Classify → suppress ALL channels within 24h (GDPR Article 21) → log audit_log + CHANGELOG |
| **OUT_OF_OFFICE** | Classify → note return date → pause Day-14 (must return before 2026-05-25) |
| **WRONG_PERSON** | Classify → investigate correct contact → log CHANGELOG |

**Do NOT sweep leads 1/3/22 under any circumstances.** Archive unconditionally final.

---

## PART D: FOLLOW-UP COPY STATUS

All copy is READY in `data/daily_email_plan.json`. No new copy required today.

| Section | Status |
|---|---|
| `day7_new_angle` | USED — 4 signal variants. Assumed sent Tuesday 2026-05-19. Retained for CHANGELOG reference. |
| `day14_breakup` | **READY** — 4 signal variants. Next send Tuesday 2026-05-26. |
| `conditional_handling` | Ready — interested/not_interested/OOO/unsubscribe variants |

**Day-14 send brief for HANDS (Tuesday 2026-05-26):**
1. IMAP sweep per Batch 5 lead (NOT leads 1/3/22) before each individual send — in send order
2. Apply correct Day-14 template by signal (see `day14_breakup` section in daily_email_plan.json)
3. Fill [bracketed placeholders] from 2026-05-12 send records
4. Send as NEW standalone email. New subject. 10-minute stagger. 09:00-10:30 window.
5. Do NOT send to any lead with INTERESTED reply before 2026-05-26 — use proposal flow instead
6. After sends: update lead status to `sequence_complete`, note reapproach 2026-11-26, log CHANGELOG

---

## PART E: VALUE DELIVERY — INTERESTED LEADS

**Current status: 0 INTERESTED replies in Batch 5.**

If an INTERESTED reply arrives today (post-Day-7 wave peak):

**SSL leads (most likely signal):**
- Option A: SSL only — £75-100
- **Option B: SSL + mobile — £150-200** ← recommended entry point
- Option C: SSL + mobile + local SEO — £300-350

**No-website leads (rural Ryedale, 20+ reviews):**
- Option A: Single-page site — £300
- **Option B: 5-page site + contact form + Google Business Profile — £500** ← recommended
- Option C: Option B + 3 months local SEO — £550 + £75/month

**Proposal rules:** Bespoke to their signal. Reference their specific URL/issue from Day-0. Give 3 options. Offer 15-minute call. Respond within 24h from reply time (24/7 — non-negotiable).

---

## PART F: CAMPAIGN ANALYTICS & PATTERNS

### Confirmed Winning Patterns (100% of INTERESTED leads)
1. **SSL → PAS → first-name subject → town name → specific URL** — 3/3 INTERESTED rate (Batches 1-4)
2. **Post-bank-holiday Tuesday AM send** — all 3 INTERESTED replies followed bank-holiday-adjacent sends
3. **Day-7 genuinely different pain point** — ranking angle vs Day-0 trust angle
4. **One pain point per email** — single clear signal. Multiple signals = 0% response
5. **Town name in subject AND body** — local credibility confirmed by every INTERESTED reply
6. **No question marks in subject** — statement of fact outperforms question hook
7. **Chrome's exact wording** — `'Not Secure'` builds verifiable credibility

### Observed Failure Patterns (to correct for Batch 6)
1. **LinkedIn never activated** — 54-session failure. Two warm pipelines written off. £800-1,175 confirmed.
   - **Root cause:** No same-session execution mechanism. BRAIN writes plan; HANDS does not execute.
   - **Batch 6 fix required:** LinkedIn must be executed within Day 3-7 of initial send, same session. profiles.json written immediately after each search — one entry per lead, no batching.
2. **IMAP gap (46 days)** — inbox state permanently uncertain. Compliance risk (GDPR Article 21).
   - **Fix:** IMAP before every send, no exceptions. Per-lead, not bulk.
3. **CHANGELOG 52+ days overdue** — audit risk.
4. **No HANDS send confirmation** — 54 sessions of "ASSUMED" data. BRAIN cannot assess performance.
   - **Fix for Batch 6:** HANDS must write `data/batch_sends/YYYY-MM-DD.json` same session as each send batch. Machine-readable: lead_id, business_name, signal, timestamp, subject_used.

### Subject Line Performance (historical)
- **Best performing:** `[First name] — [town] [trade] site flagged 'Not Secure'` → 3/3 INTERESTED (SSL-PAS)
- **Second best:** `[First name] — [business name] flagged 'Not Secure'` → similar structure
- **Key variable:** First name in subject is confirmed as a material lift vs business-name-only subject

---

## BATCH 6 SCOPING DECISION

**Trigger condition:** Batch 5 INTERESTED replies ≥ 2 by Wednesday 2026-05-20 (TODAY).

**Current state:**
- Confirmed INTERESTED replies: **0** (new_replies.json unchanged since 2026-04-04)
- IMAP gap: **46 days** — there may be replies not yet captured
- Decision status: **PENDING IMAP confirmation**

**If trigger met (≥ 2 INTERESTED after IMAP today):**
- Fire Batch 6 scoping immediately
- Territory: Harrogate District (Knaresborough, Ripon new leads only, Boroughbridge) + Craven District (Skipton, Settle, Grassington, Gargrave)
- Method: Google Maps → SSL check → score → email finder → email plan
- Initial sends: Tuesday 2026-06-02 (Tuesday AM premium window)
- LinkedIn: must activate within Day 3-7 — Day 3 = Friday 2026-06-06 (ABSOLUTE DEADLINE, no deferrals)

**If trigger NOT met (< 2 INTERESTED after IMAP today):**
- Review signal mix before expanding
- No Batch 6 scraping until full Batch 5 post-mortem complete (after Day-14, Tuesday 2026-05-26)
- Evaluate: was SSL-PAS signal the right choice for Ryedale? Were town/sector combinations correct?
- Decision: Batch 6 geography confirmed but start date deferred to after post-mortem

---

## OPERATIONAL PRIORITIES — WEEK 9 REMAINDER (Days 54-60)

| Priority | Action | Deadline |
|---|---|---|
| **1** | **IMAP sweep per Batch 5 lead** — post-Day-7 reply wave peak | TODAY Wednesday 2026-05-20 |
| **2** | **Classify any new replies** — write new_replies.json, classify reply_classifications.json | Same session as IMAP |
| **3** | **24h proposal SLA** — if INTERESTED reply found | 24h from reply time (24/7) |
| **4** | **Batch 6 trigger decision** — after IMAP confirms reply count | TODAY if IMAP ≥ 2 INTERESTED |
| **5** | **CHANGELOG.md** — 52+ days overdue | TODAY — same session as IMAP |
| **6** | **Thursday IMAP** — secondary reply peak (48-72h post-Day-7) | Thursday 2026-05-21 |
| **7** | **Day-14 breakup sends** — final touchpoint | Tuesday 2026-05-26, 09:00-10:30 |
| **8** | **Full Batch 5 post-mortem** | Tuesday 2026-05-27 BRAIN run |
| **9** | **Batch 6 launch prep** — if triggered | From Wednesday 2026-05-21 if triggered |

---

*BRAIN layer — Wednesday 2026-05-20 (Day 54). HANDS layer must read this before any daily execution.*  
*Next BRAIN run: Tuesday 2026-05-26 morning — Day-14 results analysis + Batch 5 post-mortem + Batch 6 decision.*  
*Or: Thursday 2026-05-21 if INTERESTED replies received today requiring proposal review.*
