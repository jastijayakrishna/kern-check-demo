# Wire up @supabase/server for JWT verification in /api/analyze

## Summary
- Installs `@supabase/server` (the new Supabase server-utilities SDK) for project `pkydkbuodikttfeawqsw`.
- Replaces the hand-rolled `createClient(url, anonKey).auth.getUser(token)` auth check in `src/app/api/analyze/route.ts` with `verifyAuth(req, { auth: 'user' })` from `@supabase/server/core` — cryptographic JWT verification against the project's JWKS instead of a network round-trip to the Auth API.
- Adds the new server-only, non-secret env vars to `.env.local.example`: `SUPABASE_URL`, `SUPABASE_PUBLISHABLE_KEY`, `SUPABASE_JWKS_URL`.
- `SUPABASE_SECRET_KEY` is intentionally left as an unset/commented placeholder — no route currently needs `createAdminClient`/`auth: 'secret'`, and the real value must never be committed.
- `foundry-console/` is untouched: it's deliberately client-only + RLS-enforced (its README states the service-role key is never used in its frontend, and it has no server routes), so `@supabase/server` has no consumer there yet.
- Installed the `supabase-server` AI-coding skill via `npx skills add supabase/server` (`.agents/skills/`, `.claude/skills/`, `.hermes/skills/`, `skills-lock.json`), matching the existing convention from the `emilkowalski/skills` install.

## Required env vars (repo / Vercel)
Add to the Vercel project's environment variables (Production, Preview, Development) alongside the existing `NEXT_PUBLIC_SUPABASE_*` / `ANTHROPIC_API_KEY` vars:
- `SUPABASE_URL=https://pkydkbuodikttfeawqsw.supabase.co`
- `SUPABASE_PUBLISHABLE_KEY=sb_publishable_obr-7Y0u02p5c5pD-5f3Sw_zda5lWTa`
- `SUPABASE_JWKS_URL=https://pkydkbuodikttfeawqsw.supabase.co/auth/v1/.well-known/jwks.json`

None of these are secret. `SUPABASE_SECRET_KEY` is not required by this change and was not set anywhere — add it later only if a route needs to bypass RLS.

## Housekeeping note
A local-only, unpushed branch `codex/supabase-server-setup` (single scaffold commit `chore: add Supabase server SDK`) also touches `package.json`/`.env.local.example` for the same package, but doesn't wire it into any route and repurposes the publishable key as `NEXT_PUBLIC_SUPABASE_ANON_KEY`'s value (a browser-client decision out of scope here). This PR supersedes it — recommend deleting that branch after this merges.

## Test plan
- [x] `npx tsc --noEmit` — clean
- [x] `npm run build` — succeeds, `/api/analyze` still builds as a dynamic route
- [x] `npm run lint` — only pre-existing, unrelated warnings
- [ ] Manual: sign in via the Constraint Validator UI and confirm `/api/analyze` still accepts a valid session token and rejects an invalid/missing one, once the env vars above are set in Vercel

🤖 Generated with [Claude Code](https://claude.com/claude-code)
