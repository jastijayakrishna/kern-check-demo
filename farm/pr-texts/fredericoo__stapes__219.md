# feat(renderer): draw the mesh, light and interest windows under ?debug=1

TL;DR: Everything the play renderer decides is a window around a view nobody can see out of, so "is that window too wide" and "did that chunk arrive before I needed it" were questions answered with console logs and no picture attached. `?debug=1` pulls the camera back off the play square and draws all of them.

The play view is a fixed 23×23 square. Around it sit three windows of very different sizes, and none of them is visible from inside it:

- `visibleChunkKeys` builds geometry six cells past the camera, rounded out to whole chunks.
- `lightWindow` reads a level span and an apron further still.
- `app/net/interest.ts` keeps each client supplied with a square **176 cells across**.

## Before

![Play at its normal zoom: the view is exactly the 23×23 play square, and nothing on screen says what the renderer is keeping around it](https://github.com/user-attachments/assets/e519eead-95aa-4376-b88a-9b71dda02331)

## After

`/play?debug=1` — the same moment, camera pulled back three play squares. The white box is what a player actually sees; green is the chunk columns that exist as geometry; amber is how far the light bake reads; blue is every chunk column this client holds.

![The same scene at ×3: a white square in the middle marks the play view, a green grid of meshed chunk columns extends one column past it on every side, an amber rectangle marks the lighting window, a faint blue chunk grid covers the rest, and a panel top-left lists the counts in matching colours](https://github.com/user-attachments/assets/73de868c-add9-4572-acb6-3005f48b302d)

## What this changes

- **`?debug=1` on `/play` and `/online`** turns the view on. `[` and `]` take it between ×1 and ×8. There is no toggle and nothing in the UI mentions it.
- **`WorldView.playSquare` pins every window.** This is the whole mechanism. Each window is derived from `cameraWindow`, which *was* the drawn frame — so a zoomed-out camera grew them all with it and showed a bigger ordinary frame and nothing else. When `playSquare` is set, `cameraWindow` answers from the play square instead of the canvas. It is absent in every shipped frame and in the editor, where the camera is the view.
- **`isWithinView` measures the play square, not the drawn frame.** Zooming out never grants a target you could not hold or a name you could not read.
- **`fitViewport` takes the span it is fitting**, so the render scale stays a whole number at any zoom and the art stays on its pixel grid.
- **The outlines are culled to the drawn frame** (`columnTouches`). In single player the whole map counts as "sent", so without this the view would add a rectangle per chunk of the world and the draw-call number it reports would be mostly itself.
- **`app/render/debugColors.ts` is the one colour table**, shared by the outlines and the panel rows, so the panel *is* the legend and cannot drift from it.
- **Documented in `docs/notes.md`** and pointed at from the `renderer-perf` skill. Nowhere player-facing.

## Developer impact

`makeRectOutline` takes an optional trailing `opacity` (default `1`). The editor's call site is unchanged and draws exactly what it did.

`renderer.info.autoReset` is turned off while the view is on, because a frame here is three render passes and the live counter reports whichever went last. It is restored when the view is off.

## Out of scope

- Nothing about the windows themselves moved. This only draws them.
- The subscription boundary does not fit on screen at a readable zoom — it is 176 cells against a 23-cell view — so you have to go to ×7 or ×8 to see blue end. That is a fair picture of the ratio rather than something to fix here.

## Risk

- The debug view costs what it reports: a couple of hundred extra draw calls. Bounded by the cull, not free, and the `draws` row says so. **A frame time read in this mode is not a frame time for the shipped game.**
- `cameraWindow` is now the *play* window rather than the drawn one. Nothing reads the drawn frame except the debug view's own cu
