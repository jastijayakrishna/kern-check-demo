# feat(frontend): make overlays leave promptly and blur smoothly

# Motivation

Overlays should leave promptly and their backdrop blur should appear smoothly.

# Changes

- Use 200/150 ms toast motion, a 125 ms modal exit, 150/100 ms popover panels, and 250/200 ms bottom sheets.
- Animate backdrop dim and blur directly, with 75/150 ms timing; use intro-only 25 ms container fades for popovers and modals so Chrome can draw the blur and the child exits remain visible.
- Reuse the reduced-motion wrappers and update the motion spec, reusable-pattern docs and PRODUCT.md.

# Tests

- Full Vitest suite before the intro-only container follow-up: 1,253 files and 24,620 tests passed (one existing skip, one todo). After the follow-up, all 65 affected modal, popover, menu and transition tests pass.
- Full lint and Svelte checking pass with zero warnings; focused tests cover overlay inputs, backdrop dim/blur and reduced motion.
- Mock browser checks cover desktop menu dim/blur in light and dark and the mobile activity sheet in both themes. Browser tooling does not expose reduced-motion emulation; that behavior is checked with unit tests and compiled CSS.
- `npm run format`, full lint, Svelte checking and test type-checking all pass. Test type-checking uses a temporary overlay with the exact lockfile SDK 11; shared dependencies remain unchanged.

Implemented with OpenAI `gpt-6-astra` via Codex (high reasoning).
