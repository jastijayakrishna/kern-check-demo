# feat: IPC ports, channel nodes, and meridian link — static cross-system graphs (ADR 0002)

## The idea

Static analysis can't follow a call across a process boundary — but **both ends are statically visible, and they share a channel key** (the IPC channel string, the route path). So IPC becomes a *join*: detect typed **ports** per repo, materialize **channel pseudo-nodes**, and `meridian link` joins separately generated artifacts into one system graph. Fully static — **no runtime, no telemetry, no manual marking**. Documented as [ADR 0002](knowledge/adr/0002-ipc-ports-and-linking.md).

## Layer 1 — ports & channels (per repo)

- Extractors report `Port { nodeId, direction, protocol, channel, label, callSite }` via `extensions.ports` — the ADR-0001 escape hatch, **zero schema change**.
- **Matcher registry** (TS v1): electron `ipcRenderer.send/invoke` / `ipcMain.on/handle` / `webContents.send`; `fetch`/axios exits (method + path, origin/query stripped); express route registrations. Matching is textual on import names, so cloned repos work without `node_modules`.
- **Honesty rule:** the channel is read only from string literals — a dynamic channel is reported with `channel: null`, never guessed.
- Matched ends join through a channel node: `sender —sends→ [ipc:electron/notes:load] —handles→ handler`. A **one-ended channel stays dangling — that IS the finding** ("someone sends and nobody listens").

## Layer 2 — `meridian link` (cross-repo)

```
meridian link web.graph.json api.graph.json -o system.graph.json
  linked      2 systems through 5 channel(s)
  joins       3 cross-system, 1 via route templates
  dangling    2 channel(s) have only one side — nobody answers
```

- Each source becomes a `sys:<name>` frame; node ids are **namespaced** (`ts:src/x.ts` → `ts:orders-api/src/x.ts`) so identical paths never collide. `ext:`/`unresolved:`/`ipc:` ids deliberately stay **shared** — the space systems meet in.
- Concrete HTTP exits unify onto entry **route templates** (`GET /api/orders/123` → `GET /api/orders/:id`), most-specific-first; ambiguous ties honestly match nothing.
- The output is a plain `GraphArtifact` — `view`, `coverage`, and every consumer work on it unchanged.

## Fixtures (all with deliberate dangling + dynamic cases)

- `examples/desktop-notes` — electron main+renderer in one repo: 5 channels incl. an unanswered `notes:export` and a dynamic `send(channel)`.
- `examples/checkout-web` + `examples/orders-api` — the cross-repo pair: fetch exits joining express routes, plus a dangling exit (`/api/recommendations`) and a dangling route (`DELETE`).

## Verification

- 363 unit tests (24 new: channel grammar, materialization, template matching, linker namespacing/joins/re-linking, matcher goldens over the real fixtures) + 5 headless-Chromium e2e; typecheck clean.
- Real CLI runs shown above; the linked artifact validates **strict** and renders in `view` with zero console errors (both systems' modules visible).

## Scope notes / follow-ups

- Renderer v1 is minimal by design: kind accents (gold channels, steel system frames), gold IPC wires, and `sends`/`handles` in the behavioural edge set. **Drawing channel wires between system frames on the Service-composition view is the natural follow-up** (composition charts class/module coupling only today).
- `link` does not remap per-repo `extensions.logicFlow` (the logic view stays a per-repo lens).
- Next evidence tiers per ADR 0002 (docker-compose env resolution, contract files, package-registry joins) raise `edge.confidence` on the same edges without shape changes.

Also removes `undefined/logic-cov.png`, a stray screenshot accidentally committed during PR #53 (my probe script bug — sorry!).


The logic (exactly what the code does)

For whatever you're currently rooted at:

1. Count the surviving units in its subtree.
2. ≤ 120 units → draw the real unit scorecards (classes/modules — the actual code).
3. > 120 → draw one card per package one directory level below the root; each card rolls up all units beneath it. IPC/coupl
