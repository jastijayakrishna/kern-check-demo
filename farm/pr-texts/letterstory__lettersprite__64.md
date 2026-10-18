# fix: cast baked bot-manifest JSON through unknown before ManifestPayload

## What

Hotfix for #63: all three initial test-site production redeploys (eldercareamerican.com, letternode.com, govtechrev.com) failed `npm run build` on Vercel with:

```
Type error: Conversion of type '{ ok: boolean; version: number; generatedAt: string; ... }' to type 'ManifestPayload' may be a mistake because neither type sufficiently overlaps with the other.
```

A clean local `npm run build` against the identical commit and file content (`src/generated/bot-manifest.json` = `{"ok":false}`, confirmed via `git show origin/main:...`) passes with zero errors — so this is specific to Vercel's build-time type check, not the committed source. Root cause not conclusively pinned (looks like a stale build-cache artifact on Vercel's side inferring a shape from a different generation of the file), but the fix is correct independent of cause: `bot-manifest.json` is regenerated per build (placeholder today, a live vendor payload tomorrow) and `compile()` already validates its actual shape at runtime — trusting `resolveJsonModule`'s build-time structural inference for a file whose content varies by design was never the right tool. Routing the cast through `unknown` first (exactly what TS's own error message suggests) makes it immune to whatever gets inferred.

## Verification
- tsc, vitest (35 tests), eslint, and `npm run build` all pass locally.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
