# Remove Albanian Pool Royale variant and hide HUD points in portrait HUD

### Motivation
- Remove the new Albanian (race-to-61) variant because it was added recently and is slowing game load and runtime paths. 
- Stop showing per-frame point totals in the portrait player frame so the avatar + username framing is cleaner and lighter for mobile portrait.
- Keep the Pool Royale variant set and visuals consistent for `8ball`, `uk` and `9ball` only.

### Description
- Deleted the Albanian rules implementation and types by removing `lib/albanianBilliards.js` and `lib/albanianBilliards.d.ts`, and removed its unit test `test/albanianBilliards.test.js`.
- Removed Albanian support from the rules resolver and runtime by dropping the `albanian` branch and related serialization/apply logic from `src/rules/PoolRoyaleRules.ts` and updated `PoolVariantId` to only include `8ball`, `uk`, and `9ball`.
- Removed the Albanian entry from the lobby and variant thumbnail/configs in `webapp/src/pages/Games/PoolRoyaleLobby.jsx` and `webapp/src/config/gameAssets.js` so the lobby selector only presents `8Ball` and `9-Ball`.
- Removed HUD score rendering in the portrait player frame so the frame now shows avatars and usernames without the points; updated relevant portrait HUD JSX in `webapp/src/pages/Games/PoolRoyale.jsx`.
- Made a small related visual tweak in the 3D table marking setup in `webapp/src/pages/Games/PoolRoyale.jsx` (marking material color, line thickness, and ensuring the baulk line is visible/render-ordered) to preserve legibility on mobile screens.
- Committed the changes on the working branch (commit message: `Remove Albanian Pool Royale variant and HUD points`).

### Testing
- Ran the rules unit tests: `npm test -- --runInBand test/poolRoyaleRules.test.ts` and the suite passed (5 tests passed).
- Built the webapp production bundle: `npm --prefix webapp run build` and the Vite build completed successfully.
- Started the dev server (`npm --prefix webapp run dev`) to smoke-check the lobby page; Vite reported ready (Playwright screenshot attempt failed in this environment because browsers are not installed).

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a966eb130008329a1f888aee8e5cdcf)
