# [codex] wire git ref chip native overlay

## Summary
- wire the terminal Git ref chip through the native overlay menu transport
- keep copy feedback pending until the owner renderer confirms clipboard success
- make the Git ref overlay theme-aware, opaque, and keep the Git chip borderless in all states
- centralize Escape dismissal without double-closing controlled context menus

## Validation
- pre-push suite: 365 test files passed, 4454 tests passed, 3 skipped
- lint-staged on commit/amend: eslint, prettier, tsc
- focused native overlay/GitRefChip/Menu checks during development


Refs VIM-263
