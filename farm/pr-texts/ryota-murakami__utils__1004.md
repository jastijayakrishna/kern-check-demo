# Fix lint errors in next-react package (#1003)

# Fix lint errors in next-react package

This PR addresses issue #1003 by fixing lint errors in the packages/next-react directory:

## Changes
- Removed unused imports (`beforeEach`, `debug`, `Mail`) from various files
- Fixed unescaped HTML entities in Dialog.stories.tsx
- Replaced `any` type assertions with proper TypeScript types in:
  - Chart.stories.tsx
  - Form.stories.tsx
  - InputOTP.stories.tsx
- Created custom story types to properly type Storybook components

## Testing
- Verified all changes with `pnpm lint` in the packages/next-react directory
- All ESLint warnings and errors have been resolved

Link to Devin run: https://app.devin.ai/sessions/2353d59366f449a89003100f17d3b580
Requested by: Ryota Murakami


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **Refactor**
  - Simplified Storybook stories for chart, form, and OTP input components by removing indirection through `args` and updating type definitions for improved clarity.
  - Updated story definitions to use explicit render functions and direct prop usage.
  - Cleaned up imports and removed unused icons and variables in several component stories and test files.

- **Style**
  - Replaced straight apostrophes with HTML entities in some story content for consistency.
  - Adjusted minor whitespace in select files.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->
