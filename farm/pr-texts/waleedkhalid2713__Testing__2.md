# Support live-chart TradingView embeds, AI notes, and forecast schema enhancements

### Motivation

- Enable a non-invasive live-chart workflow using TradingView's hosted Advanced Chart widget while preserving existing screenshot evidence and avoiding iframe scraping.
- Add structured workflow metadata and optional pre/post-trade images so live-chart forecasts can be saved without destructive data migrations.
- Expand AI automation to both extract visible values from images and to draft editable forecast/result notes from structured trade data.
- Improve admin UX for creating, editing, filtering, and validating forecasts with shared validation logic and clearer evidence handling.

### Description

- Add a TradingView embed component in `src/components/forecast/TradingViewChart.tsx` that loads the official hosted widget without reading iframe state or drawings.  
- Replace and refactor the admin UI in `src/pages/DailyForecastAdmin.tsx` to support two source workflows (`screenshot` and `live_chart`), image preparation/upload, AI-assisted image extraction and notes generation, richer validation, and new database fields (exchange, timeframe, source_type, take_profit_3, rationale, expected/result P&L and notes, chart_metadata).  
- Add trade utilities in `src/lib/tradeForecast.ts` and unit tests in `src/lib/tradeForecast.test.ts` for metric calculations, warnings, symbol sanitization, and draft validation, and update several small UI type signatures.  
- Update public type mapping in `src/integrations/supabase/types.ts` to include the new `trading_forecasts` columns.  
- Add a Supabase migration `supabase/migrations/20260729000000_live_chart_forecasts.sql` that makes `image_path` nullable, adds new columns and constraints, and documents behavior in column comments.  
- Enhance the Edge Function `supabase/functions/analyze-trade-image/index.ts` to support two modes (`image` for extraction and `notes` for drafting text), stricter validation, mode-specific prompts, and safer parsing of Gemini responses.  
- Update the public forecast view in `src/pages/DailyForecastView.tsx` to handle optional images, show live-chart metadata and timeframe labels, and surface new forecast fields.  
- Add `tailwindcss-animate` via `tailwind.config.ts` and minor UI improvements across components.  

### Testing

- Added unit tests in `src/lib/tradeForecast.test.ts` and ran them with `vitest`, and the new tests passed.  
- Exercise of AI Edge Function behavior was covered by the function's input validation paths (mode and image checks) during development; no automated integration tests were added for the external AI service in this rollout.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a6a196448e88333bc867c237246aa51)
