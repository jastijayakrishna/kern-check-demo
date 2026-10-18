# feat: Logic Flow sub-views — honest branches, async semantics, four projections

## What

The Logic Flow tab gains **four sub-tabs** — Exec graph / Metro / Blocks / Timeline — all projections of the **same base**: one FlowStep tree, one navigation state (root, drill trail, container dives, by-target selection). Switching tabs is a pure presentation switch.

It also fixes the two long-standing honesty gaps:

- **An `if` whose then-path returns no longer pretends the flow "continues as if nothing happened".** Returns/throws are charted as exit steps; terminated paths dead-end at red caps and never rejoin; the branch grows a synthesized `else` / `no match` pin so the implicit else is a first-class wire.
- **Awaited vs fire-and-forget calls are now distinguishable.** `await foo()` wears a ⏱ badge (latent — execution holds); `void foo()` / un-awaited Promise statements / dropped `.then` chains wear ⤳ (detached — result dropped, outlives the flow).

## Layers

- **core** — `FlowStep` gains `exit` steps + `awaited`/`detached` call flags; branch semantics become structured (`branchKind`, per-path `role`) with fallback helpers (`branchKindOf`, `pathRole`, `branchCoversAllCases`, `syntheticFallThroughLabel`, `tryArms`, `exitLabel`, `pathTerminates`) so nothing sniffs display labels (`case catchAll:` no longer seals a switch). Pure `extensions.logicFlow` payload — no schema bump.
- **extractor-typescript** — emits exits (expression calls first), roles/branchKind, and the async flags via a new `call-annotations` module (Promise-ness memoized per callee symbol; a `.then` chain is ONE hand-off).
- **renderer** — exec-graph derive upgraded (no reconverging terminated paths, synthesized fall-through pin, conditional EXIT cap, dead-code drop, badges, hot minimap caps); three new pure-derive projections + views (`metroLayout`, `blocksModel`, `timelineModel`, `components/logicviews/*`); one shared palette (`FLOW_COLORS`); sub-tab strip, `logicView` store field, `lview` URL param (replaceState).

## Verification

- 311 tests green (core 61, extractor 58, renderer 192), full `pnpm typecheck`.
- Driven live end-to-end: `generate` on an async demo fixture → `view` → Playwright screenshots of all four sub-tabs, zero console errors.
- Adversarial multi-angle review ran before commit; all 10 verified findings fixed in-branch (label-sniffing false positives, timeline try-return truncation, metro try/finally mislane, orphan dead-code nodes, minimap cast, dive-state parity, extractor checker cost, detached chain fan-out, palette/coverage-rule duplication, file-size convention).

## Screenshots

Four sub-tabs over the same `placeOrder` flow (guard return, try/catch, loop, awaits, void call, dropped `.then`): exec graph with red return caps + synthesized else pins; metro with termini/interchanges/fire-and-forget lanes; blocks with synthesized "otherwise" compartments + hand-off tray; timeline with suspend segments and background bars crossing the "function returns" line.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
