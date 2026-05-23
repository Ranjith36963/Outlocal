# Daily Strategy — 2026-05-23 (Saturday) — Day 57

**Updated:** 2026-05-23 (BRAIN Day 57 run — Saturday, Batch 5 Day 11 — Weekend Bridge)  
**Replaces:** 2026-05-22 strategy (Day 56 — Friday, Batch 5 Day 10 — Final Pre-Weekend IMAP Check)  
**Key changes from Day 56:** Day advances to 57. Batch 5 Day 11. Post-Day-7 reply wave is NOW CLOSED (72h+ cutoff passed Friday evening). Friday IMAP sweep UNCONFIRMED — 57-session HANDS pattern. IMAP gap now 49 days. Batch 6 trigger FORMALLY DEFERRED to Wednesday 2026-05-27 post-mortem (0 confirmed replies, last window Friday passed). CHANGELOG 55+ days overdue. Day-14 breakup now 3 days away (Tuesday 2026-05-26). Weekend hard block — no sends, no IMAP today or Sunday.

---

## TODAY'S SITUATION

### What has happened this week (assumed)
- **Tuesday 2026-05-19:** Day-7 new-angle sends assumed sent 09:00-10:30 (UNCONFIRMED — 57-session pattern)
- **Tuesday 2026-05-19 EOD:** LinkedIn archive trigger fired unconditionally — all Batch 5 Ryedale leads archived LOST_NO_RESPONSE on LinkedIn channel
- **Wednesday 2026-05-20:** IMAP sweep per Batch 5 lead — UNCONFIRMED (no new entries in new_replies.json)
- **Thursday 2026-05-21:** Secondary post-Day-7 IMAP — UNCONFIRMED (no new entries in new_replies.json)
- **Friday 2026-05-22:** IMAP sweep — UNCONFIRMED (same HANDS pattern). Reply wave was at its 72h+ closing boundary.
- **CHANGELOG:** Still not updated — 55+ days overdue

### What this means today
- **Post-Day-7 reply wave is NOW CLOSED** — 72h+ cutoff passed Friday evening. The structured reply window for Day-7 sends is over.
- Remaining replies this weekend are late spontaneous responses — possible but declining in probability. Day-14 breakup Tuesday opens the next structured reply window.
- Email is the only remaining channel for all Batch 5 leads (LinkedIn permanently closed 2026-05-19 EOD)
- Day-14 breakup is 3 days away — copy is READY in daily_email_plan.json (day14_breakup section)
- Batch 6 trigger is formally deferred to Wednesday 2026-05-27 — cannot confirm reply count without IMAP, and last trigger window (Friday) has passed

### The one thing that matters this weekend
**Stay ready for a spontaneous INTERESTED reply.** If one arrives (Saturday or Sunday): 24h proposal SLA from reply time — NON-NEGOTIABLE. Write to new_replies.json immediately, classify, cancel Day-14, prepare proposal. See value_delivery_queue.json for 3-option pricing.

---

## PART A: SIGNAL INTELLIGENCE

**No new leads or signals received.** HANDS has not provided new scraping data in 57+ sessions.

Waterfall assignment unchanged:

| Signal | Framework | Allocation | Notes |
|---|---|---|---|
| `ssl` (HTTP site) | PAS | 60% | Day-14 copy READY. Post-Day-7 wave closed. |
| `mobile` failure | PAS | 20% | Day-14 copy READY. |
| `no_website` (4★+ 20+ reviews) | BAB | 15% | Rural Ryedale bar (lowered from 50+). Day-14 copy READY. |
| `aida` (4.5★+ 100+ reviews) | AIDA | 5% | Day-14 copy READY. |

All Day-14 breakup copy is in `data/daily_email_plan.json` (day14_breakup section). No new copy required today, Sunday, or Monday.

---

## PART B: FOLLOW-UP ANALYSIS

### Batch 5 Ryedale Sequence Status

