# fix: align sdk contracts with public api

## Summary
- correct fetch response optionality and task response input types to match the public API DTOs
- preserve invalid empty date strings for server-side validation and require object-root structured schemas in TypeScript
- clarify fetch, search-depth, structured-output, and X402 documentation

## Validation
- `npm run build`
- `npm run lint`
- `npm test -- --runInBand` (62 tests passed)

<div><a href="https://cursor.com/agents/bc-de164d0d-da2b-434b-aa1c-c8af2c3fb8fc"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/automations/45eabdaa-cdb5-4c92-bb21-d0b466096a38"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/view-automation-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/view-automation-light.png"><img alt="View Automation" width="141" height="28" src="https://cursor.com/assets/images/view-automation-dark.png"></picture></a>&nbsp;</div>
