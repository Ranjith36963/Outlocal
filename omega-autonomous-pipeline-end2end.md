# OMEGA AUTONOMOUS PIPELINE — CLAUDE CODE INSTRUCTIONS

You are building a production-grade, independent, money-making software product. You will work autonomously through multiple sessions until every feature in feature_list.json passes. You do not stop until the product is complete.

---

## YOUR INPUT FILES

You have three files. Read all three before doing anything:

1. **The PRD** — The Product Requirements Document file in the project root. Search for the .md file containing "Product Requirements Document" or "PRD" in the project files. This defines WHAT to build across 16 dimensions. The PRD is sacred — you do not modify it. Everything you build must satisfy it.

2. **PROJECT_RESEARCH.md** — Open-source research report in the project root. Maps the best repos for each pipeline step. This is your STARTING POINT for open-source intelligence, not the final answer. You will update and expand this as you work. Use repos as intelligence sources — study their architecture, extract patterns, then build your own version. Never copy code. Never add repos as dependencies when you can build a better, focused version.

3. **This file (omega-autonomous-pipeline-final.md)** — Your operating instructions. How to work, what to do at each phase, how to manage context, how to avoid known failure modes. Follow these instructions exactly.

---

## HUMAN SETUP (before first run — founder does these manually)

These are the ONLY things that require human action. Everything else is autonomous.

1. **Git remote** — Create the GitHub repo and set the remote URL. Claude Code will push to it.
2. **API keys** — Create and add to .env file:
   - Claude API key (ANTHROPIC_API_KEY)
   - Any project-specific API keys from PRD (e.g., Google Places API, Stripe, ESP)
3. **Domain + DNS** — If project needs a live URL, set up domain and point DNS
4. **VPS access** — If deploying to VPS, provide SSH credentials or Docker registry access
5. **Third-party accounts** — Create accounts for services in PRD (e.g., Stripe, Postmark, Google Cloud Console)
6. **Webhooks** — Configure webhook URLs in third-party dashboards that point to your deployment

Claude Code does everything else: repo structure, code, tests, deployment config, documentation.

---

## FIRST SESSION: BOOTSTRAP

On your very first session in this repo, before any feature work, do ALL of the following:

### Step 1: Set up repo structure
```
project-name/
├── CLAUDE.md
├── HANDOFF.md
├── CHANGELOG.md
├── feature_list.json
├── init.sh
├── .claude/
│   ├── settings.json
│   ├── skills/  (13 SKILL.md files)
│   ├── agents/  (2 subagent definitions)
│   ├── rules/
│   └── hooks/
├── docs/
│   ├── plans/
│   ├── research/
│   ├── architecture/
│   └── releases/
├── src/
├── tests/
├── scripts/
├── docker-compose.yml
├── Dockerfile
├── .env.example
├── .gitignore
├── README.md
└── SETUP.md
```

### Step 2: Write CLAUDE.md
Keep under 200 lines. CLAUDE.md survives context compaction — it is re-read from disk. Conversation instructions do NOT survive. Put all critical rules here.

Must contain:
- Project name and one-sentence description (from PRD)
- Tech stack (from PRD)
- All shell commands: build, test, typecheck, lint, start dev server
- Architecture reference: `@./docs/architecture/current.md`
- These exact workflow rules:

```
IMPORTANT: Read HANDOFF.md and CHANGELOG.md before starting ANY work.
IMPORTANT: Run smoke test before implementing new features.
IMPORTANT: ONE feature at a time. Never one-shot everything.
IMPORTANT: Write tests FIRST, implementation SECOND (TDD).
IMPORTANT: NEVER delete or modify existing tests.
IMPORTANT: Commit and push after every meaningful unit of work.
IMPORTANT: Run tests before every commit. Never commit code that breaks existing tests.
IMPORTANT: Update HANDOFF.md before every session exit or compaction.
IMPORTANT: If approaching max-turns limit, write HANDOFF.md IMMEDIATELY before your final turn.
IMPORTANT: Log failed approaches in CHANGELOG.md with WHY they failed.
IMPORTANT: Use open-source research before writing implementation code — study the best repos first.
Do not stop tasks early. Continue until ALL features in feature_list.json pass.
Your context window will be automatically compacted as it approaches its limit. Save progress to HANDOFF.md before compaction. Do not stop early due to token concerns.
```

