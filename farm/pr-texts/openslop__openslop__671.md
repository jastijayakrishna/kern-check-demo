# refactor: nightly conventions audit 2026-08-28

Nightly CONVENTIONS.md compliance audit.

Delta-audited every non-test source file merged to master since the 2026-08-27 sweep (#654, #657, #658, #659, #660, #661, #665), minus the files covered by open PRs #662, #663, #668 and #669.

## Fixed

- `components/ui/number-scrubber.tsx` defined a private `clamp` identical to the one `lib/utils` already exports and that `SeekTooltip`, `Waveform` and `elementAttributes` all import. One home per piece of knowledge; no behavior change.

## Flagged, not fixed

- `lib/project/relativeTime.ts` is a pure display formatter with no project knowledge, living apart from its siblings in `lib/format.ts` (`formatDateTime`, `formatBytes`, `truncateMiddle`) — `CanvasHistoryPanel` imports from both. Moving it would touch `ElementHistoryPopover.tsx`, which open PR #669 owns, so it is left for a follow-up.

## Verified clean

The new canvas-version-history surface is exemplary against all seven rules: `CanvasHistory` never has to choose between continuing and beginning a version (errors defined out of existence), `canvasVersionStorage` throws on every Supabase error and parses each row with zod, `ProjectDocument` gives history one read/write unit, and the panel is registered in `EditorSidebar`'s `PANELS` record rather than special-cased. Also clean: `lib/video/durationFit.ts`, `elementLengths.ts`, `lib/agent/tools/fitDurations.ts` (registered in the `TOOLS` record), `lib/generation/concurrency.ts`, `lib/format.ts`, `storeSnapshot.ts`, `snapshots.ts`, `PlayerPositionContext`, the timeline components and `components/ui/{color-field,disclosure}`.

Repo-wide invariant greps are unchanged: bare `catch {` is still exactly 3 intentional sites, zero catch-return-null, zero `as any`, zero non-null assertions, zero provider-string sniffing, and all 4 `switch` statements are exhaustive discriminated-union dispatch. Two standing flags were resolved by merged work: `Waveform`'s unhandled `play()` rejection (#659) and the duplicated inputs/result zod schemas in `lib/project/elementHistory.ts`, now imported from `lib/generation/snapshots.ts`.

lint, typecheck, format:check, 1430 tests and `npm run build` all pass.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
