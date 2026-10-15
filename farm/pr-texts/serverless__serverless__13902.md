# refactor(aws): replace promise-queue with p-limit

## Summary

- AWS request queues and artifact uploads now use `p-limit`, which `packages/serverless` already depends on. The direct `promise-queue` and `ext` dependencies are removed.
  - The v2 and v3 AWS request queues stay separate, and each still runs at most 2 requests at a time.
  - Artifact uploads still honor `SLS_MAX_CONCURRENT_ARTIFACTS_UPLOADS` (default 3), with a new limit for each upload pass.
  - `promise-queue` leaves the dependency tree. `ext` stays, as a transitive dependency of `es6-symbol`.
- The integration test helper `getTestStageName` now removes characters that CloudFormation stack names reject from `TEST_STAGE` before shortening it. CI builds `TEST_STAGE` from the pull request author's login, and GitHub App logins such as `name[bot]` made every live suite fail before deploying. The helper moves to `packages/sf-core/tests/utils/testStageName.js`, and `runSfCore.js` re-exports it, so existing imports are unchanged. Stage names for regular logins are unchanged.

## Test plan

- [x] `npm run test:unit -w @serverless/framework`: 4262 passed
- [x] `npm run test:unit -w @serverlessinc/sf-core`: 1386 passed, including new tests for the stage name
- [x] `npm run lint`, `npm run prettier`
- [x] Side-by-side run of the previous limiters and `p-limit` on identical workloads (successes, async and synchronous failures, tasks arriving mid-run): every task starts and finishes at the same point with the same result, and no run exceeds the limit
- [x] Modified modules load and behave the same on Node.js 18
- [x] Release bundle includes `p-limit` and no longer includes `promise-queue` or `ext/promise/limit`
- [x] Live deploy, invoke, info and remove of a service with 6 individually packaged functions and a layer, on the v2 and v3 SDK paths and with `SLS_MAX_CONCURRENT_ARTIFACTS_UPLOADS=1`: at most 2 AWS requests in flight, the same uploads as the current release, and uploads one at a time with the limit set to 1
- [x] Live `simple-nodejs` suite with `TEST_STAGE='pr-cursor[bot]'`: deployed, invoked and removed
