# fix(csr-common): export form field re-edit metric key

## Hi There, I just made a Pull Request!

Adds the missing `RecordingMetricKey.FormFieldReEdit` aggregate metric identifier and classifies it as a user-interaction metric. This aligns the metric contract with the existing `RecordingCustomEventTag.FormFieldReEdit` event contract.

#### :heavy_check_mark: Checklist

- [x] All tests are passing
- [ ] Relevant documentation updated — no documentation change needed
- [x] linter/style run on changed files
- [x] Tests added for new functionality
- [x] Regression tests added for bug fixes
- [ ] Tested in a corresponding example app — no example-app behavior changed

## Validation

- `yarn format:check`
- `yarn test:csr` — 17 files, 231 tests
- `yarn build:csr`
- `yarn tsc --noEmit -p csr/csr-common/tsconfig.json`
- `yarn tsc --noEmit -p csr/csr-recorder/tsconfig.json`
- `yarn tsc --noEmit -p csr/session-recording/tsconfig.json`
- isolated-worktree equivalent of `yarn lint:csr`

Generated with [Codex](https://openai.com/codex/).
