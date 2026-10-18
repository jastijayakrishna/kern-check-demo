# fix(worker): stop importing next/headers at module scope so jobs can run

## Production incident

`inflect-worker-1` is in a restart loop on the prod VM (24 restarts at time of writing):

```
Error: ERR_MODULE_NOT_FOUND  url: file:///app/node_modules/next/headers
Node.js v24.19.0
```

`scripts/worker.ts` is a plain Node process, not a Next runtime, so `next/headers` is not resolvable inside it.

The chain is one edge long, and that's what makes it so damaging:

```
scripts/worker.ts
  └─ …any job… ─ any usecase
       └─ src/app-layer/context.ts:2   import { getSessionOrThrow } from '@/lib/auth'
            └─ src/lib/auth.ts:15      import { cookies } from 'next/headers'   ← dies here
```

`context.ts` is what every usecase imports for `getTenantCtx`, so a single static import at module scope killed the process before one executor could register.

## What this means for everything else

**No background job has ever run in production.** Not the data-lifecycle retention sweep, the evidence-expiry monitor, the deadline monitor, notification digests, or the audit-stream flush.

Nothing failed loudly — the jobs simply never executed, and every surface reading their output showed a quiet, plausible zero. This is worth holding in mind when reading any finding that assumes a sweep runs: the current evidence-retention audit says the purge "deletes rows but not blobs", but it isn't deleting anything, because the job never fires.

It also settles an open design question: an async-scan job for the AV work would have sat in Redis forever.

## The fix

The codebase already has the right pattern in the two other places that need request headers off the request path — `src/auth.ts:466` and `src/lib/security/session-tracker.ts:88` both use `await import('next/headers')` at the use site. `lib/auth.ts` was the one that didn't.

Its single use of `cookies()` sits inside a `LEGACY_JWT_SECRET`-guarded branch already wrapped in `try/catch`, so a non-request runtime now falls through to `return null` exactly as an absent cookie does. No behaviour change on the web path.

## The guard

`tests/guards/worker-safe-imports.test.ts` — named for the invariant, not this diff: **worker-reachable code (`src/lib`, `src/app-layer`) may not statically import a Next-server-only module** (`next/headers`, `next/navigation`, `server-only`). A dynamic `await import(...)` is explicitly allowed and is the intended escape hatch.

It also asserts the *other* direction — that the three known use sites still reach `next/headers` dynamically — so someone "tidying" a dynamic import back into a static one reintroduces the crash and gets told.

`"use client"` modules are excluded. That's a statement about the runtime (browser code cannot be in the worker graph, and `next/navigation` hooks belong there) rather than a carve-out for convenience; a *server* module that wants an exemption gets a dynamic import instead. Exactly one file relies on it: `src/lib/hooks/useUrlFilters.ts`.

**Mutation-verified:** putting the static import back turns the guard red and names `src/lib/auth.ts`. Without that check the guard could have been vacuous.

## Verification

- worker-safe-imports: 6/6
- auth suites (`tests/unit/auth`, `credentials-auth`, `auth-server-gate-coverage`, `auth-surface-tokens`): 6 suites / 55 tests green

**Post-merge:** the worker needs watching on the VM to confirm it stays up and the job backlog drains — a green CI run only proves the import is gone, not that the process survives. I'll verify directly after deploy.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
