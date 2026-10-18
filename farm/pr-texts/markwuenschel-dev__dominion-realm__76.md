# feat(timeline): light up /timeline in the nav

Flips the Timeline nav entry from `ready: false` to live, so the reveal-gated `/timeline` route (merged in #74) actually appears in the sidebar + mobile nav. It was hidden, which is a big part of why the homepage looked unchanged.

Still seeded with example beats — replace `src/content/timeline/` with the manuscript's real beats when ready.

Verified: `/timeline` now shows in the homepage nav; `pnpm build` ✅.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
