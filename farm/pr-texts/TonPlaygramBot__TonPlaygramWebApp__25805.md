# Fix Snooker Royal shot release, player camera/scale, and bridge-hand safety

### Motivation
- Make Snooker Royal use the same reliable shot/strike flow as Pool Royale so mobile power releases cannot reset before cue impact and the cue-stroke animation remains consistent.
- Pull the player perspective camera in a bit for tighter portrait framing so the table and cue feel closer on phones.
- Ensure characters visually scale to be 25% taller than the selected cue and prevent the left (bridge) hand from overlapping balls or illegally penetrating cushions.
- Provide situational bridge finger poses (open / compact / raised) so the planted hand adapts to available shooting space.

### Description
- Synchronized the internal shot lock immediately when the Three.js shot state changes by assigning `shootingRef.current = value` inside `setShootingState` so UI input cannot race the visual impact. (edited `webapp/src/pages/Games/SnookerRoyal.jsx`)
- Tightened portrait camera framing by adjusting `PLAYER_CAMERA_DISTANCE_FACTOR` and `STANDING_VIEW_DISTANCE_SCALE` for a closer player perspective. (edited `webapp/src/pages/Games/SnookerRoyal.jsx`)
- Make player characters sized relative to the cue by adding `targetHeight: cueLen * 1.25` when creating `PoolRoyalHumanPlayers` so characters are 25% taller than the cue. (edited `webapp/src/pages/Games/SnookerRoyal.jsx`)
- Add `poolRoyalBridgeSafety.ts` implementing `resolveSafeBridgeAnchor` which searches nearby candidate bridge positions behind the cue ball, avoids ball overlap, and clamps the planted-hand footprint inside table bounds while permitting cushion contact. (added `webapp/src/pages/Games/shared/poolRoyalBridgeSafety.ts`)
- Wire live scene information into the pose solver by passing `bridgeObstacles` (active balls) and `bridgeBounds` into `PoolRoyalHumanPlayers.update`, then using `resolveSafeBridgeAnchor` to pick a safe bridge anchor and a bridge `style`. (edited `webapp/src/pages/Games/shared/PoolRoyalHumanPlayers.ts`)
- Extend the bridge-finger solver to accept a `style` and apply alternative finger spreads for `open`, `compact`, and `raised` bridge poses so fingers adapt to the chosen anchor. (edited `webapp/src/pages/Games/shared/poolRoyalPlayerPose.ts`)
- Call `refinePoolRoyalBridge` with the chosen `bridgeStyle` so the visible hand pose matches the selected safety behavior. (edited `webapp/src/pages/Games/shared/PoolRoyalHumanPlayers.ts`)
- Add focused unit tests covering normal placement, obstacle avoidance, and cushion-clamping behavior for `resolveSafeBridgeAnchor`. (added `webapp/src/pages/Games/shared/poolRoyalBridgeSafety.test.ts`)

### Testing
- Ran the focused unit tests with `npx vitest run src/pages/Games/shared/poolRoyalBridgeSafety.test.ts`, which succeeded: `3 tests passed`.
- Ran `npx eslint --no-ignore --no-warn-ignored` on the changed files; linter run completed (no rule failures reported for the touched files in the run).
- Built production assets with `npm run build`; the Vite production build completed successfully.
- Ran `npx tsc --noEmit -p tsconfig.json` which reported pre-existing repository-wide typing errors unrelated to these changes; the new code compiles in the runtime build and the focused unit tests pass despite the unrelated TypeScript noise.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6aa2815582bc8329a95cbc2a71a54d92)
