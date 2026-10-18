# Pin a locked project's orientation to the device

## Summary

A locked project's orientation was only a *layout* choice: the interface still reflowed on rotation (the landscape rules were `@media (orientation: landscape)`), and only landscape locks forced the export shape. Turning the phone mid-project therefore changed both the interface and the film. Now a locked project is pinned, both ways — like a native camera app.

Three parts:

**1. The pin itself.** `screen.orientation.lock()` stays as the best path, but it only exists in installed Android PWAs and rejects silently everywhere else (every iOS browser), which is why the bug was visible at all. So the shell counter-rotates the OS's auto-rotate away — new `lib/shell-rotation.ts` picks the direction from the lock, the viewport shape, and `screen.orientation.angle`, and `#root` gets a CSS transform with swapped dimensions:

```css
html[data-rotate='ccw'] #root {
  position: fixed; width: 100dvh; height: 100dvw;
  transform-origin: 0 0;
  transform: translateY(100dvh) rotate(-90deg);
}
```

The locked layout keeps its own box (a portrait film held sideways still lays out 412×839) and simply appears sideways, with the existing mismatch hint asking for a turn. The transform also makes `#root` the containing block for its `position: fixed` descendants, so sheets and overlays come along.

Landscape layout rules move off the viewport onto the shell's resulting shape — `@media (orientation: landscape) { .orientation-landscape … }` → `html[data-shell='wide'] .orientation-landscape …` — so a pinned landscape project keeps its rail-and-stage layout while held upright. `data-shell` now tracks the shape the shell *ended up* with (`landscape && (rotated || landscapeViewport)`), which keeps the desktop exemption intact: a fine-pointer window isn't something you turn, so it is never pinned and a narrow window keeps the phone column.

**2. Gestures.** Pointer events keep arriving in viewport coordinates, so every gesture that reads `clientX/clientY` (drag-to-zoom, timeline scroll/reorder/autoscroll/fling, trim, audio, image-duration handles) maps through the shell's own axes:

```ts
contentX({clientX, clientY}) // rotation -90 → -clientY
contentExtentX(rect)         // rotation -90 → { start: -rect.bottom, ... }
```

These are direction- and difference-preserving, not absolute (no valid viewport origin) — fine because all of these gestures were already relative. Verified in a real pinned Chromium: dragging the trim end handle toward the strip's start goes 30.8s → 20.3s kept.

**3. Exports and storage.** `pickOutputSize` already forced either orientation; only landscape was ever passed. Portrait locks are now stored (they used to be deleted, indistinguishable from "never locked") so the export can force them:

```diff
-const orientation = effectiveOrientation() === 'landscape' ? 'landscape' : undefined
+const orientation = project?.orientation
```

Absent still means "never locked" — legacy projects and desktop/screen recordings keep following their clips rather than suddenly center-cropping. Backups carry either explicit lock (a landscape lock is still dropped when importing without Plus).

Unit + e2e cover the pinned box, both directions, and the new portrait persistence.

**Drive-by, needed for green CI:** the landscape home layout was a coin flip in dev — `main.tsx` loads `global.css` and `home.css` with `Promise.all`, so whichever sheet lands last wins between `.screen { display: flex }` and `.home-screen { display: grid }` (equal specificity). `home.spec.ts` failed under load on `main` too; the landscape rule is now `.screen.home-screen`.


Link to Devin session: https://app.devin.ai/sessions/772ca74c8cb3475b9e084e2b7484ab40
Requested by: @kentcdodds
