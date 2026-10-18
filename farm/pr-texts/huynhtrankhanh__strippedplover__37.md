# Add indexed entry pagination

### Motivation
- Paginated enumeration and search currently materialize and sort all entries in memory which is slow and scales poorly.
- Provide indexed scan/query paths so pagination and prefix/substring search can run efficiently without full in-memory sorts.

### Description
- Introduce `EntrySortOrder`, `EntryQueryOptions`, and `EntryQueryResult` types and a new `queryEntries` API on `DatabaseSync` to support paginated indexed queries.
- Add LMDB-backed secondary indexes (`entries_by_translation`, `entries_by_stroke`, `entries_by_stroke_length`) and helpers `indexKey`, `indexPrefix`, `indexPrefixEnd`, and `strokeLength` for building/index scanning.
- Maintain indexes on startup (`rebuildEntryIndexes`) and keep them synchronized on entry insert/update (`setEntry`), delete (`deleteEntry`), and dictionary deletion (`deleteDictionary`) via `addEntryIndexes`/`removeEntryIndexes`.
- Route `enumerate_entries` and `search_entries` in `engine.ts` through `db.queryEntries(...)` and tighten sort type usage with `EntrySortOrder` to avoid materializing and sorting all entries in the engine.

### Testing
- Ran `npm run build` and TypeScript compilation succeeded. 
- Ran targeted tests with `npx vitest run src/engine.entry-search.test.ts src/engine.python-import.test.ts src/engine.dictionary.persistence.test.ts` and they passed. 
- Ran the full test suite with `npm test` and all tests passed.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a4bec06d3a4832ea6782e8545a28429)
