# feat(playground-ui): share composer slash-command suggestions

**─────── TLDR ───────**
> Type `/` in the conversation story to select a command through reusable playground-ui components.

Using commands in `AI/Chat / Conversation`
&nbsp;&nbsp;├─ **was** — `/` stayed plain text with no suggestions
&nbsp;&nbsp;└─ **now** — filter commands, open options, and submit a fixture message

Adds `ComposerSuggestions` and `useComposerCommands` to the Composer exports. The hook owns matching, keyboard selection, and focus; the caller supplies commands, the draft, and execution. Exact commands without options and free-form arguments keep the caller's normal submission path.

Includes focused stories for command options, unmatched input, disabled suggestions, and 500 commands. Factory adoption follows in #23768.

Verified 68 targeted tests, the package typecheck, and library and Storybook builds. All five conversation interaction stories pass in the browser; command menus were checked at desktop, tablet, and mobile widths, with 500 commands and reduced motion. React Doctor found no issues in the changed files.

---

> ██████████████████ **shared UI** `+253`
> ████████████ **stories and fixtures** `+166 −7`
> ██████████ **interaction tests** `+134`
> ██ **changeset** `+24`

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## ELI5

This PR lets users type `/` in a chat box to find and run available commands. Users can filter commands, choose options with the keyboard or mouse, and keep normal message submission for regular text.

## Changes

- Added reusable `ComposerSuggestions` and `useComposerCommands` APIs.
- Added command and option matching utilities.
- Added keyboard navigation, selection, focus management, IME handling, and disabled-state support.
- Preserved normal submission for exact commands without options and free-form input.
- Exported the new components, hook, utilities, and types from `Composer`.
- Added Storybook examples for options, unmatched commands, disabled suggestions, and 500-command lists.
- Added interaction tests for filtering, navigation, selection, submission, Escape behavior, IME input, and changing command lists.
- Added a minor changeset.

Targeted tests, typechecking, builds, Storybook interaction stories, responsive checks, reduced-motion testing, and React Doctor validation passed.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->
