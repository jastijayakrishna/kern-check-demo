# feat: replace custom period filter label with calendar icon

Closes #84

## Summary

Replaces the visible "Custom" / "Perso" text on the custom period slot with a 16px `Calendar03Icon` inside the existing join group.

## Changes

- Custom slot only: `btn-sm btn-square join-item` with `btn-outline` / `btn-primary` when active
- Tooltip + `aria-label` still use existing `period.custom` i18n key
- `7d` / `30d` / `90d` remain text buttons
- Date inputs unchanged (shown only when `period_key === 'custom'`)

## Verification

- [x] `npm run check` passes locally

<div><a href="https://cursor.com/agents/bc-6302d51c-b32c-48f7-9fba-92341f26578f?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/automations/09f675ba-942a-11f1-ba66-0e7d0216e441"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/view-automation-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/view-automation-light.png"><img alt="View Automation" width="141" height="28" src="https://cursor.com/assets/images/view-automation-dark.png"></picture></a>&nbsp;</div>


