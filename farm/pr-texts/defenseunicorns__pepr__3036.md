# chore: remove heredoc implementation and update templates

## Summary

- Removes the custom `heredoc` tagged template literal (`src/sdk/heredoc.ts`) and its unit tests
- Removes the unused `heredoc` npm package (`^1.3.1`) from dependencies and template data
- Replaces all inline `heredoc` usage with fixture files for cleaner test readability
- Cleans up the Dockerfile (no longer needs to `rm -rf node_modules/heredoc`)

## Context

The custom `heredoc` utility was introduced in #1262 as part of the cosign image-validation feature. When cosign was removed in #1948, `heredoc` was left behind — both the custom implementation in `src/sdk/` and the npm package in `package.json`. Neither serves a purpose anymore:

- The custom `heredoc.ts` was only used as a dedent utility for multi-line template literals in 3 files
- The npm `heredoc@^1.3.1` package was listed as a dependency but **never imported** in any source file

This PR completes the cleanup that #1948 started.

## Changes

**Removed:**
- `src/sdk/heredoc.ts` — custom tagged template literal implementation
- `src/sdk/heredoc.unit.test.ts` — associated unit tests
- `heredoc` npm dependency from `package.json` and `src/templates/data.json`
- `rm -rf node_modules/heredoc` line from `Dockerfile` (package no longer installed)

**Refactored:**
- `integration/helpers/resource.test.ts` — test data extracted to fixture files (`integration/helpers/fixtures/`)
- `hack/load.unit.test.ts` — test data extracted to fixture files (`hack/fixtures/`)
- `hack/load.cli.ts` — octave graph script extracted to `hack/fixtures/octave-graph-template.m`

## Test plan

- [x] `npx vitest run hack/load.unit.test.ts` — 33 tests pass
- [x] `npx vitest run integration/helpers/resource.test.ts` — 8 tests pass
- [x] `npm run build` — builds cleanly
- [ ] CI pipeline passes


🤖 Generated with [Claude Code](https://claude.com/claude-code)
