# add copen `https://app.devin.ai` (fixes #838)

## Summary
Adds **Devin** (`https://app.devin.ai/`) to the built-in list of copen (context opener) AI tool launchers, so it appears in the copen/run-in-agent split-button menus alongside Claude, Codex, Copilot, etc.

Two source-of-truth lists are updated:
- `DEFAULT_COPENS` in `src/modules/copen-manager.js` — `{ id: 'devin', label: 'Devin', icon: 'engineering', url: 'https://app.devin.ai/', isDefault: true }`
- `COPEN_OPTIONS_STATIC` in `src/utils/copen-config.js` — matching static option entry (`value`/`label`/`icon`).

No other changes needed — the menus render these lists dynamically. Existing unit tests (`copen-manager`, `copen-config`) assert membership/shape rather than exact length, so all 1207 unit tests still pass.

Link to Devin session: https://app.devin.ai/sessions/fa5e4adcfc844fda865a4506851cf717
Requested by: @dogi
