# Clean up README status badges

## Summary

Clean up the README badge row so it no longer advertises stale or misleading external status.

- Pin Unit Tests and CodeQL badges to the workflow files on `main`, which avoids the old workflow-name badge endpoint reporting false failures.
- Replace the dynamic Codecov percentage badge with a neutral coverage report badge while Codecov is still reporting `72%`.
- Replace the FOSSA scan badges with the repository license badge and plain Apache-2.0 license text.

## Validation

- Verified the old Unit Tests badge reports `failing` while the new `actions/workflows/tests.yml?branch=main` badge reports `passing`.
- Verified replacement badge endpoints resolve: Unit Tests passing, CodeQL passing, coverage report, Apache-2.0 license, and release `v2.0.0`.
- `git diff --check`

