# Daily Strategy — 2026-05-17 (Sunday) — Day 51

**Updated:** 2026-05-17 (BRAIN Day 51 run — Sunday bridge, Batch 5 Day 5)  
**Replaces:** 2026-05-16 strategy (Day 50 — Saturday bridge, Batch 5 Day 4)  
**Key changes from Day 50:** Reply peak now at 48h post-bump (Sunday is still in peak window, closes Monday morning). TOMORROW is the absolute final LinkedIn window. Day-14 breakup copy generated early this run — all 4 signal variants ready in daily_email_plan.json. IMAP gap: 43 days. CHANGELOG: 50+ days overdue.

---

## CRITICAL ALERTS — DAY 51

### ALERT 1: LinkedIn — TOMORROW IS THE FINAL WINDOW (Monday 2026-05-18)
`data/linkedin_profiles.json` NOT WRITTEN in 50+ consecutive sessions. LinkedIn has never been executed.  
**Monday 2026-05-18 — TOMORROW — is the absolute last window. Archive trigger fires Tuesday 2026-05-19 EOD.**  
This is not a future deadline. It is tomorrow morning.  
Consequence of failure: ALL Batch 5 leads archived LOST_NO_RESPONSE — same outcome as warm pipeline.

### ALERT 2: Reply Peak Closing — Sunday is 48h Post-Bump
Day-3 bumps assumed sent Friday 2026-05-15. 48h post-bump peak is open now (Sunday).  
**Peak closes Monday morning at 72h. An INTERESTED reply today enables a Monday morning proposal.**  
Check IMAP now while the window is still live.

### ALERT 3: CHANGELOG 50+ Days Overdue
**Must be completed Monday 2026-05-18 before Tuesday sends.** No further deferrals.

### ALERT 4: IMAP Gap — 43 Days
No confirmed IMAP check since 2026-04-04. Monday sweep (per lead) mandatory before LinkedIn.  
Tuesday sweep (per lead) mandatory before each Day-7 send.

---

## EXECUTIVE SUMMARY — DAY 51 (SUNDAY)

No sends today. Sunday block enforced. Reply peak is at 48h — still open, closing tomorrow.

### NEW THIS RUN: Day-14 Breakup Copy Generated Early
Day-14 breakup copy was scheduled for Tuesday 2026-05-19 evening. Generated today instead — all 4 signal variants complete in `data/daily_email_plan.json` (day14_breakup section). HANDS can prepare Day-14 sends (Tuesday 2026-05-26) without waiting for Tuesday evening BRAIN run. Tuesday evening BRAIN will focus on Day-7 results analysis and Batch 6 scoping instead.

**Critical path for the next 48 hours:**

**Today Sunday 2026-05-17:** If HANDS has IMAP access: sweep all Batch 5 leads (NOT leads 1/3/22). Post-bump reply peak is open. An INTERESTED reply today = 24h SLA (Sunday evening deadline = Monday evening proposal). No sends today.

**TOMORROW Monday 2026-05-18 (FINAL LINKEDIN WINDOW):** IMAP sweep per Batch 5 lead (first thing) → LinkedIn connection requests for all leads → Write linkedin_profiles.json same session (mandatory) → Update CHANGELOG.

**Tuesday 2026-05-19 (DAY 7):** IMAP per lead before each send → Day-7 new-angle sends 09:00-10:30 → LinkedIn archive trigger fires EOD for any lead without confirmed LinkedIn.

---

## CAMPAIGN STATUS — DAY 51

| Metric | Value | Delta from Day 50 | Notes |
|---|---|---|---|
| Campaign day | 51 | +1 | Sunday 2026-05-17 |
| Batch 5 day | 5 | +1 | 48h post-bump — reply peak still open |
| Batch 5 replies | 0 confirmed | 0 | Peak window open Sunday, closes Monday morning |
| IMAP gap (confirmed) | 43 days | +1 | Last confirmed: 2026-04-04 |
| LinkedIn executed | 0 in 50+ sessions | 0 | **TOMORROW IS FINAL WINDOW — archive trigger Tuesday EOD** |
| CHANGELOG lag | 50+ days | +1 | **Mandatory before Tuesday** |
| Day-7 copy | READY | — | data/daily_email_plan.json (day7_new_angle) |
| Day-14 copy | **READY (new)** | **Generated today** | data/daily_email_plan.json (day14_breakup) |
| No sends today | Confirmed | — | Sunday weekend block |

---

## SUNDAY IMAP MONITORING

**Post-bump reply peak is open now.** Day-3 bumps assumed sent Friday 2026-05-15. 48h post-bump = today Sunday. Peak closes Monday morning (72h mark).

If HANDS can check IMAP today:
1. Sweep all Batch 5 leads — NOT leads 1/3/22 (archive unconditionally final)
2. If INTERESTED reply found: write to new_replies.json immediately, classify in reply_classifications.json, begin proposal draft. **24h SLA runs from moment of reply — not from next business day. Sunday evening reply = Monday evening deadline.**
3. If NOT_INTERESTED: classify, suppress email permanently, block LinkedIn permanently, log CHANGELOG
4. If UNSUBSCRIBE: suppress ALL channels within 24h (GDPR Article 21 — applies at all times including Sundays), log audit_log and CHANGELOG immediately
5. If clean: confirms normal state. Monday LinkedIn remains the priority.

