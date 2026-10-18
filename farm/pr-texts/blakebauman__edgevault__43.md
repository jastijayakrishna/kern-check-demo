# feat(console): upgrade React Router 7 → 8

Upgrades `apps/console` from React Router **7.18.2 → 8.3.0**, following the [official v7→v8 guide](https://reactrouter.com/upgrading/v7): adopt the future flags on v7 first, fix the fallout, then take the major. Three commits, each independently green, so this is reviewable (and revertable) in stages.

### Why it wasn't just a version bump

`v8_middleware` changes `context` in loaders/actions from a plain object into a `RouterContextProvider`. This app reads Workers bindings off `context.cloudflare` in **61 places across 39 files**, so all of them break at once. Enabling the flag on v7 surfaced the entire surface as type errors up front rather than at runtime.

### The three steps

**1. `465e639` — align deps, enable the no-code flags**
`@react-router/dev` was still on 7.16.0 while `react-router` had moved to 7.18.2 (the dependabot PR bumped only one). Then `v8_splitRouteModules`, `v8_passThroughRequests`, `v8_trailingSlashAwareDataRequests`.

`passThroughRequests` hands loaders the raw `Request`, so `request.url` on a data request now carries a `.data` suffix. I checked all 22 `request.url` reads: every one takes `origin`, `protocol` or `searchParams` — none reads `pathname` — so none is affected.

**2. `4bd06b6` — move bindings onto the middleware context**
One typed context key in `app/lib/cloudflare.ts` holding `{ env, ctx }`. `workers/app.ts` is the sole writer (builds the provider, sets the value); all 61 readers go through `context.get(cloudflareContext)`. The `declare module 'react-router'` `AppLoadContext` augmentation is deleted — that interface no longer types the argument under middleware. `entry.server.tsx`'s `loadContext` param becomes `Readonly<RouterContextProvider>`.

**3. `82b7308` — the bump**
The flags graduate in v8, so the whole `future` block goes away (`splitRouteModules` is now a top-level field defaulting to `true`). Two documented renames remained: `meta()` gets `loaderData` not `data`, and `useMatches()` entries expose `loaderData` not `data`.

### Verification

Type checking alone wouldn't catch the failure mode that matters here — [cloudflare/workers-sdk#14555](https://github.com/cloudflare/workers-sdk/issues/14555) reports `instanceof RouterContextProvider` failing at runtime under the Cloudflare plugin from a dual-package hazard. So I booted the dev server and exercised the paths this migration actually touches:

- `/` and `/login` → **200**, correctly rendered; their loaders read bindings through the new context
- `/login.data` → **200** with a valid turbo-stream payload for root + login, covering `passThroughRequests` and the data-request URL change
- no `instanceof` failure, no runtime errors in the server log

Repo-wide: `biome ci`, `pnpm boundary`, `pnpm typecheck`, `pnpm test` (13 packages), `pnpm build` — all green.

### Notes

- `@cloudflare/vite-plugin` stays at 1.39.2. The newest (1.51.1) wants `wrangler ^4.120.0` and all 8 workspace packages are pinned to 4.98.0, so bumping it belongs in its own PR — nothing here needed it.
- Prerequisites were already satisfied: Node 26.5 (≥22.22), React 19.2.7 (the exact v8 minimum), Vite 7.3.5.
- `#14555` was closed for lack of a reproduction rather than by a fix, and it involved CJS deps (`@mui/material`) this app doesn't use — so the residual risk is real but unproven, and the dev-server run above is the evidence against it.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
