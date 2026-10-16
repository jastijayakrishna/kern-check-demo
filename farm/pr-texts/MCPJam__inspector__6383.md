# fix(client): replace repeated swarm persona summaries with one warning

## User story

**As a** developer reusing personas in a swarm,
**I want** one clear warning when existing goals will run against a different setup,
**so that** I can review the change without reading repeated persona summaries.

### Acceptance criteria

- [x] Confirm shows one yellow warning when any reused goals move to a different setup, even when multiple personas are affected.
- [x] Confirm does not repeat persona names, goal counts, or “Different server group” paragraphs above the cards.
- [x] The warning stays hidden when goals already match the selection or no destination resolves.
- [x] Persona cards, goal editing, and launch overrides still work unchanged.

## What this does

Replaces the per-persona disclosure introduced in [#5430](https://github.com/MCPJam/inspector/pull/5430) with one warning: “Some existing goals were written for a different setup and will run against the one selected for this swarm.” The existing move predicate still decides when it appears. No goal generation, server selection, or execution behavior changes. This warns about a changed setup, not verified tool incompatibility.

Verification: all 69 Swarms test files / 1013 tests pass, client typecheck passes, and `npm run slop:check` passes.

Rebased onto `main` at `68a7f43a6b38731d2ce7b171e528de9a9ccda049`; the PR head is `f64c5082416f23581974c539fcbb919ffd155634`. Current CI has 33 passing checks and no failures: required CI, all six inspector shards, Build and Test, E2E Smoke, security, and the rerun of the advisory visual pipeline pass. [Chromatic build 662](https://www.chromatic.com/build?appId=6acb684ad17911b3293b6e17&number=662) still awaits visual review, so UI Tests is pending.

## Architecture

None: no new component or flow.

## Screenshots and recordings

| Before | After |
| --- | --- |
| ![Repeated persona disclosures](https://app.devin.ai/api/presigned_proxy?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjpudWxsLCJidWNrZXRfbmFtZSI6ImRldmluYXR0YWNobWVudHMiLCJidWNrZXRfa2V5IjoiYXR0YWNobWVudHNfcHJpdmF0ZS9vcmctNTcxMjk3ZjJhOGJkNGY2OWI0MjY3MWVjMGMzZTFlZTQvMTcwODQ1ZTQtY2NiYi00NzM3LWI2MTctMjk5MmVmMjAwZTE5IiwiaWF0IjoxNzkxOTE4NzM4LCJvcmdfaWQiOiJvcmctNTcxMjk3ZjJhOGJkNGY2OWI0MjY3MWVjMGMzZTFlZTQiLCJmaWxlbmFtZSI6ImltYWdlLnBuZyJ9.2EtX4S-u6y_T2-rLIKpzsuHkJahzBDX3xb2ayw0y7A0) | Confirm screenshots pending real QA member sign-in. |

The local app on `f64c508` connects to the real QA backend and now opens the real dev WorkOS sign-in form using the committed public AuthKit defaults. A QA member must complete login/MFA before callback completion, backend provider trust, Confirm, theme rendering, or goal editing can be verified. Guest access cannot reach Swarms Confirm. No mocks, authentication bypass, production credentials, backend deployment, or paid swarm launch were used.

## Deleted

The repeated per-persona explanatory list and its obsolete copy assertions. Replaced them with coverage for the single warning, matching targets, legacy clients, multiple affected personas, and unresolved targets.

## Reused

`describeReusedEnvironmentMove`, the design-system `Alert` / `AlertDescription`, and the existing persona cards and goal editor.

## Production signal

After deployment, Swarms Confirm should show one warning above the persona cards for moved existing goals, and none for matching goals. No new telemetry is required for this presentation-only change.

## Checklist

- [x] I can explain every line of this diff without the agent that wrote it.
- [x] Under 400 hand-written changed lines, or labelled `large-pr` / `mechanical`.
- [x] No new `as any`, empty `catch`, `.catch(() => {})` or raw `console` on the server.
- [x] Comments say why the code is this way, not how it got here.

Link to Devin session: https://app.devin.ai/sessions/cc4b699a4204432d987d9d6aab2cfb1f
Open in Devin Desktop: https://app.devin.ai/desktop/session/cc4b699a4204432d987d9d6aab2cfb1f?variant=devin
Requested by: @prathmeshpatel

<!-- codesmith:footer -->
---
<a href="https://app.blacksmith.sh/MCPJam/codesmith/inspector/pr/6383?autoLogin=true&ref=codesmith_pr_footer"><picture><source media="(prefers-color-scheme: dark)" srcset="https://pr-comments-assets.blacksmith.sh/codesmith/view-with-codesmith-dark-v3.svg"><source media="(prefers-color-scheme: light)" srcset="https://pr-comments-assets.blacksmith.sh/codesmith/view-with-codesmith-light-v3.svg"><img alt="View with [code]smith" src="https://pr-comments-assets.blacksmith.sh/codesmith/view-with-codesmith-dark-v3.svg"></picture></a> <a href="https://backend.blacksmith.sh/track/enable-autofix?expires=1794608225&installation_model_id=436730&pr_number=6383&ref=codesmith_pr_footer&repository=MCPJam%2Finspector&return_to=https%3A%2F%2Fgithub.com%2FMCPJam%2Finspector%2Fpull%2F6383&signature=992cb1cf549b8909a1cb8c05d529659284ba56a578bced4f1a9b33e4f47d2e55"><picture><source media="(prefers-color-scheme: dark)" srcset="https://pr-comments-assets.blacksmith.sh/codesmith/autofix-with-codesmith-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://pr-comments-assets.blacksmith.sh/codesmith/autofix-with-codesmith-light.svg"><img alt="Autofix with [code]smith" src="https://pr-comments-assets.blacksmith.sh/codesmith/autofix-with-codesmith-dark.svg"></picture></a>
<sup>Need help on this PR? Tag <code>@codesmith-bot</code> with what you need.</sup>

<!-- codesmith:autofix:disabled -->
<!-- /codesmith:footer -->
