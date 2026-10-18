# feat(surface): build + serve a pushed surface — Surface Git Transport Phase 0b

## Surface Git Transport — Phase 0b (surface-host half)

On the hub's post-push notify (`POST /surface/api/git-pushed`), surface-host **pulls** the pushed SOURCE from the hub git endpoint, **builds** it in a sandbox, and **serves** it under `/surface/<name>`. Completes the Phase 0b spine: a plain `git push` becomes a served surface.

Design: `parachute.computer/design/2026-06-30-surface-git-transport.md` (§5, §7, "Decisions locked" #4).
**Pairs with** parachute-hub #728 (the notify half) — reviewed + tested together.

### What's here
- **`admin-routes.ts`** — `POST /surface/api/git-pushed`. Auth = `enforceScope(surface:admin)` (the SAME gate the hub's credential delivery uses — an unauthenticated caller can't trigger a build). Validates `{surface, clone_url, pull_token}`; rejects a host-reserved mount name up front. **FAIL-CLOSED**: a failed pull/build never touches the served bundle (last-good keeps serving) and never crashes the daemon; a backed-surface `server` block is **refused** (its code would run in-process *outside* the build sandbox — static surfaces only in Phase 0b).
- **`git-deploy.ts`** (new):
  - `pullSurfaceSource` — fresh `git clone --depth 1` from the hub; bearer rides the git child's **ENV scoped to the clone origin** (`http.<origin>/.extraHeader`) — never argv (no `ps` leak), never persisted config, never a cross-host redirect; `GIT_TERMINAL_PROMPT=0`. Modular network pull (no shared disk).
  - `buildSurface` — `bun install --ignore-scripts` (dependency lifecycle scripts can't run) + `bun run build`, behind a swappable **`BuildRunner`** seam. Served identity **PINNED** to the pushed name (source `meta.json` can't hijack another mount). No build script + prebuilt `dist/` → serve as-is.
  - `constrainedSubprocessRunner` (default, **Option A**) — scrubbed env (NO hub secrets / operator token; HOME/TMPDIR/PARACHUTE_HOME redirected into a throwaway build dir), **process-GROUP** wall-clock timeout (detached → SIGKILL `-pid`, so a grandchild is reaped not orphaned; hang-proof), bounded output, non-root.
- **`config.ts`** — `resolveSurfaceSrcDir` (`$PARACHUTE_HOME/surface/src/`, throwaway checkouts, distinct from served `uis/`).

### 🔒 Build-sandbox trust boundary — Option A now, **Option B is the Phase 0c gate**
The pusher holds operator-granted `surface:<name>:write` → **CI trust model**. The build runs attacker-influenceable code (the surface's own build script).

- **Option A (shipped, behind the `BuildRunner` seam):** the constrained subprocess above.
- **A's residual (explicit):** *no kernel FS/network confinement.* A build can READ **and WRITE** files this user can reach via **absolute paths** (incl. on-disk creds; could clobber a sibling served bundle), with open egress + no disk quota. **This is MOOT in Phase 0b:** the only writer is the operator (hand-minted `surface:<name>:write`), who already holds that credential — zero new exposure. Process containment IS handled in A (process-group kill).
- **Option B — HARD Phase 0c gate, MUST merge before Phase 2 (not a slippy fast-follow):** swap `BuildRunner` for a kernel-sandbox runner (`@anthropic-ai/sandbox-runtime` — Seatbelt/bubblewrap, the same engine parachute-agent uses) that confines the filesystem to the build dir + restricts egress. Phase 2 is when **non-operator agents / external clients** can push — which is exactly when A's residual would start to matter. The seam keeps 0c a pure swap with no spine changes. When wiring it, **reuse the agent's hard-won Linux fixes** (the `apply-seccomp` / `resolveSeccompReadBinds` class, bubblewrap deps) rather than re-discovering them.

### Tests
`git-deploy.test.ts` — pull (bearer in env not argv; bad-url + clone-fail), build (prebuilt passthrough; **real** constrained runner proves the env scrub; **process-group timeout kills a grandchild + never hangs**; build-failure; identity pinning), endpoint (401 unauth; happy path build+serve; **fail-closed** on build AND clone failure keeps last-good; bad/reserved payloads
