# feat(ux): novice-first product experience (NOVICE FIRST · EXPERT FAST)

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary

System-wide UX pass so a first-time, non-technical user can operate HQ without training — while keeping full ops power, routes, auth, APIs, and ticket/WhatsApp logic.

### Shared patterns
- Primary nav: **ראשי · תקלות · הודעות · סניפים · עוד**
- Human Hebrew status vocabulary
- `src/modules/ux/human-copy.ts` — next-action interpretation
- Simple typography page headers (no black title plates on reports)

### Screens
- **ראשי** — assistant feed + soft “מה קורה היום”
- **תקלות** — next-step block, verb CTAs, progressive SLA details
- **הודעות** — “אתה עונה עכשיו” / “החזר לבוט”
- **סניפים / ציוד / דוחות / ניהול** — renamed and re-described

## Checklist

- [x] Unit tests pass (245)
- [x] E2E golden-path + visual-pack updated locally
- [ ] CI green after e2e snapshot refresh

## Test plan

- [x] `npm test`
- [x] `npx playwright test e2e/golden-path.spec.ts e2e/visual-pack.spec.ts --project=chromium`
- [ ] Full CI suite

<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-01a03fd0-74e8-7c6d-a3fb-f7039a7b18b3?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-01a03fd0-74e8-7c6d-a3fb-f7039a7b18b3&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>


