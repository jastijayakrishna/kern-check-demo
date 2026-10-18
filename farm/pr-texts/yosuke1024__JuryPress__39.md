# Teach varied attribution wording and per-sentence attribution scope

## Problem

"According to the README" dominates the published articles. Measured across all five:

| | attribution phrases |
|---|---|
| public-apis | 168 |
| freecodecamp | 88 |
| open-llm-leaderboard | 24 |
| i-rl | 14 |
| vinhhien112 | 14 |

**183 of 308 (59%) are "according to the README"**, and the two articles generated under the current claim-provenance rule carry 6–12× more attribution phrasing than the bootstrap-era ones.

Three causes compounded:

1. **Attribution is required per sentence** — the volume driver. README is the primary evidence, so most statements need their own attribution.
2. **The validator accepted only a closed six-phrase list**, making one opener the only reliably safe choice. Deviating meant a hard failure — `season-2-request-36` proved it.
3. **The prompt's own examples anchored on that opener.**

Cause 2 is fixed separately in #38. This PR is the prompt side (causes 1 and 3).

## Change

- **Enumerates what actually satisfies the rule**: an `According to …` / `Per the …` opener, **or** a creator-authored source noun followed by a reporting verb. The model can now vary without guessing at what the gate accepts.
- **Instructs varying the wording** and naming the source actually cited, explicitly warning against repeating one opener — while forbidding variation that costs accuracy ("attribute the source the evidence actually is").
- **States that attribution is PER SENTENCE** and never carries over from a preceding sentence, with a PASS/FAIL pair built from the real `season-2-request-36` failure (an attributed first sentence followed by an unattributed benchmark assertion) — empirically the shape that bites.

`evaluation_prompt_version` 2.1.0 → 2.2.0. **The rubric, personas, scoring, thinking level, prohibited phrases and every other evaluation instruction are unchanged**; this touches only the attribution wording repertoire and its scope statement.

## Test

New `tests/unit/prompt-validator-sync.test.ts` asserts **every attribution example the prompt teaches** against the real `CREATOR_ATTRIBUTION` / `COMMUNITY_ATTRIBUTION` patterns — PASS examples must match, FAIL counterexamples must not — plus that the prompt still carries the instructions those assertions depend on. The prompt and the validator can no longer drift apart silently, which is the desync that produced both of the pipeline's only quality failures.

Existing `evaluator-routing.test.ts` prompt-contract assertions still pass (one caught an example I had dropped while editing — restored).

Local: `typecheck` ✅ / `test:unit` **637 passed** ✅ / `test:e2e` 25 passed ✅
Both published records still validate as `passed`, so nothing already live is affected.

## Merge order

Best merged **after #38** — the widened validator is what makes the varied phrasings safe. Merging this first would instruct variation that the old narrow pattern would then reject.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
