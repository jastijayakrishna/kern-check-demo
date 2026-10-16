# refactor: simplify source changed since v0.38.9 not in #6812/#6832 (round 2)

## What

Round-2 comprehensive simplification of **source code changed since v0.38.9** that was **not** covered by the two existing cleanup PRs:

- #6812 (merged) — round-1 source simplification
- #6832 (open) — test-suite simplification

This PR is the complement: the source files changed since v0.38.9 that neither touched.

## Scope & method

- Enumerated all source (non-test) files changed since `v0.38.9`, subtracted the file sets of #6812 and #6832, and focused on the **461 files with meaningful churn (≥10 changed lines)**. The ~225 files with trivial 1–9 line changes were intentionally skipped to respect the anti-churn bar.
- Grouped into coherent, disjoint per-module batches and ran a code-simplifier over each, then an **adversarial verify pass** per batch that re-read the actual diff and checked behavior-preservation, scope, and convention compliance (self-repairing on any high-severity finding).
- **Test files changed since v0.38.9 were deliberately excluded** to avoid colliding with the still-open test PR #6832.

## Result

**55 files, +291 / −334 (net −43 LoC).** Representative changes:

- Collapse redundant `if/else` chains into early returns or short-circuit expressions
- Inline trivial single-use closures/helpers; flatten a throw/recatch and a few wrapper layers
- Dedupe local helpers against existing shared utilities (`escape-string-regexp`, `path.basename`, shared formatters)
- Pass Zod shape objects directly to `.extend()` (drop redundant spreads); minor Zod v4 idiom tidy
- Tighten import grouping and normalize new-comment prose

No public APIs, exports, or observable behavior changed.

## Verification

- `tsc --noEmit` green for repo-root `src`, `tsconfig.test-kernel.json`, `packages/extension`, and `packages/cli`
- `eslint` clean on all changed files
- Prettier clean (pre-commit hook)
- Rebased onto current `main`; the 3 files that also changed upstream were re-verified individually (typecheck + lint + manual diff review)

## Notes

- The sensitive `auth-bridge` and `codexOAuthClient` edits are limited to behavior-preserving local refactors and were reviewed by hand.
- A pre-existing observation (not introduced here): the `skills` CLI command's NDJSON output dropped its per-record `ts` field when it moved to `emitCliResult` on `main` — flagging for a maintainer to confirm it was intentional.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- CURSOR_SUMMARY -->
---

> [!NOTE]
> **Low Risk**
> Mechanical refactors with typecheck/lint called out in the PR; the only subtle areas (auth callback parsing, agent key migration, mainView active flags) appear equivalent to prior logic. No new features or security surface.
> 
> **Overview**
> Round-2 **behavior-preserving** cleanup across ~55 files (net −43 LoC): local refactors, deduplication, and comment/prose tidy—no intentional API or product behavior changes.
> 
> **CLI / TUI:** `Select` centralizes cancel handling in `cancelAndDrop`; orchestration model-step titles/subtitles are shared variables; OpenRouter toggles invalidate the model cache once; auth callback JSON parsing separates `JSON.parse` from Zod validation.
> 
> **Extension / desktop:** Chat export uses a `switch` on format and `path.basename`; Models tab ChatGPT switches use named handlers; unused imports/types dropped; Zod `.extend(fileOpConfigFields)` without redundant spread.
> 
> **Core agent / models:** `withAgentName` dedupes source-qualified key rewrites; filename migration matches qualified keys via `key !== name`; OpenAI Responses adds `findLastUserMessage`; Google Interactions folds media resolution into `mediaResolutionFields`; `formatToolResultAsText` merges shared user-patch/instruction handling; `RunUsageAccumulator` comments tightened; `executionRegistry` stop flow uses early returns.
> 
> **Shared / misc:** `PREFERRED_TOOL_USE_AGENTS` reuses `BUILTIN_TEAM_ROOT_AGENT_NAMES`; external-inquiry permission schemas share a base; `AgentNameSchema` uses `.regex()`; Codex OAuth adds shared `postJson`; `XmlOutputManager` uses `escape-string-regexp`; default team seeding prefers recorded default before host fallback; auth-bridge OAuth error copy simplified.
> 
> <sup>Reviewed by [Cursor Bugbot](https://cursor.com/bugbot) for commit 4a9056e0fc597ab0e14656f70c4862d62c46bde9. Bugbot is set up for automated code reviews on this repo. Configure [here](https://www.cursor.com/dashboard/bugbot).</sup>
<!-- /CURSOR_SUMMARY -->
