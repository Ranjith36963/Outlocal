# Daily Strategy — 2026-05-18 (Monday) — Day 52

**Updated:** 2026-05-18 (BRAIN Day 52 run — Monday, FINAL LinkedIn execution window, Batch 5 Day 6)  
**Replaces:** 2026-05-17 strategy (Day 51 — Sunday bridge, Batch 5 Day 5)  
**Key changes from Day 51:** Day advances to 52. Batch 5 Day 6. Reply peak now at 72h post-bump (closing boundary — Monday morning). LinkedIn execution window is TODAY, not tomorrow. Day-7 sends are TOMORROW, not next week. CHANGELOG deadline is TODAY.

---

## CRITICAL ALERTS — DAY 52

### ALERT 1: LinkedIn — TODAY IS THE FINAL WINDOW (Monday 2026-05-18)
`data/linkedin_profiles.json` NOT WRITTEN in 52+ consecutive sessions. LinkedIn has never been executed.  
**Monday 2026-05-18 — TODAY — is the absolute last window. Archive trigger fires TOMORROW Tuesday 2026-05-19 EOD.**  
This is not a future warning. It is a same-day mandatory action.  
Consequence of failure: ALL Batch 5 leads archived LOST_NO_RESPONSE — same outcome as warm pipeline (£800-1,175 written off).

### ALERT 2: Day-7 Sends — TOMORROW (Tuesday 2026-05-19, 09:00-10:30)
Day-7 new-angle copy is complete and ready in `data/daily_email_plan.json` (day7_new_angle section).  
IMAP sweep per lead is mandatory before each send. Archive trigger fires EOD for any lead without confirmed LinkedIn.

### ALERT 3: CHANGELOG — 50+ Days Overdue (Absolute Deadline: TODAY)
Must be completed Monday 2026-05-18 before tomorrow's Day-7 sends. No further deferrals. This is the 50th+ deadline.

### ALERT 4: IMAP Gap — 44 Days
No confirmed IMAP check since 2026-04-04. TODAY sweep (per lead, before LinkedIn) mandatory.  
TOMORROW sweep (per lead, before each Day-7 send) mandatory.

---

## EXECUTIVE SUMMARY — DAY 52 (MONDAY)

Two things happen today and tomorrow that close or open significant pipeline value.

**TODAY (Monday 2026-05-18):**  
- IMAP sweep per Batch 5 lead (before LinkedIn)  
- LinkedIn profile searches + connection notes for all Batch 5 leads  
- Write linkedin_profiles.json same session  
- CHANGELOG.md update (mandatory before tomorrow)

**TOMORROW (Tuesday 2026-05-19):**  
- IMAP per lead before each Day-7 send  
- Day-7 new-angle sends, 09:00-10:30 (copy ready — standalone new email, new subject, different pain point)  
- LinkedIn archive trigger fires EOD: any Batch 5 lead without confirmed LinkedIn → archive LOST_NO_RESPONSE immediately

---

## CAMPAIGN STATUS — DAY 52

| Metric | Value | Delta from Day 51 | Notes |
|---|---|---|---|
| Campaign day | 52 | +1 | Monday 2026-05-18 |
| Batch 5 day | 6 | +1 | LinkedIn execution day |
| Batch 5 replies | 0 confirmed | 0 | Reply peak at 72h closing boundary. IMAP sweep today confirms. |
| IMAP gap (confirmed) | 44 days | +1 | Last confirmed: 2026-04-04. TODAY sweep mandatory. |
| LinkedIn executed | 0 in 52+ sessions | 0 | **TODAY IS FINAL WINDOW — archive trigger TOMORROW EOD** |
| CHANGELOG lag | 50+ days | +1 | **Mandatory TODAY before tomorrow sends** |
| Day-7 copy | READY | — | data/daily_email_plan.json (day7_new_angle) |
| Day-14 copy | READY | — | data/daily_email_plan.json (day14_breakup) — generated early Day 51 |
| Sends today | None | — | No email sends Monday |
| LinkedIn today | YES — EXECUTE | — | **FINAL WINDOW** |

---

## MONDAY IMAP SWEEP

**Mandatory — before each LinkedIn note. Per lead, not bulk. NOT leads 1/3/22.**

If today's IMAP sweep finds a Batch 5 reply:

| Reply type | Action |
|---|---|
| **INTERESTED** | Write to new_replies.json immediately. Classify. Still proceed with LinkedIn — do NOT mention email in note. Prepare proposal within 24h from reply time (24/7 SLA). Cancel Day-7 — use interested variant from daily_email_plan.json instead (reply in thread). |
| **NOT_INTERESTED** | Classify. Block LinkedIn permanently. Cancel Day-7 permanently. Suppress email. Log CHANGELOG. |
| **UNSUBSCRIBE** | Classify. Suppress ALL channels within 24h (GDPR Article 21). Log audit_log + CHANGELOG. Cancel Day-7 and Day-14. |
| **OOO** | Classify. Note return date. LinkedIn still valid (passive). Day-7: send day after return if before 2026-05-25. |
| **Clean** | LinkedIn approved. Proceed with connection request. |

