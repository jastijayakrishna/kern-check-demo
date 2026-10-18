# Restore site to Aug 28 21:40 state — AirHockey rematch, PoolRoyale flag revert, SnookerRoyal fixes

### Motivation
- Restore the repository code to the state that existed at 2026-08-28 21:40 (UTC+2) to recover prior gameplay and UI behavior.
- Re-enable the Air Hockey server/ client rematch flow and synchronized state handling that players expect after a match ends.
- Revert a recent Pool Royale flag-label change and restore Snooker Royal camera/aim/cue behavior to match the previously working experience.

### Description
- Restored server-side Air Hockey rematch handling by adding a `airHockeyRematch` handler that tracks per-table rematch readiness and emits `airHockeyRematchRequested` and `airHockeyRematchStart` events to clients.
- Reinstated Air Hockey client state/revision handling and added rematch UI and socket listeners in `webapp/src/components/AirHockey3D.jsx`, including `rematchStatus` state, `Play Again` button, and handlers for `airHockeyRematchRequested` and `airHockeyRematchStart`.
- Reverted the Pool Royale in-file flag-label resolution change by removing the `resolveFlagLabel` helper to restore previous flag-label behavior in `webapp/src/pages/Games/PoolRoyale.jsx`.
- Restored multiple Snooker Royal gameplay and camera/aim adjustments in `webapp/src/pages/Games/SnookerRoyal.jsx`, including tuned `STANDING_VIEW_DISTANCE_SCALE`, increased `AIM_LINE_WIDTH`, forcing cue visibility in standing/cue views, and switching several aim/guide calculations to use the spin-adjusted `guideDir` so visual guides match physics targeting.
- Applied the restoration across the working tree so the running site build and assets reflect the selected 21:40 snapshot.

### Testing
- Restored tree verification: confirmed the working tree matches the selected 21:40 snapshot (staged tree equality check) and staging/working tree consistency — success.
- Static checks: ran the repository cached-diff checks for whitespace/overlap errors — no issues found.
- Webapp build: ran `npm --prefix webapp run build` (Vite production build); the build completed and produced bundles (Vite build output and asset list reported) — success.
- Environment limitations: automated environment lacks a configured remote and no `make_pr` helper was available, so no pull request was created from this environment.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a91f3ebcba48329b15646c4a316b9d4)
