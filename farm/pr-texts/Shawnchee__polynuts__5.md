# feat(waitlist): pre-launch waitlist page (Polymarket-for-options theme + app teasers)

Pre-launch waitlist capture page, in this same repo/Vercel project — no second repo, no extra infra.

## What this adds
- **`/waitlist` page** — dark, on-brand capture page. Email + optional RainbowKit wallet (for launch allowlisting), client honeypot, `upsert(ignoreDuplicates)` so re-submits silently no-op, `?ref=`/referrer channel attribution. Positioned as **"the Polymarket of crypto options."**
- **App teaser gallery** — three dark-mode captures of the live app (markets grid, bet ticket, leaderboard), framed as browser windows under *"The product is built. You're early to the door."*
- **`waitlist` table** (migration `0004`) — mirrors the `feedback` write-only RLS posture: anon `INSERT`, **no public `SELECT`**, so the list is **unscrapeable from the browser**. Verified with the live anon key: `INSERT` → 201, `SELECT *` → `[]`, count → `*/0`. Already applied to the project.
- **`proxy.ts`** — serves the page as the front door of `join.*` hosts (geo-block still runs first). Dormant until the custom domain is added; today the page is at `/waitlist`.

## Commits (modular)
- `39fcc47` data: waitlist table + anon-insert RLS
- `c77a39c` ui: join page + subdomain proxy rewrite
- `a370d38` ui: Polymarket positioning + teaser gallery

## Notes / decisions
- On `*.vercel.app` today, so `join.polynuts.xyz` can't exist yet — add the domain + `join` CNAME later and the rewrite activates automatically.
- Teasers are real captures in `public/teasers/`, served via `next/image`.
- US visitors hit the existing geo-block (`/not-available`) on the waitlist too — flag if you want the waitlist exempt.
- The "Polymarket" framing is in the copy *and* metadata — punchy, but it's a competitor's mark; consider whether to keep it in `<title>`/OG long-term.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **New Features**
  * Launched a dedicated waitlist landing page with hero section and product showcase
  * Users can sign up with email validation and track their position
  * Optional wallet address integration for enhanced user profiles
  * Waitlist accessible via dedicated subdomain with branded messaging and benefits overview

<!-- end of auto-generated comment: release notes by coderabbit.ai -->
