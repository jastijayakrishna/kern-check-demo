# PLAN-005: Add recipe discovery foundation

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary
- adds provider-independent recipe discovery abstraction (`RecipeDiscoveryProvider`)
- adds Edamam Recipe Search API v2 adapter with server-only credentials
- normalizes external recipes into Fitness Autopilot discovery candidates
- supports cuisine, meal type, protein-query, high-protein, and supported dietary filters
- reports unsupported constraints (including dislikes) without silently claiming enforcement
- preserves source attribution and URLs
- adds deterministic deduplication (`provider + externalId`) and typed provider errors
- exposes `POST /functions/v1/recipe-discovery-search`
- adds `pnpm discover:recipes:dev` for manual live searches

## Why
Weekly strategy testing showed that unconstrained LLM generation repeatedly falls back to generic dishes. This creates a discovery layer that can supply richer real-world recipe candidates before weekly planning.

## Validation
- [x] lint
- [x] typecheck
- [x] tests (`pnpm test:unit` — domain/contracts/llm/mobile/cors all green)
- [x] build
- [ ] manual provider search — **not run**: `EDAMAM_APP_ID` / `EDAMAM_APP_KEY` were unavailable in this environment

## Out of scope
- recipe discovery UI (PLAN-005.5)
- planner integration (PLAN-004 unchanged)
- candidate ranking/enrichment
- nutrition verification
- portion solving

## Notes
- Max **4** external Edamam searches per discovery request
- Source nutrition on candidates is metadata only (not authoritative FA nutrition)
- Config documented in `supabase/.env.example` and `docs/architecture/recipe-discovery-v1.md`

<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-01a09714-32ff-7c7c-a4a4-d1245cba61ce?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-01a09714-32ff-7c7c-a4a4-d1245cba61ce&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>


