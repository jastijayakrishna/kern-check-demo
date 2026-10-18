# fix(dashboards): avoid duplicate ARRAY JOIN aliases for usage and cost type

<!-- aws-preview-pin:start -->
🟡 **Live preview: [pr-16750.preview.langfuse.com](https://pr-16750.preview.langfuse.com)**
<!-- aws-preview-pin:end -->

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## What does this PR do?

ClickHouse rejects dashboard usage-by-type / cost-by-type queries with `Duplicate alias in ARRAY JOIN: usageType` (and the `costType` equivalent).

`ARRAY JOIN mapKeys(...) AS usageType` already binds that alias. The query builder then re-emitted `usageType AS usageType` in SELECT, which ClickHouse treats as a second alias of the same name. This PR emits the pair-expand key as a bare column in SELECT instead.

Fixes #16655

## Type of change

- [x] Bug fix (non-breaking change which fixes an issue)

## Impacted packages

- `@langfuse/shared` (query builder)
- `web` (existing pairExpand SQL assertion)

## Verification

- `pnpm --filter @langfuse/shared run test queryBuilder.pairExpand.test.ts` — `Tests 2 passed (2)`
- `pnpm --filter @langfuse/shared run test queryBuilder` — `Tests 43 passed (43)`
- `pnpm --filter @langfuse/shared run lint` — passed after building `@repo/eslint-plugin`
- `pnpm --filter @langfuse/shared run typecheck` — passed
- Pre-commit `turbo run lint` — `Tasks: 7 successful, 7 total`

Skipped ClickHouse/web integration tests and worker tests: this environment cannot talk to Docker, and the worker does not use this query builder. The regression is SQL generation; the new unit tests assert the compiled query no longer re-aliases the ARRAY JOIN key on both the single-level (dashboard) and two-level paths.

## Mandatory Tasks

- [x] Make sure you have self-reviewed the code.

## Checklist

- Tests cover the reported dashboard `usageByType` timeseries SQL and the two-level inner SELECT path

<!-- CURSOR_AGENT_PR_BODY_END -->

Linear Issue: [LFE-15675](https://linear.app/clickhouse/issue/LFE-15675/bug-duplicate-alias-in-array-join-for-usagetypecosttype-on-dashboard)

<div><a href="https://cursor.com/agents/bc-6857516e-1a5f-4236-8f8a-a45b232a4aa3?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-6857516e-1a5f-4236-8f8a-a45b232a4aa3&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>



<!-- greptile_comment -->

<details open><summary><h3>Greptile Summary</h3></summary>

This PR fixes ClickHouse dashboard queries for usage-by-type and cost-by-type by projecting ARRAY JOIN keys without redundantly re-aliasing them.

- Centralizes pair-expand key projection in a helper used by single-level and two-level query paths.
- Adds focused regression coverage for usage and cost query generation.
- Extends the existing web assertion to reject duplicate aliases.
</details>


<details><summary><h3>Confidence Score: 5/5</h3></summary>

The PR appears safe to merge, with the changed projections remaining aligned with every current pair-expand declaration and query grouping path.

The two existing pair-expand dimensions always define aliases matching their ARRAY JOIN bindings, and all changed SELECT paths now reference those bound names consistently without changing the output-column contract.
</details>

<sub>Reviews (1): Last reviewed commit: ["fix(dashboards): avoid duplicate ARRAY J..."](https://github.com/langfuse/langfuse/commit/70ca80b2317a5265bb72c8a9d94c1d8
