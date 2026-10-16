# Add selective alias disable and version check

## Summary
- store disabled component aliases in `PomlFile`
- allow `getComponent` to take a disabled set
- skip disabled aliases when searching and suggesting
- expand meta tag tests to cover alias-only disabling
- Support minVersion and maxVersion check

## Testing
- `npm run build-webview`
- `npm run build-cli`
- `npm run lint` *(with warnings)*
- `npm test`
- `python -m pytest python/tests`


------
https://chatgpt.com/codex/tasks/task_e_687739351228832eb5d8933aca68352d
