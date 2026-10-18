# fix(components): add divider between filled buttons in compact ButtonGroup

## Summary

Split buttons built from a compact `ButtonGroup` (`Button` + `IconButton`, both `variant="primary"`) render as one uninterrupted blue slab — there is no line separating the two halves. Reported in LaunchDarkly's #cringe channel on the approval request "Apply changes" split button.

Why: `.buttonGroup` only strips inner radii and overlaps the halves with `margin-inline-start: -1px`; the visible seam used to come from the buttons' own 1px border, which `primary`/`destructive` lost in #1472 (`border: none`). The legacy `SplitButton` package drew the seam explicitly (`border-right: 1px solid …` on the main half) and that behavior disappeared with the RAC migration.

Changes:
- `ButtonGroup` now emits `data-spacing={spacing}` alongside the existing `data-orientation`, so styles can key off compact grouping.
- `Button.module.css` gives `.primary`/`.destructive` a `--lp-button-divider-color` and draws a 1px `border-inline-start` (or `border-block-start` when vertical) on any such button that isn't the first child of a compact group. Bordered variants (`default`) already show a seam from their own border and are untouched; `minimal`/`picker` are untouched.
- New `PrimarySplitButton` and `DestructiveSplitButton` stories so Chromatic covers both filled split buttons.

The divider color is `color-mix(in oklab, var(--lp-color-shadow-interactive-primary) 40%, <variant fill>)` — the filled-button focus-ring token blended into the variant's base fill rather than into `transparent`, so the line is fully opaque and doesn't shift when the button underneath it hovers or is pressed. `--lp-color-border-interactive-primary-base` was the first candidate but resolves to `transparent` in both themes, which yields an invisible line.

Because the border is added on the overlapped edge only, the group's overall width/height is unchanged (`box-sizing: border-box` + the existing -1px margin).

## Screenshots (if appropriate):

Light theme — before / after

![before light](https://app.devin.ai/api/presigned_proxy?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcmdfaWQiOiJvcmdfaGVBMWRpc2owVHVLd2VVSyIsInVzZXJfaWQiOm51bGwsImJ1Y2tldF9uYW1lIjoiZGV2aW5hdHRhY2htZW50cyIsImJ1Y2tldF9rZXkiOiJhdHRhY2htZW50c19wcml2YXRlL29yZ19oZUExZGlzajBUdUt3ZVVLL2ZlNTlkZjQ0LWEyOGUtNDc1MS1hNDM4LTQwOWZlOTc5MzFjOSIsImlhdCI6MTc4NTI2MTI0NCwiZXhwIjoxNzg1ODY2MDQ0LCJmaWxlbmFtZSI6InNwbGl0LWJ1dHRvbi1iZWZvcmUucG5nIn0.UDSBVg-fhp9SZvxu1Zykdj_ZYQlC1T24r5nnS47Lc_A)

![after light](https://app.devin.ai/api/presigned_proxy?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcmdfaWQiOiJvcmdfaGVBMWRpc2owVHVLd2VVSyIsInVzZXJfaWQiOm51bGwsImJ1Y2tldF9uYW1lIjoiZGV2aW5hdHRhY2htZW50cyIsImJ1Y2tldF9rZXkiOiJhdHRhY2htZW50c19wcml2YXRlL29yZ19oZUExZGlzajBUdUt3ZVVLL2NjMTQ5YTAyLTM3ZjItNGRiMy05MTZmLTYyMjM5ODg3YzM4YSIsImlhdCI6MTc4NTI2MTI0NCwiZXhwIjoxNzg1ODY2MDQ0LCJmaWxlbmFtZSI6InNwbGl0LWJ1dHRvbi1hZnRlci5wbmcifQ.TKpYS0rQIOBBJxhtcJmrtBw8nIEUg5EOTZB95K8980w)

Dark theme — before / after

![before dark](https://app.devin.ai/api/presigned_proxy?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcmdfaWQiOiJvcmdfaGVBMWRpc2owVHVLd2VVSyIsInVzZXJfaWQiOm51bGwsImJ1Y2tldF9uYW1lIjoiZGV2aW5hdHRhY2htZW50cyIsImJ1Y2tldF9rZXkiOiJhdHRhY2htZW50c19wcml2YXRlL29yZ19oZUExZGlzajBUdUt3ZVVLLzMzMWJhMGYxLWVjNTktNGY3Yy05MWM3LWE2ZDg4YzM1MDJmMCIsImlhdCI6MTc4NTI2MTI0NCwiZXhwIjoxNzg1ODY2MDQ0LCJmaWxlbmFtZSI6InNwbGl0LWJ1dHRvbi1iZWZvcmUtZGFyay5wbmcifQ.DxFrJ2TsPwpy6Xix7xaSbPiU7xNU74LFHZiLRu3MGgA)

![after dark](https://app.devin.ai/api/presigned_proxy?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcmdfaWQiOiJvcmdfaGVBMWRpc2owVHVLd2VVSyIsInVzZXJfaWQiOm51bGwsImJ1Y2tldF9uYW1lIjoiZGV2aW5hdHRhY2htZW50cyIsImJ1Y2tldF9rZXkiOiJhdHRhY2htZW50c19wcml2YXRlL29yZ19oZUExZGlzajBUdUt3ZVVLLzI3NmUzOGNmLWQ3NGUtNDQyMy1hNWFjLTFhOGY2YmQxNTkxMyIsImlhdCI6MTc4NTI2MTI0NSwiZXhwIjoxNzg1ODY2MDQ1LCJmaWxlbmFtZSI6InNwbGl0LWJ1dHRvbi1hZnRlci1kYXJrLnBuZyJ9.kL_8wCph0KhfZClp57EjOkz3yM8EaxmCzxAZ39n4iTQ)

Hovering the primary half — divider color is unchanged

![after hover](https://app.devin.ai/api
