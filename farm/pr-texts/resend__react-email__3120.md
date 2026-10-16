# chore(editor): bring over dashboard's email theming updates over

## Description

This PR refactors the email theming CSS transformation logic to make the base font size used for em unit calculations configurable, rather than hardcoded to 13px.

## Changes

- **Added `DEFAULT_INBOX_FONT_SIZE_PX` constant** (14px) to `themes.ts` to define the standard inbox font size
- **Updated `transformToCssJs` function signature** to accept a `baseFontSize` parameter, replacing the hardcoded 13px value used in fontSize em conversions
- **Updated all callers** of `transformToCssJs` in `extension.tsx` to pass `DEFAULT_INBOX_FONT_SIZE_PX`
- **Renamed `PREVIEW_THEME_OVERWRITE`** to `INBOX_EMAIL_DEFAULTS` for clarity
- **Updated `RESET_BASIC` theme** to use 14px as the base font size (changed from 16px)
- **Reorganized test structure** in `css-transforms.spec.ts` to use `describe` blocks for better organization
- **Updated test expectations** to reflect the new 14px base font size in em calculations

## Test Plan

Existing unit tests in `css-transforms.spec.ts` have been updated and now verify that:
- Font size conversions use the configurable `DEFAULT_INBOX_FONT_SIZE_PX` value
- All CSS transformation scenarios continue to work correctly with the new base font size
- The function properly handles edge cases (null, undefined, non-array inputs)

All tests pass with the updated calculations.

https://claude.ai/code/session_01YCjv2SgRT4zNMQsArocnV2

<!-- This is an auto-generated description by cubic. -->
---
## Summary by cubic
Make font-size conversion configurable with a 14px base to standardize email rendering and fix font sizing in email themes. Aligns theme structure and properties with the latest editor spec.

- **Refactors**
  - `transformToCssJs(styleArray, baseFontSize)` now accepts a base; callers pass `DEFAULT_INBOX_FONT_SIZE_PX` (14).
  - Renamed `PREVIEW_THEME_OVERWRITE` → `INBOX_EMAIL_DEFAULTS`; `RESET_BASIC.body.fontSize` set to 14px; tests updated for 14px em math and the “Text” rename.
  - Bumped `@react-email/editor` to `0.0.0-experimental.32`.

- **New Features**
  - Added `DEFAULT_INBOX_FONT_SIZE_PX` and helpers `resolveResetValue`, `getThemeBodyFontSizePx`.
  - Added `h1`, `h2`, `h3` panel groups; renamed “Typography” to “Text”; `PanelGroup` now supports `category`.
  - Added `letterSpacing` to supported CSS properties.

<sup>Written for commit ed521dc30712ef4d9a63a23be342ff888b979c58. Summary will update on new commits.</sup>

<!-- End of auto-generated description by cubic. -->
