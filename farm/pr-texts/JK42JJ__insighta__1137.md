# fix(mandala-book): stop LLM retries on JSON parse failure + per-stage cost tags

## Problem (measured)
Book-fill makes **9–17 Sonnet calls/book** vs the §7.5 "book당 1콜" cost model. One driver confirmed in code + OpenRouter CSV: the model emits a **raw newline** (or a maxTokens truncation) inside a JSON string → `JSON.parse` trips → `SYNTHESIS_ATTEMPTS`/`SKELETON_ATTEMPTS` **re-called Sonnet** to dodge it. **4 of a measured 13 calls/book were these parse retries.** The prompt-side "개행 금지" defense (`topic-synthesis.ts:111`) is not reliably obeyed — the fix belongs in the parser, not the prompt.

## Fix (CP504 §11) — salvage in-attempt, no new LLM call
- **`src/utils/lenient-json.ts`** (new): `escapeUnescapedJsonNewlines` + `closeUnclosedJsonBrackets` + `parseJsonLenient` (direct → newline-escape → bracket-close). Extracted from `mandala/generator.ts`'s proven robust-extract helpers → three parsers now share **one** copy (generator imports them; −65 lines of dup).
- **topic-synthesis / book-skeleton**: parse via `parseJsonLenient`; `*_ATTEMPTS` now retry **PROVIDER faults only** (parse failure is no longer a retry reason). A `via` counter is logged so we can verify retries → 0 post-fix. Content preserved (newline restored on parse, collapsed to space as before — no word loss).

## Per-stage cost instrumentation (CP504 §3)
`cost_usd` is already priced (`llm-pricing.ts`), but every call logged `module='openrouter'`, hiding which stage spends. Add `GenerateOptions.purpose` → written to the **existing** `llm_call_logs.module` column (no schema change). Book stages now tag `cell_synthesis` / `book_skeleton` / `chapter_weave` / `book_research` / `book_factcheck` → per-stage cost = `GROUP BY module`. Absent = `'openrouter'` (additive no-op).

## Verification
- `tsc --noEmit`: clean
- New/updated tests: lenient-json (10), topic-synthesis salvage + no-retry-on-parse (26 total), book-skeleton raw-newline/truncation salvage, generator DRY regression (19). All pass.
- `hardcode-audit`: unchanged (33 baseline)
- Backend-only; **no serving-path change**. The 3 unit suites that fail locally (pipeline-runner / key-alarm / auto-add-recommendations) fail **identically on origin/main** — pre-existing env-dependent, unrelated to this diff.

## Out of scope (measurement-gated)
`cell→book 1-call` consolidation (§2-2) and `skeleton` model downgrade (§2-3): the design doc defers these to **"측정 후 확정"**, and they need a prod A/B the LLM-ban blocks CC from running. Analysis found **2-2 is call-count 8× but not cost 8× (output tokens ≈ constant)** — it is primarily a *quality* fix (cross-cell narrative + chapter intro). The purpose tags here land the measurement basis so 2-2/2-3 can be decided on real per-stage numbers under James's quality gate.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
