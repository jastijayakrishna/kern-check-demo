# fix(sdk): drop react-dom/server from map tooltips to fix util.TextEncoder crash

## Problem

SDK consumers hit `TypeError: util2.TextEncoder is not a constructor` when a map visualization renders, crashing the dashboard via the error boundary.

Root cause: `SimpleMap` imported `renderToString` from `react-dom/server` solely to build the choropleth tooltip HTML for Leaflet's imperative `layer.bindTooltip()`. The SDK build **externalizes** `react-dom/server`, so the consumer's bundler resolves it — and its export map's `default`/`node` condition points at React's **Node** server build (`react-dom-server.node.development.js`), which does `new (require('util').TextEncoder)()`. In a browser bundle `util` is stubbed, so `TextEncoder` is undefined → "not a constructor".

### Who is affected vs not

- **Affected:** SDK consumers whose bundler resolves `react-dom/server` to the `node`/`default` export condition (commonly Vite `optimizeDeps`/esbuild prebundling, or React 19 / SSR-influenced resolution) **and** who render a map. The crash is in the consumer's bundle, not ours — our bundle only ever shipped the bare external import.
- **Not affected:** The main Lightdash frontend app (its bundler resolves the `browser` condition), and consumers who never render a map.

This was latent since **v0.2728.0** (the vite-8/rolldown build transition that began externalizing `react-dom/server`); prior builds inlined React's browser server, so the node build never reached consumers.

## Fix

Remove the `react-dom/server` import entirely. Replace `renderToString(<MapTooltipContent/>)` at the one imperative call site with `getMapTooltipHtml(...)`, a plain HTML-string builder that mirrors the component's markup and escapes data-derived labels/values (`escapeHtml`) to preserve the auto-escaping React was providing.

The react-leaflet `<Tooltip>` JSX path (`MapTooltipContent`) is unchanged — it renders through normal React and never needed the server renderer.

Removing the import (rather than aliasing to `react-dom/server.browser`) fixes the crash at the root for **all** consumers regardless of their bundler config.

### Tradeoff

The tooltip markup now exists in two adjacent forms — the `MapTooltipContent` React component (JSX path) and the `getMapTooltipHtml` string builder (Leaflet path) — which must be kept visually in sync.

## Testing

- `frontend typecheck:fast`: no new errors.
- No `react-dom/server` / `renderToString` references remain in the component.

---

> ⚠️ **Ticket reference pending** — please add the `Closes: PROD-XXXX` (and `Closes: #XXXXX` if a GitHub issue exists) line for the production SDK crash. Left out rather than fabricated.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
