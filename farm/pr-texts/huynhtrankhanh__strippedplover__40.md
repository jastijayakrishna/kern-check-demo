# Improve entry pagination and search performance

### Motivation
- Exposed pagination and search APIs were materializing and sorting all dictionary entries in memory which became unbounded and slow for large dictionaries.
- Full-text search (FTS) was being rebuilt unconditionally at startup which is unnecessary and expensive for persisted databases.
- Need repeatable stress coverage for large dictionaries (100k–1M entries) to validate API performance and behavior.

### Description
- Query SQLite directly for `enumerate_entries` and `search_entries` using `ORDER BY`, `LIMIT`/`OFFSET`, and `COUNT` to avoid materializing all entries in memory and to keep API response cost bounded.
- Add covering NOCASE indexes (`idx_entries_translation_stroke_dictionary_nocase`, `idx_entries_stroke_translation_dictionary_nocase`) to accelerate common translation/stroke/dictionary sort and filter patterns and preserve existing per-dictionary indexes.
- Use the `entries_fts` table for exposed output substring searches (3+ characters) and use indexed `LIKE` with an `ESCAPE` clause for prefix/mixed searches, with helper methods `sortOrderSql`, `escapeLike`, and `ftsQuery` to build safe SQL.
- Only rebuild the FTS table at startup if there are entries but the FTS table is empty, preventing unnecessary rebuilds on every start.
- Add an opt-in stress test file `src/engine.entry-search.stress.test.ts` that inserts bulk entries directly into the DB and exercises pagination, prefix, and substring query patterns with a 100k smoke test and an opt-in 1,000,000-entry stress run guarded by `RUN_MILLION_ENTRY_STRESS=1`.

### Testing
- Built the project with `npm run build` and the TypeScript compilation succeeded.
- Ran the full test suite with `npm test` and test files passed (unit tests and the added stress smoke test passed; one stress test is opt-in).
- Exercised the stress scenarios by running `npm test -- src/engine.entry-search.stress.test.ts` and `RUN_MILLION_ENTRY_STRESS=1 npm test -- src/engine.entry-search.stress.test.ts`, and both smoke and opt-in million-entry runs completed successfully.
- Verified the new SQL-backed pagination/search behavior reduced memory usage and bounded request latency in the provided smoke and stress tests.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a4c923ffbec832eb231142ebde90afc)