---

## MONDAY LINKEDIN EXECUTION — TODAY (FINAL WINDOW)

| Priority | Action | Notes |
|---|---|---|
| 1 | IMAP sweep — per Batch 5 lead (NOT leads 1/3/22) | First thing. Before LinkedIn. |
| 2 | LinkedIn profile searches — sector priority | Solicitors → Estate agents → Hotels/B&Bs → Restaurants → Boutique retail → Trades. Primary: `site:linkedin.com/in "[Full Name]" "[Business Name]"`. Fallback: sector_discovery_fallback_queries in linkedin_search_plan.json. |
| 3 | Check posts from last 60 days per confirmed profile | Post-reference note = 3-4x higher acceptance. ALWAYS check before defaulting to sector template. |
| 4 | Send connection request — 200-char hard limit | Post found: write bespoke post_reference note. No post: use monday_fallback_notes from linkedin_connection_notes.json (sector templates, direct-use). Count characters in plain-text editor before sending. |
| 5 | Write data/linkedin_profiles.json — MANDATORY | One entry per lead (including PROFILE_NOT_FOUND). Write immediately after each search — do NOT batch at end. |
| 6 | CHANGELOG.md update | 50+ days overdue. Log: all Batch 5 Day-0 sends, Day-3 bumps, fu_041-045 outcomes, archive decisions, IMAP results since April, today's LinkedIn outcomes. |

**Town priority:** Malton → Helmsley → Pickering → Kirkbymoorside → Norton-on-Derwent → Hovingham  
**Do not approach:** leads 1/3/22 (archive final), 2 (NOT_INTERESTED), 7/19 (suppressed)

---

## TUESDAY EXECUTION ORDER — 2026-05-19 (DAY-7 SEND DAY)

| Priority | Action | Condition |
|---|---|---|
| 1 | IMAP sweep — each Batch 5 lead before their Day-7 send | Per lead (NOT leads 1/3/22). If INTERESTED: use interested variant (daily_email_plan.json conditional_handling), reply in thread, classify, 24h proposal SLA. If NOT_INTERESTED: cancel Day-7 permanently, block all channels. If UNSUBSCRIBE: suppress 24h, GDPR Article 21. |
| 2 | Day-7 new-angle sends — 09:00-10:30, 10-min stagger | NEW standalone email. NOT thread reply. New subject. Different pain point. HANDS fills [bracketed placeholders] from 2026-05-12 send records. Full copy: data/daily_email_plan.json (day7_new_angle section). |
| 3 | LinkedIn archive trigger — EOD Tuesday 2026-05-19 | Any Batch 5 lead without confirmed LinkedIn (note_sent: true in linkedin_profiles.json): archive immediately as LOST_NO_RESPONSE. Log CHANGELOG same session. No exceptions. |

---

## DAY-7 SEND BRIEF — TOMORROW TUESDAY 2026-05-19

**Send window:** 09:00-10:30 | **Stagger:** 10 minutes between sends  
**Type:** Standalone NEW email — NOT a thread reply. New subject. New pain point.  
**IMAP precondition:** Per lead before each send

| Signal | Day-7 Angle | Recommended subject |
|---|---|---|
| **SSL (60%)** | Google local ranking penalty for HTTP | "[First name] — the 'Not Secure' warning is also a Google ranking issue for [business name]" |
| **Mobile (20%)** | SSL for ALL visitors OR missing click-to-call | "[First name] — [business name]: one more issue I noticed on the website" |
| **No-website (15%)** | Named competitor ranking / missed enquiries | "Following up — who's getting the [trade] calls in [town]" |
| **AIDA (5%)** | Reviews not converting to search visibility | "[First name] — [business name] has [N] great reviews but low search visibility in [town]" |

**Full copy with body text in `data/daily_email_plan.json → day7_new_angle section`. Ready to use.**

---

## DAY-14 BREAKUP BRIEF — TUESDAY 2026-05-26 (COPY ALREADY READY)

**Generated:** Sunday 2026-05-17 (Day 51) — ahead of schedule  
**Send window:** 09:00-10:30 | **Stagger:** 10 minutes between sends  
**Type:** Breakup — FINAL touchpoint. 3 lines max. No pressure. No question marks. Door open.

| Signal | Recommended subject | Key tone |
|---|---|---|
| **SSL (60%)** | "[First name] — closing the loop on [business name]" | Warm exit. Reference 'Not Secure' briefly. Door open. |
| **Mobile (20%)** | "[First name] — [business name]: last note from me" | Self-aware. Won't keep nudging. Happy to help if ever relevant. |
| **No-website (15%)** | "Last note — [business name]" | No first name if unknown. Won't keep at it. Easy to reach if priority changes. |
| **AIDA (5%)** | "[First name] — last note on [business name]" | 'Leave it with you.' If timing changes, happy to pick it up. |

