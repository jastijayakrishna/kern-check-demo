# feat: include daily motivational quote at top of morning market briefing

## Summary
- Extracts the ZenQuotes fetch + deterministic fallback logic from `/api/daily-quote` into a shared `lib/daily-quote.ts` helper (the API route now delegates to it; response shape unchanged).
- The morning market briefing cron fetches the same daily quote shown on the dashboard's top-left banner and stores it on `BriefingData` (`quote?: { quote, author }`) in the Redis cache. Quote fetch failure never blocks the briefing (falls back to `undefined`).
- Renders the quote at the top of the briefing email (accent-bordered card above the header) and at the top of the in-app Morning Market Briefing modal.

## Verification
- `tsc --noEmit` clean and `next build` succeeds locally on a fresh install.
- Old cached briefings without a `quote` field render unchanged (field is optional in both surfaces).

🤖 Generated with [Claude Code](https://claude.com/claude-code)
