# Upgrade remix to 3.0.0-rc.2

## Summary

Bumps `remix` `3.0.0-beta.10` → `3.0.0-rc.2` (exact pin; lockfile updated via `npm install remix@3.0.0-rc.2 --save-exact`, no other deps touched). Installed tree now has `@remix-run/ui@0.9.0`, `@remix-run/spa@0.1.1`, `@remix-run/route-pattern` etc.

### rc.1 / rc.2 breaking-change audit — nothing applies

This app is a pure client-side Vite + Cloudflare Pages SPA that only imports `remix/ui` and `remix/route-pattern/match`. Every rc.1/rc.2 breaking change was grepped for and is N/A:

| Change | Result |
|---|---|
| `addEventListeners()` removed | never used — all listeners already `addEventListener(..., { signal })` |
| `rmx-*` → `data-rmx-*` (docs/tests too) | zero occurrences in `src/`, `index.html`, `tests/`, docs |
| `fileMap` → `mounts`, `fingerprint: true`, `files.cacheKey`, `getScriptEntry()`/`<ImportMap>`, HMR `data` record | no `remix/assets` / asset server / custom render pipeline — Vite owns bundling |
| router 405 / HEAD | no `remix/router` usage (Cloudflare `functions/` are plain handlers) |
| script children serialization | no server rendering |
| Atmosphere auth removal, `remix db`, `remix.json` | no auth provider, no Remix-managed DB/migrations (IndexedDB only), no Remix CLI config — nothing to consolidate |

### What changed beyond the bump

- **`handle.update()` during setup** (rc.2: now `console.warn` + skipped; pre-commit calls throw `Cannot call handle.update() before … initial render commits`). The app already avoided sync setup-time updates via `needs*Paint` guards in `SharePlusSheet`, `UnlockedPage`, `ReceivePage`. Those guards stay (they still prevent a warning + wasted paint); their comments no longer describe the old `"scheduleUpdate not implemented"` rejection.
- The two regression tests for that pattern (`share-plus-sheet.test.ts`, `receive-page.test.ts`) filtered unhandled rejections on `'scheduleUpdate'`, a string rc.2 no longer emits — they would have passed vacuously. They now also match `'handle.update()'` and assert `console.warn` never received an `Ignored handle.update()` message (verified the spy catches the rc.2 warning with a throwaway component that calls `handle.update()` in setup).
- Stale `beta.10` / `beta.5` references in `README.md`, `docs/contribute/environment.md`, `.github/workflows/ci.yml` → `rc.2`.

### Kept on purpose

- `src/lib/array-at-polyfill.ts` — `@remix-run/route-pattern` (and now `@remix-run/ui`'s reconciler) still call `.at(-1)`; the polyfill guards old WebViews and is unchanged.
- `src/components/lazy-page.tsx` deploy-window chunk recovery and the SW update flow — unrelated to anything Remix fixed upstream.
- No scroll-restoration / Navigation-API / CSS range-media / aborted-`renderToStream` workarounds existed to remove (the app never used frame navigation or SSR).

## Decisions for Kent

**Not migrating the hand-rolled router to `remix/spa` (`render()`/`run()` + `data-rmx-target`/`data-rmx-history`).** I evaluated `@remix-run/spa@0.1.1` and recommend staying on `src/router.tsx` for now:

1. `run()` drives navigation through the `remix/ui` runtime, which only intercepts when `window.navigation` **and** `NavigateEvent.prototype.sourceElement` exist (`@remix-run/ui/dist/runtime/navigation.js` → `getInterceptableNavigation`); otherwise it "gracefully degrades" to **full document navigation**. Firefox and older iOS Safari would reload the page on every in-app link — for a camera PWA that means dropping the live `getUserMedia` stream / recorder state mid-session. The current `pushState` router works everywhere in the `chrome107/safari16/firefox104` build targets.
2. `run()` renders route responses into the document's top frame and requires a `fetch-router`-style `Request → Response` layer. The app has no request/response model (all data is local IndexedDB, pages own their loading), and `index.html` owns a static boot hero inside `<main id="app">` for LCP that `createRoot(appEl)` takes over. Adopting `remix/spa` would be a rewrite of boot + every page's data
