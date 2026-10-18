# Harden production security boundaries

## Summary
- Require authenticated actors and owner checks for orchestrator REST turn/history/approval/dispatch/delivery/interrupt flows.
- Route unauthenticated frontend mission starts into sign-in/sign-up instead of creating anonymous orchestrator state.
- Stabilize auth callback routing so local/dev sign-in returns to the current browser origin instead of flipping between localhost and 127.0.0.1.
- Add an account menu and a real Profile & Settings drawer with Account, Profile, Skills, Project Memory, and Preferences sections.
- Persist profile display name/default brief/default skills/private notes through the existing protected user profile API.
- Keep LLM/provider/agent adapter configuration out of user settings; those remain system/admin concerns.
- Lock production workspaces under a server-owned root, default agent dispatch back to local-dispatch, and document external CLI risk.
- Make normalized Postgres the default database-backed store, add relational constraints where the current model supports them, and harden full-store sync order.
- Remove the temporary `/dev` probe route, add GitHub CI, and upgrade/override audited dependencies.
- Expand the Postgres smoke check to cover core normalized entities and the current local-artifact model.

## Verification
- `corepack pnpm typecheck`
- `corepack pnpm lint`
- `corepack pnpm test`
- `corepack pnpm audit --audit-level moderate`
- `DATABASE_URL=postgres://roundtable:roundtable@localhost:5432/roundtable ROUNDTABLE_STORE_DRIVER=postgres_normalized ROUNDTABLE_STORE_KEY=codex_hardening_smoke2 corepack pnpm db:smoke:local`
- `NEXTAUTH_SECRET=ci-nextauth-secret NEXTAUTH_URL=http://localhost:3000 DATABASE_URL=postgres://roundtable:roundtable@localhost:5432/roundtable ROUNDTABLE_STORE_DRIVER=postgres_normalized corepack pnpm build`
- `NEXTAUTH_SECRET=ci-nextauth-secret NEXTAUTH_URL=http://localhost:3000 corepack pnpm build`
- Manual local smoke: dev-auth sign up, open account menu, open Profile & Settings, save Profile, inspect Skills/Project Memory tabs.
- Runtime API smoke: sign up through dev auth, open Settings, save Profile, visit Skills and Project Memory with no `/api/*` 4xx/5xx and no console errors.

