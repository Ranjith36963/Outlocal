# OUTLOCAL Frontend PRD — Dashboard for Solo Founder

## Purpose
Personal dashboard for Ranjith to operate the OUTLOCAL cold outreach engine. This is NOT a SaaS product. One user, zero authentication. Connects to the existing FastAPI backend (localhost:8000).

## Tech Stack
- **Framework:** Next.js 15 (App Router)
- **Language:** TypeScript
- **Styling:** Tailwind CSS v4
- **Charts:** Recharts (lightweight, React-native)
- **HTTP Client:** fetch (built-in, no axios needed)
- **Auth:** None (solo founder tool)
- **State:** React hooks (no Redux, no Zustand — too simple for state management)

## Architecture
```
frontend/                    ← Separate Next.js app in project root
├── src/
│   ├── app/
│   │   ├── layout.tsx       ← Root layout with sidebar nav
│   │   ├── page.tsx         ← Dashboard (overview stats)
│   │   ├── campaigns/
│   │   │   └── page.tsx     ← Launch + manage campaigns
│   │   ├── leads/
│   │   │   └── page.tsx     ← CRM pipeline view
│   │   ├── analytics/
│   │   │   └── page.tsx     ← Charts + A/B test results
│   │   └── settings/
│   │       └── page.tsx     ← One-time service config
│   ├── components/
│   │   ├── Sidebar.tsx
│   │   ├── StatsCard.tsx
│   │   ├── LeadCard.tsx
│   │   ├── CampaignCard.tsx
│   │   ├── PipelineColumn.tsx
│   │   └── MetricsChart.tsx
│   └── lib/
│       └── api.ts           ← API client wrapping FastAPI endpoints
├── tailwind.config.ts
├── next.config.ts
├── tsconfig.json
└── package.json
```

## Backend Connection
All data comes from the existing FastAPI API at `http://localhost:8000/api/v1`. No separate database. No data duplication.

```
Frontend (Next.js :3000)  ──HTTP──▶  Backend (FastAPI :8000)  ──▶  SQLite DB
```

## Screens

### Screen 1: Dashboard (Home Page `/`)
The first thing you see. Quick overview of everything.

**Shows:**
- Total leads, total sent, total replies, total interested (4 stat cards)
- Active campaigns with status badges
- Recent interested leads (the hot leads you should respond to NOW)
- Today's activity feed (what the system did today)

**User actions:** None — this is read-only overview.

### Screen 2: Campaigns (`/campaigns`)
Where you launch new outreach and manage existing campaigns.

**Shows:**
- Campaign creation form:
  - Search query (e.g., "restaurants")
  - Location (e.g., "Bristol")
  - Min lead score (default 50)
  - Max emails to send (default 20)
  - Your service offering (loaded from settings)
- List of active/completed campaigns with stats per campaign
- Campaign status: draft → active → paused → completed

**User actions:**
- Create new campaign (INPUT 1: query + location)
- Pause/resume campaign
- View campaign details

### Screen 3: Leads / CRM Pipeline (`/leads`)
Kanban-style pipeline showing all leads grouped by status.

**Shows:**
- Pipeline columns: NEW → ENRICHED → SCORED → CONTACTED → REPLIED → INTERESTED → CONVERTED
- Each lead card shows: business name, town, score, email, last action
- Filter by: campaign, town, score range, status
- Interested leads highlighted with reply text preview

**User actions:**
- Click lead to see full detail + activity log
- Move lead between statuses (drag or button)
- Mark as converted (you got a client!)
- Mark as lost

### Screen 4: Analytics (`/analytics`)
How your outreach is performing.

**Shows:**
- Campaign metrics: open rate, click rate, reply rate, conversion rate
- Daily send volume chart (bar chart)
- Best subject lines by open rate
- A/B test results with winner indicator
- Per-campaign comparison table

**User actions:** Read-only. Data comes from backend analytics.

### Screen 5: Settings (`/settings`)
One-time setup + configuration.

**Shows:**
- Your service description (what you offer to businesses)
- Your name and business name (for email signatures)
- SMTP configuration status (connected/not connected)
- API key status (Groq/OpenRouter/Gemini — connected or missing)
- Domain auth status (SPF/DKIM/DMARC check results)
- Compliance: business address, unsubscribe URL

**User actions:**
- Save service description (used in AI email generation)
- Check domain authentication
- View suppression list count

## Design Principles
- Dark mode by default (founder tool, used late at night)
- Minimal UI — no decorative elements, no illustrations
- Data-dense — show numbers, not pretty graphics
- Fast — static generation where possible, client-side data fetching
- Mobile-responsive but desktop-first (you'll use this on your laptop)

## Non-Goals
- No user authentication (you're the only user)
- No real-time WebSocket updates (polling or manual refresh is fine)
- No drag-and-drop (button-based status changes are simpler)
- No email composer (AI generates the emails, you just launch campaigns)
- No landing page or marketing site
