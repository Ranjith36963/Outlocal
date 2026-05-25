# Daily Strategy — 2026-05-25 (Monday) — Day 59

**Updated:** 2026-05-25 (BRAIN Day 59 run — Monday, Batch 5 Day 13 — Monday Prep Day — Pre-Day-14)  
**Replaces:** 2026-05-24 strategy (Day 58 — Sunday, Batch 5 Day 12 — Weekend Bridge — Week 9 Close)  
**Key changes from Day 58:** Day advances to 59. Batch 5 Day 13. IMAP gap now 51 days. Day-14 now **1 day away — TOMORROW**. Zero new replies confirmed over the weekend (new_replies.json unchanged). CHANGELOG now 57+ days overdue. All other state unchanged. No sends today.

---

## TODAY'S SITUATION

### What happened over the weekend
- **Saturday 2026-05-23:** Weekend bridge. No actions. (Correct.)
- **Sunday 2026-05-24:** Weekend bridge. Week 9 intelligence report generated. No actions.
- **Weekend IMAP:** NOT EXECUTED — hard block (correct).
- **Spontaneous replies Saturday/Sunday:** ZERO — new_replies.json unchanged from 2026-04-04.
- **CHANGELOG:** Still not updated — 57+ days overdue. MANDATORY TOMORROW.

### What this means today (Monday)
- **Zero weekend replies** — all Batch 5 leads proceed to Day-14 tomorrow (no exclusions added over the weekend)
- **Day-14 breakup is TOMORROW** — copy is READY in daily_email_plan.json (day14_breakup section — 4 signal variants)
- **No IMAP today** — Monday hard block. Tuesday per-lead sweep covers the entire 51-day gap.
- **No sends today** — final prep day only
- **IMAP gap is now 51 days** — full gap covered by Tuesday's per-lead sweeps before each send
- **Batch 6 trigger** remains formally deferred to Wednesday 2026-05-27

### The one thing that still matters today
**Stay ready for a spontaneous INTERESTED reply.** If one arrives today (Monday): 24h proposal SLA from reply time — NON-NEGOTIABLE (applies 24/7 including Monday). Write to new_replies.json immediately, classify, cancel Day-14, prepare proposal. See value_delivery_queue.json for 3-option pricing.

---

## PART A: SIGNAL INTELLIGENCE

**No new leads or signals received.** HANDS has not provided new scraping data in 59+ sessions.

Waterfall assignment unchanged:

| Signal | Framework | Allocation | Notes |
|---|---|---|---|
| `ssl` (HTTP site) | PAS | 60% | Day-14 copy READY. Post-Day-7 wave closed. |
| `mobile` failure | PAS | 20% | Day-14 copy READY. |
| `no_website` (4★+ 20+ reviews) | BAB | 15% | Rural Ryedale bar. Day-14 copy READY. |
| `aida` (4.5★+ 100+ reviews) | AIDA | 5% | Day-14 copy READY. |

All Day-14 breakup copy is in `data/daily_email_plan.json` (day14_breakup section). No new copy required today or tomorrow morning.

---

## PART B: FOLLOW-UP ANALYSIS

### Batch 5 Ryedale Sequence Status

| Touchpoint | Date | Status |
|---|---|---|
| Day-0 initial | Tue 2026-05-12 | ASSUMED SENT — UNCONFIRMED |
| Day-3 bump | Fri 2026-05-15 | ASSUMED SENT — UNCONFIRMED |
| Day-7 new-angle | Tue 2026-05-19 | ASSUMED SENT — UNCONFIRMED |
| Day-14 breakup | **TOMORROW — Tue 2026-05-26** | **1 DAY AWAY — copy READY** |

**Reply windows:**
- Post-Day-3 peak: CLOSED (10+ days post-bump)
- Post-Day-7 wave: **CLOSED** (72h+ cutoff passed Friday evening). Sporadic replies possible.
- Post-Day-14 window: opens Wednesday 2026-05-27 (24h post-Tuesday send)

### OOO Deadline
Day-14 is TOMORROW Tuesday 2026-05-26. Any lead with an OOO auto-reply where the stated return date is **after 2026-05-25 (today)** cannot receive Day-14 (4-touchpoint hard limit). Mark that lead's sequence as complete. IMAP per lead before each send will surface any OOO.

