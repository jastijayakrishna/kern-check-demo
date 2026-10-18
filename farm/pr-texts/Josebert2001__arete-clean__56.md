# fix(ai): stop Gemini reasoning tokens from truncating Simplify/Tutor answers

## Summary
- `api/simplify.js` / `api/tutor.js`: zero Gemini's hidden thinking budget on the final answer step (same fix `explainer.js` already had) — reasoning tokens were eating into the visible-answer budget and cutting responses short
- `api/simplify.js` system prompt: long enumerated sections (e.g. ENT 221's 20-item Critical Success Factors list) now get grouped by theme instead of demanding one bullet per item, which was unsatisfiable under the old 3-6 bullet / 200-word cap regardless of model
- `api/_lib/model.js`: light-tier Gemini bumped `gemini-3.1-flash-lite` → `gemini-3.5-flash-lite`; simplify moved back to the light tier now that the thinking-budget fix addresses the reason it was moved off it

## Test plan
- [ ] Open the preview deployment, sign in, hit Simplify on a long lecture-note heading (worst case: ENT 221 → "3.5 Critical Success Factors in Entrepreneurship") — confirm the rewrite isn't cut off and covers all the themes
- [ ] Ask the AI Tutor a real question that needs a full answer (not a greeting) — confirm the reply isn't unexpectedly short/truncated
- [ ] Merge once both check out

🤖 Generated with [Claude Code](https://claude.com/claude-code)
