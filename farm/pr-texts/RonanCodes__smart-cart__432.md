# ✨ feat: real-time landing user counter (Durable Object + WebSocket)

## What

The landing's "N home cooks planning with Souso" number now ticks up **live** as people sign up, no refresh.

A single global `CounterDO` (Cloudflare Durable Object) holds the latest count and the set of open landing WebSockets (hibernatable). On signup the auth hook POSTs the new total to the DO, which broadcasts it to every open socket; the landing eases the displayed number up.

## How it's wired

- **`CounterDO`** (`src/lib/live-count/counter-do.ts`): hibernatable WebSockets (`ctx.acceptWebSocket` + `webSocketMessage`/`webSocketClose`). Count persisted in DO storage (survives hibernation) and **monotonic** (never ticks down). Pure count maths extracted to `counter-core.ts` and unit-tested (20 tests).
- **Export approach**: `export { CounterDO } from '#/lib/live-count/counter-do'` in `src/server.ts`. The re-export from the existing custom entry was enough — `wrangler deploy --dry-run` resolves the binding, no separate `src/worker.ts` needed.
- **wrangler.jsonc**: `durable_objects.bindings: [{ name: "COUNTER_DO", class_name: "CounterDO" }]` + `migrations: [{ tag: "v1", new_sqlite_classes: ["CounterDO"] }]` (DO storage = KV-style get/put, fine under sqlite classes).
- **Routing**: `/api/live-count` is forwarded to the global DO (`idFromName('global')`) inside the `createServerEntry` fetch wrapper, before delegating to Start. All other paths (SSR, server-fns, cron) pass through unchanged.
- **Signup bump**: `databaseHooks.user.create.after` calls `bumpLiveCount()` (best-effort, self-swallowing — never breaks sign-up). It reads the `COUNTER_DO` **binding** via `import('cloudflare:workers')` and POSTs the real `user`-table total (same source as the admin notifier / SSR `getUserCount`).
- **Landing client**: `useLiveCount` opens a WS on mount, seeds the DO with the SSR count on connect, and degrades to the static SSR count if the socket fails (guards for SSR / no-window). `useCountUp` eases the number up (respects `prefers-reduced-motion`).

## Validation gate (all green)

- `pnpm build` ✅
- `npx wrangler deploy --dry-run` ✅ — binding resolved: `env.COUNTER_DO (CounterDO) Durable Object`
- `pnpm typecheck` / `pnpm lint` (0 new errors) / `pnpm test` (1370 passing) ✅
- Pre-push gate (`pnpm quality`) passed.

## Merge note (Landing.tsx)

origin/main already has the beta-badge changes. My Landing.tsx edits are localized to the counter only: the import line, two hook calls after the `useState`s, and the social-proof `<p>` (gate on `liveCount`, display `displayCount` + `aria-live`). Easy to merge alongside any further beta-badge work.

## Prod risk notes

- DO is **additive**: a missing/failed binding degrades to the static SSR count everywhere (server route guarded, bump self-swallows, client falls back). Sign-up cannot be broken by the counter.
- First deploy creates the DO migration `v1`. Count seeds from the first client connect / first signup (monotonic, so a late seed can only correct upward).
- No merge here — left for orchestrator review of this prod-sensitive change.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
