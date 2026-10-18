# spike: Module Map — import-composition lens (zoomable containment hierarchy)

## Spike: Module Map — import-composition lens

Reinvents "service composition" around the **import graph**. A new 4th renderer lens (`viewMode:
"modules"`, **"Module map"**) rendered as **one zoomable containment hierarchy**: level 0 is the
package overview, double-click any package/directory to **zoom in** one level, breadcrumb to **zoom
out**. Each level shows the focus's children (sub-dirs as group cards, files as file cards) wired by
the import graph *folded to that level*. The shipped SOLID "Service composition" lens is untouched.

> 📄 Full design, file map, Autopilot extraction recipe & follow-ups: **`docs/module-map-spike.md`**

### Design (final)
1. **Real `imports` edges** from a new TS-extractor pass — no schema change (`imports` already in the
   vocabulary), always-on so `meridian web` gets it free.
2. **Containment-zoom navigation**, not blast-radius: a single `moduleFocus` state; double-click to
   descend, `ancestorsOf` breadcrumb to ascend; single-child levels auto-collapse (`app → src`).
3. **Package fold** — extractor tags `npm-package` roots; level 0 folds files to their owning package.
4. **Depth slider → paint-only selection radius** (highlight a node's N-hop import neighbourhood);
   hidden until a node is selected.
5. **Per-level ELK `layered` layout**; import graph built once and cached.

> Evolution: began as an entry-rooted depth-ring blast-radius (`18dc79a`); a package fold (`09f9c8c`)
> and overview (`386a5fe`) followed; the final rewrite (`d43ac44`) unified everything into the
> containment hierarchy and **removed** the mode toggle, the ring layout, and the blast-radius drill.

### Validated on a real monorepo
Drove it on `UiPath/Autopilot`: correct extraction needs `--lang typescript` + the source-mapping
`tsconfig.typecheck.json`. Produces the 18-package family (389 cross-package edges) and, with a
combined tsconfig, the full TS surface incl. `aria/app` (2,861 files; `aria/app` 1,914). Deep-dive
descends `Repository › aria › app › src` → 24 sub-dir groups / 221 import edges, and keeps going.

### Status
- [x] Extractor: real `imports` edges + `npm-package` tags + goldens
- [x] Renderer: `deriveLevel` containment fold, per-level ELK layout, cached import graph, paint radius
- [x] Zoom-in/out + breadcrumb + chain-collapse; toggle & ring layout removed
- [x] 144 renderer tests green; build + `copy-renderer` green
- [x] Validated headless on shopfront, the meridian renderer, and Autopilot
- [ ] Deferred: cross-focus **boundary ghost-stubs** (edges leaving the focus reappear on zoom-out)

### How to run
```bash
pnpm build && pnpm --filter @meridian/cli copy-renderer
node packages/cli/dist/bin.js generate examples/shopfront -o /tmp/mm-shopfront.json
node packages/cli/dist/bin.js view /tmp/mm-shopfront.json   # → "Module map" lens; double-click to zoom
```

🤖 Generated with [Claude Code](https://claude.com/claude-code)

