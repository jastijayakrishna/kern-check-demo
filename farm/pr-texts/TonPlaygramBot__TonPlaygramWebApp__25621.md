# Albanian 61 scoring + variant broadcast HUDs (Albanian / 9-ball / 8-ball)

### Motivation
- Align Pool Royale with TV-style broadcast scorecards and correct Albanian Billiards fouling semantics so balls potted on a foul credit the incoming player and can immediately decide the race-to-61. 
- Ensure 8-ball and 9-ball follow TV presentation (no numerical point accumulation) while preserving visible pot rows, avatars and active-turn highlights on portrait HUDs.

### Description
- Updated the Albanian rules in `lib/albanianBilliards.js` so object balls potted during a foul are removed from the table but their face-value is awarded to the incoming player, with `pointsAwardedTo` included in shot results and immediate-win detection when reaching `targetScore`.
- Propagated foul-pot points into the authoritative frame state in `src/rules/PoolRoyaleRules.ts` by reporting foul points in the HUD metadata and using the Albanian snapshot scores for `players` values.
- Stopped using numerical pot-count scoring for 8-ball/UK variants in `PoolRoyaleRules` (scores are now represented in HUD metadata as group status rather than numeric totals) and kept 9-ball logic unchanged with no point counting.
- Added portrait broadcast-style match cards and layouts in `webapp/src/pages/Games/PoolRoyale.jsx` with distinct variants: a green points scoreboard for Albanian 61, an amber race card for 9-ball, and a blue group-status card for 8-ball; all cards keep avatars, names, potted-ball rows and active-turn highlighting.
- Added/updated unit tests in `test/albanianBilliards.test.js` and `test/poolRoyaleRules.test.ts` to cover foul-pot transfer and the opponent-winning-by-foul scenario, and adjusted expectations for 8-ball HUD behavior.

### Testing
- Ran `node --test test/albanianBilliards.test.js` and all Albanian-Billiards tests passed (5/5).
- Ran `npx jest test/poolRoyaleRules.test.ts --runInBand` and the `PoolRoyaleRules` suite passed (6/6).
- Built the web UI with `npm --prefix webapp run build` which completed successfully and produced `dist` assets.
- Linted the modified files with `npx eslint` which ran without blocking errors for the changed files.
- Attempted an automated Playwright portrait screenshot to visually verify the HUD but a headless/browser environment issue prevented a reliable screenshot artifact, so no screenshot was produced.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a96650634b88329be0523b02d359071)
