# feat: hero cards brand only the header and the ranking bars

## Summary
- `DemoCard` no longer wears its scene's palette on the whole card — the founder call: too two-tone
- `data-register` now scopes exactly two subtrees: the in-card **HeaderBar** wrapper and the **ranking bars** `<ol>` (shared by the blurred decoy and the live climbing bars)
- Everything else in the card reverts to the page's default blue

## Test plan
- [x] 53 hero-demo tests pass
- [x] tsc clean, Prettier clean

🤖 Generated with [Claude Code](https://claude.com/claude-code)