- Code style (from PRD tech stack)
- Security rules: never commit secrets, validate inputs, parameterize SQL
- Reference to `.claude/rules/security.md`

### Step 3: Generate feature_list.json from the PRD
Read every pipeline step in the PRD. Convert each into testable features. Use JSON format — models are less likely to overwrite JSON than Markdown.

Format:
```json
[
  {
    "id": "F001",
    "category": "core",
    "description": "What this feature does in one sentence",
    "steps": ["Step 1 to verify", "Step 2 to verify", "Step 3 to verify"],
    "passes": false
  }
]
```

Every pipeline step in the PRD becomes 1-5 features. Each feature must be independently testable. Aim for 50-100 total features depending on project complexity.

### Step 4: Install dependencies
Read the PRD tech stack. Set up the project's language and package ecosystem:
- **Python projects:** Create virtual environment, write requirements.txt, run `pip install -r requirements.txt`
- **Node projects:** Write package.json, run `npm install`
- **Both:** Install whatever the PRD specifies
- Install Playwright for QA testing: `pip install playwright && playwright install chromium` or `npx playwright install chromium`
- Verify all core imports work by running a simple smoke script

### Step 5: Write init.sh
A script that starts the dev server. Every subsequent session reads this first to avoid wasting tokens figuring out how to run the project. Include dependency checks and virtual environment activation if applicable.

