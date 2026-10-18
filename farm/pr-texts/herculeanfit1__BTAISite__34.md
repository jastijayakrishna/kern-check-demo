# fix: serve security headers via next.config.js headers()

**The site has been serving no security headers in production** — no CSP, no `X-Content-Type-Options`, no `Referrer-Policy`, no `Permissions-Policy`. They were declared in `staticwebapp.config.json` `globalHeaders`, which the Azure SWA Next.js hybrid adapter silently ignores. Verified against the SWA origin directly, ruling out Cloudflare: **0 of 5 present**.

## The policy

Declared in `next.config.js` `headers()` for `/(.*)`. Two relaxations, both forced by the codebase and documented inline:

| Directive | Why |
|---|---|
| `script-src 'unsafe-inline'` | Next's inline bootstrap runs on prerendered routes; no working nonce path exists (the nonce middleware never executed in this runtime) |
| `style-src 'unsafe-inline'` | components use inline `style=` attributes throughout; a Tailwind-only migration would let this tighten |

No `'unsafe-eval'`, no nonce directives, no `'strict-dynamic'`. GA and App Insights hosts are pre-allowed so the deferred analytics work needs no CSP change. **No HSTS** — the platform already serves one, and two differing HSTS headers is worse than one. `X-Frame-Options` is replaced by `frame-ancestors 'none'`.

## staticwebapp.config.json — surgical, not scorched

**Kept:** the `/about`, `/solutions`, `/contact` redirects. They return real 301s in production; replacing a working mechanism with an unproven one would be backwards.

**Removed as proven dead:** `globalHeaders`; `routes[].headers` (the `/` rule configured `max-age=60`, production served `s-maxage=31536000`); `responseOverrides` (401→`/login` and 403→`/unauthorized` point at nonexistent routes, and the 404 rewrite targets a file the build never emits — Next's `not-found` handles it, proven by `/banana`).

A header comment now records which parts of that schema the adapter actually honours.

## Two quality gates were validating the fiction

- **`g_security.sh`** grepped `staticwebapp.config.json` for a CSP and **required a `nonce-` string** — it was enforcing the literal `'nonce-{nonce}'` placeholder SWA never substituted, and passed for years while production served no CSP, because it only ever grepped a file. Now checks `next.config.js`, still rejects `'unsafe-eval'`, and rejects `'unsafe-inline'` in `default-src` specifically.
- **`g_test.sh`** ran `test:middleware` against a file this PR deletes. Now runs `test:security-headers`, which parses the exported config and asserts the directives that must never loosen.

## Deletions

`middleware.ts` — set `X-Development-Mode` in dev and nothing else, while its docstring pointed maintainers at the dead `globalHeaders` mechanism. Its test goes with it (subject removed); replaced by 5 real assertions.

## Deliberately kept

The Next `redirect()` stub pages for `/about`, `/solutions`, `/contact`. **They look redundant and are not** — `staticwebapp.config.json` doesn't run in local dev, so the stubs give dev parity with the production 301s.

`middleware.ts.bak` / `.bak-hybrid` stay — PLAN-004-adjacent cruft, not this PR's job.

## Verification

`npm run validate` — all six gates. Headers confirmed present in the **local built output**.

**Unproven:** whether `headers()` surfaces through the SWA adapter — the same adapter ignores `globalHeaders` and never runs middleware. Production verification follows the deploy; fallback rung is a minimal static-header middleware.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
