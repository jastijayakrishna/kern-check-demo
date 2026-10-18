# Baseline-align the chat byline

## What

The chat byline's three written parts — the agent name, the `AGENT` role tag and the HH:MM stamp — now share one baseline. The identity mark stays centred on the row.

## Why

The byline row was `alignItems: 'center'`, and its children are set at two sizes in two faces: a 16px Space Grotesk name (25px line box) next to a 10px IBM Plex Mono tag and stamp (14px line boxes). Centring those line boxes against each other left the small mono floating roughly half a line above the name's feet — visible in the reported screenshot, where `AGENT` and `14:24` sit high against `Fable`.

## How

`Byline` (`apps/mobile/sources/components/buzz/Ledger.tsx`) wraps the name, tag and stamp in a nested row with `alignItems: 'baseline'`. The face tile stays a direct child of the outer row, which keeps `alignItems: 'center'` — the mark is a picture rather than a word, so baseline alignment is the wrong rule for it, and it does not move.

The nested row carries `flex: 1` and `minWidth: 0` so the stamp's `marginLeft: 'auto'` still has the whole remaining row to push against, and a long name shrinks in place instead of shoving the clock off the edge. The tile remains the byline's first child on the content edge with no style of its own, so the C70 edge rule and the alive-ring gutter are untouched.

`ActivityTimeline` renders the same exported `LedgerBylineView`, so the live draft lane picks this up identically and nothing moves when a draft settles.

`DESIGN.md` records the rule alongside the rest of the byline spec.

## Tests

- New case in `Ledger.test.ts`: the name, role tag and stamp share one parent whose `alignItems` is `baseline`; the mark's parent row is `center` and the mark is still its first child.
- `Ledger.test.ts`, `Ledger.provisional.test.tsx`, `ActivityTimeline.test.tsx`, `RoomMessageVariants.test.tsx` — 81 passed.
- `npm run typecheck` (apps/mobile) — clean.
- Full `vitest run` in apps/mobile — 1629 passed, 3 failed in `appBranding.test.ts` and `mobileOtaRelease.test.ts`. Those three fail identically on a stashed clean tree in this worktree, so they are pre-existing and unrelated to this change.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
