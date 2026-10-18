# Show full card art instead of a thumbnail in TCG embeds

## Summary
- `tcgHandler`'s embed now uses `image` instead of `thumbnail` for `extra.metadata.imageUrl`. `thumbnail` renders as a small corner icon; `image` spans the embed width, showing the card art at the size it appears on the linked inspect page.
- Updated `tcgHandler.test.js` accordingly (field name + test descriptions).

## Test plan
- `npx vitest run src/__tests__/tcgHandler.test.js` — all 7 tests pass.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
