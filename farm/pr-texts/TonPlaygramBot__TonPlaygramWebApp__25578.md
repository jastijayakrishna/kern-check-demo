# Remove Ludo human characters and voice commentary to improve performance

### Motivation
- Remove seated human models and real-time voice commentary from the Ludo Battle Royal experience to reduce runtime cost, network asset loading, and perceptible game slowdown.  
- Keep all other gameplay, UI, and customization features unchanged so players retain token, table, and capture animation options.  

### Description
- Stop loading and rendering seated human actors in the arena by clearing `seatedHumanActorsRef` and removing the seated-model construction logic in `webapp/src/pages/Games/LudoBattleRoyal.jsx`.  
- Remove human-character option usage from AI loadout generation and appearance normalization so `humanCharacter` is no longer part of `createAiUniqueLoadout`, `DEFAULT_APPEARANCE`, `CUSTOMIZATION_SECTIONS`, or `normalizeAppearance`.  
- Remove human-character inventory, store items, labels, and default loadout entries from `webapp/src/config/ludoBattleInventoryConfig.js`.  
- Delete the Ludo-specific voice commentary module file `webapp/src/utils/ludoBattleRoyaleCommentary.js` so no Ludo voice templates or commentary events are emitted.  

### Testing
- Ran the unit test `jest test/inventoryCrossGameConfig.test.js` with `npm test -- --runInBand test/inventoryCrossGameConfig.test.js`, and it passed.  
- Built the frontend with `npm --prefix webapp run build` and the production build completed successfully.  
- Ran lint on the modified files with `npm --prefix webapp run lint -- src/pages/Games/LudoBattleRoyal.jsx` and the lint command executed (no blocking errors in the modified Ludo page).  
- Attempted a headless browser screenshot to visually confirm no characters, but Playwright’s browser binaries were not available in the environment so the screenshot step could not complete (build and local preview were otherwise exercised).

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a958ae542848329ab1f6bffa71842d9)
