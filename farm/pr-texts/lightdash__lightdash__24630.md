# fix: keep reference line visible when hiding grouped series via legend (PROD-7119)

## Problem

Reference lines (ECharts `markLine`) on grouped line/bar charts disappeared when a user hid a series via the **interactive legend** (single-click to hide one group, or double-click to isolate one). The markLine is attached to a single data series at config time, so when that series is toggled off at ECharts runtime, its markLine vanishes with it — even though the reference line relates to the whole dataset, not one group.

This is a **separate code path** from PROD-2619, which only handled series hidden via the chart Series settings panel (config-time `applyReferenceLines`). Legend toggling happens at ECharts runtime and bypasses that logic.

## Root cause

Legend selection is captured into React state (`useLegendDoubleClickSelection` → `legendselectchanged`) and fed back into `useEchartsCartesianConfig` as `validCartesianConfigLegend`, but the series→markLine attachment was never reconciled against which series are currently visible.

## Fix

Add `relocateMarkLinesToVisibleSeries` in `useEchartsCartesianConfig`: when a series carrying a markLine is hidden via the legend, re-attach its reference-line data to a still-visible series (preferring one without its own markLine, falling back to any visible series). It is applied via a `useMemo` keyed on the series and the legend selection, and **recomputes purely from the base series on every legend change**, so repeated toggling never duplicates or accumulates reference lines, and un-hiding restores the original attachment.

## Verification

- Confirmed the runtime wiring: `legendselectchanged → onLegendChange → selectedLegends` state is passed into `useEchartsCartesianConfig`, so the relocation triggers on every legend interaction.
- `pnpm -F frontend typecheck:fast` clean for the changed file (the only failures are pre-existing, unrelated `toHaveAttribute` jest-dom typings in EE aiCopilot test files). Lint + format clean via pre-commit.
- **Suggested manual check before merge:** grouped line chart (date x-axis, metric y-axis, ≥3 groups) + horizontal metric reference line → hide the first group via the legend and double-click to isolate another group; the reference line should remain visible in all states.

Fixes PROD-7119.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