---

## MONDAY EXECUTION ORDER — 2026-05-18 (TOMORROW — FINAL LINKEDIN WINDOW)

| Priority | Action | Condition |
|---|---|---|
| 1 | IMAP sweep — per Batch 5 lead (NOT leads 1/3/22) | First thing. Before LinkedIn. Per lead, not bulk. If NOT_INTERESTED or UNSUBSCRIBE: block LinkedIn + Day-7 send for that lead permanently. If INTERESTED: still proceed with LinkedIn — do NOT reference email in note. |
| 2 | LinkedIn profile searches — sector priority order | Solicitors → Accountants → Estate agents → Hotels/B&Bs → Restaurants → Boutique retail → Trades. Primary query: `site:linkedin.com/in "[Full Name]" "[Business Name]"`. Fallback: sector_discovery_fallback_queries in linkedin_search_plan.json. |
| 3 | Check posts from last 60 days per confirmed profile | Post-reference note has 3-4x higher acceptance. Essential step — do not skip. |
| 4 | LinkedIn connection requests — confirmed profiles | **Use monday_fallback_notes in linkedin_connection_notes.json — active execution plan, direct-use.** 200-char hard limit. Count in plain-text editor before sending. |
| 5 | Write data/linkedin_profiles.json — MANDATORY | One entry per lead searched (including PROFILE_NOT_FOUND). Write immediately after each search — do not batch. This is the only confirmation mechanism. |
| 6 | CHANGELOG.md update | **50+ days overdue. Absolute deadline before Tuesday. Log: all Batch 5 Day-0 sends, Day-3 bumps, fu_041-045 breakup outcomes, archive decisions, IMAP results since April, LinkedIn outcomes.** |

---

## TUESDAY EXECUTION ORDER — 2026-05-19 (DAY-7 SEND DAY)

| Priority | Action | Condition |
|---|---|---|
| 1 | IMAP sweep — each Batch 5 lead before their Day-7 send | Per lead (NOT leads 1/3/22). If INTERESTED: use interested variant (daily_email_plan.json conditional_handling), reply in thread, classify, 24h proposal SLA. If NOT_INTERESTED: cancel Day-7 permanently, block all channels. If UNSUBSCRIBE: suppress 24h, GDPR Article 21. |
| 2 | Day-7 new-angle sends — 09:00-10:30, 10-min stagger | NEW standalone email. NOT thread reply. New subject. Different pain point. HANDS fills [bracketed placeholders] from 2026-05-12 send records. Full copy: data/daily_email_plan.json (day7_new_angle section). |
| 3 | LinkedIn archive trigger — EOD Tuesday 2026-05-19 | Any Batch 5 lead without confirmed LinkedIn (note_sent: true in linkedin_profiles.json): archive immediately as LOST_NO_RESPONSE. Log CHANGELOG same session. No exceptions. |

---

## DAY-7 SEND BRIEF — TUESDAY 2026-05-19

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

## DAY-14 BREAKUP BRIEF — TUESDAY 2026-05-26 (COPY READY NOW)

**Generated:** Sunday 2026-05-17 (this run) — ahead of schedule  
**Send window:** 09:00-10:30 | **Stagger:** 10 minutes between sends  
**Type:** Breakup — FINAL touchpoint. Maximum 4 total touchpoints. Hard limit.

| Signal | Recommended subject | Key tone |
|---|---|---|
| **SSL (60%)** | "[First name] — closing the loop on [business name]" | Warm exit. Reference 'Not Secure' briefly. Door open. |
| **Mobile (20%)** | "[First name] — [business name]: last note from me" | Self-aware. Won't keep nudging. Happy to help if ever relevant. |
| **No-website (15%)** | "Last note — [business name]" | No first name if unknown. Won't keep at it. Easy to reach if priority changes. |
| **AIDA (5%)** | "[First name] — last note on [business name]" | 'Leave it with you.' If timing changes, happy to pick it up. |

**Full copy with body text in `data/daily_email_plan.json → day14_breakup section`. Ready to use. No Tuesday evening BRAIN run required solely for Day-14 copy.**

**Exclusions:** Do NOT send to any lead who replies INTERESTED before 2026-05-26 — use proposal flow instead.

---

## LINKEDIN BRIEF — TOMORROW MONDAY 2026-05-18 (FINAL WINDOW)

**Status:** 50+ consecutive sessions without execution. This is the last opportunity.  
**Archive trigger fires Tuesday 2026-05-19 EOD — no deferral path exists. This is unconditional.**

