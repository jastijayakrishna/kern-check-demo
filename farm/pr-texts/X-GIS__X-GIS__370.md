# fix(tiler): full-fidelity low-zoom geojsonvt tiles so enclosed seas do not drop (#360 F2)

Fixes #369. Part of #360 — the **enclosed-sea facet (F2)**. (Polar facet F1 stays on #362.)

## Bug (oracle-verified — actual real-GPU pixels + raw point-in-polygon, controls valid)
`ocean_land` (layer ocean=`ne_110m_ocean` fill-sky-900, layer land=emerald). At low zoom the **Mediterranean, Black Sea, Caspian, Gulf-of-Guinea, and a large NE-Atlantic/Arctic tile block render BLACK** — land renders correctly (green), only the OCEAN polygon is dropped. Raw PIP confirms those lonlats are ocean (sky-900 expected); clear color is black (`background-pass.ts`); so black = **dropped ocean geometry** = data-faithfulness violation.

## Root cause (GPU-free tolerance bisect, controls valid)
Active tiler = in-repo fork `compiler/src/tiler/geojsonvt` (npm geojson-vt is test/bench only). Probe via the real `getTile` path: **Med(18,34)@z1 = COVERED at `tolerance:0`, BLACK at `tolerance:6`** (the prod default); z≥2 covered either way; open-ocean control covered throughout. → the per-zoom Douglas-Peucker tolerance (`tile.ts`) at z0–3 straightens the world-ocean ring's narrow inlets (the ring chord cuts across the inlet mouth → enclosed sea excluded → clear/black). The NE-Atlantic block + Guinea are the same mechanism.

## Fix (one threshold, surgical)
`geojsonvt/tile.ts`: `tolerance = 0` for `z <= 3` (world-zoom full fidelity), else the zoom-scaled tolerance (unchanged), maxZoom already 0. At the **consumer threshold**, not the DP algorithm — detail zooms byte-identical. Vertex cost at world zoom trivial (single-digit-thousands worldwide). Intentional divergence from upstream geojson-vt at low zoom. **OFM-Bright (PMTiles/raster) doesn't use geojsonvt → unaffected.**

## Verification
- **No-GPU gate** `ocean-low-zoom-coverage.test.ts` (fail-before/pass-after): Med/Black/Caspian/sub-85°-Arctic COVERED at z0–3; open-ocean control covered.
- **Real-GPU oracle** (ocean_land, before→after, same cameras, controls valid): every black enclosed sea + the NE block now **sky-900**; land green; **no new seam**; console clean (no NaN/arena-oom/frame-validation).
- 14/14 geojsonvt + 187 tiler + arch ratchet green; `bun run build` typecheck exit 0.

Judged against the formal render-output oracle (`.omc/research/render-output-oracle.md`): actual = expected (ocean→sky-900). F1 (polar ±85–90° band + seam + pole-fan) is structural (projectY [0,1] clamp) and remains for #362 — NOT in this PR.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
