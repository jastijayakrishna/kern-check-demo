# Promote Head-to-Head to production (verified in staging)

## Summary
Re-applies Head-to-Head (Mode 2), this time after real verification in staging rather than guessing off flaky local tooling.

Timeline: #77 (H2H) merged → apparent production outage → reverted (#78) → re-applied (#79) → same symptom recurred → reverted again (#80). At that point I couldn't tell whether the code was actually broken or my browser-testing tooling had degraded after a very long session (a clean test showed even the known-good reverted code hanging in the same tool). Rather than guess a third time, deployed to the `dev` branch's Cloudflare Pages preview (`dev.eyewallanalytics.pages.dev`) — fully isolated from production — and Matt clicked through it directly in his own browser: fast, clean, no issues.

This PR cherry-picks just the Head-to-Head re-application commit onto a fresh branch from `main` (not a merge of `dev`, which also carries unrelated in-progress BottomNav debug work that shouldn't ship yet) — diff is scoped to exactly the same 7 files as the original #77/#79.

## Test plan
- [x] `npm run test` (162/162), `npx vite build` clean
- [x] Verified working on the `dev` Cloudflare Pages preview by Matt directly (fast loads, full click-through)
- [ ] Merge, then confirm production once more after deploy

🤖 Generated with [Claude Code](https://claude.com/claude-code)
