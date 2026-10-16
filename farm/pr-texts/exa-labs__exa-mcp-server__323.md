# Use highlights: true instead of maxCharacters: 2000 in web_search_exa

## Summary
Updates `web_search_exa` to request `contents.highlights: true` from the Exa API instead of the previous `{ query: cleanedQuery, maxCharacters: 2000 }` form. This lets Exa return its default highlight selection rather than capping at 2000 characters.

Changes:
- `src/tools/webSearch.ts`: swap `highlights: { query: cleanedQuery, maxCharacters: 2000 }` for `highlights: true`.
- `tests/unit/tools/webSearch.test.ts`: update expected request payload.
- `tests/fixtures/exaResponses.ts`: update fixture response type to match `{ highlights: true }`.

The `ExaSearchRequest.contents.highlights` type already accepts `boolean`, so no type changes are required.

## Review & Testing Checklist for Human
- [x] Confirm `highlights: true` is the desired payload shape (vs. e.g. `{}` or omitting `query`/`maxCharacters` while keeping object form).
- [ ] Spot-check a real `web_search_exa` call to verify highlights still come back in the response and are rendered in the formatted output.

### Notes
- No changes to other tools (`webSearchAdvanced`, `deepSearch`, `exaCode`, `webFetch`) — they use `maxCharacters` for different purposes (text extraction, deep search highlights, etc.) and weren't part of this request.
- `npm run ci` (typecheck + vitest) passes locally.

Link to Devin session: https://app.devin.ai/sessions/de320cd3bac84ecda2acfe18de4ba892
Requested by: @scottlangille
