# fix(int2): fail closed on missing verification tools

## What changed

- re-land the 14-case INT-2 task-family/D3 suite behind a draft PR
- build the pilot sandbox from the task fixture's exact lockfile so `tsc` and `vitest` resolve under `--network none`
- pin the kernel's generic environment-preflight and persistent-container ownership fixes
- declare a profile environment preflight and assert its baseline evidence before dispatch
- prove the pilot toolchain can run as the host workspace owner before case 1
- read criterion details from the sealed verification report when the event payload is compacted
- correct the two scripted JSONL commands exposed once the toolchain actually ran, while preserving their acceptance criteria

This PR depends on `averray-agent/agent-harness#35` at `3355f4906864b0f0e0fe5fd5eb5220172e174206`. It must not merge before that kernel change.

## Root cause

The dispatcher dependency cache was seeded into the approved source checkout, but the kernel subsequently created a clean self-contained Git clone for the run. Ignored `node_modules` correctly did not cross that boundary, and the Docker provider mounted only the clean run workspace. The prior baseline had no generic environment probe, so missing binaries produced a false `baseline_failures: 0` and were attributed to verification after the change.

Once the toolchain was present, the first hosted run exposed the adjacent Linux-only boundary: later `docker exec` commands inherited the persistent container's root identity, created root-owned compiler output, and left runs at `finalizing` when the runner could not clean it up. The fix belongs in the kernel provider, which now creates and validates the container with the workspace owner's uid/gid. The pilot image only supplies the pinned offline dependencies and a writable non-root cache.

The next hosted run proved that ownership fix: docs verification and cleanup passed, while only the two complete Vitest-suite checks failed after encountering the kernel's fixed 30-second command ceiling. A second hosted run produced sealed reports with `reason: timeout` at 60 seconds while all recorded test results remained green. Existing profiles retain the 30-second default. This profile therefore uses its existing 120-second elapsed budget, below the kernel's hard five-minute profile bound; the command and full-suite acceptance criteria are unchanged. Terminal diagnostics now resolve the sealed verification report instead of preserving only the compact event.

## Checks

- final local INT-2 automated suite: 14/14 passed in 454s; all three task families reached `handoff_ready` with baseline failures 0 and their required command/search criteria passing
- focused ceremony mechanics: 22 passed, 14 integration cases intentionally skipped without the suite-enable environment
- hosted Linux CI run `30959936213`: green; 14/14 executed in 928s, non-skip marker present, docs/add-unit-test/small-refactor all `handoff_ready`
- hosted command verification: docs 3.22s, add-unit-test 93.10s, small-refactor 93.31s; every required criterion passed
- prior branch gate: `npm run typecheck` exit 0; `npm test` 185 files passed, 2 skipped / 2,709 passed, 18 skipped; `npm run build` exit 0

## Surface and operations

- affects dispatcher ceremony/CI, pilot image, tests, and runbook only
- no production runtime image, contracts, Caddy, frontend export, secrets, wallet, or deployment changes
- no new environment/VPS secret is required beyond the existing read-only kernel deploy key
- no merge or deploy is authorized; keep this draft until both kernel and hosted dispatcher gates are green