**Full copy in `data/daily_email_plan.json → day14_breakup section`. Ready. No Tuesday evening BRAIN run required solely for Day-14 copy — BRAIN Tuesday evening will cover Day-7 results and Batch 6 scoping.**

---

## ANALYTICS — CONFIRMED PATTERNS

| Pattern | Performance | Current application |
|---|---|---|
| SSL-PAS with first-name subject | 3/3 INTERESTED — campaign-best rate | Batch 5 SSL = 60% of sends |
| Tuesday AM send window | All 3 INTERESTED replies followed Tuesday sends | Day-7 = TOMORROW Tuesday 2026-05-19. Day-14 = Tuesday 2026-05-26. |
| Day-7 new angle (not reframe) | 1 conversion (Tom) from fresh pain point | Copy ready — Google ranking angle for SSL leads |
| Town name in subject | All INTERESTED replies engaged local angle | Non-negotiable for all Batch 5 sends |
| One pain point per email | 100% of replies engaged the specific signal | Non-negotiable |
| Post-bump peak | Batch 1-4 data confirms 24-72h post-bump = peak | Peak closing now at 72h. IMAP sweep today confirms. |
| Day-7 reply wave | Day 7 sends generate a second reply peak | Post-Day-7 peak: Wed-Fri 2026-05-21-23 — monitor inbox |

---

## BATCH 5 PERFORMANCE OUTLOOK

| Metric | Expected | Basis |
|---|---|---|
| Total INTERESTED (full sequence) | 2-3 | 15% SSL-PAS rate on 12-18 sends |
| Post-Day-3-bump reply peak | Closing now (72h, Monday) | Confirmed pattern across Batches 1-4 |
| Post-Day-7 reply peak | Wed-Fri 2026-05-21-23 | Historically strongest for undecided leads |
| Expected revenue if converted | £300-1,050 | SSL+mobile £150-200, no-website £500 |

---

## BATCH 6 PLANNING — TRIGGER CONDITIONS

Fire Batch 6 scoping **if Tuesday 2026-05-19 Day-7 replies ≥ 2** (confirms Ryedale rural model):
- **Territory:** Harrogate District (Knaresborough, Ripon new leads only, Boroughbridge), Craven District (Skipton, Settle, Grassington)
- **Start:** Data collection from Wednesday 2026-05-20. Initial sends: Tuesday 2026-05-26 or 2026-06-02.
- **Avoid:** Beverley/Bridlington/Driffield (Batch 4 reapproach October only). Pateley Bridge (lead 2 NOT_INTERESTED until October). Otley fitness/wellness.

If Day-7 replies = 0: review signal mix and sector targeting before expanding. Do not scrape Batch 6 until Batch 5 full sequence analysis complete.

**Batch 6 scoping BRAIN run: Tuesday 2026-05-19 evening.**

---

## FORWARD CALENDAR

| Date | Day | Action |
|---|---|---|
| **Mon 2026-05-18** | **52** | **TODAY — HANDS: IMAP per lead → LinkedIn FINAL WINDOW → profiles.json → CHANGELOG** |
| Mon 2026-05-18 eve | 52 | BRAIN (if profiles.json written): per-lead LinkedIn note personalisation |
| **Tue 2026-05-19** | **53** | **HANDS: IMAP per lead → Day-7 sends 09:00-10:30 → LinkedIn archive trigger EOD** |
| Tue 2026-05-19 eve | 53 | BRAIN: Day-7 results analysis + Batch 6 scoping (Day-14 copy already done) |
| Wed 2026-05-20 | 54 | Batch 6 data collection (if Day-7 replies ≥ 2) |
| **Tue 2026-05-26** | **60** | **HANDS: Day-14 breakup sends 09:00-10:30 (copy in daily_email_plan.json — READY NOW)** |

---

## COMPLIANCE REMINDERS

- IMAP sweep before every send — 44-day gap is a compliance risk. Both today and tomorrow mandatory.
- Unsubscribes: suppress within 24 hours (GDPR Article 21), log audit_log — applies 24/7
- 4-touchpoint maximum — hard limit, no exceptions. Day-14 is the final touch.
- LinkedIn: do not approach leads who replied NOT_INTERESTED on any channel
- B2B only — business emails, legitimate interest basis
- OOO pauses are mandatory — never re-send during stated OOO period
- Do not contact archived leads: 1, 3, 22, 49, 51, 53, 54 under any circumstances

---

*Strategy maintained by OUTLOCAL BRAIN layer.*  
*Day 52 — Monday 2026-05-18. Batch 5 Day 6.*  
*LinkedIn execution: FINAL WINDOW TODAY. Archive trigger TOMORROW EOD.*  
*Day-7 sends: TOMORROW Tuesday 2026-05-19, 09:00-10:30.*  
*CHANGELOG: mandatory TODAY before tomorrow sends.*  
*active_strategy.md full review completed Day 50 — valid to 2026-05-24.*
