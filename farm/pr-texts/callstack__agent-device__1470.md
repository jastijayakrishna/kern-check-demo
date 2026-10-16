# feat(scripts): blast-radius query — dependents, owning gates, live-coverage owners (#1425)

## Summary

Closes #1425 (Track C, #1412). "Who depends on this and which tests own it" was four lookups
(depgraph, check-affected, iOS coverage manifest, ADR 0011 matrix); it is now one, and every part
of the answer is read from the existing source of truth rather than a second copy of it.

```sh
pnpm depgraph affected src/utils/exec.ts            # bounded text, ~0.5s
pnpm depgraph affected src/daemon/ref-frame.ts --json --limit 25
```

```
blast radius: src/utils/exec.ts  [zone utils, fan-in 81, fan-out 3]
dependents: 67 direct, 197 transitive (value edges; 14 type-only and 0 dynamic direct importers not counted)
  by zone: platforms 103, daemon-server 98, cli 14, utils 7, daemon-client 6, (root) 5, … (+7 more)
  direct:  src/cli/auth-session.ts, … (+57 more)
  widest:  src/platforms/android/adb-executor.ts (fan-in 40), … (+254 more)
gates for this set: format, lint, typecheck, layering, fallow, build, vitest-related, coverage, provider-integration
  run: pnpm check:affected --run
public commands whose handler chain reaches it (52): alert (snapshot), … (+42 more)
live scenario owners: test/integration/ios-simulator-e2e/coverage-manifest.ts is not in this tree …
guarantee-matrix rows implemented here (0):
```

Wiring, and the judgement calls that are not obvious from the code:

- **dependents** — reverse reachability over `scripts/depgraph/model.ts`'s **value** edges.
  Type-only and dynamic dependents are excluded from the counts (a type-only edge is free at
  runtime) but *reported separately* as `weakDirect`, because a pure vocabulary module
  (`src/contracts/*`) otherwise prints "0 dependents", which is the opposite of true.
- **gates** — `selectChecks({ changedFiles: [file, ...dependents.all] })`, i.e. check-affected's
  own model. The two cannot contradict each other by construction; the cross-check below confirms
  it on real diffs.
- **owning commands** — the daemon route table is parsed out of
  `src/daemon/request-handler-chain.ts` (`parseRouteEntries`) and joined with
  `DAEMON_COMMAND_DESCRIPTORS` × `PUBLIC_COMMANDS`; the chain closure follows value **and dynamic**
  edges, because every handler is loaded through `import()`. A route the table stops declaring
  throws and names the file to fix — a silently empty command list would read as "nothing owns
  this".
- **live scenario owners** — #1408's `IOS_SIMULATOR_E2E_COVERAGE` is consumed through the narrowest
  shape this lane needs (command → level/owner/assertion), loaded only if the manifest exists. It
  is not in main yet, so the query says so instead of implying no live coverage; verified against
  the #1408 branch's manifest, where the same run reports 49 owners for `ref-frame.ts`.
- **guarantee rows** — ADR 0011 cells whose `via` module path equals the file (prose `delegated`
  cells name no module by construction). `src/selectors/resolve.ts` → 5 rows across three paths.

Bounded by default (`--limit`, default 10, every list discloses `+N more`); `--json` is unbounded.
`scripts/depgraph/load.ts` is the now-shared graph read used by both the report and the query.

## CI scope

**No CI work added.** The only gate change is that `depgraph:test` also runs
`scripts/depgraph/affected.test.ts` inside the existing `Layering Guard` job: **+0.7s**
(`depgraph:test` 0.24s → 0.95s locally, 20 tests). No new workflow, job, permission, or lane.

## Validation

- `pnpm format:check && pnpm lint && pnpm typecheck` — clean
- `pnpm test:unit` (524 files / 4671 tests), `pnpm check:layering`, `pnpm test:output-economy`,
  `pnpm check:fallow`, `pnpm depgraph:test` — all green
- Acceptance perf: `src/utils/exec.ts` 0.53s, `src/daemon/ref-frame.ts` 0.5s wall clock (budget
  10s); asserted in-test at <10s.

### Cross-check against `check:affected` (no contradictions)

For each sample diff: `selectChecks` over that diff's production files vs. the union of the blast
radius gate plans for the same files. Blast radius may be *wider* (it also plans for dependents);
it must never be narrower.

| diff | prod files | `check:affected` (prod files) | `depgraph affected` union | selected by check:affected but not by blast radius |
| --- | --- | --- | --- | --- |
| b2b116fef (#1450) | 10 | format, lint, typecheck, layering, fallow, build, vitest-related | same | **(none)** |
| 4c02b6ad2 (#1433) | 5 | format, lint, typecheck, layering, fallow, build, vitest-related | same | **(none)** |
| e8b779cb3 (#1392) | 4 | format, lint, typecheck, layering, fallow, build, vitest-related | same | **(none)** |
| fcaa6c995 (#1435) | 77 | format, lint, typecheck, layering, fallow, build, vitest-related | + `coverage`, `provider-integration` | **(none)** |

The fourth diff is the informative one: dependents of the moved contracts reach `src/platforms/**`,
so the blast radius correctly adds the two platform-owned gates that a file-local plan misses.

## Scope

One issue per PR: nothing from #1423 (repo-health snapshot) or #1424 (delta comment) is
implemented here, and #1408's manifest is consumed, not vendored.


Link to Devin session: https://app.devin.ai/sessions/0d8e3e21666746dd828556a1c4646008
Requested by: @thymikee
