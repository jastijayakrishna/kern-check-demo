# refactor(compute): rename `compute logs` to `compute events`

## Summary

- Renames `compute logs <id>` → `compute events <id>`. The OSS endpoint behind it returns Fly machine lifecycle events (start/stop/exit/restart), not container stdout/stderr — the new name is honest.
- Mirrors the parallel OSS rename: [InsForge#1062](https://github.com/InsForge/InsForge/pull/1062) moves `/api/compute/services/:id/logs` → `/events`. Both must ship together.
- Frees up `compute logs` for the future container stdout/stderr feature (roadmap; see OSS spec `2026-04-07-compute-dashboard-ux-design.md`).

## Why this is OK as a breaking change
- 0.1.59 ships only the misleading `compute logs`. Most users invoke via `npx` so the next run picks up the rename.
- Reusing the freshly-vacated `compute logs` for *actual* log streaming later avoids permanent semantic debt.

## Test plan
- [x] `npm run lint` passes (149 tests, 13 skipped).
- [ ] Manual: `npx insforge-cli compute events <id> --limit 5` returns the events array (against OSS PR #1062 build).

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

## Release Notes

* **New Features**
  * Added `compute events <id>` command to retrieve compute machine lifecycle events (start, stop, exit, restart) with timestamps and messages. Supports `--limit` (1–1000, default 50) and `--json` output formatting.

* **Breaking Changes**
  * Removed `compute logs` command; use `compute events` instead.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->
