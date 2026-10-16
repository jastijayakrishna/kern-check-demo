# fix: tests in the horizon branch

## Summary
Fixes TypeScript compilation errors in indexer-cli tests by adding the required `isLegacy` property to Action model test data.

Also adds `@graphprotocol/horizon` and `@graphprotocol/subgraph-service` as explicit dependencies to resolve address book issues.

## Context
1. The `Action` model in indexer-common now requires an `isLegacy` property, but the test utility in indexer-cli was creating Action records without this property, causing TypeScript compilation errors.

2. The `@graphprotocol/toolshed` package requires `@graphprotocol/horizon` and `@graphprotocol/subgraph-service` for their address book files, but these weren't declared as dependencies. This caused "Address book path not found" errors when running tests.

## Changes
- Added `isLegacy: false` to both Action.create() calls in `packages/indexer-cli/src/__tests__/util.ts`
- Added `@graphprotocol/horizon` v0.4.1 and `@graphprotocol/subgraph-service` v0.4.1 as explicit dependencies to indexer-common
- Minor linting/formatting adjustments in other files

## Test Results
After these changes:
- **indexer-common**: All tests pass ✅
- **indexer-agent**: All tests pass ✅
- **indexer-cli**: TypeScript compilation errors resolved ✅

## Note
Adding these packages as explicit dependencies avoids the circular dependency issue discovered in https://github.com/graphprotocol/contracts/pull/1210

🤖 Generated with [Claude Code](https://claude.ai/code)
