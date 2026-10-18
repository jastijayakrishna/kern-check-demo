# feat(design-studio): edge grips stretch one axis, and the model gains an ellipse

# feat(design-studio): edge grips stretch one axis, and the model gains an ellipse

A layered carve is built from nested rectangles, and "make this one 20 mm wider without
making it taller" had no gesture at all — only two typed numbers in the inspector. The
selection carried four corner grips, all uniform scales, because a per-axis stretch had
nowhere to put its result: `SketchCircle` holds a single radius, so widening a circle
would have deformed it into something the model could not represent.

So this adds both halves: the grips, and the entity arm that makes them honest.

## What you get

Eight grips instead of four. The corners still scale uniformly. The four new edge grips
stretch their own axis and hold the other — and report a factor of exactly `1` on the held
axis, so the dimension you did not touch survives rounding as well as intent.

## Per-axis exactness, stated per kind

A stretch is not exact for every shape, so each kind is handled by what it can honestly
represent rather than by one rule that quietly rounds:

| kind | under a one-axis stretch |
|---|---|
| rect (square corners), line, path | exact |
| circle | becomes an **ellipse** — exact, and the reason the new arm exists |
| ellipse | stays an ellipse — exact |
| rect (rounded) | corner radius follows the **smaller** factor; a true stretch makes the corners elliptical, which `RectangleSpec` cannot hold |
| arc | **baked to a path** at the sampled tolerance — a stretched arc is an elliptical arc, which neither this model nor `G2`/`G3` can express |

`stretchEntities` is a separate operation from `scaleEntities` and delegates to it whenever
the two factors are equal, so a corner grip can never quietly bake an arc.

`SketchEllipse` is axis-aligned with independent radii. A circle is **not** re-expressed as
an equal-axis ellipse: a circle drawn as a circle keeps its radius, its diameter field, and
its exact arcs. There is deliberately no ellipse drawing tool — the arm exists to make the
stretch honest, and a tool for it is separable work.

The scene needed no change: an ellipse materializes through the same `EllipseSpec` carrier
a circle already used, so the applied part stays re-editable on the main canvas and `.lf2`
gains no new shape.

Governed by **ADR-272 Amendment 4**, added in this PR.

## Verified

- Full vitest suite, typecheck, eslint, prettier, the ADR-number gate and the barrel-export
  ratchet — all clean (counts in the PR checks).
- 11 new cases in `stretch-entities.test.ts` pinning each kind's answer, reversibility, and
  the no-op returns; 6 new in `design-handles.test.ts` for edge geometry and the
  exactly-1 held axis; 2 new in `design-resize-session.test.ts` for the gesture end to end.
- **Live in a real browser**, driving real `PointerEvent`s on the 3D viewport:
  - Rectangle, east grip dragged to ×1.3: width `159.70450164769773` → `207.61584623326232`,
    height `119.77837134996837` → `119.77837134996837`, origin unchanged to the last digit.
    Exact, no drift.
  - Circle r `72.11102550927978`, east grip: became `kind: "ellipse"` with
    `radiusXMm 101.07`, `radiusYMm 72.11102550927978` — the held axis bit-identical. Same
    entity id, same layer. The inspector title changed Circle → Ellipse.
  - The ellipse survived a page reload and the layers panel counted it.

## NOT verified

- No hardware cut (no machine available).
- WebGL pixels not screenshot-diffed — the harness pane does not composite; DOM, store and
  storage reads stand in. **Nobody has looked at the eight grips on screen.**
- 2D-canvas grips are still not painted at all — pre-existing (the 3D viewport is the
  default surface and is the only one that draws them), unchanged by this PR, and the edge
  grips inherit it.
- Curve caveat found while verifying: a grip anchors to the selection's **sampled** bounds,
  which for a circle sit ~0.049 mm inside the true outline (85 segments, just under the
  0.05 mm chord tolerance). The held edge therefore drifts by that inset times
