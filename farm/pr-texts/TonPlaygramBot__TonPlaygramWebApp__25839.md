# Improve Racing Royal vehicle scale and circuit precision

### Motivation
- Vehicles visually appeared undersized on portrait mobile screens and needed a single road-scale target so racers read as substantial beside widened road ribbons. 
- Track edges and authored route centrelines required more precise outer boundaries so curbs, tyre barriers and road decals follow corners without pulling inward. 
- The Grand (Lana–Pyramid) variant and event ribbons should match the larger vehicle footprint for consistent gameplay and visuals. 

### Description
- Use a 3.25 m target vehicle length by default: `normaliseVehicleDimensions(..., 3.25)` and scale the authored Apex model to match; the asset adapter still applies the adapter-scale per model.  (files updated: `vehicleAssetConfig.mjs`, `renderer.ts`, `vehicleAssetAdapter.ts`) 
- Widen all Tirana Racing Royal ribbons from `16` to `20` metres and apply the same width to the generated Grand route. (files updated: `legacySimulation.mjs`, `raceCatalog.mjs`) 
- Add `circuitSides(points, halfWidth)` to compute miter-joined left/right boundaries for closed circuits and use it to build the road mesh, curbs and tyre placements so edges meet precisely at corners. (files updated: `trackEdges.mjs`, `trackEdges.d.mts`, `renderer.ts`) 
- Update vehicle-fitting and renderer logic so tires, curbs and kart visuals are placed and oriented from the precise joined sides; keep physics and gameplay unchanged. 
- Tests and test expectations updated for the new width and vehicle scale; updated regression coverage verifies track width, finite joined boundaries, corner joins and vehicle fitting. (tests: `test/racing-precision.test.mjs`, `test/racingMilitaryVehicles.test.mjs`) 

### Testing
- Ran unit tests with `node --test test/racing-precision.test.mjs test/racingMilitaryVehicles.test.mjs` and all included subtests passed locally.
- Performed a production build `npm run build` in `webapp` and verified build completed successfully.
- Ran `git diff --check` to ensure no whitespace or diff errors; clean.
- Launched a local preview (`vite preview`) and captured a portrait screenshot (390×844) of the Racing Royal standalone page for visual verification.
- Final changes were committed; PR prepared as: `Improve Racing Royal vehicle scale and circuit precision`.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6aa3938ae3dc832998baf05f1ab70ad0)
