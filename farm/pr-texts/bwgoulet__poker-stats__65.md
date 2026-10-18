# Add example equation to Outcome Swing tooltip

### Motivation
- Outcome swing wording was confusing and needed a concrete example showing how the value is computed from normalized profits. 
- The same explanation should appear in both the players table tooltip and the individual player detail page for consistency.

### Description
- Add `OUTCOME_SWING_DESCRIPTION` to `src/lib/stats/player-classification.ts` containing a short explanation and a worked example that shows the median, median absolute deviation (MAD), and final `1.4826 × MAD` equation (example: normalized profits −1×, 0×, +2× → outcome swing = `1.4826 × 1× = 1.48×`).
- Use the new `OUTCOME_SWING_DESCRIPTION` constant in `src/components/players/PlayersTable.tsx` for the Outcome Swing column tooltip.
- Use the same `OUTCOME_SWING_DESCRIPTION` in `src/app/players/[playerId]/page.tsx` for the Outcome swing help text in the player detail view.

### Testing
- Ran `npm test` and all tests passed (`37 tests passed`).
- Ran `npm run typecheck` and TypeScript checks succeeded.
- Ran `git diff --check` and no whitespace/diff issues were reported.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a992e5a22f483329e32c1c71d801b2b)