### Step 6: Create .claude/settings.json
Write hooks using the ACTUAL commands from the PRD tech stack — do NOT hardcode npm or pip. Read the PRD to determine the correct test, lint, and typecheck commands for this project.

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Bash",
      "hooks": [{
        "type": "command",
        "command": "node .claude/hooks/block-dangerous-commands.js",
        "timeout": 10
      }]
    }],
    "PostToolUse": [{
      "matcher": "Edit|MultiEdit|Write",
      "hooks": [{
        "type": "command",
        "command": ".claude/hooks/auto-format.sh",
        "timeout": 30
      }]
    }],
    "Stop": [{
      "hooks": [{
        "type": "command",
        "command": ".claude/hooks/lint-on-stop.sh"
      }]
    }],
    "PreCompact": [{
      "hooks": [{
        "type": "command",
        "command": "node .claude/hooks/save-state-before-compact.js"
      }]
    }]
  }
}
```

**Note on permissions:** When running interactively, add a `permissions` block with project-specific allow/deny rules. When running with `--dangerously-skip-permissions` (headless), permissions are bypassed entirely — only `--disallowedTools` applies.

Hooks fire 100% of the time. CLAUDE.md rules fire ~80%. Anything that MUST happen goes in hooks.

Known bug: hooks silently stop firing after ~2.5 hours. Restart sessions before this threshold.

**Hook scripts must use the correct commands for this project's tech stack:**
- `auto-format.sh` — runs the project's formatter (prettier for JS/TS, black for Python, etc.)
- `lint-on-stop.sh` — runs the project's linter + typechecker + test command (e.g., `ruff check . && mypy . && pytest` for Python, `npm run lint && npm run typecheck && npm test` for Node)
- `block-dangerous-commands.js` — blocks `rm -rf`, `sudo`, `curl | sh`
- `save-state-before-compact.js` — writes current progress to HANDOFF.md

### Step 7: Write the 13 SKILL.md files
Each skill goes in `.claude/skills/NN-skillname/SKILL.md`. Each must be under 500 lines. The `description` field is a trigger — it tells you WHEN to activate this skill. Write each using the detailed instructions in the "13 SKILLS" section below.

### Step 8: Write the 2 subagent definitions
Place in `.claude/agents/`. Details in the "SUBAGENTS" section below.

### Step 9: Create initial HANDOFF.md and CHANGELOG.md
HANDOFF.md: "First session. Bootstrap complete. Ready to start Feature F001."
CHANGELOG.md: "Project initialized. No features built yet."

### Step 10: Git init, commit, push
Initialize git. Add all files. Commit with message "Bootstrap: repo structure, CLAUDE.md, feature_list.json, skills, hooks". Push to remote (the remote URL should already be configured by the founder).

---

## EVERY SESSION AFTER BOOTSTRAP: SESSION START PROTOCOL

At the start of every session, before ANY feature work:

```
1. Run: pwd
2. Read: CLAUDE.md (for project rules and commands)
3. Read: HANDOFF.md (for where you left off)
4. Read: CHANGELOG.md (for failed approaches — DO NOT re-attempt these)
5. Read: feature_list.json (find highest-priority feature where passes = false)
6. Run: ./init.sh (start dev server)
7. Run: smoke test (verify existing features still work)
8. Only THEN begin work on the next feature
```

If the smoke test fails, fix the broken feature FIRST before starting new work.

---

## THE 13 SKILLS

### Skill 1: /think
```
---
name: think
description: Triggers when starting work on a new feature or making scope decisions
---
```
What you do:
- Read the feature from feature_list.json
- Generate 5-10 approaches to implement it. No filtering. Creative thinking.
- For each approach, state: what it solves, what it misses, implementation cost, risk level
- Challenge scope: Is this the right thing to build? Does it create or protect revenue?
- Consider four modes: EXPAND (ambitious version), SELECTIVE EXPAND (baseline + opportunities), HOLD SCOPE (exactly what's specified), REDUCE (minimum viable)
- Select the best approach with justification
- Ask: "If this is the ONLY feature that ships, does it still deliver value?"

### Skill 2: /writing-plans
```
---
name: writing-plans
description: Triggers after /think to crystallize decisions into a buildable plan
---
```
What you do:
- Write a structured plan with clear boundaries: what's IN scope, what's OUT
- Define "done" in testable terms that map to feature_list.json steps
- List assumptions, risks, dependencies
- Include: which open-source patterns to study (from PROJECT_RESEARCH.md)
- Save to `docs/plans/feature-FXXX-plan.md`
- Verify plan against feature_list.json requirements — every step must be covered

### Skill 3: /research-and-extract (THE OMEGA LAYER)
```
---
name: research-and-extract
description: Triggers before writing ANY implementation code. Studies open-source repos to extract patterns.
---
```
What you do:

Stage 1 — Identify targets:
- Read PROJECT_RESEARCH.md for this feature's pipeline step
- Identify top 3-5 repos by stars, activity, relevance
- If research report doesn't cover this or is stale, search GitHub fresh

Stage 2 — Study source code:
- Spawn research-explorer subagent (keeps your context lean)
- Subagent clones repos to `/tmp/research/`, studies source code, deletes after extraction
- Subagent reads ACTUAL source code — architecture, data models, API design, error handling
- Subagent returns structured report: what works, what's poor, key patterns

Stage 3 — Extract patterns:
- Write to `docs/research/feature-FXXX-patterns.md`
- Document: data structures, algorithms, API contracts, config schemas
- Check license compatibility
- Flag: clever-but-fragile vs boring-but-bulletproof. ALWAYS prefer boring-but-bulletproof.

Stage 4 — Design your version:
- Using patterns as INTELLIGENCE (not code to copy), design the implementation
- Must be: simpler, focused on YOUR use case, production-grade
- Write brief spec referencing which patterns adopted and why

Stage 5 — Update knowledge:
- If you found better repos than PROJECT_RESEARCH.md, update it
- The research report is v1. Your live research is v2, v3, v∞.

RULES:
- NEVER write implementation code without completing Stages 1-3
- NEVER say "I already know how to do this" — check the research first
- NEVER install a repo as a dependency when you can build a focused version
- ALWAYS prefer boring-but-bulletproof over clever-but-fragile

### Skill 4: /plan-eng-review
```
---
name: plan-eng-review
description: Triggers after research, before implementation. Locks in architecture.
---
```
What you do:
- Define architecture: system boundaries, data flow, component interactions
- DRAW DIAGRAMS (Mermaid or ASCII): sequence, state, component, data-flow. Diagrams force hidden assumptions into the open.
- Define edge cases and failure modes for each component
- Define trust boundaries: what's inside the security perimeter, what's outside
- Define deployment architecture: cron jobs, API endpoints, queue workers
- Build test matrix: what to test, how, what "pass" looks like
- Save to `docs/architecture/feature-FXXX-architecture.md`

### Skill 5: /plan-design-review
```
---
name: plan-design-review
description: Triggers for user-facing features only. Skip for API-only or internal tools.
---
```
What you do:
- Audit UI across: typography, spacing, hierarchy, color, responsive, interactions, motion, content, performance, AI slop
- AI Slop Detection: flag purple gradients, 3-column icon grids, uniform border-radius, centered text everywhere
- Grade each category A through F
- Report only — no code changes in this phase
- SKIP entirely for API-only projects or internal tools

### Skill 6: /subagent-driven-development
```
---
name: subagent-driven-development
description: Triggers for non-trivial implementation. Spawns specialized subagents.
---
```
What you do — spawn THREE subagents:

1. **Spec Reviewer subagent**: Receives plan + architecture. Reviews for gaps, ambiguities, missing edge cases. Returns: approved spec or issues list.

2. **Implementer** (you, main agent): Write the code with research patterns as context. One feature at a time. Clean git after each.

3. **Code Quality Reviewer subagent**: Receives code in SEPARATE context (no knowledge of your shortcuts). Reviews: security, error handling, test coverage, performance, duplication. Returns: severity-ranked findings with file:line.

This three-part split IS the generator-evaluator pattern. Separate context = honest evaluation. Single agent + subagents uses 70% fewer tokens than agent teams.

### Skill 7: /test-driven-development
```
---
name: test-driven-development
description: Triggers for ALL implementation. Tests first, code second. Always.
---
```
What you do:
1. Write tests FIRST defining what code should do
2. Announce "doing TDD" to prevent mock implementations
3. Confirm tests FAIL before writing implementation
4. Commit tests
5. Write code to make tests pass
6. NEVER modify tests to make them pass — fix the implementation
7. Run full suite to verify nothing broke
8. Commit implementation

Test design (optimized for LLM):
- Few lines of output per test
- ERROR on same line as reason (grep-friendly)
- Include a `--fast` flag for 10% random subsample
- Coverage: 80%+ business logic, 100% payment/auth
- Spawn test-runner subagent for verbose output

### Skill 8: /systematic-debugging
```
---
name: systematic-debugging
description: Triggers when something fails. Investigate systematically, never guess.
---
```
What you do:
1. Reproduce with minimal test case
2. Form 3-5 hypotheses, ranked by likelihood
3. Test EACH methodically
4. Fix ROOT CAUSE, not symptom
5. Add regression test
6. Run full suite
7. Log failure and fix in CHANGELOG.md

### Skill 9: /careful
```
---
name: careful
description: Triggers for code touching money, auth, credentials, client data, API keys.
---
```
What you do:
- Slow, thorough, line-by-line review
- OWASP Top 10 check
- STRIDE threat model
- Verify: inputs validated, SQL parameterized, no secrets in code, errors handled without leaking internals
- First run: create .env.example with all required env vars documented, verify .env in .gitignore
- Payment code: test success, failure, webhook retry, idempotency

### Skill 10: /qa
```
---
name: qa
description: Triggers after implementation. Runs as SUBAGENT in separate context.
---
```
Runs as subagent — separate context. This IS the generator-evaluator pattern for live app testing.

QA subagent:
- Tests live running application (not just unit tests)
- Web apps: Playwright browser testing — clicks, forms, navigation
- APIs: curl/httpie/Hurl on every endpoint
- Grades against HARD thresholds
- Performance benchmarking against targets
- Bugs: reports with file, line, what's wrong, what should happen
- Auto-generates regression tests per bug
- Main agent fixes, QA re-verifies

**QA fix loop cap: if the same bug fails QA 3 times after 3 different fix attempts, log the bug in CHANGELOG.md with all attempted fixes and WHY they failed, then move to the next feature. Return to this bug later with fresh context.**

Layered QA — all three must pass:
```
Layer 1: Deterministic — compile, tests pass, lint clean, types check
Layer 2: Security — no secrets, deps scanned, inputs validated
Layer 3: Agentic — QA subagent tests live app, grades OUTCOMES not PATHS
```

### Skill 11: /verification-before-completion
```
---
name: verification-before-completion
description: Final gate. Nothing ships without this.
---
```
What you do:
1. Re-read feature requirements from feature_list.json
2. Verify EACH step met with evidence
3. Run full test suite
4. Check: code matches plan, plan matches requirement
5. Verify no regressions
6. ONLY if all pass: set `"passes": true` in feature_list.json
7. NEVER say "done" without all checks

### Skill 12: /ship
```
---
name: ship
description: Triggers when feature is verified. Git, deploy, post-deploy verify.
---
```
What you do:
1. Sync with main branch
2. Run full suite + type checking
3. Audit coverage
4. Git commit: "feat(FXXX): [description]"
5. Push to remote
6. First run: bootstrap CI, Docker config, test framework
7. Deploy: `docker compose pull && docker compose up -d`
8. Post-deploy: hit endpoints, check health, check logs
9. If fails: /systematic-debugging → `git revert` → re-ship

### Skill 13: /document-release
```
---
name: document-release
description: Triggers after successful deployment. Updates all docs.
---
```
What you do:
- Update README.md, SETUP.md, API docs
- Generate CHANGELOG.md entry
- Catch stale references
- Every note: what changed, why it matters

---

## SUBAGENTS

### .claude/agents/research-explorer.md
```markdown
---
name: research-explorer
description: Explores open-source repos to extract architectural patterns
tools: Read, Bash, Grep, Glob
model: sonnet
memory: project
maxTurns: 15
---
You study open-source code. For each repo you are given:
1. Clone to /tmp/research/ (git clone --depth 1 for speed)
2. Read actual source code, not README
3. Identify: architecture, data models, API design, error handling, performance
4. Rate: clever-but-fragile vs boring-but-bulletproof
5. Check license compatibility
6. Delete the cloned repo when done (rm -rf /tmp/research/repo-name)
Return structured report with code snippets. Under 2000 tokens.
```

### .claude/agents/test-runner.md
```markdown
---
name: test-runner
description: Runs tests, returns concise results
tools: Bash, Read
model: sonnet
maxTurns: 5
---
Run full test suite. Return ONLY:
1. Pass/fail count
2. Failed test names with ERROR messages
3. Coverage percentage
Under 500 tokens.
```

---

## CONTEXT MANAGEMENT

Beyond 40% context, you become unreliable. This is the #1 failure cause.

Rules:
1. Compact at 50-80%: `/compact Focus on [current feature]`
2. Subagents for verbose ops (tests, logs, research)
3. CLAUDE.md survives compaction. Conversation does NOT.
4. Persistent memory = HANDOFF.md + CHANGELOG.md + feature_list.json
5. `/clear` between unrelated tasks
6. If approaching max-turns limit, write HANDOFF.md IMMEDIATELY — max-turns exit is a hard stop, not a compaction, and PreCompact hook will NOT fire.

Before EVERY exit or compaction:
1. Write state to HANDOFF.md
2. Update CHANGELOG.md with failed approaches
3. Update feature_list.json
4. Clean git state

Environment:
```bash
CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=75
CLAUDE_CODE_MAX_OUTPUT_TOKENS=32000
DISABLE_NON_ESSENTIAL_MODEL_CALLS=1
```

---

## THE AUTONOMOUS LOOP

```
SESSION START
  → Read CLAUDE.md, HANDOFF.md, CHANGELOG.md
  → Read feature_list.json → pick next incomplete
  → Run init.sh → smoke test
  ↓
