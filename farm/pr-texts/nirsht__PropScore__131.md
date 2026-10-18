# fix(etl): decouple the free daily cron from OPENAI_API_KEY

## Problem

`propscore-etl-daily` (`pnpm nightly:base`) was failing — and it looked OpenAI-related, which didn't make sense because the daily pipeline is supposed to be free.

It is free. I traced every base-mode stage (etl-sync, offboard-stale, sfpim/landuse/permits/zoning/code-enforcement/dbi-complaints/housing-inventory, rent-control, rent-comps, walkscore, crime, neighborhood-comps, recompute-scores) and **none** reach an OpenAI call site. All OpenAI usage lives in `llm: true` stages that only run in `nightly:llm`.

The daily wasn't *spending* on OpenAI — it was **crashing because of OpenAI**. `env.ts` declared `OPENAI_API_KEY` as **required at module-load time** (`z.string().min(1)`), and every script imports `env.ts` transitively (`etl:sync → bridge-client → env`). So the free daily needed a valid key just to boot, and died at startup with `OPENAI_API_KEY: Required` whenever the key was absent — e.g. pulled or rotated during an OpenAI billing lapse — despite never using it.

## Fix

Mirrors the existing `NEXTAUTH_SECRET` pattern (optional at parse time, enforced at the real use site):

- **`src/lib/env.ts`** — `OPENAI_API_KEY` is now optional at parse time, so transitively-importing free crons no longer crash without it.
- **`src/lib/openai.ts`** — throws a clear error if the key is missing. Only OpenAI-spending agents import this module, so the paid `nightly:llm` cron and the web app still fail loudly; the base pipeline (which never imports it) is unaffected.
- **`scripts/render-sync.ts`** — stop pushing `OPENAI_API_KEY` to the daily cron. Render's bulk env PUT replaces the managed set, so the next `render:sync` also **removes** the stale key from that cron — fully decoupling the free daily from OpenAI so a billing lapse can't break it again.

## Reviewer notes

- Behavior verified: `env.ts` loads without the key; `openai.ts` throws a clear message without the key and loads fine with it.
- `pnpm typecheck` clean; `pnpm test` 217/217 passing.
- **Deploy step:** after merge, run `pnpm render:sync` so the daily cron's OpenAI key is actually stripped on Render. The `render.yaml` blueprint was already correct (`propscore-etl-daily` → `pnpm nightly:base`); only the pushed env set changes.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
