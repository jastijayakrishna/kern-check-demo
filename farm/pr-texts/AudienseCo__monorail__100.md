# Explain deploy failures in logs and Slack

## Why
Since 2026-09-29, every socialbro deploy failed at the merge step: a criss-cross history made GitHub's merge into `master` conflict on the version bump. Jenkins had already deployed every service each time, but monorail reported:

- **Slack:** `Unhandled error. Monorail didn't deploy anything.` This was wrong: production had changed and `master` was behind.
- **Logs:** `error: Error deploying {"timestamp":…}`. The error was lost, because winston drops extra arguments and serializes `Error` objects as `{}`.
- **Every debug line** dumped the full repo config, including the Jenkins password and the GitHub token.

## What
- **Slack:** a failed deploy now gets a message for the step that failed, followed by the underlying error:
  - `build`: services may be partially deployed, nothing was merged, and the deploy branch was kept.
  - `merge`: services were deployed, but `master` is behind production; merge by hand before the next deploy.
  - `labels` / `release`: deployed and merged, but that final step failed.
  - Failures before the build (`INVALID_REPO_CONFIG`, `INVALID_REPO_STATUS`, `BRANCH_CREATION_FAILED`) keep a "didn't deploy anything" message, which is accurate there. Unknown reasons no longer claim nothing was deployed.
- **Errors:**
  - `deploy()` tags each step's error, and `startDeploy` passes `failStep` / `failMessage` to the notification.
  - The Jenkins driver reports `Jenkins job <job> #<n> finished with <RESULT> (<url>)` and says which Jenkins call failed (trigger, queue or build poll).
  - Merge errors say which merge failed, plus the HTTP status.
- **Logger:**
  - Keeps error messages and stacks, and merges all extra arguments into one meta object.
  - Redacts `password` / `token` / `secret` / `webhook` keys at any depth.
  - Logs errors once instead of twice (`debug` + `error`).
- **Less noise:** debug logs in `startDeploy` show a summary of the repo info (`repo`, `sha`, `branch`, `tag`, `prIds`, failure fields) instead of the whole config, and `callCIDriver` no longer logs the CI settings.
- **Fixes:** the Slack error path in `startDeploy` referenced an undefined `err`, and `'use scrict'` in that file is now `'use strict'`.

The last deploy's failure, replayed through the new code:
```
error: Error deploying socialbro at step "merge": Error merging deploy-1790775686982 into master: Merge conflict (HTTP 409) {"branch":"deploy-1790775686982","sha":"06251a84","error":{…,"status":409},…}
```
> Services were deployed, but Monorail couldn't merge the deploy branch `deploy-1790775686982` into master and dev, so master is behind production. Merge it by hand before the next deploy.
> > Error merging deploy-1790775686982 into master: Merge conflict (HTTP 409)

## Tests
`npm test`: 222 passing (new specs for the logger, Jenkins failures, deploy step tagging, `startDeploy` failure fields and the Slack templates).

## Not in this PR
- Merging `master` (instead of the deploy branch) into `dev` after each deploy, to prevent criss-cross histories. That's a separate PR once deploys are healthy again.
- The Jenkins password and GitHub token were already exposed in past logs and need rotating separately.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