PHASE 1: THINK
  → /think → /writing-plans
  → GATE: plan covers feature_list.json steps
  ↓
PHASE 2: RESEARCH (OMEGA LAYER)
  → /research-and-extract
  → Study repos → extract patterns → design own
  ↓
PHASE 3: DESIGN
  → /plan-eng-review → /plan-design-review (UI only)
  → GATE: architecture verified against research
  ↓
PHASE 4: BUILD
  → /subagent-driven-development (3 subagents)
  → /test-driven-development (tests FIRST)
  → /systematic-debugging (when broken)
  → /careful (money, auth, data)
  → One feature. Clean git.
  ↓
PHASE 5: SHIP
  → /qa (subagent — live test, benchmark, grade)
     → FAILS? → back to BUILD (max 3 fix attempts per bug)
  → /verification-before-completion (final gate)
  → /ship (deploy + post-deploy verify)
  → /document-release
  → Update HANDOFF.md, CHANGELOG.md, feature_list.json
  ↓
NEXT FEATURE
  → Pick next passes = false
  → Loop to PHASE 1
  → Continue until ALL pass
  ↓
ALL FEATURES PASS — PROJECT COMPLETE
  → Run full test suite one final time
  → Run /qa across entire application (full regression)
  → Write final CHANGELOG.md entry: "All features complete"
  → Update README.md with complete project documentation
  → Git tag: v1.0.0
  → Deploy final version
  → Write HANDOFF.md: "Project complete. All features passing. Deployed v1.0.0."
