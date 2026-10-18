# Reapply #301: /ops/promotions Partner Preview demo — the deploy failure was unrelated

Reapplies #301 (reverted in #302). **The revert was based on a wrong inference of mine — #301 never caused the deploy failure.**

## What actually failed

The Vercel build log for `0e51fb3`:

```
src/app/layout.tsx
`next/font` error:
Failed to fetch `Geist Mono` from Google Fonts.
  [Error: Failed to fetch font file from `https://fonts.gstatic.com/s/geistmono/...woff2`]  ×6
> Build failed because of webpack errors
```

`next/font/google` downloads font files **at build time**, so a transient failure reaching `fonts.gstatic.com` from the build container fails the whole build — in `src/app/layout.tsx`, a file #301 never touched.

## Why I got it wrong

The two commits before #301 deployed green, #301 failed, and the revert deployed green. I read that sequence as proof of causation. It wasn't — the revert simply built at a moment when the font fetch succeeded. A flaky, network-dependent build step produces exactly the pattern of a real bisect, and I should have insisted on the log before acting on the inference rather than after.

## This PR

An **exact reapply** — `git diff 0e51fb3 HEAD` is empty, so the content is byte-identical to what was reviewed and merged in #301 (including the review fixes: the price-raise guard, PIVOTA-code trust, brand scope, `humanReadableRule`, and the 9-test store suite).

Verified on a clean worktree: `npm ci` → `npm run build` exit 0 (`/ops/promotions` emitted, 10 kB), vitest **117 files / 943 passed**.

## Root cause is still live

This will recur on any PR, at random, until the build stops depending on a network fetch to Google. `src/app/layout.tsx` fetches three families (`Newsreader`, `Geist`, `Geist_Mono`) at build time. Self-hosting them via `next/font/local` removes the dependency entirely — proposed separately rather than smuggled into a re-land, since it touches global typography.

Compounding factor worth fixing too: this repo runs **no preview deployments** for PRs (#301's head SHA has zero deployments), so build failures — flaky or real — are only discovered after they land on main.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
