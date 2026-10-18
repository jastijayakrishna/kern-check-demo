# fix(api): treat prompt version metrics dimensions as numbers

<!-- aws-preview-pin:start -->
🟡 **Live preview: [pr-16746.preview.langfuse.com](https://pr-16746.preview.langfuse.com)**
<!-- aws-preview-pin:end -->

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## What does this PR do?

The metrics query data model declared `promptVersion` and `observationPromptVersion` as strings, but ClickHouse stores `prompt_version` as `Nullable(UInt16)`. That mismatch made the public Metrics API unable to slice scores by prompt version:

- Grouping by `observationPromptVersion` returned `null`
- `type: "string"` filters were accepted and silently did nothing
- `type: "number"` filters returned 400
- `contains` compiled to `position(UInt16, …)` and 500'd

This aligns those dimensions with the table definitions (already `type: "number"`) so numeric filters compile to a ClickHouse number predicate and string/`contains` filters are rejected with 400.

**Filter contract change:** clients must send `type: "number"` (for example `{"column":"observationPromptVersion","operator":"=","value":2,"type":"number"}`). The previous `type: "string"` form never filtered correctly.

Fixes #16351

## Type of change

- [x] Bug fix (non-breaking change which fixes an issue)

The accepted filter type for these dimensions changes from `string` to `number`. Existing string filters were already ineffective.

## Mandatory Tasks

- [x] Make sure you have self-reviewed the code.

## Impacted packages

- `@langfuse/shared` (metrics data model + query builder)
- `web` (metrics v2 API tests)

## Verification

- `pnpm --filter @langfuse/shared run test src/features/query/server/queryBuilder.filterValidation.test.ts` — Tests 37 passed (37)
- Related query-builder suites — Tests 35 passed (35)
- Pre-commit `turbo run lint` — Tasks: 7 successful, 7 total
- First CI run: `tests-web` and `tests-shared` passed; `lint`/`web` preview build failed on `makeAPICall` defaulting to `IngestionAPIResponse` (fixed)
- Local `tsc` on web after the test typing fix produced no `metrics-v2-api` errors

## Checklist

- Self-reviewed
- Tests added for the number-filter path and the rejected string/`contains` path

<!-- CURSOR_AGENT_PR_BODY_END -->

Linear Issue: [LFE-15368](https://linear.app/clickhouse/issue/LFE-15368/bug-metrics-api-scores-cannot-be-grouped-or-filtered-by)

<div><a href="https://cursor.com/agents/bc-b6e19f93-9ada-4c4c-a227-f8d8ebf1b16e?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-b6e19f93-9ada-4c4c-a227-f8d8ebf1b16e&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>



<!-- greptile_comment -->

<details open><summary><h3>Greptile Summary</h3></summary>

Aligns prompt-version metric dimensions with their numeric ClickHouse representation and ensures relation-backed dimensions retain their declared types.
- Declares prompt-version dimensions as numbers in v1 and v2 observation and score views.
- Validates numeric filters while rejecting incompatible string filters.
- Adds query-builder and Metrics API coverage for filtering and grouping by prompt version.
</details>


<details><summary><h3>Confidence Score: 5/5</h3></summary>

The PR appears safe to merge, with the declaration, validation, and API tests consistently enforcing numeric prompt-version behavior.

The v1 and v2 declarations 
