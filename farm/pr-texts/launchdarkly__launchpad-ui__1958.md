# fix(components): align multi-select ListBox checkbox to the primary line

## Summary

[DSYS-271](https://launchdarkly.atlassian.net/browse/DSYS-271). `ListBoxItem` inherits `align-items: center` from the shared Menu item rule, so in multi-select items with a stacked label/description the selection checkbox floats between the two lines. Per design review the checkbox should sit with the primary (label) line.

`styles/ListBox.module.css` now top-aligns the row only when the item renders a selection checkbox, and gives that checkbox `height: 1lh` with centered content — the same pattern `Checkbox.module.css` `.container` already uses to align a checkbox to the first line of its label:

```css
.item {
	composes: item from './Menu.module.css';

	&:has(.checkbox) { align-items: start; }
	& .checkbox { height: 1lh; align-items: center; }
}
```

`ListBox.tsx` passes the new class through `checkboxStyles({ className: styles.checkbox })`. The `:has()` / descendant selectors are deliberate: `.item` composes the Menu item class, so a bare `.item { align-items: start }` loses the cascade to `Menu.module.css` in the built bundle.

Single-select and non-selectable items keep their current centering, and Menu items are untouched.

## Screenshots (if appropriate):

LaunchPad Storybook — `Components/Collections/ListBox → Descriptions` with `selectionMode: multiple`.

Before:

![before](https://app.devin.ai/api/presigned_proxy?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcmdfaWQiOiJvcmdfaGVBMWRpc2owVHVLd2VVSyIsInVzZXJfaWQiOm51bGwsImJ1Y2tldF9uYW1lIjoiZGV2aW5hdHRhY2htZW50cyIsImJ1Y2tldF9rZXkiOiJhdHRhY2htZW50c19wcml2YXRlL29yZ19oZUExZGlzajBUdUt3ZVVLL2Y5NDNmZDBiLTRkYjYtNGE5MC04ODkyLTJmOWM1M2Q1ODVlMyIsImlhdCI6MTc4NTIwMDAwMSwiZXhwIjoxNzg1ODA0ODAxLCJmaWxlbmFtZSI6ImJlZm9yZS5wbmcifQ.OurlffwkqnMXWXr78zvcIMwyqZXo40BPYoZHyy5kRiU)

After:

![after](https://app.devin.ai/api/presigned_proxy?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcmdfaWQiOiJvcmdfaGVBMWRpc2owVHVLd2VVSyIsInVzZXJfaWQiOm51bGwsImJ1Y2tldF9uYW1lIjoiZGV2aW5hdHRhY2htZW50cyIsImJ1Y2tldF9rZXkiOiJhdHRhY2htZW50c19wcml2YXRlL29yZ19oZUExZGlzajBUdUt3ZVVLLzMyMWZhMTgyLTI3ZWUtNGI0MC1hZWIxLWI1YjY3YjBmYWViMyIsImlhdCI6MTc4NTIwMDAwMSwiZXhwIjoxNzg1ODA0ODAxLCJmaWxlbmFtZSI6ImFmdGVyLnBuZyJ9.2G3fTMtQzH37EPOOT6i6Ld-QnVxriD8ph0IgsTYYfew)

Single-line multi-select and icon items are unaffected:

![grouping](https://app.devin.ai/api/presigned_proxy?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcmdfaWQiOiJvcmdfaGVBMWRpc2owVHVLd2VVSyIsInVzZXJfaWQiOm51bGwsImJ1Y2tldF9uYW1lIjoiZGV2aW5hdHRhY2htZW50cyIsImJ1Y2tldF9rZXkiOiJhdHRhY2htZW50c19wcml2YXRlL29yZ19oZUExZGlzajBUdUt3ZVVLLzI3YjIwZGM1LTYyMjgtNGI4ZC05YTQ2LWI4ZTgzNzNmNzYwYSIsImlhdCI6MTc4NTIwMDAwMSwiZXhwIjoxNzg1ODA0ODAxLCJmaWxlbmFtZSI6Imdyb3VwaW5nLnBuZyJ9.P9Sdsvo8CXXRQBC9ZzdU_TW-cU0a3Ne92DDKNEXiBK4)

![icons](https://app.devin.ai/api/presigned_proxy?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcmdfaWQiOiJvcmdfaGVBMWRpc2owVHVLd2VVSyIsInVzZXJfaWQiOm51bGwsImJ1Y2tldF9uYW1lIjoiZGV2aW5hdHRhY2htZW50cyIsImJ1Y2tldF9rZXkiOiJhdHRhY2htZW50c19wcml2YXRlL29yZ19oZUExZGlzajBUdUt3ZVVLL2YyNDExYTY2LTUxZDAtNDcxMC04NzZlLWUyYzlhMTk4MzIyNyIsImlhdCI6MTc4NTIwMDAwMSwiZXhwIjoxNzg1ODA0ODAxLCJmaWxlbmFtZSI6Imljb25zLnBuZyJ9.WTx9IzoK4RejacBF_yvaQoYyrm06FtSgQyowTxnYto4)

### Product consumers (gonfalon Storybook, built package linked in)

`ContextKindSelector` (multi-select, kinds with descriptions) — the ticket's case:

Before:

![context kind selector before](https://app.devin.ai/api/presigned_proxy?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcmdfaWQiOiJvcmdfaGVBMWRpc2owVHVLd2VVSyIsInVzZXJfaWQiOm51bGwsImJ1Y2tldF9uYW1lIjoiZGV2aW5hdHRhY2htZW50cyIsImJ1Y2tldF9rZXkiOiJhdHRhY2htZW50c19wcml2YXRlL29yZ19oZUExZGlzajBUdUt3ZVVLL2FiN2I4YTMzLWI2OWMtNGUwZS1iMzg4LWZmZjEwMTc2MjFmNCIsImlhdCI6MTc4NTIwMDAwMSwiZXhwIjoxNzg1ODA0ODAxLCJmaWxlbmFtZSI6ImNrZGVzYy1iZWZvcmUucG5nIn0.WnJvKBeA1z-7QDDZP15cMFn9b7ncfCDoxIlk0Yh2SdA)

After:

![context kind selector after](https://app.devin.ai/api/presigned_proxy?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcmdfaWQiOiJvcmdfaGVBMWRpc2owVHVLd2VVSyIsInVzZXJfaWQiOm5
