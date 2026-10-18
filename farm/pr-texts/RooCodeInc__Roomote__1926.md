# Make Slack automation configuration less prominent

## Summary

- replace Configure buttons in Slack automation result cards with a single-item overflow menu
- place the overflow in the first available section accessory so it appears at the upper right of compact cards
- fall back to the actions row for Markdown, table, image, or otherwise occupied layouts
- preserve primary task, pull request, and automation-specific actions

## Validation

- 460 Slack package tests
- 74 affected SDK tests
- 17 affected API tests
- Slack, SDK, and API TypeScript checks
- repository pre-push lint, fast typecheck, and knip gates
