# DCON-4542: exclude *_History collections from /stats?sizes=true

## Summary

Follow-up to the `/stats?sizes=true` endpoint (merged in #2308). In **sizes mode**, exclude `*_History` collections from the report.

Rationale:
- History collections live on a **separate cluster** (`cl-prod-fhir-history`), so their sizes don't reflect the client-db working set.
- `$indexStats` isn't run against them (they returned `not authorized` / single-node noise anyway).
- They roughly **double** the collection count and add noise to the data/index-size ranking used to find cache consumers.

## Behavior

- `/stats?sizes=true` → now lists only non-history collections.
- `/stats` (default) → **unchanged**; still lists history collections (existing test unaffected).

Verified against the dev deploy: sizes populate correctly; this simply drops the `*_History` rows from the heavy-mode output.

Ref: DCON-4542.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