| Step | Action |
|---|---|
| 1 | IMAP sweep each Batch 5 lead before their note |
| 2 | LinkedIn profile search (queries in linkedin_search_plan.json) |
| 3 | Check posts from last 60 days BEFORE writing note |
| 4 | Post found: write bespoke post_reference note (3-4x acceptance) |
| 5 | No post: use sector note from linkedin_connection_notes.json (monday_fallback_notes — direct-use) |
| 6 | Send connection request — 200-char hard limit, count first |
| 7 | Write entry to data/linkedin_profiles.json immediately — mandatory |

**Town priority:** Malton → Helmsley → Pickering → Kirkbymoorside → Norton-on-Derwent → Hovingham  
**Sector priority:** Solicitors → Estate agents → Hotels/B&Bs → Restaurants → Boutique retail → Trades

---

## ANALYTICS — CONFIRMED PATTERNS

| Pattern | Performance | Current application |
|---|---|---|
| SSL-PAS with first-name subject | 3/3 INTERESTED — campaign-best rate | Batch 5 SSL = 60% of sends |
| Tuesday AM send window | All 3 INTERESTED replies followed Tuesday sends | Day-7 = Tuesday 2026-05-19. Day-14 = Tuesday 2026-05-26. |
| Day-7 new angle (not reframe) | 1 conversion (Tom) from fresh pain point | Copy ready — Google ranking angle for SSL leads |
| Town name in subject | All INTERESTED replies engaged local angle | Non-negotiable for all Batch 5 sends |
| One pain point per email | 100% of replies engaged the specific signal | Non-negotiable |
| Post-bump peak | Batch 1-4 data confirms 24-48h post-bump = peak | Today Sunday is 48h post-bump — peak open NOW |
| 24h proposal SLA | Tom asked for pricing — never received it (lost) | MANDATORY for Batch 5 INTERESTED replies |

---

## BATCH 5 PERFORMANCE OUTLOOK

| Metric | Expected | Basis |
|---|---|---|
| Total INTERESTED (full sequence) | 2-3 | 15% SSL-PAS rate on 12-18 sends |
| Reply window post-bump | Sat-Mon (24-72h peak) | Consistent across Batches 1-4 |
| Expected revenue if converted | £300-1,050 | SSL+mobile £150-200, no-website £500 |
| Day-7 uplift | +1 INTERESTED expected | New angle (ranking) produces new engagement from undecideds |

---

## BATCH 6 PLANNING — TRIGGER CONDITIONS

Fire Batch 6 scoping **if Tuesday 2026-05-19 Day-7 results show ≥ 2 replies** (confirms Ryedale rural model):
- **Territory:** Harrogate District (Knaresborough, Ripon new leads only, Boroughbridge), Craven District (Skipton, Settle, Grassington)
- **Start:** Data collection from Wednesday 2026-05-20. Initial sends: Tuesday 2026-05-26 or 2026-06-02.
- **Avoid:** Beverley/Bridlington/Driffield (Batch 4 reapproach October only). Pateley Bridge (lead 2 NOT_INTERESTED until October). Otley fitness/wellness.

If Day-7 replies = 0: review signal mix and sector targeting. Do not scrape Batch 6 until Batch 5 full sequence analysis complete.

---

## FORWARD CALENDAR

| Date | Day | Action |
|---|---|---|
| **Sun 2026-05-17** | **51** | **TODAY — Sunday. Monitor inbox. Reply peak 48h post-bump, closing tomorrow. No sends.** |
| **Mon 2026-05-18** | **52** | **HANDS: IMAP per lead → LinkedIn (FINAL WINDOW) → profiles.json → CHANGELOG** |
| Mon 2026-05-18 eve | 52 | BRAIN (if profiles.json received): per-lead LinkedIn note personalisation |
| **Tue 2026-05-19** | **53** | **HANDS: IMAP per lead → Day-7 sends 09:00-10:30 → LinkedIn archive trigger EOD** |
| Tue 2026-05-19 eve | 53 | BRAIN: Day-7 results analysis + Batch 6 scoping (Day-14 copy already done) |
| **Tue 2026-05-26** | **60** | **HANDS: Day-14 breakup sends 09:00-10:30 (copy in daily_email_plan.json — READY)** |

---

## COMPLIANCE REMINDERS

- IMAP sweep before every send — 43-day gap is a compliance risk
- Unsubscribes: suppress within 24 hours (GDPR Article 21), log audit_log — applies 24/7
- 4-touchpoint maximum — hard limit, no exceptions. Day-14 is the final touch.
- LinkedIn: do not approach leads who replied NOT_INTERESTED on any channel
- B2B only — business emails, legitimate interest basis
- OOO pauses are mandatory — never re-send during stated OOO period
- Do not contact archived leads: 1, 3, 22, 49, 51, 53, 54 under any circumstances

---

*Strategy maintained by OUTLOCAL BRAIN layer.*  
*Day 51 — Sunday 2026-05-17. Batch 5 Day 5.*  
*Reply peak window: 48h post-bump, open now, closing Monday morning.*  
*Monday LinkedIn is TOMORROW — FINAL window. Archive trigger fires Tuesday EOD.*  
*Day-14 breakup copy generated early this run — all 4 signal variants ready.*  
*active_strategy.md full review completed Day 50 — valid to 2026-05-24.*
