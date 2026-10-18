# fix(surface): CLI mints surface:admin token + pin intra-monorepo deps to workspace:* (0.3.3-rc.1)

Redo of the reverted #146 (`parachute-surface add`/`list` auth fix), done properly — with the root cause of the CI break that forced the revert (#148) fixed.

## The bug (#146's target)
`parachute-surface add`/`list`/etc. → HTTP 401 `hub JWT audience mismatch: expected "surface", got "operator"`. The CLI presented the on-disk operator token (`aud: "operator"`) directly to the daemon's admin endpoints, which require a hub-issued `aud: "surface"` token.

## Why #146 was reverted (the CI break)
The version bump to `0.3.3-rc.1` tripped the **workspace caret-miss**: sibling packages depended on `@openparachute/surface` (and the already-rc `surface-client`/`surface-server`) via caret ranges (`^0.3.1`), and a caret range **excludes prereleases** — so the workspace silently resolved those siblings from npm (`surface-client@0.3.2`, `surface-server@0.1.2`) instead of local source → two divergent copies → `SurfaceHostContext` type mismatch → `typecheck` FAIL. The version bump also wasn't synced into `bun.lock` → `bun install --frozen-lockfile` failed first.

## What this PR does

### 1. Re-applies #146's auth fix (verbatim, via cherry-pick)
New `packages/surface-host/src/cli-token.ts`: the CLI exchanges the operator credential for a short-lived (300s) `surface:admin` token via the hub `POST /api/auth/mint-token` (capability attenuation — the same path the admin SPA uses) and presents that. **Daemon admin auth is unchanged** — no new accepted audience, no widened scope, no escalation. + `cli-token.test.ts` and updated `cli.test.ts` (hermetic credential env). Reviewer-LGUT'd in #146.

### 2. Fixes the caret-miss at the root
Every **intra-monorepo** dependency on a sibling workspace package now uses `workspace:*` (matching `notes-ui`'s existing `surface-client` pin), across `docs-editor`, `meeting-ingest`, `meeting-mcp`, `pebble-config`, `surface-host`, `notes-ui`, `surface-render`, `surface-server`. A prerelease bump can never caret-miss again. External `@openparachute/*` packages (`scope-guard`, published from another repo) keep their caret ranges.

**Publish-time substitution verified** with `bun pm pack`: in the surface-host tarball, `@openparachute/surface-client: "workspace:*"` becomes `"0.3.3-rc.2"` (the real version) and the package itself publishes as `0.3.3-rc.1` — published consumers still pin correctly.

### 3. Version + lockfile
`@openparachute/surface` → `0.3.3-rc.1` (rc-first per committed-core governance). `bun.lock` synced — `bun install --frozen-lockfile` passes (the gate that broke last time). The lockfile diff confirms the previously-external sibling resolutions are gone (all intra-monorepo deps now resolve to workspace).

## Gate verification (all green, final committed tree)
| Gate | Result |
|---|---|
| `bun install --frozen-lockfile` | ✅ exit 0 |
| `bun run typecheck:all` (all packages + admin SPA) | ✅ exit 0 |
| `bun run test` | ✅ exit 0 — 1475 bun tests + 918 notes-ui + 61 surface-render, 0 fail (incl. 26 cli/cli-token) |
| `bun run build` | ✅ exit 0 |

`biome check .` reports 20 errors — **all pre-existing on `main`** (identical files/count; verified via a clean-main worktree). None are in this PR's changed files; biome is not a gate in `ci.yml`. Left as-is (out of scope).

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01T6HAzWsgiJy4ndsWSCWY5S
