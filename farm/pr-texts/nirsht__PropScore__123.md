# fix(zoning): repoint ETL to relocated DataSF zoning dataset

## Root cause

The nightly ETL `zoning` stage failed with a **404 `dataset.missing`**:

```
[zoning] [enrich-zoning] failed: Error: Zoning 404 Not Found: {
  "code" : "dataset.missing",
  "id" : "8br2-hhp3"
}
```

DataSF retired the Socrata resource `8br2-hhp3` that the zoning client fetched. The current dataset is **"Zoning Map - Zoning Districts"** at resource id [`3i4a-hu95`](https://data.sfgov.org/Geographic-Locations-and-Boundaries/Zoning-Map-Zoning-Districts/3i4a-hu95).

## Fix

- Repoint `ZONING_URL` from `8br2-hhp3` → `3i4a-hu95`.
- **Bump `$limit` 10000 → 50000.** The replacement dataset is parcel-level (~10.6k features) rather than the old dissolved-district set (~hundreds). At `$limit=10000` Socrata would silently truncate ~617 polygons, leaving those parcels without zoning coverage. 50000 is Socrata's anonymous cap and comfortably above the true count.
- Add `zoning_sim` / `districtna` to the `readDistrict` fallback list — the new export ships those column names (the district code is still primarily under `zoning`, which `readDistrict` already reads first).
- Refresh stale resource-id references in the doc comments.

The point-in-polygon join and `ZoningRule` resolution are unchanged; the new dataset keys districts under the same `zoning` code (e.g. `RH-2`, `NCT-3`).

## Verification

Ran `fetchZoningDistricts()` against the live dataset:

```
features: 10617
with district: 10617
distinct districts: 120
```

No truncation, every feature resolves a district code. `tsc --noEmit` reports no new errors in the touched files (the two pre-existing `locationCalibration` errors are unrelated — stale Prisma client).

🤖 Generated with [Claude Code](https://claude.com/claude-code)
