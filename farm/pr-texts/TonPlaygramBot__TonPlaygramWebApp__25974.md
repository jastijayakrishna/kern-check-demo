# Align Snake & Ladder presentation with Ludo Battle Royal

### Motivation
- Make Snake & Ladder visually match the Ludo Battle Royal presentation so boards, table, chairs, HDRI, dice and seated humans read at the same world-space scale and portrait framing.
- Make board tiles visibly respond when a token occupies them so gameplay feedback is clearer on portrait phones.

### Description
- Calibrated arena and object scales to Ludo: added shared `ARENA_SCALE`/`MODEL_SCALE` constants, adjusted `TABLE_RADIUS`, `TABLE_HEIGHT`, `BOARD_SCALE`, `BOARD_FOOTPRINT_SCALE`, and set `DEFAULT_HDRI_RESOLUTIONS` to `['2k']` in `webapp/src/components/SnakeBoard3D.jsx` so Snake uses the same authored Ludo measurements and portrait camera tuning.
- Normalized dice and token footprint: set `DICE_SIZE` to the Ludo value and adjusted board footprint sizing to match Ludo Battle Royal.
- Tile glow on occupancy: stored per-tile base emissive intensities and implemented `applyTileHighlight` + `resetTileAppearance` to set emissive colors and intensities, and extended `updateTilesHighlight` to accept `occupiedCells` so tiles that have tokens remain strongly illuminated while trails are still shown.
- Portrait/seat tuning: adjusted seat radius, bottom-seat pushback and seated-human target height so avatars and chairs align visually with the shared table scale.
- Weapon/prop scaling: applied an `ARENA_SCALE_RATIO` when sizing parked firearms and updated seat-weapon layout logic to keep props clear of dice lanes.
- Tests and test fixtures: updated `webapp/src/utils/snakeWeaponParking.snake.test.ts` to reflect the new arena scaling used during geometry checks.

### Testing
- Ran the Snake test suite with `npm run test:snake --prefix webapp` and ended with all tests passing: 13 test files, 93 tests (final test run: 93 passed).
- Ran `npx eslint --no-ignore --no-warn-ignored src/components/SnakeBoard3D.jsx src/utils/snakeWeaponParking.snake.test.ts` with no reported errors.
- Verified `git diff --check` and committed changes (commit message: "Align Snake tabletop scale with Ludo and glow occupied tiles").
- Attempted a Playwright portrait capture to visually validate 390×844 rendering; Playwright/browser dependencies were installed but the headless capture did not produce a stable screenshot during the preview navigation window, so no reliable screenshot is attached.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6aa8ca6f0ad88329b48d9aca5982d974)
