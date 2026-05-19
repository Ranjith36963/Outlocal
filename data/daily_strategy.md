# Daily Strategy — 2026-05-19 (Tuesday) — Day 53

**Updated:** 2026-05-19 (BRAIN Day 53 run — Tuesday, Batch 5 Day 7 SEND DAY)  
**Replaces:** 2026-05-18 strategy (Day 52 — Monday, Final LinkedIn execution window)  
**Key changes from Day 52:** Day advances to 53. Batch 5 Day 7. Day-7 sends are TODAY (not tomorrow). LinkedIn archive trigger fires TODAY EOD (was: tomorrow). Post-Day-3 reply peak closed. Post-Day-7 reply wave opens after sends today.

---

## TODAY'S STATUS — SINGLE-LINE SUMMARY

**Day-7 new-angle sends TODAY 09:00-10:30. LinkedIn archive trigger fires TONIGHT EOD. linkedin_profiles.json STILL MISSING (53-session failure). IMAP per lead before each send. CHANGELOG 51 days overdue — mandatory today.**

---

## CRITICAL EVENTS TODAY (Tuesday 2026-05-19)

| Time | Event | Status |
|---|---|---|
| 09:00-10:30 | Day-7 new-angle sends — all Batch 5 leads | SEND TODAY |
| All day | IMAP per lead before each send | MANDATORY |
| EOD | LinkedIn archive trigger fires | UNCONDITIONAL |
| Any time | CHANGELOG.md update | MANDATORY — 51 days overdue |

---

## EXECUTION ORDER — HANDS (Today)

### Priority 1: IMAP sweep per lead (before each Day-7 send)
- Per Batch 5 lead, in send order
- NOT leads 1/3/22 — archive unconditionally final
- If INTERESTED: use interested variant from `daily_email_plan.json` (conditional_handling section) — reply in thread. Cancel Day-7 send. 24h proposal SLA (non-negotiable).
- If NOT_INTERESTED: cancel Day-7 permanently. Suppress all channels. Log CHANGELOG.
- If UNSUBSCRIBE: suppress within 24h GDPR Article 21. Log audit_log + CHANGELOG.
- If OOO: note return date. Pause Day-7. Send day after return if before 2026-05-25.

### Priority 2: Day-7 new-angle sends (09:00-10:30)
- NEW standalone email — NOT a thread reply
- New subject line — different from Day-0 (see subject templates in `daily_email_plan.json` `day7_new_angle` section)
- Different pain point — NOT a reframe of Day-0
- Fill [bracketed placeholders] from 2026-05-12 send records
- 10-minute stagger between sends
- Expected: 12-18 sends

**Day-7 pivot by Day-0 signal:**
- Day-0 SSL → Day-7: Google local ranking penalty for HTTP sites
- Day-0 mobile → Day-7: SSL 'Not Secure' for ALL visitors (if HTTP) OR missing click-to-call
- Day-0 no-website → Day-7: named competitor ranking for '[trade] [town]' OR 'businesses from nearby area'
- Day-0 AIDA → Day-7: great reviews but Google not surfacing site in local search

### Priority 3: LinkedIn archive trigger (EOD today)
- `linkedin_profiles.json` STILL MISSING — 53-session failure
- If HANDS executes LinkedIn at any point today (before EOD): write `linkedin_profiles.json` immediately after each search — one entry per lead
- EOD: any Batch 5 lead without `note_sent: true` in `linkedin_profiles.json` → archive LOST_NO_RESPONSE immediately. Log CHANGELOG.
- No extensions. No deferrals. This trigger is unconditional.

### Priority 4: CHANGELOG.md (mandatory today)
- 51 days overdue
- Log: Batch 5 Day-0 sends (date, lead IDs, business names, signals), Day-3 bumps, fu_041-045 breakup outcomes, archive decisions (leads 1/3/22, 49/51/53/54), all IMAP sweep results since April, today's Day-7 send outcomes, LinkedIn outcomes (including any archive decisions from today's trigger)

---

## COPY STATUS

| Send type | Status | Location |
|---|---|---|
| Day-7 new-angle (all 4 signal variants) | **READY** | `data/daily_email_plan.json` → `day7_new_angle` section |
| Day-14 breakup (all 4 signal variants) | **READY** | `data/daily_email_plan.json` → `day14_breakup` section |

---

