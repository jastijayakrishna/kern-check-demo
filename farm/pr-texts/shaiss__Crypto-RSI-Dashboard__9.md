# fix: RSI chart history via TAAPI v2 `results` window

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Problem
`GET /api/session?token=btc&timeframe=1h` returned `rsiSeries` with **length 1** because the client called legacy `https://api.taapi.io/rsi` with `results`, but live responses stayed a single scalar `value` — so `normalizeRsiSeriesPayload` wrapped one point and the Plotly line looked flat.

## Solution
- Call **TAAPI v2** `GET https://v2.taapi.io/indicator/rsi` with `Authorization: Bearer $TAAPI_SECRET`, `timeframe`, compact symbol (`BTCUSDT`), and `results` for a real oldest→newest window.
- **Clamp** `results` to plan limits (Basic **50**, Pro 300, Expert 2000) via optional `TAAPI_PLAN` (defaults to `basic`).
- **Retry** when v2 returns `pending: true` (cold cache).
- **Fallback** to legacy v1 `/rsi?secret=…` if v2 fails; if v2 returns only one point while more were requested, try v1 as well.

`session.rsi` / `rsiAsOf` still come from the latest point in the series.

## Example series length (btc / 1h)
With default settings (`DEFAULT_RSI_CHART_RESULTS=60`, `TAAPI_PLAN` unset → basic): **`rsiSeries.length === 50`** (60 requested, clamped to Basic cap). Set `TAAPI_PLAN=pro` on Vercel for up to 60 points per request (300 max).

## Tests
`npm test` — 57 passing (v2 request shape, v1 fallback, session series length with clamp).

## Docs
README updated for v2 endpoint, `TAAPI_PLAN`, and plan limits.
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-1a8c5668-e031-5706-b8c2-36784986c536?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-1a8c5668-e031-5706-b8c2-36784986c536&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
