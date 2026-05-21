# Daily Strategy — 2026-05-21 (Thursday) — Day 55

**Updated:** 2026-05-21 (BRAIN Day 55 run — Thursday, Batch 5 Day 9 — Secondary Post-Day-7 Monitoring)  
**Replaces:** 2026-05-20 strategy (Day 54 — Wednesday, Batch 5 Day 8 — Post-Day-7 Monitoring)  
**Key changes from Day 54:** Day advances to 55. Batch 5 Day 9. Secondary post-Day-7 peak TODAY (48-72h post-send assumed Tuesday). Wednesday IMAP sweep UNCONFIRMED — 55-session HANDS execution pattern. IMAP gap now 47 days. CHANGELOG 53+ days overdue. Day-14 breakup: 5 days away (Tuesday 2026-05-26). Reply wave closes FRIDAY — this is the last monitoring day before the weekend.

---

## TODAY'S SITUATION

### What happened this week (assumed)
- **Tuesday 2026-05-19:** Day-7 new-angle sends assumed sent 09:00-10:30 (UNCONFIRMED — 55-session pattern)
- **Tuesday 2026-05-19 EOD:** LinkedIn archive trigger fired unconditionally — all Batch 5 Ryedale leads archived LOST_NO_RESPONSE on LinkedIn channel
- **Wednesday 2026-05-20:** IMAP sweep per Batch 5 lead — UNCONFIRMED (no new entries in new_replies.json)
- **CHANGELOG:** Still not updated — 53+ days overdue

### What this means today
- **Post-Day-7 secondary reply peak is RIGHT NOW** (48-72h post-send assumed Tuesday)
- Reply wave closes Friday 2026-05-22 — this is the penultimate monitoring window
- Email is the only remaining channel for all Batch 5 leads
- Day-14 breakup is 5 days away — final touchpoint
- If IMAP finds ≥ 2 INTERESTED: Batch 6 trigger fires today. If not: defer to post-mortem.

### The one thing that matters today
**IMAP per Batch 5 lead — do it now.** The reply wave closes tomorrow. 47-day IMAP gap means there may be replies sitting unread. If there is an INTERESTED reply: 24h proposal SLA from reply time (24/7 — non-negotiable).

---

## PART A: SIGNAL INTELLIGENCE

**No new leads or signals received.** HANDS has not provided new scraping data in 55+ sessions.

Waterfall assignment unchanged:

| Signal | Framework | Allocation | Notes |
|---|---|---|---|
| `ssl` (HTTP site) | PAS | 60% | SSL → Google ranking angle confirmed winning. Day-14 copy READY. |
| `mobile` failure | PAS | 20% | Day-7 pivot: SSL or click-to-call. Day-14 copy READY. |
| `no_website` (4★+ 20+ reviews) | BAB | 15% | Rural Ryedale bar (lowered from 50+). Day-14 copy READY. |
| `aida` (4.5★+ 100+ reviews) | AIDA | 5% | Keyword gap verifiable only. Day-14 copy READY. |

All Day-14 breakup copy is in `data/daily_email_plan.json` (day14_breakup section). No new copy required today.

---

## PART B: FOLLOW-UP ANALYSIS

### Batch 5 Ryedale Sequence Status

| Touchpoint | Date | Status |
|---|---|---|
| Day-0 initial | Tue 2026-05-12 | ASSUMED SENT — UNCONFIRMED |
| Day-3 bump | Fri 2026-05-15 | ASSUMED SENT — UNCONFIRMED |
| Day-7 new-angle | Tue 2026-05-19 | ASSUMED SENT — UNCONFIRMED |
| Day-14 breakup | **Tue 2026-05-26** | **5 DAYS AWAY — copy READY** |

**Reply windows:**
- Post-Day-3 peak: CLOSED (6+ days post-bump)
- Post-Day-7 wave: **SECONDARY PEAK TODAY** (48-72h post-send assumed Tuesday). Closes Friday.
- Post-Day-14 window: opens 2026-05-27

**Key fact:** The post-Day-7 reply wave is historically the strongest window for undecided leads. They had 7 days to sit on the Day-0 pain point; the Day-7 new angle (ranking impact) creates fresh urgency. If anyone is going to reply before Day-14, Thursday-Friday is the window.

### LinkedIn Channel — PERMANENTLY CLOSED

Archive trigger fired Tuesday 2026-05-19 EOD. All Batch 5 leads archived LOST_NO_RESPONSE on LinkedIn. Email only.

Second consecutive LinkedIn failure:
- Warm pipeline (leads 1/3/22): 49-session failure → archived 2026-05-08 → £800-1,175 written off
- Batch 5 Ryedale: 54-session failure → archived 2026-05-19 → pipeline value TBD