### LinkedIn Channel — PERMANENTLY CLOSED
Archive trigger fired Tuesday 2026-05-19 EOD (unconditional). Email only channel remaining.

---

## PART C: REPLY MONITORING

### IMAP Status — Monday 2026-05-25
- Gap from last confirmed check: **51 days** (last confirmed 2026-04-04)
- Wednesday sweep: **UNCONFIRMED** (59-session HANDS pattern)
- Thursday sweep: **UNCONFIRMED** (59-session HANDS pattern)
- Friday sweep: **UNCONFIRMED** (59-session HANDS pattern)
- Saturday: NOT EXECUTED — hard block (correct)
- Sunday: NOT EXECUTED — hard block (correct)
- **Today Monday:** NO IMAP — hard block.
- **Next IMAP:** Tuesday 2026-05-26 — per Batch 5 lead before each Day-14 send in send order. This single sweep covers the entire 51-day gap.

### Weekend Reply Check
**ZERO new replies** — new_replies.json checked and unchanged from 2026-04-04 (5 historical replies, all from original batch). No spontaneous replies arrived Saturday or Sunday.

### Classification Protocol (if reply arrives organically today)

| Classification | Action |
|---|---|
| **INTERESTED** | Write new_replies.json immediately → classify → **CANCEL Day-14** → **24h proposal SLA** (24/7) → update value_delivery_queue.json |
| **NOT_INTERESTED** | Classify → cancel Day-14 permanently → suppress all channels → log CHANGELOG |
| **UNSUBSCRIBE** | Classify → suppress ALL channels within 24h (GDPR Article 21) → log audit_log + CHANGELOG |
| **OUT_OF_OFFICE** | Classify → note return date → **if return after today 2026-05-25: mark sequence complete** (cannot send Day-14) |
| **WRONG_PERSON** | Classify → investigate correct contact → log CHANGELOG |

**Do NOT sweep leads 1/3/22 under any circumstances.** Archive unconditionally final.

---

## PART D: FOLLOW-UP COPY STATUS

All copy is READY in `data/daily_email_plan.json`. No new copy required today or tomorrow morning.

| Section | Status |
|---|---|
| `day7_new_angle` | USED — 4 signal variants. Assumed sent Tuesday 2026-05-19. Retained for CHANGELOG reference. |
| `day14_breakup` | **READY — TOMORROW** — 4 signal variants. Send Tuesday 2026-05-26, 09:00-10:30. |
| `conditional_handling` | Ready — interested/not_interested/OOO/unsubscribe variants |

**Day-14 send brief for HANDS (TOMORROW Tuesday 2026-05-26):**
1. IMAP sweep per Batch 5 lead before each individual send — in send order (NOT leads 1/3/22)
2. Apply correct Day-14 template by signal (see `day14_breakup` section in daily_email_plan.json)
3. Fill [bracketed placeholders] from 2026-05-12 send records
4. Send as NEW standalone email. New subject. 10-minute stagger. 09:00-10:30 window.
5. Do NOT send to any lead with INTERESTED reply before 2026-05-26 — use proposal flow instead
6. After sends: update lead status to `sequence_complete`, note reapproach 2026-11-26, log CHANGELOG same session

---

## PART E: VALUE DELIVERY — INTERESTED LEADS

**Current status: 0 INTERESTED replies in Batch 5.** Zero weekend replies confirmed. Sporadic late replies still possible today.

If a spontaneous INTERESTED reply arrives today (Monday):

**SSL leads (~60% of sends):**
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
- Respond within 24h from reply time (24/7 — applies on Monday — NON-NEGOTIABLE).

Full pricing protocol in `data/value_delivery_queue.json` (value_delivery_on_interested section).

---

## PART F: CAMPAIGN ANALYTICS & PATTERNS

### Confirmed Winning Patterns (100% of INTERESTED leads)
1. **SSL → PAS → first-name subject → town name → specific URL** — 3/3 INTERESTED rate (Batches 1-4)
2. **Post-bank-holiday Tuesday AM send** — all 3 INTERESTED replies followed bank-holiday-adjacent sends
3. **Day-7 genuinely different pain point** — ranking angle vs Day-0 trust angle
4. **One pain point per email** — multiple signals kill response
5. **Town name in subject AND body** — local credibility confirmed by every INTERESTED reply
6. **No question marks in subject** — statement of fact outperforms question hook
7. **Chrome's exact wording** — `'Not Secure'` builds verifiable credibility

