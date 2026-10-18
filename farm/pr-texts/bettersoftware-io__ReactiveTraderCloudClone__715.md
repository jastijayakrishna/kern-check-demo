# Dockview: stacked-tab chrome (Phase 2) — inactive title chips, tab seam, active seat

## What

Phase 2 of the Dockview-native features workstream ([spec](../blob/main/docs/superpowers/specs/2026-09-10-dockview-native-features-design.md), [plan](../blob/main/docs/superpowers/plans/2026-09-12-dockview-tab-stacks-phase2.md)): centre-drop tab stacks become first-class visually. **User-accepted 2026-09-12** via the skin acceptance strip (repo rule for new visible UI).

Before: an inactive stacked tab rendered its full interactive head slot — a 279px merged-header soup with no affordance. After: inactive tabs collapse to a muted title chip (hover brightens), a 1px card-border seam between tabs, a 2px accent seat under the active tab. Controls never duplicate (the group actions slot already belongs to the active panel).

## How

- Pure CSS in `dockview-hud.css` (both clients inherit), keyed on dockview's own `dv-active-tab`/`dv-inactive-tab` and guarded by `:has(.dv-tab + .dv-tab)` — single-tab bars are untouched **by selector construction and by measurement**: all 1823 pre-existing visual cells byte-identical on react AND solid.
- One bridge addition (both clients): the tab slot carries `data-panel-title`, since the framework-neutral stylesheet cannot address hashed CSS-module nodes; contract-witnessed (`panelTitleMarker`).
- New scenario `shell/layout-dockview-stacked` (10 skins) — the workstream's **first single-engine scenario**: stacks are layer-3 dockview-private by the disparity doctrine, so no in-house twin exists (justified in the scenario comment). Seeded via a version-2 stacked blob fixture, load-only (a restore correctly fires no save).
- No new tokens; no re-stack-on-expand (recorded YAGNI); no new e2e (Phase 1's drag suite already covers stacking mechanics).

## Verification

layout-dockview 101/101 · contract 833/833 both clients · full visual 1833/1833 react AND solid (re-verified after catching up over #713/#714's solid-bindings changes) · gauntlet 19/19. arm64 stacked goldens committed; x86 via `update-visual-goldens.yml` on this branch, `scenario_pattern=layout-dockview-stacked` (equal to the local `-g`).

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01Pj7VqoYEfNBSBdsad4BXSG
