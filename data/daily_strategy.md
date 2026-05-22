# Daily Strategy — 2026-05-22 (Friday) — Day 56

**Updated:** 2026-05-22 (BRAIN Day 56 run — Friday, Batch 5 Day 10 — Final Pre-Weekend IMAP Check)  
**Replaces:** 2026-05-21 strategy (Day 55 — Thursday, Batch 5 Day 9 — Secondary Post-Day-7 Monitoring)  
**Key changes from Day 55:** Day advances to 56. Batch 5 Day 10. Reply wave CLOSES TODAY (72h+ post-Day-7). Thursday IMAP sweep UNCONFIRMED — 56-session HANDS execution pattern. IMAP gap now 48 days. CHANGELOG 54+ days overdue. Day-14 breakup: 4 days away (Tuesday 2026-05-26). This is the absolute final pre-weekend IMAP check — after today, remaining replies will be sporadic until Day-14.

---

## TODAY'S SITUATION

### What has happened this week (assumed)
- **Tuesday 2026-05-19:** Day-7 new-angle sends assumed sent 09:00-10:30 (UNCONFIRMED — 56-session pattern)
- **Tuesday 2026-05-19 EOD:** LinkedIn archive trigger fired unconditionally — all Batch 5 Ryedale leads archived LOST_NO_RESPONSE on LinkedIn channel
- **Wednesday 2026-05-20:** IMAP sweep per Batch 5 lead — UNCONFIRMED (no new entries in new_replies.json)
- **Thursday 2026-05-21:** Secondary post-Day-7 IMAP — UNCONFIRMED (no new entries in new_replies.json)
- **CHANGELOG:** Still not updated — 54+ days overdue

### What this means today
- **Reply wave CLOSES TODAY** — 72h+ post-Day-7 send (assumed Tuesday). After today, remaining replies drop sharply and become sporadic.
- This is the absolute final structured IMAP check window before Day-14 (Tuesday 2026-05-26)
- Wednesday and Thursday sweeps both UNCONFIRMED — 48-day IMAP gap means there may be replies sitting unread right now
- Email is the only remaining channel for all Batch 5 leads (LinkedIn permanently closed 2026-05-19)
- Day-14 breakup is 4 days away — copy is READY

### The one thing that matters today
**IMAP per Batch 5 lead — do it now.** Reply wave closes today. 48-day gap with two consecutive missed sweeps. If there is an INTERESTED reply: 24h proposal SLA from reply time (24/7 — non-negotiable). After today, the next IMAP is Tuesday morning before Day-14 sends.

---

## PART A: SIGNAL INTELLIGENCE

**No new leads or signals received.** HANDS has not provided new scraping data in 56+ sessions.

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
| Day-14 breakup | **Tue 2026-05-26** | **4 DAYS AWAY — copy READY** |

**Reply windows:**
- Post-Day-3 peak: CLOSED (7+ days post-bump)
- Post-Day-7 wave: **CLOSING TODAY** (72h+ post-send assumed Tuesday). After today: sporadic only.
- Post-Day-14 window: opens Wednesday 2026-05-27

**Key fact:** The post-Day-7 reply wave peaks at 24-48h, with the 72h window (today) being the last structured peak. Wednesday and Thursday sweeps were both UNCONFIRMED — today's sweep covers all three missed windows in one go. Do not split it.

### OOO Deadline
Day-14 is Tuesday 2026-05-26. Any lead with an OOO auto-reply where the stated return date is **after 2026-05-25** cannot receive Day-14 (4-touchpoint hard limit). Mark that lead's sequence as complete. Do NOT extend the sequence for an OOO lead returning after 2026-05-25.

### LinkedIn Channel — PERMANENTLY CLOSED

Archive trigger fired Tuesday 2026-05-19 EOD (unconditional). Email only channel remaining.

---

## PART C: REPLY MONITORING

### IMAP Status — Friday 2026-05-22
- Gap from last confirmed check: **48 days** (last confirmed 2026-04-04)
- Wednesday sweep: **UNCONFIRMED** (56-session HANDS pattern)
- Thursday sweep: **UNCONFIRMED** (56-session HANDS pattern)
- Friday sweep: **MANDATORY NOW** — reply wave CLOSES TODAY. This covers all three missed windows.

### Classification Protocol (on any new reply)

| Classification | Action |
|---|---|
| **INTERESTED** | Write new_replies.json immediately → classify → **CANCEL Day-14** → **24h proposal SLA** (24/7) → update value_delivery_queue.json |
| **NOT_INTERESTED** | Classify → cancel Day-14 permanently → suppress all channels → log CHANGELOG |
| **UNSUBSCRIBE** | Classify → suppress ALL channels within 24h (GDPR Article 21) → log audit_log + CHANGELOG |
| **OUT_OF_OFFICE** | Classify → note return date → **if return after 2026-05-25: mark sequence complete** (cannot send Day-14) |
| **WRONG_PERSON** | Classify → investigate correct contact → log CHANGELOG |

**Do NOT sweep leads 1/3/22 under any circumstances.** Archive unconditionally final.

### OOO handling detail
If a Batch 5 lead returns an OOO with return date on or before 2026-05-25: they can receive Day-14 on Tuesday 2026-05-26.  
If return date is 2026-05-26 or later: **mark sequence complete — 4-touchpoint hard limit prevents sending Day-14 after their return date**.

---

## PART D: FOLLOW-UP COPY STATUS

All copy is READY in `data/daily_email_plan.json`. No new copy required today or over the weekend.

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

