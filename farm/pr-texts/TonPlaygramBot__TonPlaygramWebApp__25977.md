# Improve seated human actor loading and simplify dice pickup sync in Ludo3D

### Motivation
- Reduce brittle, height-based actor normalization and simplify per-seat character loading with robust fallbacks for human and AI seats.
- Remove complex, tightly-coupled pose timeline in dice pickup to eliminate visible pickup lag and make hand-snapping deterministic and frame-friendly.

### Description
- Replace the previous actor normalization logic with a computed `baseScale` using `SEATED_HUMAN_TARGET_HEIGHT`, `SEATED_HUMAN_BASE_HEIGHT`, and `SEATED_HUMAN_VISUAL_SCALE_MULTIPLIER`, then apply `actor.scale.setScalar(baseScale)` when cloning seated human templates.
- Load a seat-specific `humanOption` per player and attempt `await loadSeatedHumanTemplate(renderer, humanOption)` with a fallback to the default template on error, then attach `actor`, save rig, apply idle pose, align feet, create `actionHelpers`, and push a simplified entry into `seatedHumanActorsRef.current`.
- Remove the per-entry `requestCharacter` replacement flow and the old height-driven `multiplyScalar` path, and replace logging text to be more specific when seated human actors fail to attach.
- Simplify `syncDiceToThrowHand` to accept an optional `duration` parameter, validate `dice`/`parent` presence, immediately snap the die to the hand helper to remove pickup lag, then lerp towards the hand over the specified duration using a smoother blend curve, and make the hook depend on `sampleHumanActionHelperPosition` and `sampleSeatedContactEffectorPosition`.
- Update `test/ludoBattleGameplay.test.mjs` expectations to match the new code paths and function signatures (e.g. `humanOption` loading, `actor.scale.setScalar`, `position.set`, and `syncDiceToThrowHand` signature/duration use).

### Testing
- Updated unit expectations in `test/ludoBattleGameplay.test.mjs` to reflect the new seated human loading and dice sync behavior and ran the file as part of the project test suite.
- Ran the project's automated test suite and the updated tests completed successfully.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6aa8d23da1a08329a51120caf04c6ab0)
