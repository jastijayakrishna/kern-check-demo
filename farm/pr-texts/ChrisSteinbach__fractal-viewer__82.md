# Extract shared flame/solid render-session shape from main.ts (fr-2jk)

## Summary

`main.ts`'s `enterFlameMode`/`exitFlameMode` and `enterSolidMode`/`exitSolidMode` were near-twins — the solid comment literally said it "mirrors the flame session above exactly". Both carried the same **enter/exit/terminate** choreography, the same **hasImage/hasTexture first-frame gate**, the same **defensive double-entry terminate**, and the same **error→exit** fallback, differing only in their genuine specifics.

This extracts that shared skeleton into **`RenderSession<C>`** (`render-session.ts`), the optional third tier of fr-w8t (after `edit-session` and `four-d-view`).

## What moved

`RenderSession<C>` owns the session **handle** (`{ post, terminate }`), the **first-frame gate** (`hasFirstFrame` / `markFirstFrame`), and the **enter/exit ordering** (defensive terminate → clear notes → reset progress → reset gate → start → activate; and terminate → reset gate → clear notes → deactivate).

The genuine per-mode differences are injected via five deps (`start`, `clearNotes`, `resetProgress`, `activate`, `deactivate`):
- **Flame** injects its WebGPU host choice + `SharedArrayBuffer` transport + the `start` payload, and freezes the camera.
- **Solid** injects its live-camera path + the transform-selection drop (its lens has no guide box).

Both worker handles now share one `{ post, terminate }` shape — the flame `FlameSessionHost` already was one, and the solid path wraps its voxel `Worker` in one. `start` posts its own `start` command through the freshly-built handle (typed, so both payloads stay type-checked), since `RenderSession` only stores the returned handle afterwards.

## Behavior

Pure refactor — line-by-line behavior-preserving. The enter/exit step ordering is identical to the originals; only independent bookkeeping (the gate bool, notes, `flameShared`, the active flag) was regrouped into the injected hooks.

## Tests

`render-session.ts` is a pure module (no DOM/Three.js/worker globals), unit-tested with fakes like `EditSession`/`FourDView` — **11 new tests** covering enter/exit ordering, the defensive terminate (and its absence on first enter), the first-frame-gate lifecycle, and `post` forwarding (before/during/after a session).

## Quality gates

- `npm test` — lint clean; **1245 tests pass** (37 files, +11 new)
- `npm run build` — passes

## Browser verification (end-to-end)

Driven in a real browser (Playwright + Chromium new-headless with SwiftShader WebGL) against `npm run dev` — **16/16 checks passed**:

- **Boot**: WebGL context up, 100k-point cloud generated, cross-origin isolated (flame SAB transport path live).
- **Flame**: `enter()` flips the UI (`activate`) → worker's first frame flips the gate (`markFirstFrame`) → an exposure change forwards through `controlEffects.postFlame → flameSession.post` with no error → `exit()` restores the explorer (`deactivate` + terminate).
- **Solid**: `enter()` flips the UI (with the selection drop) → first grid flips the gate → a **resolution change fires `restartSolidRender → solidSession.enter()` over a running session = the defensive double-entry terminate**, which stayed active and kept converging with no error → `exit()` restores the explorer.
- No unexpected console errors, no uncaught page errors throughout.

Closes fr-2jk.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

