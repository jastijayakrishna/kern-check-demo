# refactor(card-form): simplify saveCard input (No issue)

## Related issue

None.

## Summary

Make `saveCard` accept only `{ id, frontText, backText, tags }` and read the current authentication session internally. Move pending state, duplicate-submit protection, toast feedback, and navigation callbacks into `runCardSave`, preserving the existing editor behavior.

## Testing

- `mise run check` passed: 125 test files, 714 tests.
- Reviewer completed with no findings.

