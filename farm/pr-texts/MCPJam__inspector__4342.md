# feat(cli): six exit codes for `eval run --wait` (E1)

## Summary

Evals v2, Lane E, step **E1**: `mcpjam cloud eval run --wait` now maps run outcomes onto the six-code exit contract from PRD §18.4, replacing the legacy two-outcome mapping (0 launched-and-waited, 1 launch-or-completion problem). Default (no `--wait`) behavior is byte-identical. `eval gate` is untouched and keeps its own four-code contract (0/1/2/3, `3` = incomplete) as a deliberate v1 compatibility exception, per the Lane E charter.

- **0** pass · **1** a completed run's verdict failed (the *only* producer of `1`) · **2** usage error / invalid suite file · **3** auth failed (before work, or mid-wait) · **4** connection/setup failure the CLI itself observed (or a local `--out` write failure) · **5** no valid verdict (`inconclusive`, null/unrecognized result, a non-verdict run status, a wait timeout, a non-auth mid-poll failure, or an unassembled report).
- A multi-target launch merges these worst-of in the fixed order `1 > 3 > 4 > 5 > 0`.
- No infrastructure condition ever maps to `1`.

**Every flip named explicitly** (also in the changeset):
- Completed + failed verdict: `0` → `1`
- Wait deadline hit, run non-terminal: `1` → `5`
- Partial/wholly-failed fan-out: `1` → `4`
- Missing credential / `UNAUTHORIZED`/`FORBIDDEN`/`OAUTH_REQUIRED` (launch or mid-wait): `1` → `3`
- Local `--out` write failure: generic `1` → `4`

## Implementation

- New pure module `cli/src/lib/eval-run-exit-code.ts`: `evalRunWaitExitCode`, `classifyLaunchErrorExitCode`, `classifyWaitErrorExitCode`. Imports `isNonVerdictRunStatus`/`isNonVerdictRunResult` from `eval-gate-exit-code.ts` rather than redefining them. Full doc block covers the table, the no-infra-maps-to-1 doctrine, the severity order and its defense, the `eval gate` exception, the `billing_limit_reached` → 4 reading, and the `status: "failed"` → 5 (not 4) reasoning.
- `cli/src/commands/eval.ts` (`eval run` action only, `--wait`-scoped):
  - An explicit `preflightCloudCredentials` call before launch remaps a missing-credential `operationalError` (exit 1) to exit 3; usage errors (exit 2, malformed `--api-url`) pass through untouched.
  - The launch call is wrapped so a thrown `CliError` with `exitCode !== 2` gets reclassified via `classifyLaunchErrorExitCode` (reads the wire `code`, since `toCliError` drops the HTTP status).
  - The per-target wait catch now captures the wire `errorCode` (never the key `code` — see the `#4310`/`#4313` redaction bug called out in the code) before stringifying the error, so a mid-poll 401 is classifiable.
  - The two old exit sites (`setProcessExitCode(1)` on outcome, `throw operationalError(...)` on wait/report errors) are replaced by one `evalRunWaitExitCode(...)` computation; the write-before-exit guarantee (artifact → reporter/receipt → only then exit) is preserved exactly.
  - `--out` write failures are now caught and remapped to exit 4 instead of falling through to the generic `INTERNAL_ERROR` (exit 1) `normalizeCliError` would otherwise produce.

## Tests

- `cli/tests/eval-run-exit-code.test.ts` (new): table-driven unit tests over all three pure functions, including the full severity matrix (24 tests).
- `cli/tests/eval.test.ts`: extended `EvalFixtureOptions` (`runCaseStatus` gains `cancelled`/`timed_out`/`failed`, `runCaseResult` gains `null`, `runCasePolicyVersion2`, `authFailure: "launch" | "poll"`, `singleRunLaunchError`, `closeAfterLaunch`, `groupRunOverrides`). Five previously-pinned tests updated to the new codes (JSON/JUnit failed-report leg → 1, reporting-failure leg tightened to 5, partial-fan-out leg → 4, wait-timeout leg → 5, and the old "exit 5 belongs to E1" sentinel rewritten as its inverse). 14 new integration tests cover every table row (missing credential, malformed `--api-url`, launch-phase auth/invalid/infra codes, `billing_limit_reached`, total fan-out failure, mid-poll 401 with real wire `errorCode`, mid-wait network failure, `--out` write failure) plus the three merge consequences (partial-fan-out-all-passed → 4, partia
