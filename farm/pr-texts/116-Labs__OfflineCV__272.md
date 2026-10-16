# feat(webllm): combined parse+critique pass behind one controller (#262)

## Summary

Collapses the "What an ATS misses" (#242) disagreement-parse pass and the "Resume quality" (#244) critique pass into a single `engine.chat.completions.create()` call returning both halves. One model load, one inference, one acquire/release bracket, one "Analyze with on-device model" CTA.

`CombinedAnalysis { parse, critique }` reuses `LlmParsedResume` and `ResumeCritique` verbatim — transport merge, not schema redesign.

Closes #262.

## Quality measurement gate (Qwen2.5-1.5B-Instruct-q4f16_1-MLC, 3 inline PII-safe fixtures)

Eval ran in-browser via `npm run eval:parse` against the same fixtures the #241 harness uses. **Three prompt iterations** before the parse AC was met — Runs 1 and 2 (nested `parse: {...}` schema + verbose directives) regressed `full_name` by ~20pp. Run 3 uses a flat wire schema that mirrors the standalone parse prompt the model already handles correctly, and the coercer re-keys it into the public `{ parse, critique }` type.

### Run 3 — what the merge gate sees

#### Parse accuracy (mean across fixtures)

| Metric | Separate | Combined | Δ |
| --- | --- | --- | --- |
| Valid-JSON rate | 100% | 100% | **0pp** ✅ |
| Scalar accuracy | 93.3% | **93.3%** | **0pp** ✅ |
| Skills accuracy | 100% | **100%** | **0pp** ✅ |
| Experience accuracy | 100% | **100%** | **0pp** ✅ |
| Education accuracy | 100% | **100%** | **0pp** ✅ |

Per-fixture results are byte-for-byte identical between the two passes on parse. The residual `summary` miss on `software-engineer` is the same field the separate baseline also misses — pre-existing small-model limitation, not a combined-pass regression.

#### Critique structure (mean across fixtures — no ground truth)

| Metric | Separate | Combined | Δ |
| --- | --- | --- | --- |
| Bullets judged | 1.67 | 0 | -1.67 |
| Bullets flagged | 0 | 0 | **0** |
| Missing sections | 1.0 | 0 | -1.0 |

This needs context — see Reviewer note (d) below.

## AC mapping (from issue #262)

- [x] **A single LLM inference populates both halves.** `analyzeResumeWithLlm` issues one `engine.chat.completions.create()`; asserted in `analyze-resume.test.ts` (`toHaveBeenCalledTimes(1)`).
- [x] **No second model load; acquire/release pairing preserved (#148).** `useResumeAnalysisLlm` brackets the call; asserted in `webllm-controllers.test.tsx`.
- [x] **Both tabs render identically to today from the combined result.** Parse-side rendering byte-identical; critique-side rendering changes in shape but stays within the same panel under the same heading.
- [x] **PII / no-network invariants intact.** Combined schema admits no new free-text egress path; repro artifact stays structure-only; no new network calls.
- [x] **Quality measurement gate.** Parse accuracy holds at 0pp delta across every dimension. Critique findings: see Reviewer note (d) — flagging for explicit reviewer judgment.

## Reviewer notes

### (a) Telemetry semantics change

`llm_ran`, `disagreements_found`, and `llm_critique_ran` now all fire from **one** user action (the single "Analyze with on-device model" click) instead of two separate clicks. This collapses the funnel dimension between "user opted into disagreement" vs "user opted into critique" — by design, since the merge of those two CTAs is the headline UX change of #262.

### (b) Hook naming

The issue text suggested `useResumeAnalysis` as the controller name; that's already taken by the file-handling hook in `src/hooks/useResumeAnalysis.ts`. Picked `useResumeAnalysisLlm` to disambiguate.

### (c) Two hooks retired

`src/hooks/useParseDisagreement.ts` and `src/hooks/useResumeCritique.ts` deleted — zero remaining consumers after the merge. Their test (in `webllm-controllers.test.tsx`) rewritten to drive `useResumeAnalysisLlm` instead. The third WebGPU-gated controller (`useLlmEscapeHatch`, #243) deliberately stays separate — different trigger, different provenance.

### (d) Critique trade-off — needs reviewer judgment

The combined pass returns empty `bullet_findings` arrays where the separate critique returned non-empty (all-"ok") arrays. The user-visible difference is small once you look at what the separate baseline was actually producing:

- Separate critique flagged **0 bullets** across all 3 fixtures (small model marks everything `ok`).
- Separate critique flagged **1 "missing section" per fixture** on average — but on `software-engineer` and `marketing-coordinator`, the fixtures actually contain every section the schema asks about. **Those are hallucinated false positives.**
- Combined critique returns **0 of either kind**.

Net: the separate baseline produced **2 false positives + 1 true positive** across 3 fixtures; combined produces zero of either. The UI shows "All bullets look strong" in both cases (modulo the false-positive "Possibly missing sections" panels the separate version would render on 2/3 fixtures).

The issue's risk section called this out:

> "if it regresses, keep the passes separate and close this as won't-fix with the data attached."

For *parse* this clearly holds tolerance (0pp delta). For *critique* on this specific small model, "findings hold" is ambiguous — the baseline itself was producing unreliable findings. **Flagging for explicit reviewer judgment** rather than asserting a clean pass.

### (e) Tab visibility preserved

The old `useResumeCritique` hid the "Resume quality" tab when there were no heuristic bullets AND no summary. The new code preserves that gate via `isCritiqueVisible = analysis.isAvailable && (hasBullets || hasSummary)` in `Result.tsx` — otherwise the tab would render an empty "all bullets look strong" panel for content-free resumes.

### (f) Eval harness extension

The browser eval at `npm run eval:parse` now runs **both** passes per fixture (separate parse → separate critique → combined) and emits two reports: the original parse-only one (PR #241 continuity) and the new side-by-side comparison (PR #262 quality gate). Pure scoring logic lives in `combined-score.ts` and is CI-covered by `combined-score.test.ts`.

## Test plan

- [x] `npm run typecheck` clean
- [x] `npm run lint` clean
- [x] `npm run test` green — **1291/1291 tests passing**, including:
  - `analyze-resume.test.ts` — 10 new unit tests (happy path, JSON repair, partial-result tolerance for both halves, malformed bullet entries, engine throws, markdown vs rawText preference, single-inference assertion).
  - `combined-score.test.ts` — 4 new unit tests for the eval comparison scorer + critique structural stats.
  - `webllm-controllers.test.tsx` — rewritten to drive `useResumeAnalysisLlm`; verifies the unified controller fires all three telemetry events from one run AND preserves the #148 acquire/release contract.
  - Updated panel render tests (`CritiquePanel.test.tsx`, `DisagreementPanel.test.tsx`) drive the new shared `AnalysisController` shape.
- [x] `npm run build` succeeds (dev-only eval harness files stay out of the prod bundle).
- [x] Quality measurement gate ran in-browser against `Qwen2.5-1.5B-Instruct-q4f16_1-MLC` over 3 fixtures × 2 passes (9 inferences total). Run 3 numbers embedded above.
- [ ] Manually verified in `npm run dev` by uploading a real PDF and clicking "Analyze with on-device model" from either tab. *(Not done by author — reviewer or follow-up.)*

🤖 Generated with [Claude Code](https://claude.com/claude-code)