## POST-DAY-7 REPLY WAVE FORECAST

Day-7 sends today open a fresh reply window. Historical data shows this is the **strongest reply window in the full sequence** for undecided leads:
- They have had 7 days to think about the Day-0 pain point
- The new angle (ranking / competitor / click-to-call) creates fresh urgency
- It's a different email entirely — not a repeat

**Expected reply window:** Wednesday-Friday 2026-05-21-23 (24-72h post-send)  
**Expected replies:** 2-4 (based on 15% SSL-PAS rate, 12-18 sends)  
**IMAP monitoring:** Daily Wednesday-Friday minimum. Per lead on confirmation of reply.

---

## BATCH 6 SCOPING TRIGGER

| Condition | Action |
|---|---|
| Day-7 replies ≥ 2 by Wednesday 2026-05-21 | Fire Batch 6 immediately. Scrape Harrogate + Craven. Initial sends: Tue 2026-05-26 or Tue 2026-06-02. |
| Day-7 replies = 0-1 by Wednesday | Review signal mix. Do not expand until Batch 5 full sequence complete (after Day-14, Tue 2026-05-26). |

**Batch 6 territory (if triggered):**
- Harrogate District: Knaresborough, Ripon (new leads only), Boroughbridge
- Craven District: Skipton, Settle, Grassington, Gargrave
- Signal priority: ssl (HTTP) → mobile → no-website (4★+ 20+ reviews)

---

## FORWARD CALENDAR

| Date | Day | Event |
|---|---|---|
| **Tue 2026-05-19** | **53** | **Day-7 sends TODAY (09:00-10:30) + LinkedIn archive trigger EOD** |
| Wed 2026-05-20 | 54 | Post-Day-7 reply wave peak opens. IMAP monitoring. Batch 6 trigger check. |
| Thu 2026-05-21 | 55 | Post-Day-7 reply wave peak. IMAP monitoring. Batch 6 decision if ≥2 replies. |
| Fri 2026-05-22 | 56 | Post-Day-7 reply wave (72h boundary). Classify any replies. |
| Tue 2026-05-26 | 60 | **Day-14 breakup sends (09:00-10:30) — FINAL touchpoint. Copy READY.** |
| Tue 2026-11-26 | — | Earliest reapproach for no-reply Day-14 leads (6 months minimum) |

---

## LINKEDIN STATUS — FINAL DETERMINATION

**53-session failure. Archive trigger fires TONIGHT.**

This is the same failure pattern that lost leads 1/3/22 (£800-1,175). The trigger is unconditional. If `linkedin_profiles.json` is not written today before EOD:
- All Batch 5 leads without confirmed LinkedIn → archived LOST_NO_RESPONSE immediately
- No extensions, no overrides, no future LinkedIn window for these leads
- Reapproach: 6 months minimum (earliest: 2026-11-19 for email; LinkedIn channel PERMANENTLY CLOSED)

---

## WINNING PLAYBOOK REMINDERS (non-negotiable)

1. **SSL → PAS → first-name subject → town name → specific URL** — 3/3 INTERESTED rate
2. **Day-7 genuinely different pain point** — not a reframe. A reframe of Day-0 produces 0% responses.
3. **One pain point per email** — single clear signal. Listing multiple issues kills response.
4. **Town name in subject AND body** — local credibility confirmed by every INTERESTED reply
5. **No question marks in subject** — statement of fact outperforms question hook
6. **Chrome's exact wording** — `'Not Secure'` (not "unsecured")
7. **IMAP before every send** — 45-day gap is both a compliance and commercial risk

---

## IMAP GAP RISK NOTE

**45 days since confirmed IMAP check (2026-04-04).** An undetected INTERESTED reply, NOT_INTERESTED reply, or UNSUBSCRIBE request in the inbox represents:
- Commercial risk: missed proposal opportunity (24h SLA cannot be met retroactively)
- Compliance risk: GDPR Article 21 unsubscribe suppression obligation within 24h

The per-lead IMAP sweep before each send today is mandatory. Do not send without it.

---

*BRAIN layer — Day 53, 2026-05-19. HANDS layer reads this file before executing.*  
*Next BRAIN run: Tuesday 2026-05-19 evening — Day-7 results analysis + Batch 6 scoping decision.*  
*Day-14 breakup copy already generated (Day 51) — no Tuesday evening run required solely for Day-14 copy.*
