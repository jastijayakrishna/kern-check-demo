# fix(doctor): preserve per-agent memory search during upgrades

Closes #134256

Reported by @vdruts.

## What Problem This Solves

Fixes an issue where operators running `openclaw doctor --fix` after an upgrade could silently lose every per-agent memory-search override when Doctor converted `agents.list` to keyed `agents.entries` first. This removed settings such as `extraPaths`, `sources`, `experimental.sessionMemory`, and `enabled`.

## Why This Change Was Made

Doctor now visits both keyed agent entries and legacy list entries at the migration owner. It moves `memorySearch` before unknown-key cleanup, preserves explicit canonical values, and applies the existing provider, nested-field, and retired-path migrations to the moved data.

The shared agent-scope traversal replaces two duplicate traversal implementations. The regression was introduced by #112678, which moved roster normalization before the older list-only migration from #111527.

## User Impact

Per-agent memory-search settings now survive `openclaw doctor --fix` and remain attached to the correct agent. Operators no longer lose per-agent retrieval paths silently during this upgrade path.

## Evidence

- Red on current-main baseline `8abb80073c8648e85d11a0e9bd22b09d1d2bfac2`: [Testbox run 33466170600](https://github.com/openclaw/openclaw/actions/runs/33466170600) removed the legacy block and retained only the pre-existing canonical field.
- Green on exact head `983df6b6ddf33ffad80f32874966ffeeaf0a803f`: [Testbox run 33467597600](https://github.com/openclaw/openclaw/actions/runs/33467597600) ran the real CLI, preserved supported fields and canonical precedence, verified the authored input, and produced byte-identical config on a second Doctor run.
- Regression proof: the strengthened Doctor process test fails on the baseline and passes on the head.
- `node scripts/run-vitest.mjs src/commands/doctor-config-preflight.process.test.ts` — 10 passed.
- `node scripts/run-vitest.mjs src/commands/doctor/shared/legacy-config-migrate.test.ts src/commands/doctor/shared/legacy-config-migrations.runtime.retired.memory-qmd.test.ts src/commands/doctor/shared/legacy-config-migrations.runtime.retired.test.ts` — 294 passed.
- Focused format, Oxlint, Doctor registry, coercion helper, max-lines, assertion safety, import-cycle, temp-directory, conflict-marker, and dead-export checks passed.
- Autoreview on the exact local diff: clean, no actionable P0 findings.

Agent task: https://chatgpt.com/codex/tasks/01a040d7-aa3d-7433-83eb-de7f49979443
