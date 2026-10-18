# Add hosted TradingView live-chart support, live-chart forecasts, AI notes mode, and admin/view updates

### Motivation
- Support live-chart based forecasts alongside the existing screenshot workflow and store only licensed, reproducible chart configuration rather than private iframe state or screenshots. 
- Improve AI-assisted tooling to both extract structured data from evidence images and to draft editable pre/post-trade notes from structured trade details. 
- Keep legacy screenshot data and paths compatible while adding workflow-specific metadata and safer validation. 
- Surface live market context for visitors and restore/expand admin tooling and validations uncovered by a follow-up audit. 

### Description
- Frontend: added `TradingViewChart` and `ForecastLiveMarketSection` components, reworked `DailyForecastAdmin` and `DailyForecastView` to support `source_type` = `live_chart` and to save chart metadata and an administrator-confirmed `tradingview_symbol`, plus numerous UX improvements and constraints (chart load retry, symbol load confirmation, legacy symbol warnings). 
- Backend / Edge Function: updated `supabase/functions/analyze-trade-image` to support two modes (`image` for visual extraction and `notes` for structured-note generation), improved prompts/validation, and tightened AI response handling. 
- Database: added migrations `20260729000000_live_chart_forecasts.sql` and `20260729001000_authoritative_tradingview_symbol.sql` to make `image_path` nullable, add `source_type`, `exchange`, `timeframe`, `take_profit_3`, `rationale`, expected/result P&L fields, `result_notes`, and `chart_metadata`, and to add `tradingview_symbol` with format checks and non-destructive comments/constraints. 
- Library/type updates: introduced `tradeForecast`, `livePosition`, and `forecastTradingViewSymbols` utilities with tests, updated Supabase `Tables` typings to reflect new columns, and small type/typing refinements in UI helpers. 
- Misc: added unit tests for new components and libraries, updated Tailwind config to use `tailwindcss-animate` import style, and fixed a number of validation/edge cases found in audit (NaN handling, post-trade evidence selection, admin filters). 

### Testing
- Ran unit tests with `vitest` covering new modules and components, and all added tests passed: `src/components/forecast/ForecastLiveMarketSection.test.tsx`, `src/components/forecast/TradingViewChart.test.tsx`, `src/lib/forecastTradingViewSymbols.test.ts`, `src/lib/livePosition.test.ts`, and `src/lib/tradeForecast.test.ts`. 
- Manually built the frontend to ensure the new components and Tailwind configuration compile successfully. 
- Exercised the Edge Function locally to verify both `image` and `notes` request/response flows and JSON parsing behavior; the function returns appropriate errors for invalid inputs and produces JSON notes/extraction on valid inputs.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a6a196448e88333bc867c237246aa51)
