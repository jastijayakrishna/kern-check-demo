# Fix restored progress run validation

## Motivation

Persisted `ProgressV2` state accepted unbounded problem-ID arrays from browser
storage before cloning them and rendering run markers. A very large but
otherwise schema-valid list could therefore consume excessive client work.

The static path is real, but this repository does not establish a remote
attacker or cross-user input boundary: the value comes from the learner's
same-origin `sessionStorage`. This PR treats the report as client-state
resilience hardening rather than claiming a demonstrated remote vulnerability.

## What changed

- Bound an active run between its generated three-problem baseline and the
  structural maximum of one transfer per baseline problem.
- Require every restored run ID to exist in the current problem bank.
- Replay the shared transfer insertion/reordering transition and accept only a
  schedule reachable at the persisted run step and transfer state.
- Cap completed and recent ID lists at the finite problem-bank size.
- Fall back to clean progress when any restored list violates those bounds.
- Add persistence and hook-boundary regressions for valid transfer schedules
  and oversized stored arrays.

## Review correction

The first implementation required the exact deterministic order plus at most
one insertion. GitHub Codex review identified a legitimate state it rejected:
transfer practice may move a later run problem to the next position without
changing the run length. The corrected validator preserves that normal flow.
CodeRabbit then identified that length and known IDs alone still accepted
arbitrary duplicates. The final implementation shares the production transfer
transition with restore validation and rejects schedules the session state
machine cannot reach.

## Engineering decisions

- Merged current `main` before finalizing the fix; the original hard-coded
  three-problem test had become stale after the problem-bank expansion.
- Used the session state machine's actual maximum (`baseline length * 2`)
  instead of an arbitrary global constant.
- Did not impose a raw byte cap on saved drafts. Draft size is a separate
  product-policy decision, browser storage already has a quota, and changing
  it is not required to close this list-amplification path.
- Recorded the finding assessment and review correction in
  `docs/build-log.md` as Build Week evidence.

## Verification

- `npm test -- --run src/progress/progressStore.test.ts src/session/learningSession.test.ts src/session/useLearningSession.test.tsx` — 47 tests passed.
- `npm run check` — passed.
- Vitest — 15 files, 670 tests passed.
- Problem-bank publication gate — passed.
- Production build — passed; Vite transformed 204 modules.

Codex desktop task: `019f7290-4f9c-7c01-beaa-bc106cbdd874`

Original Codex task: https://chatgpt.com/codex/cloud/tasks/task_e_6a5b753badf48320a732aaab565aaa3d
