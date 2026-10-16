# fix: prevent revenue value overflow in sponsor stats cards

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary

Fixes the CHF revenue card overflow on `/admin/sponsors` when values exceed 4 figures.

## Changes

- Reduced font size from `text-2xl sm:text-3xl` to `text-xl sm:text-2xl` to accommodate larger numbers
- Added `truncate` for overflow handling
- Added `tabular-nums` for consistent number alignment
<!-- CURSOR_AGENT_PR_BODY_END -->

[Slack Thread](https://zurichjs.slack.com/archives/C097TENNED8/p1788191980190739?thread_ts=1788191980.190739&cid=C097TENNED8)

<div><a href="https://cursor.com/agents/bc-28d3a056-3f3d-54a8-be4f-910d563d34ce?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-28d3a056-3f3d-54a8-be4f-910d563d34ce&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>



<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Style**
  * Adjusted sponsorship statistics card values for improved readability and consistency.
  * Added formatting to keep numeric values aligned and prevent overflow.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->