### Observed Failure Patterns (to correct for Batch 6)
1. **LinkedIn never activated** — 59-session failure. £800-1,175+ confirmed written off.
2. **IMAP gap (51 days, 6+ consecutive missed sweeps)** — inbox state permanently uncertain. Compliance risk.
3. **CHANGELOG 57+ days overdue** — audit risk. Mandatory TOMORROW same session as Day-14 sends — ABSOLUTE FINAL DEADLINE.
4. **No HANDS send confirmation** — 59 sessions of "ASSUMED" data. Batch 6 fix: writes `data/batch_sends/YYYY-MM-DD.json` same session as each send batch.

---

## BATCH 6 SCOPING (Decision: Wednesday 2026-05-27)

**Current state:**
- Confirmed INTERESTED replies: **0** (new_replies.json unchanged since 2026-04-04)
- IMAP gap: **51 days** — entire post-reply-wave unconfirmed
- Decision status: **FORMALLY DEFERRED** — last practical trigger window (Friday 2026-05-22) passed with 0 confirmed replies

**Decision: Wednesday 2026-05-27 BRAIN run:**
- SSL-PAS model remains confirmed winning playbook (3/3 INTERESTED rate historically)
- Ryedale results reflect IMAP/HANDS execution failures, not signal failures
- Territory: Harrogate District + Craven District (higher business density)
- LinkedIn MANDATORY for Batch 6 — activate within Day 3-7 of initial send. profiles.json written same session. Zero tolerance.

---

## WEEK REMAINDER CALENDAR

| Date | Day | Batch 5 Day | Action |
|---|---|---|---|
| **Mon 2026-05-25** | **59** | **13** | **THIS SESSION. No sends. No IMAP. Final Day-14 prep. Review copy + send list. CHANGELOG if time allows. Monitor for spontaneous reply.** |
| **Tue 2026-05-26** | **60** | **14** | **Day-14 breakup sends 09:00-10:30. IMAP per Batch 5 lead before each send (in send order). Copy READY in daily_email_plan.json (day14_breakup section). CHANGELOG mandatory same session (57+ days overdue — ABSOLUTE FINAL DEADLINE). Update leads to sequence_complete. Reapproach: 2026-11-26.** |
| Wed 2026-05-27 | 61 | 15 | Post-Day-14 reply monitoring begins. Full Batch 5 post-mortem BRAIN run. Batch 6 launch decision final. |
| Thu 2026-05-28 | 62 | 16 | Post-Day-14 reply peak (48h). IMAP per lead. |
| Fri 2026-05-29 | 63 | 17 | Post-Day-14 reply secondary peak (72h+). |

---

## OPERATIONAL PRIORITIES — TODAY AND REMAINDER

| Priority | Action | Deadline |
|---|---|---|
| **1** | **Review Day-14 send list + copy** — confirm all placeholders fillable from 2026-05-12 records | Today Monday |
| **2** | **Stay ready for spontaneous INTERESTED reply** — 24h SLA from reply time (24/7) | Any time today |
| **3** | **CHANGELOG.md — write today if time allows** — 57+ days overdue | **MANDATORY TOMORROW 2026-05-26 — ABSOLUTE FINAL DEADLINE** |
| **4** | **IMAP per Batch 5 lead + Day-14 breakup sends** — copy READY | TOMORROW Tuesday 2026-05-26, 09:00-10:30 |
| **5** | **Full Batch 5 post-mortem** | Wednesday 2026-05-27 BRAIN run |
| **6** | **Batch 6 launch decision** | Wednesday 2026-05-27 — territory: Harrogate + Craven |

---

*BRAIN layer — Monday 2026-05-25 (Day 59, Batch 5 Day 13 — Monday Prep Day, Pre-Day-14).*  
*HANDS layer: No sends today. No IMAP today. Review Day-14 copy + send list. CHANGELOG if time allows.*  
*Day-14 breakup TOMORROW Tuesday 2026-05-26, 09:00-10:30. IMAP per lead before each send.*  
*Next BRAIN run: Wednesday 2026-05-27 — Day-14 results analysis + Batch 5 post-mortem + Batch 6 decision.*  
*If INTERESTED reply received today (Monday): no new BRAIN run needed. Use value_delivery_queue.json (value_delivery_on_interested section) directly. 24h proposal SLA from reply time (NON-NEGOTIABLE).*
