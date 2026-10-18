# fix: change click-through hotkey from ⌥E to ⌥⇧E

## Summary
- `Alt+E` is a macOS dead key (acute accent) — the OS intercepts it before Tauri's global-shortcut plugin can register it, leaving the toggle silently unregistered
- Changed combo to `Alt+Shift+E` which breaks the dead-key behavior
- Updated dev-mode keydown guard and button label to match (`⌥⇧E`)

## Test plan
- [ ] Open overlay, press ⌥⇧E — overlay enters click-through mode
- [ ] Press ⌥⇧E again — overlay returns to interactive mode
- [ ] Button label in overlay toolbar shows `⌥⇧E` / `⌥⇧E·on`

🤖 Generated with [Claude Code](https://claude.com/claude-code)
