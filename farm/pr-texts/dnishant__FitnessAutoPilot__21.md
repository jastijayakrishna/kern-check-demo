# PLAN-005: Add search-grounded culinary discovery

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary

Search-grounded culinary discovery (PLAN-005): Gemini + Google Search finds diverse, source-backed recipe candidates for Fitness Autopilot — not weekly planning, not full recipes.

## Fixes included

### `DISCOVERY_NOT_GROUNDED`
1. Enables `googleSearch` **without** structured-output mime/schema (Gemini 3.x drops grounding metadata when those are combined)
2. Prompts for brief grounded notes, then a trailing fenced JSON block
3. Extracts + validates JSON server-side
4. Retries up to 3× with a stronger search nudge when grounding metadata is absent

### `WEEKLY_STRATEGY_VALIDATION_FAILED` (`sharedIngredientIntents` max length)
Gemini sometimes returns ingredient intent strings longer than 80 chars. This PR also:
- Raises the item max to 160
- Truncates oversized labels before domain validation
- Tightens the weekly-strategy prompt for short ingredient phrases

Redeployed `culinary-discovery` and `generate-weekly-strategy` to `izskiyiwoecvgkffylib`.

## Test plan

- [x] Unit tests for discovery grounding + provider retries
- [x] Unit tests for weekly-strategy ingredient intent coercion
- [x] Live discovery smoke (grounding metadata + candidates)
- [ ] Mobile Dev previews after pull: `/culinary-discovery-preview`, weekly strategy preview

<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-01a09773-3d6a-7f41-ab69-b4c9da37e514?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-01a09773-3d6a-7f41-ab69-b4c9da37e514&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>


