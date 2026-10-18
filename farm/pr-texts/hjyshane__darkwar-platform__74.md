# feat(dev): a local build for looking at the dashboard without a backend

There is no way to see this app on a Mac. No Docker means no Supabase stack, and the previous Mac session's answer was a Python mock PostgREST that is **not in the repo** — `handover.md` lists it under "made on the Mac and not committed", which is why it had to be reinvented today.

## The approach

Render the real `App` — real router, real components, real stylesheet — and fill the **query cache** before mounting.

No HTTP, so there is no protocol to get wrong. That matters: the one thing the old mock got wrong was a `204` with a body, which browsers reject and curl tolerates, and it made unstarring look broken for weeks when the app was correct.

The other half of that sentence is the limit, and both files say so at the top: **this verifies nothing** about queries, RLS, column grants or PostgREST. It shows layout, spacing, empty states and navigation.

```bash
pnpm --filter @dw/dashboard dev
```

Then open `/index.dev.html`. The production entry is untouched, and the fixtures are absent from `vite build` output — `index.dev.html` is not a build input and `dist` carries none of these strings. The one production change is exporting `queryClient` from `App.tsx` so it can be seeded; no behaviour change.

Fixtures are deliberately uneven — a third of the figures are unobserved, one collector is silent and one never started, one alliance rank has no member count, one roster row has no power. Nulls are what this UI is most likely to get wrong.

## What it found in the first ten minutes

Which is the whole argument for building it:

- **The Operations group printed "Collectors" twice running** — the section heading and the table heading directly under it. Obvious on screen; invisible in the markup checks I had been doing all session.
- **`MembersSetting`'s intro explained Role and Rank but not the Player column** added in 0066 — the one column that actually needs explaining, since it decides whether somebody sees their own history and why they cannot set it themselves.

Both are fixed here.

## Verification

`pnpm check && pnpm typecheck && pnpm test && pnpm build` pass; 221 tests, unchanged.

Driven in a real browser: overview, members, the five admin groups, and the player page. The roster shows `—` for unobserved figures, the collector table shows Live / Silent 3d / Never, and the roster history reads "5 changes across 6 captures" with the redacted capture as **Not observed** and the unread power as `—` with no delta.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