**Lesson for Batch 6 (MANDATORY before any future batch):** LinkedIn MUST activate within Day 3-7 of initial email send. Same-session execution. linkedin_profiles.json written immediately (one entry per lead — no batching). Archive trigger: Day 7 from initial send, fires unconditionally.

### Legacy Sequences
- fu_041-045 (leads 30/31/32/58/59): assumed complete 2026-05-11. Reapproach 2026-10-23.
- All Batch 1-4 sequences: complete. Reapproach dates tracked in active_strategy.md.

---

## PART C: REPLY MONITORING

### IMAP Status
- Gap from last confirmed check: **47 days** (last confirmed 2026-04-04)
- Wednesday sweep: **UNCONFIRMED** (55-session HANDS pattern — no new entries in new_replies.json)
- Thursday sweep: **MANDATORY NOW** — secondary post-Day-7 peak. Reply wave closes tomorrow.
- Zero Batch 5 replies confirmed in new_replies.json

### Classification Protocol (on any new reply)

| Classification | Action |
|---|---|
| **INTERESTED** | Write new_replies.json immediately → classify → **CANCEL Day-14** → **24h proposal SLA** (24/7) → update value_delivery_queue.json |
| **NOT_INTERESTED** | Classify → cancel Day-14 permanently → suppress all channels → log CHANGELOG |
| **UNSUBSCRIBE** | Classify → suppress ALL channels within 24h (GDPR Article 21) → log audit_log + CHANGELOG |
| **OUT_OF_OFFICE** | Classify → note return date → pause Day-14 if return after 2026-05-25 (4-touchpoint limit) |
| **WRONG_PERSON** | Classify → investigate correct contact → log CHANGELOG |

**Do NOT sweep leads 1/3/22 under any circumstances.** Archive unconditionally final.

### OOO deadline note
Day-14 is Tuesday 2026-05-26. Any lead returning from OOO AFTER 2026-05-25 cannot receive Day-14 (4-touchpoint hard limit). Mark their sequence as complete.

---

## PART D: FOLLOW-UP COPY STATUS

All copy is READY in `data/daily_email_plan.json`. No new copy required today or Friday.

| Section | Status |
|---|---|
| `day7_new_angle` | USED — 4 signal variants. Assumed sent Tuesday 2026-05-19. Retained for CHANGELOG reference. |
| `day14_breakup` | **READY** — 4 signal variants. Next send Tuesday 2026-05-26, 09:00-10:30. |
| `conditional_handling` | Ready — interested/not_interested/OOO/unsubscribe variants |

**Day-14 send brief for HANDS (Tuesday 2026-05-26):**
1. IMAP sweep per Batch 5 lead before each individual send — in send order (NOT leads 1/3/22)
2. Apply correct Day-14 template by signal (see `day14_breakup` section in daily_email_plan.json)
3. Fill [bracketed placeholders] from 2026-05-12 send records
4. Send as NEW standalone email. New subject. 10-minute stagger. 09:00-10:30 window.
5. Do NOT send to any lead with INTERESTED reply before 2026-05-26 — use proposal flow instead
6. After sends: update lead status to `sequence_complete`, note reapproach 2026-11-26, log CHANGELOG

---

## PART E: VALUE DELIVERY — INTERESTED LEADS

**Current status: 0 INTERESTED replies in Batch 5.**

If an INTERESTED reply arrives today (post-Day-7 secondary peak) or Friday:

**SSL leads (most likely signal — ~60% of sends):**
- Option A: SSL certificate fix only — £75-100 one-off
- **Option B: SSL + mobile fix — £150-200 one-off** ← recommended entry point
- Option C: SSL + mobile + local SEO (title tags, meta, Google Business Profile) — £300-350

**No-website leads (rural Ryedale, 20+ reviews — ~15% of sends):**
- Option A: Single-page contact site — £300 one-off
- **Option B: 5-page site + contact form + Google Business Profile setup — £500** ← recommended
- Option C: Option B + 3 months local SEO — £550 + £75/month

**Proposal rules:**
- Bespoke to their signal. Reference specific URL/issue from Day-0.
- Give 3 options. Offer 15-minute call.
- Respond within 24h from reply time (24/7 — non-negotiable). Tom (Ripon Road Carpentry) asked for pricing and never got it. That does not repeat.

Full pricing protocol in `data/value_delivery_queue.json` (value_delivery_on_interested section).

---

## PART F: CAMPAIGN ANALYTICS & PATTERNS

