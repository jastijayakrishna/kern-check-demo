# fix(intelligence): synthesize missing visual exhibits

## Summary

Adds an audited second-pass visual exhibit synthesizer for Ava.

When a chart-shaped or graph-shaped question finishes without the requested typed `AgentAnswer.charts` / `AgentAnswer.graphs`, the route now runs a small governed model pass that receives only:

- the user question
- the requested output shape
- retrieved sources
- final answer draft

It must return only a valid Markdown data table. The existing canonical `buildStructuredExhibits` validator then decides whether that table becomes a typed chart or relationship graph. If it cannot produce a valid table, the answer stays honest rather than fabricating a chart.

## Why

#3894 fixed the plumbing/rendering layer and deployed successfully, but the full post-deploy deep crawl proved the product is not yet consultant-grade on visuals:

- matrix: passed 5/5
- reality crawl on `94956a2c`: `155/290` overall
- tables: `44/50`
- charts: `6/50`
- graphs: `2/40`

Root cause: prompt-only compliance is not reliable enough. The model often answers chart/graph prompts in prose instead of emitting structured rows/edges. This PR adds a validated typed-exhibit fallback instead of relying on voluntary prose formatting.

## Validation

- `npx jest src/lib/intelligence/answer/__tests__/visual-exhibit-synthesis.test.ts src/lib/intelligence/answer/__tests__/structured-exhibits.test.ts src/app/api/intelligence/ask/__tests__/route.telemetry.test.ts --runInBand`
- `npx eslint src/lib/intelligence/answer/visual-exhibit-synthesis.ts src/lib/intelligence/answer/__tests__/visual-exhibit-synthesis.test.ts src/app/api/intelligence/ask/route.ts`
- `npm run release:check`
- `git diff --check`

## Post-deploy proof required

After merge/deploy, rerun:

- `node scripts/qa/tenant-matrix-gate.mjs`
- `node scripts/qa/reality-crawl.mjs`
- `node scripts/qa/reality-crawl-report.mjs`

Only mark progress green if the generated report shows materially improved chart/graph pass rates across all five tenants.