```

Do not stop until all features pass. If stuck after 3 serious attempts on one feature, log in CHANGELOG.md and move on. Return later with fresh context.

---

## KNOWN FAILURES — AVOID THESE

| Failure | What You Do Instead |
|---------|-------------------|
| One-shotting | ONE feature at a time |
| Self-evaluation blindness | QA + code-quality subagents judge in separate contexts |
| Context degradation >40% | Compact at 50%. Subagents for verbose ops. |
| Agentic laziness | Do not stop. Next feature. |
| Test deletion | NEVER modify tests. Fix code. |
| Dead-end re-attempts | Read CHANGELOG.md first. |
| Premature completion | feature_list.json is ground truth. |
| Infinite QA loop | Max 3 fix attempts per bug. Then log and move on. |
| Infinite loops on judgment | Only loop on testable outcomes. 3 attempts then move on. |
| Max-turns hard stop | Write HANDOFF.md BEFORE your final turn. |

---

## INFRASTRUCTURE

Autonomous loop script:
```bash
#!/bin/bash
# Create log directory
mkdir -p agent_logs

while true; do
    COMMIT=$(git rev-parse --short=6 HEAD 2>/dev/null || echo "init")
    LOGFILE="agent_logs/agent_${COMMIT}_$(date +%s).log"
    
    # Check if all features pass — if so, exit the loop
    if command -v python3 &>/dev/null; then
        ALL_PASS=$(python3 -c "
import json
with open('feature_list.json') as f:
    features = json.load(f)
print('yes' if all(f.get('passes') for f in features) else 'no')
" 2>/dev/null || echo "no")
        
        if [ "$ALL_PASS" = "yes" ]; then
            echo "All features pass. Project complete." | tee -a "$LOGFILE"
            break
        fi
    fi
    
    # Run Claude Code with a short prompt that reads the full instructions from disk
    claude --dangerously-skip-permissions \
           -p "Read omega-autonomous-pipeline-final.md in this repo for your full instructions. Read HANDOFF.md for where you left off. Continue building until all features in feature_list.json pass." \
           --max-turns 50 \
           --max-budget-usd 10 \
           --model claude-opus-4-6 \
           &> "$LOGFILE"
    
    sleep 5
done
```

---

## MODEL ROUTING

| Phase | Model | Effort | Why |
|-------|-------|--------|-----|
| Think/Plan | Opus 4.6 | max | Get it right first time. No rework. |
| Research | Opus 4.6 | high | Deep understanding of repo patterns. 1M context. |
| Design | Opus 4.6 | max | Architecture must be bulletproof. |
| Build | Opus 4.6 | max | Zero mistakes on first go. --dangerously-skip-permissions means no safety net. |
| QA subagent | Sonnet 4.6 | high | Parallel evaluation at 1/5th cost. Multiple reviewers cheap. |
| Test runner subagent | Sonnet 4.6 | medium | Running tests and reporting results is straightforward. |
| Research explorer subagent | Sonnet 4.6 | medium | Reading repos and extracting patterns. Returns summary. |
| Ship/Deploy | Sonnet 4.6 | high | Git, deploy, post-deploy verify — well-defined steps. |
| Document release | Sonnet 4.6 | medium | Updating docs is routine. |

Main agent: Opus 4.6 (max effort). Gets it right first time. No rework loops.
Subagents: Sonnet 4.6. They do focused tasks, return summaries. Cost-efficient at 1/5th price.
Ship/docs: Sonnet 4.6. Well-defined procedures, no judgment calls needed.

---

## SUMMARY

3 input files: PRD + Research + This Document.
13 skills. 2 subagents. 4 hooks. 3 progress files. 5 phases.
1 rule: Do not stop until all features pass.
