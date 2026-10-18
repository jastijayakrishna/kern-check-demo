# feat(assets): barcode field, smart scan, Code128 labels, mobile mode

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary

Ports five MediTactic scan patterns into Optical Center assets (follow-up to merged #50). WhatsApp QR stays separate from product barcode / asset labels.

1. **Separate `barcode` field** — migration + API/service/memory; unique per store when set; create form + table column.
2. **Scanner UX** — 1.5s debounce, camera switch, EAN/UPC/Code128 + `optical:asset` QR formats, USB/manual entry.
3. **Smart lookup** — `findAssetByCode` matches barcode → code → name → unique partial / QR payload.
4. **Labels** — Code128 (jsbarcode) + internal asset QR (`optical:asset:…`); WhatsApp QR remains its own row action.
5. **Mobile scan** — `/ops/assets/scan` continuous camera + short session history + create-on-miss.

## Checklist

- [x] Unit / e2e tests pass (`npm test` — 235 passed)
- [ ] Visual regression pack green (`e2e/visual-pack.spec.ts`, `maxDiffPixelRatio: 0.03`)
- [ ] Storybook story updated if UI primitives changed
- [x] No orphan components left behind
- [ ] Phone / RTL sanity checked when UI changed

## Test plan

- [x] `npx vitest run src/modules/assets/barcode.test.ts` (10 passed)
- [x] `npx tsc --noEmit`
- [x] `npm test` (235 passed)
- [x] `npm run lint` (no new errors)
- [ ] Create asset with barcode; scan finds it by barcode and by `optical:asset:` payload
- [ ] Label modal shows Code128 + asset QR; WhatsApp QR still downloads store prefill
- [ ] `/ops/assets/scan` continuous mode + history

<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-01a03fd0-74e8-7c6d-a3fb-f7039a7b18b3?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-01a03fd0-74e8-7c6d-a3fb-f7039a7b18b3&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>


