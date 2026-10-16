# feat: add Text component with semantic type prop and sub-components

## 📝 Description

Adds a new `Text` typography primitive to HeroUI Native with a compound API exposing `Text.Heading`, `Text.Paragraph`, and `Text.Code` sub-components. The root component selects a semantic typography preset via `type` and exposes orthogonal `align`, `color`, `weight`, and `truncate` props built on top of `tailwind-variants`.

## ⛳️ Current behavior (updates)

There is no built-in typography primitive in HeroUI Native, so consumers had to compose React Native's `Text` with custom styles for headings, body copy, and inline code.

## 🚀 New behavior

- New `Text` component with semantic `type` variants (`h1`–`h6`, `body`, `body-sm`, `body-xs`, `code`).
- Sub-components: `Text.Heading` (auto-sets `accessibilityRole="header"`), `Text.Paragraph`, and `Text.Code` (chip-styled inline monospaced text).
- Orthogonal props: `align` (RTL-aware `start`/`end`, plus `center`/`justify`), `color` (`default` | `muted`), `weight` override, and `truncate` (maps to `numberOfLines={1}`).
- Platform-appropriate monospace `fontFamily` for `code` (Menlo on iOS, `monospace` elsewhere).
- Component documentation (`text.md`), example screen, and registration in the public exports and example app navigation.

## 💣 Is this a breaking change (Yes/No):

**No** - The change is purely additive: a new component module and a new export from `src/index.tsx`. No existing APIs are modified.

## 📝 Additional Information

The component is built on the internal `HeroText` primitive and reuses `combineStyles` and `tailwind-variants` for styling, so it integrates with the existing theming system without new dependencies. An explicit `numberOfLines` prop always takes precedence over `truncate`, and `weight` overrides any weight implied by `type` via `tailwind-merge`.
