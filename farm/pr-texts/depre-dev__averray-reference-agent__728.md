# test(int2): wire the three task families that were never run

**Published on the implementer's behalf** — their `gh` hit a transient network error (`error connecting to api.github.com`). Commit `68bace4` is theirs, unmodified, and matches the reported SHA.

**Draft, and not ready.** One of the three new cases fails. Opening it so the work is reviewable and CI runs; the diagnosis is in progress.

## What this is

Three task families existed as fixtures since 2026-07-25 and were never wired to anything. Wiring them exercises `search` for the first time — one of three acceptance-criterion types that had never verified anything.

All four count sites moved 11 → 14, plus the unit guard.

## Current state

```
ten preceding cases   pass
docs-fix              Harness learning_processed, AgentTask failed (expected handoff_ready)
add-unit-test         not run
small-refactor        not run
```

The implementer stopped per the no-retry rule, and the run's evidence root was removed on teardown, so the criterion verdict and search detail were unavailable to classify the failure.

That is a tooling gap worth noting on its own: **a failing case destroys the evidence needed to diagnose it** unless `INT2_SUITE_EVIDENCE_DIR` is set explicitly. The default temp root is removed during shutdown. Anyone running this suite to investigate a failure should set that variable first — and arguably the wrapper should retain evidence on failure regardless.

Re-running now with evidence preserved; will post the criterion-level verdict here.

## Two interpretations to check on review

- the dependency cache is built from the fixture's immutable base, since its lockfile differs from current `main`
- the add-test script runs `npm run typecheck` after creating the test so workspace `dist/` exports exist before the unchanged `npm test` criterion