| Touchpoint | Date | Status |
|---|---|---|
| Day-0 initial | Tue 2026-05-12 | ASSUMED SENT — UNCONFIRMED |
| Day-3 bump | Fri 2026-05-15 | ASSUMED SENT — UNCONFIRMED |
| Day-7 new-angle | Tue 2026-05-19 | ASSUMED SENT — UNCONFIRMED |
| Day-14 breakup | **Tue 2026-05-26** | **3 DAYS AWAY — copy READY** |

**Reply windows:**
- Post-Day-3 peak: CLOSED (8+ days post-bump)
- Post-Day-7 wave: **NOW CLOSED** (72h+ cutoff passed Friday evening). Sporadic replies possible.
- Post-Day-14 window: opens Wednesday 2026-05-27 (24h post-Tuesday send)

### OOO Deadline
Day-14 is Tuesday 2026-05-26. Any lead with an OOO auto-reply where the stated return date is **after 2026-05-25** cannot receive Day-14 (4-touchpoint hard limit). Mark that lead's sequence as complete.

### LinkedIn Channel — PERMANENTLY CLOSED

Archive trigger fired Tuesday 2026-05-19 EOD (unconditional). Email only channel remaining.

---

## PART C: REPLY MONITORING

### IMAP Status — Saturday 2026-05-23
- Gap from last confirmed check: **49 days** (last confirmed 2026-04-04)
- Wednesday sweep: **UNCONFIRMED** (57-session HANDS pattern)
- Thursday sweep: **UNCONFIRMED** (57-session HANDS pattern)
- Friday sweep: **UNCONFIRMED** (57-session HANDS pattern)
- **Today Saturday:** NO IMAP — hard block.
- **Next IMAP:** Tuesday 2026-05-26 — per Batch 5 lead before each Day-14 send in send order. This single sweep covers the entire 49-day gap.

### Classification Protocol (if reply arrives organically this weekend)

| Classification | Action |
|---|---|
| **INTERESTED** | Write new_replies.json immediately → classify → **CANCEL Day-14** → **24h proposal SLA** (24/7 — applies over weekend) → update value_delivery_queue.json |
| **NOT_INTERESTED** | Classify → cancel Day-14 permanently → suppress all channels → log CHANGELOG |
| **UNSUBSCRIBE** | Classify → suppress ALL channels within 24h (GDPR Article 21) → log audit_log + CHANGELOG |
| **OUT_OF_OFFICE** | Classify → note return date → **if return after 2026-05-25: mark sequence complete** (cannot send Day-14) |
| **WRONG_PERSON** | Classify → investigate correct contact → log CHANGELOG |

**Do NOT sweep leads 1/3/22 under any circumstances.** Archive unconditionally final.

---

## PART D: FOLLOW-UP COPY STATUS

All copy is READY in `data/daily_email_plan.json`. No new copy required today, Sunday, or Monday.

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
7. Full Batch 5 post-mortem: total sends, reply rate, INTERESTED count, conversion, signal performance

---

## PART E: VALUE DELIVERY — INTERESTED LEADS

**Current status: 0 INTERESTED replies in Batch 5.** Post-Day-7 wave is NOW CLOSED. Sporadic late replies possible over the weekend.

If a spontaneous INTERESTED reply arrives this weekend:

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
- Respond within 24h from reply time (24/7 — applies over weekend — NON-NEGOTIABLE).

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
1. **LinkedIn never activated** — 57-session failure. Two warm pipelines and Batch 5 LinkedIn channel written off. £800-1,175 confirmed.
2. **IMAP gap (49 days, 4+ consecutive missed sweeps)** — inbox state permanently uncertain. Compliance risk.
3. **CHANGELOG 55+ days overdue** — audit risk. Mandatory Tuesday same session as Day-14.
4. **No HANDS send confirmation** — 57 sessions of "ASSUMED" data. Batch 6 fix: writes `data/batch_sends/YYYY-MM-DD.json` same session as each send batch.

### Subject Line Performance (historical)
- **Best performing:** `[First name] — [town] [trade] site flagged 'Not Secure'` → 3/3 INTERESTED (SSL-PAS)
- **Key variable:** First name in subject is a confirmed material lift

---

## BATCH 6 SCOPING DECISION

