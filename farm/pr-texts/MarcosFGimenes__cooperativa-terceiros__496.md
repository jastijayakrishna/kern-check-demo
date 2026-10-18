# Firestore reads audit: canonical displayStatus, search/indexes, token fixes and backfill tooling

### Motivation

- Reduce Firestore read amplification (remove N+1 queries) and make `displayStatus` canonical to enable efficient dashboard aggregation and one-index queries. 
- Provide safe write planning and chunked package creation to avoid exceeding Firestore batch limits during large operations. 
- Consolidate token handling to a canonical single-token model and add tooling to backfill search tokens, assignments and display status. 
- Add server-side caching tags and explicit cache invalidation hooks to keep UI surfaces efficient and consistent.

### Description

- Introduces a Firestore reads audit document (`FIRESTORE_READS_AUDIT.md`) and a new composite index in `firestore.indexes.json` for `services: displayStatus/packageId/folderId/createdAt` to remove the previous per-candidate folder queries. 
- Implements canonical display status and search/assignment helpers: `src/lib/serviceStatus.ts`, `src/lib/serviceSearch.ts`, `src/lib/serviceAssignment.ts`, `src/lib/accessTokenState.ts`, `src/lib/firestoreWriteLimits.ts`, and `src/lib/progressUpdateStrategy.ts`, and wires them into server functions and repo layers (`functions/src/index.ts`, `src/lib/progressHistoryServer.ts`, `src/lib/repo/services.ts`, `src/lib/repo/packages.ts`, `src/lib/repo/folders.ts`, `src/lib/repo/accessTokens.ts`). 
- Adds backfill and admin tooling: `scripts/backfill-*` (display-status, service-search, service-assignment), `scripts/backfill-common.ts`, and `scripts/run-ts.cjs`, plus `package.json` scripts to run them and a management API endpoint to revalidate service dashboard caches (`src/app/api/management/services/cache/route.ts`). 
- Client-side and infra adjustments: increased search debounce to `400ms`, added local displayStatus resolution and dashboard cache invalidation calls in service edit flows, cursor encoding/pagination improvements, safer package creation/chunked writes, and various cache/tag revalidation improvements. 

### Testing

- Ran unit tests with `npm test` (Vitest) covering newly added suites `tests/unit/*` including `accessTokens.test.ts`, `firestoreWriteLimits.test.ts`, `progressUpdateStrategy.test.ts`, `serviceAssignment.test.ts`, `serviceSearch.test.ts`, and `serviceStatus.test.ts`; all unit tests passed. 
- No production instrumentation changes were made; Firestore Console / Monitoring is recommended to validate reads after deployment.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a871109ff1883299ee3cdf68c52cffb)
