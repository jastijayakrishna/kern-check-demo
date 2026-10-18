# Codify Observation and VerificationResult indexes to fix drift

## Summary

Three indexes exist in prod MongoDB but were **not defined** in `src/indexes/customIndexes.js`, so the index-drift report (admin diagnostics) flags them as `extra: true`. Any routine `synchronizeIndexes` / `dropExtraIndexesOnly` run would **drop them** — including the `method.coding` index that fixed the `CodeSystem/cluster-model` Observation search.

This PR codifies all three using their **exact existing index names and key order**, so the drift check (`indexManager.js` matches by name, then `deepEqual` on keys) reconciles them with **no index rebuild**.

## Indexes added

| Collection | Keys | Name |
|---|---|---|
| `Observation_4_0_0` | `{method.coding.system, method.coding.code, subject._uuid, _uuid}` | `method.coding.system_1_method.coding.code_1_subject._uuid_1__uuid_1` |
| `Observation_4_0_0` | `{category.coding.code, subject._uuid, effectiveDateTime:-1, _uuid}` | `category.coding.code_1_subject._uuid_1_effectiveDateTime_-1__uuid_1` |
| `VerificationResult_4_0_0` *(new section)* | `{target._uuid, _uuid}` | `target._uuid_1__uuid_1` |

## Why

The `method.coding` index supports the persona/`cluster-model` Observation query. Measured impact after it was added (Groundcover logs + traces):

- MongoDB `find` on `Observation_4_0_0`: p50 ~61ms → ~3ms, **p95 ~420ms → ~6ms, p99 ~1,060ms → ~7.6ms, max ~12s → ~12ms**
- Signature of replacing a collection scan with an index seek (was doing thousands of keys examined).

Codifying prevents the index from being silently dropped on the next sync.

## Notes

- Longer-term, the persona records may be re-modeled as Groups (separate discussion); this simply tracks the indexes that already exist in prod so they aren't dropped in the meantime.
- Exact-name match was chosen deliberately: `synchronizeIndexesWithConfigAsync` drops "extra" by name, so matching the live name avoids an unnecessary rebuild of a populated index.

## Testing

- `node --check src/indexes/customIndexes.js` ✅
- `eslint src/indexes/customIndexes.js` ✅ (exit 0)

🤖 Generated with [Claude Code](https://claude.com/claude-code)
