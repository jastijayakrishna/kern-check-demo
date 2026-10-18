# feat(core): context-retrieval pass + corpus-wide pseudonym consistency for the PII scrub pipeline

## What

The context-retrieval pass + corpus-wide pseudonym consistency stage of the corpus PII scrub pipeline (stage position: between candidate-mining and the LLM-pass), built entirely on the landed rails — `PiiScrubService` (#14808 slice 1, PR #15139) and the `PII_SCRUB` model seam (#14809, PR #14980) — with **zero changes to either**. No new scheduler, no new queue, no second knowledge-graph store.

Closes #14805

### `packages/core/src/security/pii-pseudonym-map.ts` — one person = one replacement everywhere
- `CorpusPseudonymMap`: cluster-keyed (`entity:<entityId>` from the EntityStore alias backbone — **never surface strings**), extending the session pseudonymizer's deterministic minting (`mintSurrogate`, now exported) from per-session to corpus-persistent: mint seed is `(salt, kind, clusterId, attempt)`, salt persisted inside the (secret) snapshot, so the same person deterministically keeps the same pseudonym across runs, artifact types, and assignment orders.
- **Collision behavior:** two distinct people sharing a name are two clusters with two pseudonyms; an alias claimed by 2+ clusters is **ambiguous** — never blind-substituted (a longest-first self-mapping shields it from partial rewrites by contained shorter aliases), surfaced for model escalation with ALL candidate assignments. A newly learned real alias equal to an existing pseudonym re-mints that cluster with a `supersededPseudonyms` audit trail. Re-homing a platform identity to a second cluster **throws** — identity merges stay in the merge engine.
- **Idempotent upsert** (no duplicate clusters/aliases/identities on re-assign) and **pseudonym stability across ruleset bumps** — a `v<ruleset>` bump re-scrubs content (content-hash markers re-key) with the SAME pseudonyms, so a re-scrub never re-links identities.

### `packages/core/src/security/pii-pseudonym-map-store.ts` — the map is a secret artifact
- The alias→pseudonym map inverts the scrub, so it lives **outside the retrievable corpus**: one dedicated runtime-cache key (`pii:pseudonym-map:v1`, next to the scrub done-markers), never a document/memory row, no ingestion path — unreachable via `searchDocuments` / `searchMessages` / `searchMemories` / `SEARCH_KNOWLEDGE`, never chunked or embedded. Confidentiality is structural, plus at-rest AES-256-GCM (v2 settings-secret scheme, dedicated AAD `elizaos:pii-pseudonym-map:v1` for domain separation, `SECRET_SALT` lifecycle).
- **Fail-closed everywhere:** refuses to persist plaintext; wrong key, tampered ciphertext, non-ciphertext value, or a structurally invalid snapshot all **throw** (deliberately stricter than `decryptStringValue`'s return-original-on-error) — a partial map would silently re-mint pseudonyms for already-mapped people, which is worse than stopping the pipeline.

### `packages/core/src/security/pii-context-pack.ts` — the context-retrieval pass
- `assembleContextPack`: per chunk, resolves candidates through a **structural `EntityStore.resolve` seam** (`PiiEntityResolverStore` matches `packages/agent/src/services/knowledge-graph/entity-store.ts` field-for-field; `entityResolverFromStore(kg.getEntityStore())` wires it with zero adaptation — core does not import agent), gathers related fragments (`DocumentService.searchDocuments`, `runtime.searchMemories` under the embeddings throw-never-fabricate doctrine, `adapter.searchMessages` with explicit roomIds), clusters confident resolutions into the map, and emits the bounded pack + the per-chunk `{entityClusterId, surrogate, kind}` assignment slice — **never the whole map, never a real alias**.
- Failure doctrine: absent sources are structurally skipped and audited in `sourcesQueried`; a wired source that throws **propagates** (rails retry the item) — degraded context silently producing a wrong verdict is the failure mode this pass exists to prevent.
- `buildScrubRequestDraft` folds a chunk + pack into the landed `PII_SCRUB_REQUESTED` payload — the exported interface siblings (#14806 transcript anchors, #148
