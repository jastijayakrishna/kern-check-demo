# fix: add Tron chain icon to namespace icons in wallet list

# Description

Adds the missing Tron (TRX) chain icon that was not displaying in the multichain/multiwallet wallet list UI. Previously, the `NAMESPACE_ICONS` map in `wui-list-wallet` had `tron` mapped to `undefined`, causing no icon to render for the Tron namespace.

### Changes:
- Created `packages/ui/src/assets/svg/tron.ts` with the official TRON logo SVG
- Added `'tron'` to the `IconType` union type
- Registered the Tron SVG in the `wui-icon` component (import, phosphorIconsMap, svgOptions)
- Mapped `tron` → `'tron'` in the `NAMESPACE_ICONS` constant

> **Reviewer note:** The Tron SVG uses a `viewBox="0 0 64 64"` which is larger than other chain icons (e.g., `0 0 10 10` for TON, `0 0 10 8` for Solana). SVG scaling should handle this correctly, but please verify the icon renders properly at the small namespace icon size in the wallet list. Visual testing on a preview deployment is recommended.

## Type of change

- [ ] Chore (non-breaking change that addresses non-functional tasks, maintenance, or code quality improvements)
- [x] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)

# Associated Issues

Closes REOWN-4527

# Checklist

- [ ] Code in this PR is covered by automated tests (Unit tests, E2E tests)
- [x] My changes generate no new warnings
- [x] I have reviewed my own code
- [x] I have filled out all required sections
- [ ] I have tested my changes on the preview link
- [ ] Approver of this PR confirms that the changes are tested on the preview link

---

Link to Devin session: https://app.devin.ai/sessions/66c7934dad494a9ea9fdf841409c4c8b
Requested by: @magiziz
