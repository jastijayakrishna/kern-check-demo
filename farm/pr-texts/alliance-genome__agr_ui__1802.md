# fix: drop redundant AGR-corpus entry in DP Recent Papers

## Summary
Fixes the Disease Portal **Recent Papers** section showing two papers with the same species icon on every disease page (e.g. two "mouse" papers on Alzheimer's, Parkinson's, and Diabetes Mellitus).

## Root cause
The `latest-literature-by-disease-per-mod` endpoint returns the newest paper **per corpus** and treats the Alliance central **`AGR`** corpus as one of those slots. That extra AGR paper has no species of its own, but is itself a member of one or more MOD corpora, so the UI rendered it with the same icon(s) as those MODs' dedicated papers — looking like a duplicate. The labels were never wrong; both papers genuinely are in the mouse corpus.

## Fix
Drop the AGR entry, but **only when it is redundant**. A naive "drop every `AGR`-tagged row" filter silently removes a species, because the AGR paper is frequently the *sole* carrier of one — measured across 20 diseases on stage, ~15% lose RGD/SGD/WB that way (e.g. `['ZFIN','RGD','AGR']`, `['SGD','AGR']`, `['AGR','WB']`). So an AGR row is dropped only when **every MOD species it carries is already covered by a non-AGR row**, and repeated curies are deduped (the backend can return one paper in two slots).

## Verification
- Live stage data for all three portal pages now render one paper per MOD species with a single mouse icon.
- 0/20 sampled diseases lose a species under the new rule.
- ESLint + Prettier clean.

## Notes
The clean long-term fix is backend-side (exclude `AGR` from the per-corpus grouping, or expose which slot each paper filled); documented in `RECENT_PAPERS_API.md`.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
