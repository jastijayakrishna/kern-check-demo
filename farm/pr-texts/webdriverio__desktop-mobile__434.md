# fix(tauri-service): sync mocks via afterCommand so user command overrides survive

## Problem

To re-sync mocks after DOM mutations, the worker service registered element-scoped `overwriteCommand` wrappers for `click`/`doubleClick`/`setValue`/`clearValue` in `before()`. WDIO stores element-scoped overrides (`overwriteCommand(name, fn, /* attachToElement */ true)`) in a map **keyed by command name** — they do **not** chain (only browser-scoped overrides capture and chain `origCommand`). So the service's registration silently clobbered any user-defined `overwriteCommand('click', …)` (and, symmetrically, a user override registered last would clobber the service's mock-sync). Reported in #422.

## Fix

Move the mock re-sync to the **`afterCommand`** worker hook and stop registering element overrides entirely. The old wrappers only ran the original command and then `updateAllMocks()` — they never modified args or the return value — so `afterCommand` is a behaviour-preserving drop-in that leaves the user's command chain untouched.

- Removed `installCommandOverrides` / `overrideElementCommand` and both call sites.
- Added `afterCommand`, which runs `updateAllMocks()` for the four DOM-mutating commands (skipped when the command itself errored).
- The separate, legitimate `browser.url` override (browser mode) is unchanged.

## Behaviour note

Previously a mock-update failure rejected the triggering command. Via `afterCommand` the same failure is logged by WDIO's hook runner instead of failing the command (the `updateAllMocks` AggregateError still surfaces in logs). This is the one intentional behaviour change.

## Tests

- Replaced the "installs command overrides" unit test with a #422 regression guard (the service must **not** register element overrides), plus `afterCommand` coverage (updates mocks for the four commands; no-op for unrelated commands and when the command errored).
- `pnpm --filter @wdio/tauri-service typecheck` clean; full suite **626/626** green.

## Scope

`@wdio/electron-service` has the identical bug. Per maintainer decision it's handled separately (its fix interacts with the #292 batched `MockUpdateScheduler` + multiremote per-instance routing and ~44 test refs) — tracked in #432.

Fixes #422

🤖 Generated with [Claude Code](https://claude.com/claude-code)

