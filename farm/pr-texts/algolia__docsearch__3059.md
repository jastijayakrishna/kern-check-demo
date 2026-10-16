# fix(react): ignore Enter during IME composition

## Summary

Pressing Enter to confirm an IME conversion (Japanese Hiragana, and the same compose/confirm flow for Chinese and Korean input) was treated as select or send.

- In the sidepanel Ask AI prompt, Enter submits the prompt before the candidate is confirmed. This is reproducible on DocSearch 5.
- In keyword search, `@algolia/autocomplete-core` already ignores `keydown` while `isComposing` is true, which is why selecting a document on the confirming Enter was not reproducible on the search modal in Chrome. Safari ends the composition session before that `keydown` and reports `keyCode` 229 with `isComposing === false`, so Enter still selects the active hit. Ask AI replaces Autocomplete's input `onKeyDown`, so the modal Ask AI box had the same hole.

This does not enable `ignoreCompositionEvents`. That option is why #2909 was closed: turning it on by default was reverted in InstantSearch because Android keyboards do not behave smoothly when composition updates are ignored. Queries sent for intermediate composition text are unchanged.

## Changes

- Add `isComposingKey`, which is true when `nativeEvent.isComposing` or `keyCode === 229`.
- The sidepanel `PromptForm` returns before sending when that is true, and does not call `preventDefault`, so the IME can confirm the conversion.
- `SearchBoxForm` applies the same guard before Autocomplete's `onKeyDown` and before the Ask AI override. Enter does not select a hit or call `onAskAgain`, and arrow keys stay with the IME candidate list.
- Tests cover `isComposing: true`, `keyCode: 229`, and a normal Enter that still submits or selects.

## Testing

- `bun run test --run` (444 tests)
- `bun run lint` on the touched files
- `bun run test:types`

Not yet verified manually with a real IME in a browser; happy to add a recording if helpful.

Fixes #1304
