# feat: Widen azapi provider version constraint from ~> 2.7.0 to ~> 2.7

The azapi provider constraint `~> 2.7.0` restricts to `>= 2.7.0, < 2.8.0`, blocking adoption of future minor releases. Changed to `~> 2.7` (`>= 2.7, < 3.0`).

### Changes
- **`cdktf.json`** — Widened provider constraint
- **Generated provider bindings** (`providers-azapi/*/index.ts`) — Updated `providerVersionConstraint` metadata across all 10 resource/data source modules
- **Schema docs** — Updated version references in container app schema comments

The `providerVersion: '2.7.0'` metadata is intentionally preserved — it records the generation source version, not a runtime constraint.
