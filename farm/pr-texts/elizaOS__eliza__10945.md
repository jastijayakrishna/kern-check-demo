# fix(core): give simile-named candidate actions the exact-hint floor so the real action gets exposed

## Problem

Stage-1 (the response handler) routinely names an action by one of its declared **similes** rather than its canonical name — observed live: "generate an image of a corgi" was routed to the `media` context with `candidateActionNames: ["GENERATE_IMAGE"]`, but the registered parent action is `GENERATE_MEDIA` (`GENERATE_IMAGE` is one of its similes).

In `retrieveActions`, candidate names only feed regex/keyword scoring — the exact-hint score floor (`scoreExactHints`) matches **canonical parent names only**. So the real action earned no exact-hint floor, was displaced out of the tier cut by higher-scoring generic actions, and was never exposed to the planner. The planner then saw the simile string with no runnable tool behind it and answered:

> "I can't generate images this turn — no image-generation tool is exposed in my current action set."

…for an action that was registered and in-context. (Diagnosed live on elizaOS/eliza#10819; role gates ruled out — the sender was ADMIN.)

## Fix

`resolveCandidateToParentNames(parents, candidate)`: resolve each model-emitted candidate to the canonical parent name(s) it refers to, matching the parent's own name **or any declared simile**, and feed the result into the existing `parentActionHints` set so it earns the exact-hint score floor. Returns `[]` for a candidate that names no registered parent, so a hallucinated action never fabricates an exposure.

No new scoring stage, no behavior change for canonical-name candidates — just the simile form now resolves to the same floor the canonical form already got.

## Tests

- New regression test: catalog with `GENERATE_MEDIA` (similes `GENERATE_IMAGE`/`CREATE_IMAGE`/`GENERATE_VIDEO`) + candidate `GENERATE_IMAGE` → `GENERATE_MEDIA` ranks first with `score: 1, matchedBy: ["exact"]`.
- Full `action-retrieval` + `action-tiering` suites green on this branch (3 files / 37 tests).
- Typecheck clean.

Part of elizaOS/eliza#10819 (exposure robustness half; the capability-wiring half — cloud IMAGE handler suppression — is tracked separately there).

🤖 Generated with [Claude Code](https://claude.com/claude-code)

