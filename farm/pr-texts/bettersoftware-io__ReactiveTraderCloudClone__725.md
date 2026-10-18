# GenUI × Dockview: DEFAULT_LAYOUT_ENGINE flips to dockview (spec deliverable 2)

The one-commit-revertible flip: `DEFAULT_LAYOUT_ENGINE` `"inhouse"` → `"dockview"`, per [the spec](docs/superpowers/specs/2026-09-12-genui-dockview-docking-and-default-flip-design.md) §6, now that Jarvis docking works under Dockview (PR #724). Users with a stored preference are untouched; the in-house engine stays fully supported.

**In the sweep** (single commit, the designed revert point):
- Domain constant + `PreferencesPortContract` rewrites (writes flipped to the now-non-default `inhouse` so the assertions stay meaningful); RN pins `"inhouse"` literally (no Dockview bridge there).
- **Both engines are now static imports** — the old lazy split deferred a measured 3.8 KB gzip while arming the blank-first-frame golden class; `Suspense`/`lazy`/test-flush machinery deleted.
- The Dockview bridges mirror in-house's root `data-maximized` witness, making `waitPanelMaximized` engine-agnostic — the flagship narrator-drive e2e journey now runs under the default engine; the dock journey's opening switch inverted per the Task-10 marker.
- Test harness/visual fakes pin `"inhouse"` as their unseeded default (deliberate + documented: keeps the golden matrix and the 841-case contract baseline stable; scenarios seed the engine explicitly per twin) — hence zero golden churn in this PR (verified: `prefs/` renders identically).
- Docs: CLAUDE.md, ADR-002 (three dated clauses + As-implemented bullet), STATUS.md, architecture §06/§08/§14, layout-dockview README.

**Gates:** full unit suites, both contract suites (841/841 each) + coverage gates, typecheck 45/45, full e2e green both clients (flagship + dock journeys under the new default), doc-links clean.

Reverting this PR restores the in-house default wholesale.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01NgLoerw3XnYAHdX3LHg9sB
