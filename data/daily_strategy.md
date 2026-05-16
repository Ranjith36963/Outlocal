# Daily Strategy — 2026-05-16 (Saturday) — Day 50

**Updated:** 2026-05-16 (BRAIN Day 50 run — Saturday bridge, Batch 5 Day 4)  
**Replaces:** 2026-05-15 strategy (Day 48 — Friday evening, Batch 5 Day 3)  
**Key changes from Day 48:** Full weekly review of active_strategy.md completed (now valid to 2026-05-24). Reply peak window OPEN post-bump. IMAP gap 42 days (from confirmed check). LinkedIn still MISSING — 49+ sessions. Monday is FINAL window, Tuesday archive trigger fires. No new HANDS updates received.

---

## CRITICAL ALERTS — DAY 50

### ALERT 1: LinkedIn — 49+ Sessions, Final Window Monday
`data/linkedin_profiles.json` NOT WRITTEN in 49+ consecutive sessions. LinkedIn has never been executed.  
**Monday 2026-05-18 is the absolute last window. Archive trigger fires Tuesday 2026-05-19 EOD.**  
Consequence of another failure: ALL Batch 5 leads archived LOST_NO_RESPONSE immediately. Same outcome as warm pipeline (£800-1,175 written off).

### ALERT 2: Reply Peak Window OPEN NOW
Day-3 bumps assumed sent Friday. 24-72h post-bump is the highest probability reply window in the full sequence.  
**Saturday-Monday is the peak window. An INTERESTED reply today enables a same-day proposal draft and Monday morning send.**

### ALERT 3: CHANGELOG 49+ Days Overdue
**Must be completed before Tuesday 2026-05-19 Day-7 sends.** No further deferrals under any circumstances.

### ALERT 4: IMAP Gap — 42 Days
No confirmed IMAP check since 2026-04-04. Sweep mandatory per lead before LinkedIn (Monday) and before each Day-7 send (Tuesday).

---

## EXECUTIVE SUMMARY — DAY 50 (SATURDAY)

No sends today. Weekend block enforced. Reply peak is live — this is the highest-probability reply window.

**Critical path for the next 72 hours:**

**Today-Sunday (Sat-Sun 2026-05-16-17):** Monitor inbox. Day-3 bumps sent Friday — 24-72h post-bump is peak. If HANDS has IMAP access: sweep all Batch 5 leads (NOT leads 1/3/22). An INTERESTED reply over the weekend triggers a 24h proposal SLA — this is not deferred to Monday morning.

**Monday 2026-05-18 (FINAL WINDOW):** IMAP sweep per Batch 5 lead → LinkedIn connection requests (ALL leads) → Write linkedin_profiles.json same session (mandatory) → Update CHANGELOG.

**Tuesday 2026-05-19 (DAY 7):** IMAP per lead before each send → Day-7 new-angle sends 09:00-10:30 → LinkedIn archive trigger fires EOD for any lead without confirmed LinkedIn.

---

## CAMPAIGN STATUS — DAY 50

| Metric | Value | Delta from Day 48 | Notes |
|---|---|---|---|
| Campaign day | 50 | +2 | Saturday 2026-05-16 |
| Batch 5 day | 4 | +1 | Reply peak open Saturday-Monday |
| Batch 5 replies | 0 confirmed | 0 | Post-bump peak OPEN NOW |
| IMAP gap (confirmed) | 42 days | +1 | Last confirmed: 2026-04-04 |
| LinkedIn executed | 0 in 49+ sessions | 0 | **MONDAY IS FINAL WINDOW — no extensions** |
| CHANGELOG lag | 49+ days | +1 | **Mandatory before Tuesday** |
| Day-7 copy | READY | — | data/daily_email_plan.json (day7_new_angle) |
| active_strategy.md | UPDATED | Updated | Full review complete — valid to 2026-05-24 |
| No sends today | Confirmed | — | Saturday weekend block |

---

## WEEKEND IMAP MONITORING

**Post-bump reply peak is open now.** Day-3 bumps assumed sent Friday 2026-05-15. Cold email reply peaks consistently occur 24-72h after a bump send.

If HANDS can check IMAP Saturday or Sunday:
1. Sweep all Batch 5 leads — NOT leads 1/3/22 (archive unconditionally final)
2. If INTERESTED reply found: write to new_replies.json immediately, classify in reply_classifications.json, begin proposal draft. **24h SLA runs from moment of reply — not from next business day. Saturday evening reply = Sunday evening deadline.**
3. If NOT_INTERESTED: classify, suppress email permanently, block LinkedIn permanently, log CHANGELOG
4. If UNSUBSCRIBE: suppress ALL channels within 24h (GDPR Article 21 applies at all times including weekends), log audit_log and CHANGELOG immediately
5. If clean: nothing to action — confirms normal. Next step is Monday LinkedIn.

---

## MONDAY EXECUTION ORDER — 2026-05-18 (FINAL LINKEDIN WINDOW)

