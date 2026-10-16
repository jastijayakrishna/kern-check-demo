# feat(wms): discover OGC API tile matrix sets

## Goals

Land OGC API Tiles matrix-set discovery from #4177 on the JSON foundation, preserving the original contribution. Part of #4178. Follows merged #4252.

## Changes

- Preserve the original contribution and commit history from @athomct in #4177.
- Discover a matrix set through tileset tiling-scheme links, API identifiers, or registered URI matches.
- Add matrix-set listing and lookup methods, shared in-flight metadata loading, retries, and option-based cache invalidation.
- Honor explicit matrix-set configuration and the discovery opt-out.
- Reconcile current master imports and dependencies and document the changed discovery default.
- Leave stricter validation and availability limits to a separate follow-up.

## Validation

Local validation passed `yarn`, `yarn lint fix`, `yarn build`, `yarn build-workers`, and `yarn test-audit`. `yarn test-node`: 570 passed, 6 skipped. `yarn test-headless`: 9,459 passed, 39 skipped. Current-head CI verifies the subsequent master refresh before merge.

## Replacement rationale

#4177 conflicts with master and its contributor organization fork rejects maintainer pushes. This maintainer-requested replacement preserves the original work. Supersedes #4177.

<!-- CURSOR_SUMMARY -->
---

> [!NOTE]
> **Medium Risk**
> Default OGC API Tiles behavior changes for `{tileMatrix}` templates: extra network calls, rejected requests on discovery failure, and synchronous `getTileURL()` errors until `getMetadata()` completes unless discovery is disabled.
> 
> **Overview**
> **`OGCAPITilesSource`** now **discovers tile matrix sets by default** when `ogc-api.tileTemplate` includes `{tileMatrix}` and no `ogc-api.tileMatrixSet` is configured. It loads tileset metadata from the path before `/{tileMatrix}`, then resolves the matrix via tiling-scheme links, `tileMatrixSetId`, or `tileMatrixSetURI` against `/tileMatrixSets`.
> 
> New **`getTileMatrixSets()`** and **`getTileMatrixSet(id)`** expose the `/tileMatrixSets` API. Exported types **`OGCAPITileset`** and **`OGCAPITileMatrixSetSummary`** support the discovery path. Shared caching deduplicates concurrent discovery; failures reject (they are not cached) and **`getTileURL()`** throws until metadata has loaded when discovery is required.
> 
> **Breaking default:** failed discovery no longer falls back to using numeric **`z`** as the matrix id. Set **`ogc-api.discoverTileMatrixSet: false`** to keep the prior behavior. The v5 upgrade guide and OGC API docs describe the migration. Tests and JSON fixtures cover discovery, retries, and opt-out.
> 
> <sup>Reviewed by [Cursor Bugbot](https://cursor.com/bugbot) for commit c7adaa5c0764594f3ff6178a5a2c4865b4cd5a7d. Bugbot is set up for automated code reviews on this repo. Configure [here](https://www.cursor.com/dashboard/bugbot).</sup>
<!-- /CURSOR_SUMMARY -->
