# Add HelpMeTest to the catalog

## Summary
Adds HelpMeTest (https://helpmetest.com/) as a `Browser/RUM` entry in `src/data/tools.ts` (catalog now 132 tools; test count updated).

Grounding: per helpmetest.com and its llms.txt, it's a commercial cloud platform running Robot Framework tests in real Chrome browsers with 24/7 monitoring, CLI-driven, usage-based per-run pricing with a 14-day trial. It's continuous browser/API testing rather than load generation, so `Browser/RUM` is the closest fit; no public source repo found, so no `repoUrl`, and no verified launch year, so `firstReleased` is omitted.

Link to Devin session: https://app.devin.ai/sessions/51c75f11d6ce4de7a3c07eba1ca0e00c
Open in Devin Desktop: https://app.devin.ai/desktop/session/51c75f11d6ce4de7a3c07eba1ca0e00c?variant=devin
Requested by: @QAInsights
