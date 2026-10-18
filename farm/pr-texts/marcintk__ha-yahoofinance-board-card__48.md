# feat: add show_version option independent of debug

## Summary

- Add `show_version` boolean config option that shows the card version badge (top-left corner)
- Decouple version badge from `debug` — each flag now controls its own area independently
- `debug: true` shows debug overlay only; `show_version: true` shows version badge only

## Test plan

- [x] `show_version: true` renders version badge, no debug overlay
- [x] `debug: true` renders debug overlay, no version badge
- [x] Both together renders both
- [x] `npm test` — 264 tests pass

🤖 Generated with [Claude Code](https://claude.com/claude-code)