**Current status: 0 INTERESTED replies in Batch 5.**

If an INTERESTED reply arrives today (final Day-7 reply peak):

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
- Respond within 24h from reply time (24/7 — non-negotiable).

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
1. **LinkedIn never activated** — 56-session failure. Two warm pipelines written off. £800-1,175 confirmed.
2. **IMAP gap (48 days, 3 consecutive missed sweeps)** — inbox state permanently uncertain. Compliance risk.
3. **CHANGELOG 54+ days overdue** — audit risk. Mandatory today.
4. **No HANDS send confirmation** — 56 sessions of "ASSUMED" data. Batch 6 fix: writes `data/batch_sends/YYYY-MM-DD.json` same session as each send batch.

### Subject Line Performance (historical)
- **Best performing:** `[First name] — [town] [trade] site flagged 'Not Secure'` → 3/3 INTERESTED (SSL-PAS)
- **Key variable:** First name in subject is a confirmed material lift

---

## BATCH 6 SCOPING DECISION

**Current state:**
- Confirmed INTERESTED replies: **0** (new_replies.json unchanged since 2026-04-04)
- IMAP gap: **48 days** — Wednesday and Thursday sweeps both UNCONFIRMED
- Decision status: **LAST WINDOW TODAY** — reply wave closes after today

**If trigger met (≥ 2 INTERESTED after today's IMAP):**
- Fire Batch 6 scoping immediately today
- Territory: Harrogate District (Knaresborough, Ripon new leads only, Boroughbridge) + Craven District (Skipton, Settle, Grassington, Gargrave)
- Initial sends: Tuesday 2026-06-02 (Tuesday AM premium window)
- **LinkedIn MANDATORY:** Activate within Day 3-7. Day 3 = Friday 2026-06-06 (ABSOLUTE DEADLINE). Archive trigger: Tuesday 2026-06-09 (Day 7), fires unconditionally if profiles.json missing.

**If trigger NOT met (< 2 INTERESTED after today's IMAP — most likely given current count):**
- No Batch 6 scraping until full Batch 5 post-mortem (Wednesday 2026-05-27)
- Review: was SSL-PAS the right signal for Ryedale? Were town/sector combinations optimal?
- Batch 6 geography confirmed (Harrogate + Craven) but start date deferred to after post-mortem

---

## WEEKEND BRIEF (Saturday 2026-05-23 — Sunday 2026-05-24)

**No actions required over the weekend.** Hard block on sends and IMAP Saturday-Sunday.

If an INTERESTED reply arrives over the weekend (possible — 48-day IMAP gap, multiple missed sweeps): the 24h proposal SLA runs from the reply timestamp, not from Monday morning. That means a Saturday reply requires a proposal by Sunday, and a Sunday reply requires a proposal by Monday. This applies 24/7 — non-negotiable.

**If a reply arrives over the weekend:**
1. Write to new_replies.json immediately
2. Classify in reply_classifications.json
3. Cancel Day-14 for that lead — use proposal flow
4. Prepare bespoke proposal within 24h from reply time
5. Log CHANGELOG

---

## OPERATIONAL PRIORITIES — TODAY AND REMAINDER

| Priority | Action | Deadline |
|---|---|---|
| **1** | **IMAP sweep per Batch 5 lead** — reply wave CLOSES TODAY | TODAY Friday 2026-05-22 — immediate |
| **2** | **Classify any new replies** — write new_replies.json, reply_classifications.json | Same session as IMAP |
| **3** | **24h proposal SLA** — if INTERESTED reply found | 24h from reply time (24/7) |
| **4** | **CHANGELOG.md** — 54+ days overdue | TODAY same session as IMAP |
| **5** | **Batch 6 trigger decision** — after IMAP confirms reply count | TODAY — last practical window |
| **6** | **Day-14 breakup sends** | Tuesday 2026-05-26, 09:00-10:30 |
| **7** | **Full Batch 5 post-mortem** | Wednesday 2026-05-27 BRAIN run |

---

## WEEK REMAINDER CALENDAR

| Date | Day | Batch 5 Day | Action |
|---|---|---|---|
| **Fri 2026-05-22** | **56** | **10** | **IMAP per Batch 5 lead — reply wave CLOSES TODAY. Final pre-weekend check. CHANGELOG mandatory.** |
| Sat 2026-05-23 | 57 | 11 | No sends. No IMAP. Weekend block. |
| Sun 2026-05-24 | 58 | 12 | No sends. No IMAP. Weekend block. |
| Mon 2026-05-25 | 59 | 13 | No sends today. Final prep for Day-14 (check copy, review send list). |
| **Tue 2026-05-26** | **60** | **14** | **Day-14 breakup sends 09:00-10:30. IMAP per lead before each send. Copy READY.** |
| Wed 2026-05-27 | 61 | 15 | Post-Day-14 reply monitoring begins. Full Batch 5 post-mortem BRAIN run. Batch 6 decision final. |

---

*BRAIN layer — Friday 2026-05-22 (Day 56, Batch 5 Day 10 — final pre-weekend IMAP check).*  
*HANDS layer must read this before any daily execution.*  
*Next BRAIN run: Wednesday 2026-05-27 — Day-14 results analysis + Batch 5 post-mortem + Batch 6 decision.*  
*If INTERESTED reply received today, Saturday, or Sunday: no new BRAIN run needed. Use value_delivery_queue.json (value_delivery_on_interested section) directly. 24h proposal SLA from reply time.*
