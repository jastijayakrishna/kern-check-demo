# Prevent inline qwikloader emission inside SVG/MathML foreign content in v2 SSR

Fixes SSR inline `qwikloader` emission guards so scripts are not injected while serializing unsupported parser contexts, with focus on SVG/MathML foreign content and other blocked parser-state elements.

### Changes made

- Replaced ad-hoc guard checks with a shared blocked-elements guard in SSR container emission logic.
- Added/updated SSR container regression coverage for:
  - foreign content (`svg`, `math`)
  - blocked parser-state elements tracked by the no-script refcounter
- Updated spec loops to comply with `qwik-local/loop-style`.
- Removed the deprecated `plaintext`-specific loader behavior and its related test based on review feedback.

### Validation

- Reproduced the original lint and vitest failures.
- Re-ran targeted lint and SSR container tests successfully.
- Ran final validation (code review + CodeQL) with no blocking issues.
