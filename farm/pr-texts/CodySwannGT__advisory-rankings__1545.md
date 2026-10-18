# perf(harper): migrate profile + analytics endpoints off the loadAll() full scan

## Summary

PR-A2 of the Harper best-practices review: removes the request-wide `loadAll()` **34-table full scan** from every endpoint that can be scoped, and explicitly documents (with rationale) every scan that deliberately stays.

### Phase 1 — profile endpoints: per-entity indexed hydration (shipped)

`/ArticleView`, `/FirmProfile`, `/FirmAdvisors`, `/AdvisorProfile`, `/TeamProfile` no longer call `loadAll()`. New subject-scoped loaders (`src/harper/resource-{advisor,firm,team}-profile-load.ts`, `resource-article-view-load.ts`, shared helpers in `resource-profile-scoped-load.ts`):

- Large tables (13k-row Advisor, 90k-row EmploymentHistory, Disclosure, TransitionEvent, …) are read **only** through indexed foreign-key conditions (`rowsByAttribute`) or primary-key hydration (`rowsByIds`) — the same helpers `/Feed` and `/PublicAdvisors` already use in production.
- The five article→mention join tables and `FieldAssertion` keep the **documented full-scan + in-memory filter** (Fabric served-node secondary-index replication caveat — `resource-feed-page-load.ts` header / runbook §6). Do not "optimize" these back.
- Behavior preserved exactly: `buildScopedResourceIndex()` reuses `loadAll()`'s canonicalization + join-index pipeline, so slug/alias route resolution, the Morgan Stanley alias merge (incl. rows stored under stale alias firm ids, via new `staleFirmIdReplacements()`), and every response field behave identically. Firm/FirmAlias/Team are still read in full where the complete set is load-bearing (small dimension tables; canonicalization + slug resolution), and the subject table falls back to a one-table scan only on the slug path.
- Large-roster safeguard: advisor hydration switches from per-id lookups to one bounded Advisor scan above 200 ids (wirehouse rosters), still 1 table instead of 34.

### Phase 2 — directories + triage (shipped as documented scans)

- `FieldAssertion` in `SourceArticleTriage`: **kept as a bounded one-table scan, documented.** Investigation: no production read path exercises its `articleId` secondary index today, it is written by the same article-ingestion path as the mention tables, so its served-node index health is unverifiable — switching to indexed conditions risks the exact silent-empty failure that broke `/Feed` after #771.
- `PublicFirms` / `PublicTeams` / `PublicBranches`: **not migrated to `searchPageAndCount`, deliberately.** The alias-merge canonicalization must see every Firm row, `total` counts the post-merge/deduped set, `q` filters are case-insensitive substrings, and the legacy `(sortKey, id)` key-cursors sort by lowercased/composite keys — none expressible as indexed Harper conditions without changing cursor semantics or payloads. These endpoints read 2–3 small dimension tables (hundreds of rows), never Advisor/EmploymentHistory. Each `get()` now carries an explicit justification comment.

### Phase 3 — analytics/queue endpoints: audited scoped loads (shipped)

New `loadTables(keys)` runs the same pipeline as `loadAll()` but reads only the tables a caller names. All nine remaining callers migrated onto audited per-endpoint table sets (`resource-analytics-table-sets.ts`), with justification comments at each call site:

| Endpoint | Tables read (was 34) |
|---|---|
| AdvisorCorrectionQueue | 4 |
| AdvisorResearchQueue | 5 |
| RegulatoryDiscrepancyQueue | 6 |
| RankingsExplorer | 7 |
| RecruitingMarket / RecruitingDealDataGaps | 10 |
| DataCoverage | 18 |
| InvestorProofPacket | 22 (embeds DataCoverage + ResearchQueue) |
| AdvisorComparison | 27 (builds full advisor profiles) |

Nothing is silently left behind: every remaining whole-table read is either in a table set above or carries an explicit bounded-scan justification.

## Tests

- New `tests/profile_endpoints_bounded.test.ts` (mirrors `issue_721_directory_bounded.test.ts`): call-recorder asserts the five profile endpoints never issue an unconditioned `search({})` against Advisor / EmploymentHistory / Disclosure / TransitionEvent,
