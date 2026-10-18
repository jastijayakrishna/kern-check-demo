# refactor(native-mobile-core): make iOS toolchain probes async (no event-loop block)

Follow-up to #378 (merged via #424) — addresses the one remaining Greptile consistency note on that PR.

## Problem

`resolveIosUdid` and `warmUpXcodeToolchain` (in `packages/native-mobile-core/src/iosSetup.ts`) shell out via **synchronous `execFileSync`** with 30s timeouts. That blocks the Node event loop for the duration of each `xcrun` probe while the launcher is preparing other capabilities. It's a consistency gap with `prebuildWda` in the same file, which already uses async `spawn` *precisely* to avoid blocking the loop (and keep logging/SIGINT live).

Cosmetic — it doesn't affect correctness — but worth fixing before more checks get added to the doctor framework on top of these helpers.

## Change

- Add a small `runXcrun` promise wrapper around `execFile` (mirrors `prebuildWda`'s hand-rolled-Promise style) and make both `resolveIosUdid` and `warmUpXcodeToolchain` `async`.
- `doctorChecks` needs **no change** — `DoctorCheck` already permits a `Promise` return, and `runDoctor` awaits checks.
- `onWorkerStart` `await`s `resolveIosUdid` (already an async hook).
- Tests switch the `node:child_process` mock from `execFileSync` to callback-style `execFile` via a small `xcrunOnce`/`xcrunResolves`/`xcrunRejects` helper.

## Verification

- 108 `@wdio/native-mobile-core` unit tests pass
- `typecheck`, biome `lint`, and `format:check` all clean

🤖 Generated with [Claude Code](https://claude.com/claude-code)