| Priority | Action | Condition |
|---|---|---|
| 1 | IMAP sweep — per Batch 5 lead (NOT leads 1/3/22) | Before LinkedIn. If NOT_INTERESTED or UNSUBSCRIBE: block LinkedIn + Day-7 send for that lead permanently. If INTERESTED: still proceed with LinkedIn — do NOT reference email in note. |
| 2 | LinkedIn profile searches — sector priority order | Solicitors → Accountants → Estate agents → Hotels/B&Bs → Restaurants → Boutique retail → Trades. Primary query: `site:linkedin.com/in "[Full Name]" "[Business Name]"`. Fallback: sector_discovery_fallback_queries in linkedin_search_plan.json. |
| 3 | Check posts from last 60 days per confirmed profile | Post-reference note has 3-4x higher acceptance. Essential step — do not skip. |
| 4 | LinkedIn connection requests — confirmed profiles | **Use monday_fallback_notes in linkedin_connection_notes.json — active execution plan, direct-use.** 200-char hard limit. Count in plain-text editor before sending. |
| 5 | Write data/linkedin_profiles.json — MANDATORY | One entry per lead searched (including PROFILE_NOT_FOUND). Write immediately after each search — do not batch. This is the only confirmation mechanism. |
| 6 | CHANGELOG.md update | **49+ days overdue. Must complete before Tuesday Day-7 sends. Absolute deadline.** |

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

## LINKEDIN BRIEF — MONDAY 2026-05-18 (FINAL WINDOW)

**Status:** All previous sessions UNCONFIRMED. This is the last opportunity.  
**Archive trigger fires Tuesday 2026-05-19 EOD — no deferral path exists.**

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

**Note rules (non-negotiable):**
- Do NOT mention email outreach, website, SSL, 'Not Secure', or any technical finding
- Start with their name. Never start with 'I'.
- No exclamation marks. No 'reach out', 'synergies', 'I came across your profile'.
- Post-reference is strongly preferred. Check posts FIRST.
- End with low-pressure framing: 'in case it's useful' or 'connecting in case relevant'

---

## ANALYTICS — WHAT THE DATA CONFIRMS

| Pattern | Performance | Current application |
|---|---|---|
| SSL-PAS with first-name subject | 3/3 INTERESTED — campaign-best rate | Batch 5 SSL = 60% of sends |
| Tuesday AM send window | All 3 INTERESTED replies followed Tuesday sends | Day-7 = Tuesday 2026-05-19. Day-14 = Tuesday 2026-05-26. |
| Day-7 new angle (not reframe) | 1 conversion (Tom) from fresh pain point | Copy ready in daily_email_plan.json |
| Town name in subject | All INTERESTED replies engaged local angle | Non-negotiable for all Batch 5 sends |
| One pain point per email | 100% of replies engaged the specific signal | Non-negotiable |
| Day-3 bump effect | Not yet measured for Batch 5 | **First data arrives Saturday-Monday** |
| 24h proposal SLA | Tom asked for pricing — never received it (lost) | MANDATORY for Batch 5 INTERESTED replies |

---

## BATCH 5 PERFORMANCE OUTLOOK

| Metric | Expected | Basis |
|---|---|---|
| Total INTERESTED (full sequence) | 2-3 | 15% SSL-PAS rate on 12-18 sends |
| Reply window post-bump | Sat-Mon (24-72h peak) | Consistent across Batches 1-4 |
| Expected revenue if converted | £300-1,050 | SSL+mobile £150-200, no-website £500 |

---

## BATCH 6 PLANNING — TRIGGER CONDITIONS

Fire Batch 6 scoping **if Tuesday 2026-05-19 Day-7 results show ≥ 2 replies** (confirms Ryedale rural model works):
- **Territory:** Harrogate District (Knaresborough, Ripon new leads, Boroughbridge), Craven District (Skipton, Settle, Grassington)
- **Start:** Data collection from Wednesday 2026-05-20. Initial sends: Tuesday 2026-05-26 or 2026-06-02.
- **Avoid:** Beverley/Bridlington/Driffield (Batch 4 reapproach October only). Pateley Bridge (lead 2 NOT_INTERESTED until October). Otley fitness/wellness.

If Day-7 replies = 0: review signal mix and sector targeting before expanding Batch 6.

---

## FORWARD CALENDAR

| Date | Day | Action |
|---|---|---|
| **Sat 2026-05-16** | **50** | **TODAY — monitor inbox. Reply peak open. No sends.** |
| Sun 2026-05-17 | 51 | HANDS: Weekend IMAP monitoring (recommended) |
| **Mon 2026-05-18** | **52** | **HANDS: IMAP per lead → LinkedIn (FINAL) → profiles.json → CHANGELOG** |
| Mon 2026-05-18 eve | 52 | BRAIN (if profiles.json received): per-lead LinkedIn note personalisation |
| **Tue 2026-05-19** | **53** | **HANDS: IMAP per lead → Day-7 sends 09:00-10:30 → LinkedIn archive trigger EOD** |
| Tue 2026-05-19 eve | 53 | BRAIN: Day-14 breakup copy generation |
| **Tue 2026-05-26** | **60** | **HANDS: Day-14 breakup sends 09:00-10:30** |

---

## COMPLIANCE REMINDERS

- IMAP sweep before every send — 42-day gap is a compliance risk
- Unsubscribes: suppress within 24 hours (GDPR Article 21), log audit_log — applies 24/7
- 4-touchpoint maximum — hard limit, no exceptions
- LinkedIn: do not approach leads who replied NOT_INTERESTED on any channel
- B2B only — business emails, legitimate interest basis
- OOO pauses are mandatory — never re-send during stated OOO period

---

*Strategy maintained by OUTLOCAL BRAIN layer.*  
*Day 50 — Saturday 2026-05-16. Batch 5 Day 4.*  
*Reply peak window open now — monitor inbox Saturday-Monday.*  
*Monday LinkedIn is the FINAL window. Tuesday archive trigger fires EOD.*  
*active_strategy.md full review completed — valid to 2026-05-24.*
