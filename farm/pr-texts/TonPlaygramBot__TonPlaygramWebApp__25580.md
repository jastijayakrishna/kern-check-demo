# Remove seated human characters, avatar preconnects, and voice commentary from Domino Royal

### Motivation
- Reduce client bundle size and runtime complexity by removing seated human character models, avatar service integrations, and related animations and textures.
- Avoid external preconnects and privacy/third-party network calls from the Domino Royal arena page.
- Disable in-game voice commentary and any runtime character action hooks that are no longer required.

### Description
- Removed the entire seated human character subsystem from `webapp/public/domino-royal-game.js`, including character themes, cloth materials, loaders, rigging, actions, held-rack rendering, and cleanup logic, and removed the `SkeletonUtils` import.
- Eliminated calls to character lifecycle functions such as `rebuildDominoCharactersForChairs`, `shuffleDominoCharacterThemeOrder`, `runDominoCharacterAction`, `refreshAllDominoCharacterRacks`, `stepDominoCharacterActions`, and `clearDominoCharacters` from the main game flow.
- Updated the React loader in `webapp/src/pages/Games/DominoRoyalArena.jsx` to stop preconnecting to avatar services, removed the `window.__DOMINO_ROYAL_ENABLE_SEATED_HUMANS` flag and the `script.dataset.dominoRoyalSeatedHumans` attribute, and bumped the `DOMINO_ROYAL_SCRIPT_VERSION` string.
- Replaced the removed unit test `test/dominoRoyalCharacterScale.test.js` with `test/dominoRoyalPresentation.test.js` that asserts the arena and public script no longer reference the human character implementation, avatar hosts, or voice commentary.

### Testing
- Ran the JavaScript unit test suite with `npm test` (Jest) and the test runner completed successfully with the new `dominoRoyalPresentation.test.js` present and the deleted `dominoRoyalCharacterScale.test.js` removed.
- Verified the modified build/load path by loading the arena component in development and ensuring the updated `DOMINO_ROYAL_SCRIPT_VERSION` is used and no avatar preconnect links are injected; these checks passed in automated tests that inspect the source files.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a958ad596b08329b79bcd28068d2998)
