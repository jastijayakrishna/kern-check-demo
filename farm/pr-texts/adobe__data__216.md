# fix(ecs): index inserted rows by stored values so defaultFactory columns are indexed

## Problem
An index whose `key` or `order.by` reads a `defaultFactory` component did not contain rows whose insert omitted that component. The archetype minted and stored the value, but `decorateArchetypeForIndexes` passed the raw insert payload to `indexRegistry.applyInsert`, so the row was filed without it (and dropped from `find()` until a later update re-read the stored row).

## Fix
`applyInsert(entity, archetype)` now reads the stored row (the same reader `applyUpdate` uses) instead of taking the payload. The read is skipped when no index applies to the archetype, so un-indexed inserts cost nothing extra.

## Tests
Red/green in `default-factory.test.ts`: an index ordered by a minted `guid`, and one keyed by it, both include the minted row right after insert. Both fail before the fix and pass after it. Full monorepo `pnpm run test` / `typecheck` / `lint` pass.

Version bumped to 0.10.28.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