**Current state:**
- Confirmed INTERESTED replies: **0** (new_replies.json unchanged since 2026-04-04)
- IMAP gap: **49 days** — Wednesday, Thursday, Friday sweeps all UNCONFIRMED
- Decision status: **FORMALLY DEFERRED** — last practical trigger window (Friday 2026-05-22) has passed with 0 confirmed replies and UNCONFIRMED IMAP

**Deferred to Wednesday 2026-05-27 BRAIN run (Batch 5 post-mortem):**
- Review signal mix: was SSL-PAS viable for Ryedale rural businesses at Batch 5 volumes?
- Were Ryedale town/sector combinations optimal?
- Was the 20-review bar for no-website leads correct for the rural economy?
- Confirm Batch 6 geography (Harrogate District + Craven District)
- Set Batch 6 initial send date (expected: Tuesday 2026-06-02 or Tuesday 2026-06-09)
- **LinkedIn MANDATORY for Batch 6:** Activate within Day 3-7 of initial send. Archive trigger: Day 7 fires unconditionally if profiles.json missing. Zero tolerance for the 57-session failure pattern.

**Expected Batch 6 outcome even with 0 Batch 5 INTERESTED:**
- SSL-PAS model remains the confirmed winning playbook (3/3 INTERESTED rate historically)
- Ryedale results reflect IMAP/HANDS execution failures, not signal failures
- Batch 6 should proceed with same signal priority order — SSL first, same PAS framework
- Harrogate District has higher business density and more digital-first competition — expect higher response rates than rural Ryedale

---

## WEEK REMAINDER CALENDAR

| Date | Day | Batch 5 Day | Action |
|---|---|---|---|
| **Sat 2026-05-23** | **57** | **11** | **THIS SESSION. Weekend bridge. No sends. No IMAP. Post-Day-7 wave NOW CLOSED. Day-14: 3 days away.** |
| Sun 2026-05-24 | 58 | 12 | No sends. No IMAP. Weekend block. Day-14: 2 days away. |
| Mon 2026-05-25 | 59 | 13 | No sends today. Final Day-14 prep. Review copy + confirm send list from 2026-05-12 records. No IMAP (Tuesday sweep covers it). CHANGELOG overdue — write today if possible, mandatory Tuesday. |
| **Tue 2026-05-26** | **60** | **14** | **Day-14 breakup sends 09:00-10:30. IMAP per Batch 5 lead before each send (in send order). Copy READY in daily_email_plan.json (day14_breakup section). CHANGELOG mandatory same session. Update leads to sequence_complete. Note reapproach 2026-11-26.** |
| Wed 2026-05-27 | 61 | 15 | Post-Day-14 reply monitoring begins (24h post-send). Full Batch 5 post-mortem BRAIN run. Batch 6 launch decision final. Total campaign assessment. |

---

## OPERATIONAL PRIORITIES — TODAY AND REMAINDER

| Priority | Action | Deadline |
|---|---|---|
| **1** | **Stay ready for spontaneous INTERESTED reply** — 24h SLA from reply time (24/7) | Any time — applies over weekend |
| **2** | **Day-14 breakup sends** — IMAP per lead before each, copy READY | Tuesday 2026-05-26, 09:00-10:30 |
| **3** | **CHANGELOG.md** — 55+ days overdue | Tuesday 2026-05-26 same session as Day-14 sends. Absolute final deadline. |
| **4** | **Full Batch 5 post-mortem** | Wednesday 2026-05-27 BRAIN run |
| **5** | **Batch 6 launch decision** | Wednesday 2026-05-27 — territory: Harrogate + Craven |

---

*BRAIN layer — Saturday 2026-05-23 (Day 57, Batch 5 Day 11 — Weekend Bridge).*  
*HANDS layer: no actions required today or Sunday. Day-14 sends Tuesday 2026-05-26.*  
*Next BRAIN run: Wednesday 2026-05-27 — Day-14 results analysis + Batch 5 post-mortem + Batch 6 decision.*  
*If INTERESTED reply received Saturday or Sunday: no new BRAIN run needed. Use value_delivery_queue.json (value_delivery_on_interested section) directly. 24h proposal SLA from reply time.*
