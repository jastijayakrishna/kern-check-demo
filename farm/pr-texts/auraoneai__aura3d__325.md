# [QR-14] Gravity Post v2 shell: orbit rig, scene, evidence, specs (T2.1-T2.6)

## Summary
Gravity Post v2 shell (PRD-14 T2.1–T2.6): §6.9.13 orbit rig + one-scene system board, evidence + scenarios + browser spec, stacked on wave-3 day-0.

- `scene/world.ts` — the full union scene built once: sol disc + corona, 5 NASA well planets (typed `model(...)` + opaque rim shells + hairline orbit guides), 6 stations with capture-pulse rings + dock gates, courier-skiff pod with thrust cone + 7 trail streaks, 30 prediction beads + 48 actual-path beads, 8 dock sparks, 6 flyby drones, the Rust→Gale freightway (panels/lamps/hazard markers) and 24 orbital dust motes. Contract switches only re-pose pod/pulses → `loading.sceneSwaps === 0` (§7.2.1).
- `scene/camera.ts` — `gravity-post.orbit` rig in the direction's [40,60] fov band: elevated oblique on the whole board with a slow 0.0044 rad/s drift; the target borrows 32% of the pod position only while a flight is live so launches stay readable.
- `scene/lighting.ts` — 5800K shadowed sol key + exactly one practical (`aquaria-dock`, matching `direction.lighting.practicals = 1`) + vendored `data_galaxy_deep_space_1k.hdr` IBL @0.4. No ambient/fill.
- `boot.ts` — Rapier witness world (`engineGame.collisionWorld`): a dynamic pod proxy is driven by the authored integrator so static dock-sensor spheres fire real overlap events into `evaluateCapture`; keyboard aim steering + Enter launches (autopilot runs the same `launchKeyboardAim` path so `pod.launchedBy==="keyboard"` stays honest under autorun); pointer drag launches with live prediction beads; retained vs-actual trajectory comparison feeds `prediction.maxDivergence`; station pulses breathe toward capture; dirty-checked sci-fi-telemetry HUD; `visibilitychange` pause; aim-drag touch preset.
- Evidence (§7.2.1): `pod.state` normalizes `coasting→"in-flight"`, `ready→"aiming"`; `pod.launchedBy` is `"pointer" | "keyboard" | "autopilot"`; plus prediction divergence, flyby beats, dock event log, backend/bodyCount, `appliedLook` parity. Scenarios `delivery-1`/`hazard-mail`/`dock-approach` use real `loadContract`/`launchKeyboardAim` action hooks only.
- Tests: 5 orbit-rig unit tests (fov band, board containment cone, in-flight target borrow, drift rate, reset) + playwright spec covering autorun/kbd/touch playthroughs, required-condition deadline, canvasBlankCheck, pause-on-hide, appliedLook parity.

## Verify
- `tsc --noEmit` app + root build config: 0 errors
- `vitest tests/qr/prd14/gravity-post/`: 5/5 pass
- `vite build` in `apps/showcase-gravity-post`: green
- `eslint` on touched paths: clean

NOT RUN: browser spec + runtime art audit — remote-only in the lane workflow on macos-14.

Link to Devin session: https://app.devin.ai/sessions/af5743a23d7c4950bccd20d6837af047
Open in Devin Desktop: https://app.devin.ai/desktop/session/af5743a23d7c4950bccd20d6837af047?variant=devin
