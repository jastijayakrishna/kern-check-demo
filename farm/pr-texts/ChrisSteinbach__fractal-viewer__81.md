# Extract main.ts camera tween into a tested module (fr-dys)

Extract the auto-fit camera glide (fr-0b8) out of `main.ts`'s closure into a new injected-dependency module, `camera-tween.ts`, so the pure interpolation is unit-tested without a browser. This is the optional third tier of fr-w8t, matching the `edit-session.ts` / `four-d-view.ts` extractions.

## What moved
`camera-tween.ts` now owns:
- `fourDFramingBounds` — the rotation-invariant 4D framing box (moved verbatim).
- `CAMERA_TWEEN_MS` and a `CameraTween` class that mutates an injected `OrbitCamera` in place:
  - `fitToBounds(bounds, framing)` — reduced-motion snap vs. armed glide.
  - `advance()` — smoothstep interpolation of target + radius, clears at `t >= 1`.
  - `cancel()` — drop an in-flight glide on the next user gesture.

The clock (`now`) and the reduced-motion probe are **injected** so tests drive it with a fake clock, exactly like `edit-session.ts`'s `schedule`. The `fov`/`aspect` framing is passed **per call** because it changes on every window resize (`main.ts` reads it off `scene.camera`).

## What stayed
`main.ts` keeps only `fitCameraToAttractor` — the impure decision of *which* bounds to frame (it reads the `viewIs4D` / `lastResult` / `fourDResult` closure vars) — now delegating the glide to the module. This honors the issue's "coupled only to `OrbitCamera` + camera fov/aspect + `now()`" constraint for the extracted module. `main.ts` is **−75 lines net**.

## Tests
12 new Vitest cases cover the documented invariants:
- `fourDFramingBounds` half-diagonal == radius, centers on xyz (ignores w), fills `minR`/`maxR`.
- reduced motion snaps instantly with no glide left in flight.
- a glide reaches the fit exactly at `t >= 1` then clears; is at the midpoint at half duration; `advance`/`cancel` are no-ops when idle.

Also fixes `smoothstep`'s now-stale doc pointer in `orbit.ts` (it named `main.ts`'s `animate()`).

Behavior-preserving verbatim port. `npm test` (lint + 1234 tests) + `npm run build` green.

Closes fr-dys.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01NSkJ5s5ccgWtFE7yownwRF
