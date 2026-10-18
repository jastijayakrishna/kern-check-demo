# refactor(playground-ui): reuse scoped composer shortcuts

**─────── TLDR ───────**
> Composer commands share keyboard shortcut handling through the existing input ref.

`useComposerCommands` registers its shortcuts with `useKeydown({ … }, { target: inputRef })`. Factory and Storybook keep named handlers for normal submission and their local conditions, with an early return when `event.defaultPrevented` is true.

A shortcut targets a textarea directly
&nbsp;&nbsp;├─ **was** — the shared dispatcher skipped its unmodified keys
&nbsp;&nbsp;└─ **now** — the field handles its bindings; ancestor shortcuts leave typing alone

An IME confirmation reports `keyCode: 229`
&nbsp;&nbsp;├─ **was** — shared shortcuts could still fire
&nbsp;&nbsp;└─ **now** — the dispatcher ignores it and clears any pending sequence

Consumers should attach `inputRef` to the input and remove manual calls to `inputProps.onKeyDown`. The changeset includes the before/after integration. Exact commands without options still reach the caller's submit handler.

The listener keeps `[enabled, target, shared]` as its effect dependencies, as on `main`. Mount the input with the hook. The existing provider and scopes handle shared shortcut registration; combo matching, timed sequences, and table navigation keep their implementation from `main`.

---

> ██████████████████ **tests** `+99 −1`
> ██████████ **source** `+58 −53`
> █████ **changeset** `+30`


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## ELI5

Composer keyboard shortcuts now listen directly to the input. This removes duplicate event handling and keeps normal submission behavior unchanged.

## Changes

- Refactored `useComposerCommands` to use `useKeydown` with `inputRef`.
- Updated Factory and Storybook composers to attach `inputRef` and use local submission handlers.
- Ignored already-prevented events and IME composition events, including `keyCode: 229`.
- Preserved exact-command submission, shortcut matching, navigation, and sequence handling.
- Updated documentation, integration tests, and added keyboard listener coverage.
- Added a patch changeset for `@mastra/playground-ui`.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->
