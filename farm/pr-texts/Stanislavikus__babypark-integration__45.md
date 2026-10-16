# Draft: Export generation-bound canonical Catalog snapshots

### Motivation
- Provide a provider-neutral, generation-bound canonical Catalog snapshot suitable for downstream materialization while preserving existing CatalogReader/Service semantics.
- Ensure the snapshot exporter is fail-closed against CURRENT movement and does not produce mixed-generation artifacts.
- Avoid product-by-product N+1 read patterns by streaming deterministic domain scans from the sealed generation and provide an independent verifier to prove artifact integrity.

### Description
- Add a pinned-reader API on `CatalogReader` (`withPinnedDb` + `assertCurrent`) so an exporter can fix and prove a single exact generation for the entire export without retries. (see `src/catalog/sqlite/generation.mjs`)
- Introduce a canonical snapshot contract and exporter that streams normalized NDJSON domain files (products, product-text, variants, offers, brands, categories, product-categories, stores, store-stock, attribute-definitions, attributes, images, kit-components) and writes a manifest containing generation binding, layer watermarks, per-file counts/bytes/SHA-256 and exporter provenance; export lifecycle is `.building -> verify -> CURRENT recheck -> atomic rename -> .ready`. (see `src/catalog/snapshot/contract.mjs`, `src/catalog/snapshot/exporter.mjs`, `scripts/catalog-snapshot.mjs`)
- Add a streaming, independent verifier that enforces file set, private modes, no-symlink paths, manifest consistency, SHA-256, byte/record counts, NDJSON validity, deterministic ordering and identity uniqueness, integer-minor-unit money checks and layer metadata checks. The verifier is safe for large files (streaming read + `StringDecoder`). (see `src/catalog/snapshot/verifier.mjs`, `scripts/verify-catalog-snapshot.mjs`)
- Reuse canonical row→DTO helpers by factoring JSON/boolean parsing into `src/catalog/domain/canonical-values.mjs` so the exporter and `CatalogService` share the same canonical semantics and money/availability identity rules; the exporter performs one ordered SQLite scan per domain to prevent N+1 reads. (see `src/catalog/domain/canonical-values.mjs`, `src/catalog/service/catalog-service.mjs`)
- Update docs to describe the private snapshot lifecycle and post-FULL production state, and add npm scripts `catalog:snapshot` and `catalog:snapshot:verify`. (see `docs/CATALOG_SERVICE.md`, `docs/CURRENT_STATE.md`, `package.json`)
- This change implements the Issue contract and is intended to close the issue when merged: `Closes #44`.

### Testing
- Focused unit tests: ran `node --test --test-concurrency=1 tests/unit/catalog-snapshot.test.mjs` and observed 5/5 tests passing, covering determinism, manifest consistency, CURRENT movement fail-closed, verifier tamper/truncation cases, path/mode safety, and large-fixture streaming.
- Broader unit suites: ran `node --test --test-concurrency=1 tests/unit/catalog-generation.test.mjs tests/unit/catalog-service.test.mjs tests/unit/catalog-snapshot.test.mjs` and observed all tests passing (46/46 for that combined run), proving generation binding and reader invariants were preserved.
- Full project regression: ran `npm test` (includes `storage:validate`, unit, legacy and refactor suites) and observed the test suites pass (root/legacy/refactor suites as executed in CI: all passed locally).
- Resource / scalability evidence: large-fixture snapshot test streams 5,000 products using `Statement.iterate()` and asserts a bounded query preparation count (proof that exporter uses streaming scans and avoids per-product N+1 SQL round-trips).

Note: all test results above are automated runs executed in-repo; no production snapshot, publication, Drupal mutation or external push/deploy was performed as part of this change.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6abd6995256c8329ba78e411b4cc0d7e)
