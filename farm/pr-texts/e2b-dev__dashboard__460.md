# fix: hide ECharts toolbox in sandbox metrics chart

## Summary

The sandbox detail monitoring chart (`SandboxMetricsChart`) registers `ToolboxComponent` (required for brush/zoom), but unlike `team-metrics-chart` and `compute-usage-chart`, it was missing `toolbox: { show: false }` in its ECharts option. This caused the toolbox icons (brush, zoom, reset, etc.) to render visibly in the top-right corner of the chart.

With Turbopack this defaulted to hidden due to different module initialization order, but Webpack renders the toolbox visibly.

```diff
 return {
   backgroundColor: 'transparent',
   animation: false,
+  toolbox: { show: false },
   brush: isMobile ? undefined : { ... },
```

Link to Devin session: https://app.devin.ai/sessions/26cc0135d9e24aaa87881e8d7e2069cb
