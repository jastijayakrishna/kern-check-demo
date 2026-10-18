# feat(mobile): browsing is free in a shared session — the wall changes only on Put on the wall

## Summary

The behaviour slice of #4281, stacked on #4666 (base = `feat/4281-preview-first-sessions`; retarget to `main` when A1 merges). Closes #4281.

**In a session with 2+ climbers, browsing is free.** Swipes, climbs-list taps (with the result list seeded as the view-only suggestion track), similar-climb taps, and fresh drawer opens from the feed, logbook, profile, and playlists all pin a preview instead of writing the shared queue and lighting the wall. The catalogue is yours; the queue is everyone's — queue-sheet taps still commit. Solo behaviour is untouched, including a session of one on a home wall (distinct-user count, so two devices on one account stay solo).

- **The crew gate** is a provider-level selector (`shouldDefaultToBrowse` in `@boardsesh/play-view` + `countDistinctSessionUsers`), published through its own context memoized on the boolean — it flips only across the 1↔2+ boundary, never on roster churn.
- **The latch is one-way**: armed on the first view-only gesture in a crew, exited only by Back to live or Put on the wall. A peer dropping off, the session ending, or an angle change never silently re-arms commit-on-swipe (angle changes re-anchor the preview at the new angle instead of clearing it).
- **Zero wire change**: browsing emits nothing — no `setCurrentClimb`, no queue writes, no playback broadcasts. The sync coordinator and queue reducer are untouched. Commits launder `playlist-peek:` synthetic uuids through `resolveCommittableQueueItem` (now shared with `nextClimb()`), so they never reach the wire.
- **Busy-wall confirm**: if someone lit a different climb while you browsed, the first Put-on-the-wall tap swaps the commit row inline to "Someone just lit {name}. Put yours up instead?" — no auto-timeout; it disarms only on Keep theirs, further browsing, or the conflict resolving itself. The lit climb is read continuously from board presence (`useWallClimb`), which also makes the On-the-wall pill work after plain swipes; a late-arriving presence read is adopted as the latch-start snapshot only when it pre-dates the latch by a 60s safety margin.
- **BLE stays honest** (no files under `lib/ble/` or `ble-protocol/` touched): route playback while previewing is fully local (`viewOnly` — no frame writes, no peer broadcast), and the mirror toggle acts on-screen only mid-preview.
- One-shot browsing notices (crew join + first solo settings-preview) ride the callout surface, spoken exactly once per platform path. Commit analytics now carry `session_id` + `participantCount`.

Adversarial Fable review (2 lenses) surfaced 8 findings — 3 majors (playlist/discover taps and tick-shaped opens bypassing the crew gate) all closed at the `openDrawer` choke point + `previewOnly` activation; every behavioural fix mutation-tested. Nothing rejected.

## Release Notes

- Browsing with your crew is now free: in a session with more than one climber, swiping and tapping around never touches the queue or the wall. One button — "Put on the wall" — makes the change, and if someone just lit a climb, the app checks before taking it.
- Changing the angle mid-browse keeps your spot instead of kicking you back to the live climb.

## Test plan

- [x] `vp run typecheck:mobile` / full monorepo typecheck
- [x] `vp run test:mobile` — 701 files / 6925 tests, 0 failures (~110 new: crew-gate tables, latch one-way render tests incl. session-end survival, peek laundering, busy-wall arming + late-read adoption tables, BLE viewOnly suppress/resume + broadcast gate, notice one-shot claims — each behavioural assertion mutation-checked)
- [x] `vp test run --project i18n`, `check:i18n`, `check:i18n:orphans`
- [x] `vp run check:mobile-bundle`
- [x] `vp check`
- [x] `packages/shared/queue` untouched and green (zero wire change contract)
- [ ] Real-crew pass (2+ phones + a wall): `.boardsesh/qa-notes.md` § A2 — the group-session flows, busy-wall confirm timing, and BLE mirror/playback gating on a real board

🤖 Generated with [Claude Code](https://claude.c
