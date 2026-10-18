# Remove 3D character rendering and commentary/TTS support from MurlanRoyaleArena

### Motivation
- Reduce complexity and bundle size by removing the in-scene 3D human character system and its heavy texture/material handling.
- Remove the text-to-speech / commentary feature set which added presets, localization, queueing and browser speech API wiring.
- Simplify seat anchoring and appearance options so the arena relies on stools/chairs only and avoids fragile character-dependent logic.

### Description
- Deleted the commentary utilities file `webapp/src/utils/murlanRoyaleCommentary.js` and removed all related imports, TTS state, preset constants and storage keys such as `COMMENTARY_PRESET_STORAGE_KEY` and `COMMENTARY_MUTE_STORAGE_KEY`.
- Removed 3D human character support: deleted import of `MURLAN_CHARACTER_THEMES`, all character texture/material/cloth combos, loaders/caches, model loading (`loadCharacterModel`), rigging, bone helpers, character action animations and related caches/state variables and functions (attach/fit/enhance/preserve character materials, `createCharacterRig`, `runCharacterAction`, `stepCharacterActions`, etc.).
- Updated appearance and customization to remove the `characters` option from `DEFAULT_APPEARANCE`, `CUSTOMIZATION_SECTIONS` and `normalizeAppearance`, and removed character-related appearance persistence/roster code paths.
- Adjusted seat anchor computation and seat handling to no longer rely on `seat.characterRig.bones.head` and instead use stool/chair positions; removed rebuild/attach calls for seat characters and cleaned up related state in `threeStateRef` initialization and teardown.

### Testing
- Performed a full project build (`yarn build`) to validate bundle and compilation; build completed successfully.
- Ran the test suite (`yarn test`) and linter checks; unit tests and linting passed without failures.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a958aa06c1483299d2eec96839beddc)
