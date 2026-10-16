# Stop counting draft PRs as open Dependicus items for review

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## What's changing

The previous pass over-corrected: `searchDependicusIssues` was changed to drop *every* pull request returned by GitHub's issues endpoint, draft or not. That made the notification bot's job impossible — it couldn't see the open Dependicus PRs that legitimately needed review, and it kept honking `:package: 54 open Dependicus PRs for Editor Media Management` because the count was still being padded by drafts coming in from elsewhere.

This PR puts `searchDependicusIssues` back where it belongs:

- **Skip draft PRs only.** A draft is explicitly not "open for review", so it shouldn't count.
- **Return ready-for-review PRs alongside regular issues.** Each entry now carries an `isPullRequest` boolean so callers can tell them apart.
- **Still skip anything flagged as a draft** (PR or otherwise) defensively, so non-PR draft items can't sneak through.

The reconciler picks up the new flag and uses it to keep treating a PR title as "something already exists, don't create a duplicate", while never mutating the PR via `octokit.issues.update` (which would clobber the PR's title and body, since GitHub gives PRs and issues a shared numbering scheme).

## Tests

- New test asserts a draft PR is dropped while a ready-for-review PR is returned with `isPullRequest: true`.
- New test asserts non-PR matches are flagged with `isPullRequest: false`.
- Existing tests updated for the new field.
- Full suite passes (the unrelated `HtmlWriter.test.ts` failure on `browser-bundle.asset.js` reproduces on `main` without my changes — it needs a build first).

## Waterfowl moment

The goose finally stops honking at perfectly good ducks paddling in the review pond. Only the ducklings still tucked under the wing get left alone.
<!-- CURSOR_AGENT_PR_BODY_END -->

[Slack Thread](https://descript-inc.slack.com/archives/C0AFCPPHLKD/p1779818658724089?thread_ts=1779818658.724089&cid=C0AFCPPHLKD)

<div><a href="https://cursor.com/agents/bc-759a0c06-94fc-5967-9d5d-54524549f07c"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-759a0c06-94fc-5967-9d5d-54524549f07c"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
