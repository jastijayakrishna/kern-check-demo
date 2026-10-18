# Use Node built-in SQLite for dictionary storage

### Motivation
- Replace the LMDB-based storage layer with Node.js integrated SQLite to regain missing features and simplify deployment. 
- Ensure dictionary operations (lookup, search, import) are fast and indexable, including case-insensitive queries and full-text search. 
- Keep dictionary import throughput high by using prepared statements and transactional bulk inserts.

### Description
- Add a small wrapper `src/sqlite-database.ts` that re-exports `node:sqlite`'s `DatabaseSync` and remove the LMDB adapter `src/lmdb-database.ts`. 
- Switch code imports from `lmdb-database` to `sqlite-database` and remove the `lmdb` runtime dependency from `package.json`. 
- Replace the `entries` schema in `src/engine.ts` with `NOT NULL` columns, add composite and case-insensitive indexes, and create an FTS5 trigram virtual table `entries_fts` with `INSERT/DELETE/UPDATE` triggers to keep FTS rows in sync. 
- Keep bulk imports fast by using a prepared `INSERT OR REPLACE INTO entries` statement inside a single `BEGIN/COMMIT` transaction in `src/dictionary/steno-dictionary.ts`, and add a test that verifies indexes and FTS rows are created and populated after import. 

### Testing
- Ran `npm run build` and TypeScript compilation completed successfully. 
- Ran `npx vitest run src/engine.entry-search.test.ts` and the modified entry-search test suite passed. 
- Ran full test suite with `npm test` and all automated tests passed (`48` tests passed).

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a4c5a517a30832e91830486adf8648d)
