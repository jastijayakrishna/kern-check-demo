# fix: Resolve merge conflicts with v1 on homepage redesign

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary

Resolves the merge conflict between `design/homepage-redesign` and `v1` (PR #1161).

The only conflict was in `.changeset/pre.json`: `v1` added four changeset entries that the redesign branch did not have. Resolution keeps `v1`'s full changeset list:

- `align-missing-schema-host-hints`
- `align-v1-shared-missing-schema-errors`
- `optional-strict-shared-v1`
- `split-help-global-init-options`

Merging this into `design/homepage-redesign` should make #1161 mergeable into `v1` again.

## Test plan

- [x] Confirmed single conflict file (`.changeset/pre.json`)
- [x] Valid JSON after resolution
- [x] Matching changeset markdown files present from `v1`

<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-8aa99b59-c809-4964-b433-6e2399e9d0ca"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-8aa99b59-c809-4964-b433-6e2399e9d0ca"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
