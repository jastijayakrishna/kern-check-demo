# AII-102: TS pipeline entry: src/run-autonomous.ts + WORKFLOW.md + planning helpers

## Summary

- **`src/workflow-md.ts`** — `parseWorkflowMd(raw, envSubs)` parses WORKFLOW.md front matter (model/setup/verify/teardown/gap_analysis_model), strips HTML comments, env-substitutes `${VAR}` refs, handles `---` horizontal rules in body via state-machine detection (front matter only if file starts with `---` on line 1)
- **`src/linear-planning-fetch.ts`** — `fetchPlanningContext()` paginates Linear GraphQL (up to 3 pages × 100 comments), deduplicates by the 3 planning prefixes keeping most-recent, wraps survivors in `<planning_context>` with the prompt-injection preamble, neutralizes injected `</planning_context>` tags, byte-caps at 40 KB; returns empty string on any failure (advisory fetch)
- **`src/run-autonomous.ts`** — `runAutonomous()` reads required env vars, parses `/workspace/WORKFLOW.md` for model, fetches planning context, constructs `DefaultPipelineContext` with `ClaudeCliExecutor(workspaceDir)`, routes per-step events to `${ORCHESTRATOR_URL}/api/status`, loads `DEFAULT_PIPELINE` via `createDefaultRunner()`, exits with pipeline result code; runs as CLI entry via `import.meta.url` guard

## Approach

- Pattern-anchored on `src/pipeline/planning-pipeline.ts` for context construction and runner assembly
- Test style mirrors `src/__tests__/pipeline-runner.test.ts`: injects `pipeline` + `runner` + `llmExecutor` + `fetchImpl` options for deterministic unit tests without real I/O
- Two TypeScript fixes vs. spec: `ClaudeCliExecutor(workspaceDir)` (constructor requires workspace path); double-cast `context.data as unknown as Record<string, unknown>` for extras (strict TypeScript rejects direct Record cast from a narrower interface)

## Test plan

- [ ] `npx vitest run src/__tests__/workflow-md.test.ts` — 7 cases: front-matter extraction, horizontal rules in body, no front matter, HTML comment stripping, env substitution, unknown keys ignored, gap_analysis_model/teardown
- [ ] `npx vitest run src/__tests__/linear-planning-fetch.test.ts` — 7 cases: dedup/filter, empty result, network failure, tag neutralization, pagination, non-ok HTTP, output shape
- [ ] `npx vitest run src/__tests__/run-autonomous.test.ts` — 9 cases: success/failure exit codes, model from WORKFLOW.md, CLAUDE_MODEL fallback, default model, executor invoked, planning fetch triggered/skipped, extras on context, missing env var throws
- [ ] `npm run typecheck` — clean
- [ ] `npm run build` — produces `dist/run-autonomous.js`, `dist/workflow-md.js`, `dist/linear-planning-fetch.js`

Fixes AII-102

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- ai-implement-meta
issue_id: d47b5987-8999-463a-a5be-4daeffb4e1ee
issue_identifier: AII-102
issue_title: TS pipeline entry: src/run-autonomous.ts + WORKFLOW.md + planning helpers
issue_description_b64: IyMgUHJvYmxlbSAvIENvbnRleHQKClRoZSBUUyBwaXBlbGluZSBydW5uZXIgKGBzcmMvcGlwZWxpbmUvcnVubmVyLnRzYCkgaXMgZnVsbHkgYnVpbHQg4oCUIHN0ZXAgbW9kdWxlcyBleGlzdCBmb3IgY2xvbmUvaW5zdGFsbC9pbXBsZW1lbnQvcmV2aWV3L2ZlZWRiYWNrLWxvb3AvcHJlZmxpZ2h0L3B1c2gsIGBwaXBlbGluZXMvYXV0b25vbW91cy55bWxgIGRlY2xhcmVzIHRoZSBhdXRvbm9tb3VzIHBpcGVsaW5lLCBgQ2xhdWRlQ2xpRXhlY3V0b3JgIChhdCBgc3JjL3BpcGVsaW5lL2V4ZWN1dG9yLnRzOjlgKSBzaGVsbHMgb3V0IHRvIHRoZSBgY2xhdWRlYCBDTEkuICoqTm90aGluZyBpbnZva2VzIGl0LioqIGBzZXNzaW9uL2VudHJ5cG9pbnQuc2hgICg1NjAgbGluZXMgb2YgYmFzaCkgaXMgdGhlIGFjdHVhbCBleGVjdXRpb24gZW5naW5lIHRvZGF5LgoKVGhlIFVuaWZpZWQgUnVubmVyIHByb2plY3QgbWFrZXMgdGhlIFRTIHBpcGVsaW5lIGNhbm9uaWNhbC4gVGhpcyBpc3N1ZSBjcmVhdGVzIHRoZSBlbnRyeSBwb2ludCB0aGF0IGBzZXNzaW9uL2VudHJ5cG9pbnQuc2hgIHdpbGwgYGV4ZWNgIGludG8gKFRhc2sgNCkg4oCUIGBzcmMvcnVuLWF1dG9ub21vdXMudHNgIOKAlCBwbHVzIHR3byBzbWFsbCBoZWxwZXJzIHRoYXQgcG9ydCBsb2FkLWJlYXJpbmcgYmFzaCBsb2dpYyBpbnRvIHRlc3RhYmxlIFRTIG1vZHVsZXM6IGBzcmMvd29ya2Zsb3ctbWQudHNgIChmcm9udC1tYXR0ZXIgcGFyc2VyICsgZW52LXN1YnN0aXR1dGlvbikgYW5kIGBzcmMvbGluZWFyLXBsYW5uaW5nLWZldGNoLnRzYCAocGxhbm5pbmctY29udGV4dCBmZXRjaCBmcm9tIExpbmVhciB3aXRoIHByb21wdC1pbmplY3Rpb24gbmV1dHJhbGl6YXRpb24pLgoKIyMgVGFzawoKQ3JlYXRlIHRocmVlIG5ldyBUUyBmaWxlcyBwbHVzIHRlc3R
