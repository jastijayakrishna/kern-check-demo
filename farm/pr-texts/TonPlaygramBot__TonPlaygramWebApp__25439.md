# Domino Royal: match bottom live-video frame to Murlan and center 1v1 opponent in portrait

### Motivation

- Align the Domino Royal bottom player's live-video/avatar frame to the exact visual size used by Murlan Royale and ensure in 1v1 portrait matches the opponent is positioned at the top of the screen so players face each other.

### Description

- Add `MURLAN_BOTTOM_AVATAR_FRAME_REM`, `HEAD_TO_HEAD_OPPONENT_TOP_RATIO` and `HEAD_TO_HEAD_OPPONENT_MIN_TOP` and use them to size the anchored self-video element in `webapp/public/domino-royal-game.js` so the bottom live-video frame matches Murlan Royale's visual size.
- Change `updateSeatBadgePositions` in `webapp/public/domino-royal-game.js` to place the opponent at the top-center when `N === 2` (portrait head-to-head) instead of using a side seat.
- Adjust the inlined arena CSS in `webapp/src/pages/Games/DominoRoyalArena.jsx` so the self player badge/core uses the same `3.185rem` presentation and bump the Domino Royal script version to ensure clients load the updated layout.
- Add a regression test `test/dominoRoyalVideoLayout.test.js` that verifies the new sizing constants and the head-to-head placement logic are present in the built script and arena source.

### Testing

- `npx jest test/dominoRoyalVideoLayout.test.js test/dominoRoyalCharacterScale.test.js --runInBand` — test suites passed (2 suites, 4 tests passed).
- `npm --prefix webapp run build` — production build completed successfully.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a917dd32448832995f40be8405d8299)
