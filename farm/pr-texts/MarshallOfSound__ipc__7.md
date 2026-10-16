# fix: use export * for common external to avoid Rollup type-only export issues

## Summary

When generating `common.external`, named exports like `export { X, Y, Z }` cause Rollup to fail when some exports are type-only (e.g., interfaces imported elsewhere with `import type`).

This PR changes `common.external` to use `export *` instead, which allows Rollup to handle mixed type/value exports correctly.

## Alternative considered

We briefly considered a more sophisticated approach where we track export categories during codegen:
- Mark enums/validators as `'value'` exports
- Mark structures/subtypes/interfaces as `'type'` exports  
- Generate separate `export type { ... }` and `export { ... }` statements

However, this felt less surgical and more prone to issues since it would require changes across ~6 files (controller, wire, and each wiring module) and replicates type analysis that TypeScript/bundlers already handle. The `export *` approach solves the problem in 1 line and delegates the type/value distinction to the tools that already understand it.

## Test plan

- [x] Added failing test that asserts `common.external` uses `export *`
- [x] All 202 existing tests pass

🤖 Generated with [Claude Code](https://claude.ai/code)
