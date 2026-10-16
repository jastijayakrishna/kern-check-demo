# fix(shared): update validate() signature to accept undefined

## Summary
- Updates `validate()` in `shared` to accept `object | undefined` for `architecture` and `patternOrSchema` parameters, matching the function's existing runtime behaviour (it already handles undefined via truthiness checks)
- Adds an explicit runtime guard in the CLI caller, replacing unsafe `as object` type assertions

## Context
Raised by Copilot review on #2186 — the `as object` casts in the CLI were bypassing TypeScript's type safety. The root cause was that `validate()`'s signature declared both parameters as non-nullable `object`, even though the function already handles `undefined` internally.

## Test plan
- [x] `npm run build` passes
- [x] `npm test` passes across all workspaces (shared change requires full test run)
- [x] No downstream type breakage in CLI or VS Code plugin

🤖 Generated with [Claude Code](https://claude.com/claude-code)
