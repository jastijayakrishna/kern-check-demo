# Remove Texas Hold'em human characters and voice commentary

### Motivation
- Reduce render/audio overhead and simplify the Texas Hold'em arena by removing seated human character models, rigging, and the voice commentary system so the game performs faster while preserving core gameplay.

### Description
- Deleted the commentary module and speech pipeline by removing `webapp/src/utils/texasHoldemCommentary.js` and all imports/usages of the commentary and text-to-speech helpers in `webapp/src/pages/Games/TexasHoldemArena.jsx`.
- Removed seated human character model support and related systems from `TexasHoldemArena.jsx`, including character themes, texture/material helpers, GLTF loading/DRACO/KTX2 plumbing for characters, skeleton cloning/rigging, pose/animation functions, and contact-marker helpers.
- Stripped code paths that invoked character behaviors (attach/mount, pose actions, hand/contact updates) and removed commentary enqueue/playback/event hooks while preserving card, chip, table, chair, UI, and sound-effect logic.
- Small reorganizations: removed unused constants and imports (`cloneSkeleton`, commentary constants), reworked community card positioning constants to keep card rendering consistent for portrait mobile.

### Testing
- Built the web client: `npm --prefix webapp run build` — succeeded.
- Linted the codebase: `npm --prefix webapp run lint -- --quiet` — succeeded (no lint errors reported in the modified files).
- Ran unit tests: `npm test -- --runInBand test/texasHoldemGame.test.js test/texasHoldemHdriPreload.test.js` — all tests passed.
- Performed a portrait smoke check (Playwright) at 390x844 loading `/games/texasholdem` and captured a screenshot; the page loaded without console/page errors.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a958f1e4b548329abaab23941f7f6af)
