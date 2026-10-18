# Match Snake & Ladder dice roll to Ludo Battle Royal animation

### Motivation
- Players reported the Snake & Ladder dice appear to "shake" instead of rolling on portrait phones, so the dice motion must match the proven Ludo Battle Royal behavior.

### Description
- Replace the per-frame quaternion reconstruction with the same continuous per-axis incremental tumble used by Ludo by updating `createDiceRollAnimation` in `webapp/src/components/SnakeBoard3D.jsx`. 
- Preserve the original Ludo-style arc, eased translation, wobble, bounce, landing, and authoritative final face logic so online results remain synchronized. 
- Keep dice timing and durations (`DICE_ROLL_DURATION`, bounce/settle hold behavior) unchanged to ensure identical visual timing and server-authoritative reveal. 
- Added/kept roll identification and target-value plumbing so incoming server results apply to the correct active roll animation.

### Testing
- Ran `npm --prefix webapp run build` and the production build completed successfully. 
- Ran `npm --prefix webapp run lint -- src/components/SnakeBoard3D.jsx` and linting passed for the modified file. 
- Ran `git diff --check -- webapp/src/components/SnakeBoard3D.jsx` to validate no whitespace/merge issues and it passed. 
- Attempted an automated portrait screenshot using Playwright at 390×844, but the capture failed because the environment is missing the system library `libatk-1.0.so.0` (visual verification could not be completed in CI).

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a927d12c9e88329a5d5f30d5049cc0e)
