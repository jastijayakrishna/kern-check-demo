# feat(api): Phase 0 spike — health + echo-headers route handlers

**Phase 0 of the API consolidation plan** (`docs/projects/API-CONSOLIDATION-PLAN-2026-07-24.md`) — the zero-risk spike that proves the core bet: **the SWA managed hybrid backend serves `/api/*` natively with no linked backend**, for the cost of one tiny PR.

## What this adds
| File | Purpose |
|---|---|
| `app/api/health/route.ts` | `GET` → `{"status":"ok"}`, byte-identical to the Functions health endpoint the CI post-deploy verification greps for. `force-dynamic` + `Cache-Control: no-store`. |
| `app/api/echo-headers/route.ts` | **Temporary — removed in Phase 3 (plan A5).** Returns request header *names* + the client-IP header *values only* (never cookies/authorization), plus a per-request timestamp. Confirms `/api/*` reaches Next through SWA + Cloudflare with a usable client IP for the Phase 3 rate limiter. |

## How to verify
**On this PR's preview environment** (`deploy-pr-to-azure`):
- `GET <preview>/api/health` → `{"status":"ok"}`
- `GET <preview>/api/echo-headers` → JSON with `headerNames`, `clientIp`, `timestamp`; call it twice → the timestamps differ, proving live execution rather than an edge-cached 200 (plan Q8)

**On production after merge** (the Phase 0 gate — verified on `bridgingtrust.ai`, GET not HEAD):
- `/api/health` returns `{"status":"ok"}` with the backend still unlinked
- the CI **health poll goes green** for the first time; the `/api/contact` probe stays red until Phase 3, so `deploy-main-to-azure` remains red and comments on issue #46 — **expected, and now red for the right reason** (the health half proves the route handler works)

## Scope / safety
- Two additive files; no existing code touched. **The backend link is never touched — it stays unlinked.**
- `staticwebapp.config.json` untouched (its `/api/*` rule already permits these methods with no auth).
- Local `npm run validate`: **6/6 gates green** (build, type-check, lint, 110 tests, security, deploy-check).

**Not merged — STOP per the ritual.** This ends at a mandatory STOP so you can eyeball the Phase 0 gate before Phase 1. Merge when ready and I'll run the production verification, then report the gate table with actuals.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_016HDXTwVi2fbm3kfAR1xMwT

