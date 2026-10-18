# Add normalized Postgres store

## Summary
- add `ROUNDTABLE_STORE_DRIVER=postgres_normalized` with separate tables for users, workbenches, chats, messages, artifacts, handoffs, profiles, user skills, workbench pins, turns, and missions
- keep the existing `RoundtableData` action API while writing normalized Postgres rows inside a transaction with an advisory lock
- update migration, local Postgres smoke, env docs, and README so production/dev can opt into the normalized driver

## Verification
- `corepack pnpm typecheck`
- `corepack pnpm lint`
- `corepack pnpm test`
- `DATABASE_URL=postgres://roundtable:roundtable@localhost:5432/roundtable ROUNDTABLE_STORE_DRIVER=postgres_normalized corepack pnpm build`
- `DATABASE_URL=postgres://roundtable:roundtable@localhost:5432/roundtable ROUNDTABLE_STORE_DRIVER=postgres_normalized ROUNDTABLE_STORE_KEY=codex_normalized_smoke corepack pnpm tsx src/cli/postgres-smoke.ts`
- `ROUNDTABLE_STORE_KEY=codex_package_smoke corepack pnpm db:smoke:local`

## Notes
- the legacy `postgres` driver remains available for rollback/compatibility and still uses the single `roundtable_store` JSONB row
- new production environments should set `ROUNDTABLE_STORE_DRIVER=postgres_normalized` after migrating existing JSON data

