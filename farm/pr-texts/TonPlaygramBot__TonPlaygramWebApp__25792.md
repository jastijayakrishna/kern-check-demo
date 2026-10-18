# Add animated park landmarks to Tirana Streets

### Motivation
- Improve the visual fidelity of mapped Tirana by adding authored, mobile-budget park attractions anchored to the checked-in Rinia landmark and Grand Park area while keeping placement and provenance explicit.
- Provide mobile-friendly animated features (fountain jets, observation wheel, carousel) with distance culling and battery-mode throttling to limit runtime cost on portrait devices.

### Description
- Add `ParkAttractions` Three.js layer in `webapp/src/games/tirana-environment/ParkAttractions.ts` implementing a stone fountain basin, reflective pool, animated particle jets, an observation wheel and a carousel, and a simple distance/battery visibility policy. The attractions are explicitly documented as artistic detail and anchored to the checked-in `WORLD.landmarks` `rinia` position.
- Integrate the attractions into the shared Tirana enhancement lifecycle by importing and mounting the layer in `webapp/src/games/tirana-expansion/WorldEnhancements.ts`, and calling `attractions.update(...)` and `attractions.dispose()` alongside existing `shopfronts`, `streets` and `ground` updates/disposal.
- Add a regression test `test/tiranaParkAttractions.test.mjs` that asserts presence of the new identifiers and verifies the integration points (`update` and `dispose`) are wired into `WorldEnhancements`.
- Use `disposeTree` to release geometries/materials/textures when the attractions are disposed.

### Testing
- Ran `node --test test/tiranaParkAttractions.test.mjs test/tiranaStreetDetail.test.mjs` and the test suite covering the new park attraction assertions and the existing Tirana street-detail tests passed (28 tests passed).
- Ran `npm run build` which executed the Vite production build successfully (the run produced existing Rollup chunk-size warnings only).
- Ran `npx tsc --noEmit --pretty false` which reported pre-existing, repository-wide TypeScript typing errors unrelated to the changes in `ParkAttractions.ts` (the new code itself is isolated from those type failures).
- Attempted a Playwright mobile capture (`390x844`) to validate in-browser rendering, but the headless Chromium process could not launch in-container due to a missing system library (`libatk-1.0.so.0`), so automated screenshot capture did not complete.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6aa15e780d8c8329b1085a0a9d5d202e)
