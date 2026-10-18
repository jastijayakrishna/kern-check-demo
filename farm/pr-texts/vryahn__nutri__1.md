# fix(body): derive anthropometric indices from profile-scoped stature

## Summary

Removes `altura_cm` from the `BODY_METRICS` domain catalog. Stature is a quasi-static anthropometric attribute scoped to the user, not a per-day measurement; it was already persisted in the profile (`prefs.data.profile.height_cm`). All derived indices (BMI, FFM, FFMI) now resolve stature from the profile in both the Medidas view and the Dashboard custom-chart pipeline.

## Motivation

A bioimpedance ingest (2026-07-14) landed without `altura_cm`. `buildDashSeries` derived FFMI strictly from row-local fields of `body_metrics.metrics`, so the missing key yielded `null` and truncated the Dashboard FFMI time series at the previous sample. The Medidas view masked the defect by carrying forward last-known stature from history — an asymmetry between the two consumers of `derivedBodyMetrics`. Eliminating stature as a measurement key removes the failure mode at its root rather than patching either call site.

## Implementation

- `domain.js` — drop `altura_cm` from `BODY_METRICS` and `BODY_METRIC_MAX`; `derivedBodyMetrics(m, heightCm)` takes stature as an explicit argument; `buildDashSeries(..., heightCm)` threads it through to the derived-series resolver.
- `CustomChart.jsx` / `Body.jsx` — inject `profile.height_cm`; Body no longer inherits stature from measurement history and renders a degraded-state caption (cause + action) when the profile lacks stature.
- `importer.js` — retire the `height`/`height_cm`/`talla` CSV aliases; unrecognized columns are dropped by the existing unknown-column path.
- MCP `log_measurement` — rejects `altura_cm` by construction: input keys are validated against `BODY_METRICS`.

## Validation

- `lint`, `test` (147/147), `build` — all clean.
- Numeric fixture: FFM = 57.4 kg × (1 − 0.0914) = 52.15 kg → FFMI = 52.15 / 1.64² = 19.4 kg/m², covered by the canonical derived-metrics test.
- Both production users have `height_cm` set in their profiles (verified pre-merge): no regression surface for derived indices.

## Post-merge backfill (applied)

Residual `altura_cm` keys purged from the 6 historical `body_metrics` rows (`metrics - 'altura_cm'`). All held the value 164, identical to the profile — zero information loss. Post-condition verified: 0 rows retain the key.
