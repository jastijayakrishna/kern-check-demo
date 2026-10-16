# Fix pipeline input-set execution and search health probes

## Description
<!-- What does this PR do? -->
Fixes two critical regressions found during the recent-commit bug investigation:

1. Pipeline runs with `input_set_ids` and an empty `inputs: {}` object now materialize the saved input sets instead of fetching the runtime template and sending unresolved `<+input>` placeholders.
2. HTTP `/health` now remains a server-health probe with HTTP 200 even when optional semantic search initialization fails; the search readiness details remain in the response body for observability.

## Type of Change
- [x] Bug fix
- [ ] New feature
- [ ] Refactor
- [x] Documentation
- [ ] Other

## Checklist
- [x] `pnpm test` passes
- [x] `pnpm typecheck` passes
- [x] `pnpm build` passes
- [x] `pnpm standards:check` passes (architecture guardrails — see [docs/coding-standards.md](docs/coding-standards.md))
- [x] `pnpm docs:check` passes (if registry/tool counts changed)

## Coding Standards (registry-driven MCP model)
If this PR adds or changes Harness API coverage:
- [x] No new `server.registerTool()` calls — only toolset definitions in `src/registry/toolsets/`
- [x] Toolset registered in `ALL_TOOLSETS` and `ToolsetName` union
- [x] `operationPolicy` on every new/changed endpoint
- [x] Shared response extractors from `src/registry/extractors.ts` (no raw passthrough on real endpoints)
- [x] `identifierFields` and `scope` declared on new resources
- [x] No `console.log()` in `src/` (stdio JSON-RPC safety)

## Validation
- `pnpm exec vitest run tests/tools/tool-handlers.test.ts -t "input_set_ids|input set|runtime inputs" tests/utils/http-health.test.ts`
- `pnpm build`
- `pnpm docs:generate`
- `pnpm typecheck`
- `pnpm docs:check`
- `pnpm exec vitest run tests/tools/tool-handlers.test.ts tests/utils/http-health.test.ts`
- `pnpm test` (110 files / 2392 tests)
- `pnpm standards:check`

<div><a href="https://cursor.com/agents/bc-60044758-a632-4687-b867-0e308df30619"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/automations/5cb9073a-aa97-4047-91a1-ad6701f498b6"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/view-automation-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/view-automation-light.png"><img alt="View Automation" width="141" height="28" src="https://cursor.com/assets/images/view-automation-dark.png"></picture></a>&nbsp;</div>