### Confirmed Winning Patterns (100% of INTERESTED leads)
1. **SSL → PAS → first-name subject → town name → specific URL** — 3/3 INTERESTED rate (Batches 1-4)
2. **Post-bank-holiday Tuesday AM send** — all 3 INTERESTED replies followed bank-holiday-adjacent sends
3. **Day-7 genuinely different pain point** — ranking angle vs Day-0 trust angle. Reframes produce 0% response.
4. **One pain point per email** — single clear signal. Multiple signals kill response.
5. **Town name in subject AND body** — local credibility confirmed by every INTERESTED reply
6. **No question marks in subject** — statement of fact outperforms question hook
7. **Chrome's exact wording** — `'Not Secure'` builds verifiable credibility

### Observed Failure Patterns (to correct for Batch 6)
1. **LinkedIn never activated** — 55-session failure. Two warm pipelines written off. £800-1,175 confirmed.
   - Root cause: No same-session execution mechanism. BRAIN writes plan; HANDS does not execute.
   - **Batch 6 fix:** LinkedIn Day 3-7 hard deadline. Same-session execution. profiles.json written immediately. Archive trigger Day 7, unconditional.
2. **IMAP gap (47 days)** — inbox state permanently uncertain. Compliance risk.
   - Fix: IMAP before every send, per lead. No bulk checking.
3. **CHANGELOG 53+ days overdue** — audit risk. Mandatory today.
4. **No HANDS send confirmation** — 55 sessions of "ASSUMED" data.
   - **Batch 6 fix:** HANDS writes `data/batch_sends/YYYY-MM-DD.json` same session as each send batch.

### Subject Line Performance (historical)
- **Best performing:** `[First name] — [town] [trade] site flagged 'Not Secure'` → 3/3 INTERESTED (SSL-PAS)
- **Key variable:** First name in subject is a confirmed material lift vs business-name-only subject line

---

## BATCH 6 SCOPING DECISION

**Current state:**
- Confirmed INTERESTED replies: **0** (new_replies.json unchanged since 2026-04-04)
- IMAP gap: **47 days** — there may be replies not yet captured
- Wednesday IMAP: UNCONFIRMED (HANDS pattern)
- Decision status: **PENDING IMAP confirmation — TODAY is the last practical trigger window**

**If trigger met (≥ 2 INTERESTED after today's IMAP):**
- Fire Batch 6 scoping immediately
- Territory: Harrogate District (Knaresborough, Ripon new leads only, Boroughbridge) + Craven District (Skipton, Settle, Grassington, Gargrave)
- Method: Google Maps → SSL check → score ≥ 55 → email finder → email plan
- Initial sends: Tuesday 2026-06-02 (Tuesday AM premium window)
- **LinkedIn MANDATORY:** Activate within Day 3-7 of initial send. Day 3 = Friday 2026-06-06 (ABSOLUTE DEADLINE — no deferrals, no extensions, no batching). Archive trigger: Tuesday 2026-06-09 (Day 7), fires unconditionally if profiles.json missing.

**If trigger NOT met (< 2 INTERESTED after today's IMAP):**
- No Batch 6 scraping until full Batch 5 post-mortem (Tuesday 2026-05-27)
- Review: was SSL-PAS the right signal for Ryedale? Were town/sector combinations optimal?
- Batch 6 geography confirmed (Harrogate + Craven) but start date deferred to after post-mortem

---

## OPERATIONAL PRIORITIES — WEEK 9 REMAINDER (Days 55-60)

| Priority | Action | Deadline |
|---|---|---|
| **1** | **IMAP sweep per Batch 5 lead** — secondary post-Day-7 peak | TODAY Thursday 2026-05-21 — reply wave closes TOMORROW |
| **2** | **Classify any new replies** — write new_replies.json, reply_classifications.json | Same session as IMAP |
| **3** | **24h proposal SLA** — if INTERESTED reply found | 24h from reply time (24/7) |
| **4** | **CHANGELOG.md** — 53+ days overdue | TODAY — same session as IMAP. Absolute final deadline. |
| **5** | **Batch 6 trigger decision** — after today's IMAP confirms reply count | TODAY — last practical trigger window |
| **6** | **Friday IMAP** — final pre-weekend check (72h+ post-Day-7) | Friday 2026-05-22 |
| **7** | **Day-14 breakup sends** — final touchpoint | Tuesday 2026-05-26, 09:00-10:30 |
| **8** | **Full Batch 5 post-mortem** | Tuesday 2026-05-27 BRAIN run |
| **9** | **Batch 6 launch prep** — if triggered today | From today if triggered |

---

*BRAIN layer — Thursday 2026-05-21 (Day 55, Batch 5 Day 9 — secondary post-Day-7 monitoring).*  
*HANDS layer must read this before any daily execution.*  
*Next BRAIN run: Tuesday 2026-05-26 morning — Day-14 results analysis + Batch 5 post-mortem + Batch 6 decision.*  
*If INTERESTED reply received today or Friday: no new BRAIN run needed. Use value_delivery_queue.json (value_delivery_on_interested section) directly. 24h proposal SLA from reply time.*
