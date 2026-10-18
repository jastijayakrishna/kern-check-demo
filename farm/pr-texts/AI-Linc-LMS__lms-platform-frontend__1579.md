# perf(fonts): stop re-downloading Satoshi, twice, on every page load

Part of the "site feels slow again" RCA. Two measured wins on the critical path of **every route, every tenant**.

## 1. Self-hosted fonts had no cache rule

`netlify.toml` gives `/assets/models/*` a year of immutable caching but nothing covers `/assets/fonts/*`, so Netlify served `public/` at its default `public, max-age=0, must-revalidate` — and answered with the **full body**, not a 304.

Measured on `learn.agileologyedu.com/login`:

```
25 KB  637 ms  /assets/fonts/satoshi/Satoshi-400.woff2   age: 0
25 KB  519 ms  /assets/fonts/satoshi/Satoshi-700.woff2
25 KB  637 ms  /assets/fonts/satoshi/Satoshi-500.woff2
```

75 KB re-downloaded on every document load. The preloads sit in the root layout, so that's every route, every visit.

## 2. The same font is fetched a second time from Fontshare

Satoshi was moved in-repo, but **all 24 tenants** that set `fontImportUrl` still point at `api.fontshare.com` for it:

```sql
tenants with a fontImportUrl: 24
  of which point at Satoshi (already self-hosted): 24
```

`ClientFontLink` injects that stylesheet, opening **two more third-party origins for four requests at ~200 ms each** — ~800 ms of DNS+TLS+RTT to fetch a family the browser already has locally.

The guard is narrow on purpose: an import is skipped only when **every** family it asks for is one we self-host, so a tenant asking for `satoshi + clash-display` still gets Clash Display. There's a test for exactly that case.

## Deliberately NOT in this PR

Making `AppChrome`'s shell a `dynamic()` import. It removes 223 KB from `/login` and passes typecheck — but it **fails the jobs-board suite** with 2 timeouts, and the same file passes on `origin/main` in 35s:

```
branch : Tests 2 failed | 41 passed   (142s)
main   : Tests 43 passed              (35s)
```

`dynamic()` delays `ChromeProvider` by a tick, so `MainLayout` renders its full non-nested layout first and collapses after. That is the same failure mode that forced the **#1148 revert**. It needs the provider kept synchronous with only the visual leaves lazy, plus its own verification — not something to rush into a perf PR.

## Verification

- 5 tests, revert-proofed: removing the cache rule and reverting the guard each fail.
- `npx tsc --noEmit` — clean apart from the two pre-existing `tutorAutoContinue.test.ts` errors.
- Full suite green with this change alone (the only failure was the AppChrome experiment, now dropped).

🤖 Generated with [Claude Code](https://claude.com/claude-code)
