# Require citizenship agreement checkbox on validation step

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary
Adds a Citizenship Agreement checkbox to the citizen onboarding validation step (`/citizenship/validation`). Applicants must accept the agreement before they can finalize citizenship.

## Changes
- Show the existing Citizenship Agreement checkbox (with link to the agreement doc) above the apply CTA for non-members on the validation step
- Disable the apply button until the checkbox is checked
- Guard the apply API call so it cannot proceed without acceptance

## Notes
- Reuses existing EN/PT strings (`subscriptions_citizen_read_agreement`, `subscriptions_citizen_agree_to_terms`) and the same agreement URL already used in `CitizenApply` / finance flows
- Buy/finance token paths are unchanged; those CTAs live in the tokens quest card and finance already requires the agreement separately

<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-01a04ccc-025d-7a82-8489-2ee4b12e0ec8?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-01a04ccc-025d-7a82-8489-2ee4b12e0ec8&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
