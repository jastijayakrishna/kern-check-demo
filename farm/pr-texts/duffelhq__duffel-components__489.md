# Add years to dashboard stay summary dates

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary
- update the stays summary check-in and check-out labels to use the long date format with the year included
- add a focused component test covering the rendered check-in and check-out strings
- pin GitHub Actions used by the CI workflow to full commit SHAs so checks can start under the repository policy

## Testing
- `yarn test src/tests/components/StaysSummary.test.tsx --runInBand`
- `yarn check-types`
- `yarn prettier-check .github/workflows/ci.yml`
- `yarn eslint src/components/Stays/StaysSummary.tsx src/tests/components/StaysSummary.test.tsx`

## Post-merge rollout
1. Manually publish a new `@duffel/components` release.
   - `3.13.1` is already the live npm version, so the release flow needs a version bump first (for example, the next patch version) before publishing.
   - The publish script in this repo is `yarn build-and-publish`.
2. Once that new version is live, upgrade `@duffel/components` in both dashboards.
   - Update the dependency to the released version.
   - Refresh the lockfile.
   - Verify the stays summary check-in / check-out dates show the year.
3. Suggested Cursor prompt for each dashboard repo after publish:
   - `Upgrade @duffel/components to <released-version>, update the lockfile, verify the stay summary check-in and check-out dates now include the year, run the relevant tests/build, and open a PR.`
<!-- CURSOR_AGENT_PR_BODY_END -->

[Slack Thread](https://duffel.slack.com/archives/C06E7PV0UMV/p1776677857196659?thread_ts=1776677857.196659&cid=C06E7PV0UMV)

<div><a href="https://cursor.com/agents/bc-73dbb412-e938-5068-be64-25e84f0c7c91"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-73dbb412-e938-5068-be64-25e84f0c7c91"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
