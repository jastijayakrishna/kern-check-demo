# fix: omit hardcoded pivot values from downloaded chart-as-code YAML (PROD-8299)

## Problem

When a cartesian chart with a pivot/group-by dimension is downloaded via `lightdash download` (chart-as-code), `chartConfig.config.eChartsConfig.series` was serialized with **one entry per pivot dimension value**, each hardcoding the actual data value under `encode.yRef.pivotValues[].value` (plus data-derived `name`/`color`/computed hashes).

This made the YAML **non-portable**: uploading it to an environment with a different set of pivot values is wrong, and the series array grows with the cardinality of the pivot dimension.

## Root cause

Pivoted cartesian series are auto-generated at load time from `pivotConfig` + live query data, but the download path persisted the materialised, data-specific series verbatim.

## Fix

- Add `removePivotedSeriesValuesFromChartConfig` in `@lightdash/common`, which strips the data-level pivot values from pivoted series (using the existing `isPivotReferenceWithValues`) and dedupes the result by `getSeriesId`, so the series regenerate from `pivotConfig` on load.
- Apply it in `CoderService` when serializing `chartConfig` for download.
- Non-pivoted series and their per-series customizations are left untouched.

## Verification

- New unit tests in `savedCharts.test.ts` (5 passing): strips + dedupes pivoted series, keeps multiple metrics as separate portable series, leaves non-pivoted series/customizations untouched, passes through non-cartesian and empty/missing-series configs.
- `pnpm -F common typecheck:fast` and `pnpm -F backend typecheck:fast` clean; lint clean (no new warnings).

Fixes PROD-8299.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
