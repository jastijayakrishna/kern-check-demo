# fix: restyle Temporary Upcoming Campaigns on-page copy

## Summary
On-page copy changes to `/public/temporary-upcoming-campaigns` (the visible page content — separate from the link's title/description shown in link previews, which is already admin-editable via `/admin/public-links` from #131):

- H1: "Temporary Upcoming Campaigns" → **"AFJ Temporary Campaign List"**
- The "ALL LEADERS please…" paragraph is now a bulleted list, one instruction per line, with the key action word bolded in each:
  - **Check** that your campaign details are correct
  - Click on the **Edit** button to make changes
  - Click on the **Download** button to save a copy
- Bumped that whole text block from `text-sm` to `text-base` for readability.

## Test plan
- `npm test` — 299 tests pass (unchanged, copy-only change).
- `npx tsc --noEmit` — clean.
- `npm run lint` — 0 errors.
- `npm run build` — succeeds.
- Manually verified in-browser (fresh tab, no session): copy, bold words, and larger text all render correctly in light mode, dark mode, and mobile viewport; no console errors.

This is a copy/styling-only change with no logic affected — no new test coverage needed per the testing policy.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
