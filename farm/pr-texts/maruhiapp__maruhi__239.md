# Migrate repo tooling from wrangler CLI to cf CLI (1.0.0-beta.5)

## Summary

Migrates the repo's tooling from `wrangler` to Cloudflare's new `cf` CLI (open beta `1.0.0-beta.5`, the wrangler successor). Configs move to `cloudflare.config.ts` (TS, evaluated via `ctx.mode`), deploy/dev/D1/R2/secret commands move to `cf`, and CI + docs follow. Remote-side behavior is verified by command-surface parity (`--help`, `--dry-run`, local simulation) only — **no real deploy, remote write, or secret upload was performed** (per task rules).

### Config migration

- `apps/server`: `wrangler.jsonc` → `cloudflare.config.ts` + `wrangler.config.ts` bundler shim (`assetsDirectory` only). The three deploy shapes are now `cf --mode`s of one file: default → `maruhi-server` (self-host), `--mode hosted` → `maruhi-server-hosted`, `--mode restore` → `maruhi-restore` (replaces `wrangler.restore.jsonc`, deleted). Shared bindings are hoisted into `DAILY_TRIGGERS` / `RATE_LIMIT_BINDINGS` / `SPA_ASSETS` / `PROJECT_CHAIN_EXPORTS` so self-host and hosted literally cannot drift on the values they share.
- `apps/server/wrangler.jsonc` **stays** as the test-harness mirror: `@cloudflare/vitest-plugin` only reads `wrangler.*` files, and `vitest.config.ts` / `serving-topology` / `spa-topology` call `unstable_readConfig` on it. `scripts/check-hosted-config.ts` was rewritten to normalize BOTH files into one shape and assert field-by-field equality (self↔self, hosted↔hosted) plus all previous hosted invariants and the restore-mode shape — runs in CI step 8c.
- `apps/site`: `wrangler.jsonc` deleted → `cloudflare.config.ts` + `wrangler.config.ts` (nothing read the old file).
- `wrangler` stays in devDependencies of server/site/web: `cf deploy`/`cf dev` delegate builds to the workspace wrangler internally (`Delegating to Wrangler`), and the test harness needs it.

### wrangler → cf command mapping

| Before (wrangler) | After (cf) | Where | Verified how |
|---|---|---|---|
| `wrangler deploy` | `cf deploy` | `apps/server` deploy script, SELF_HOSTING | `cf deploy --dry-run` passes (self-host, `--mode hosted`, `--mode restore`) — all bindings, triggers, domains and assets resolve |
| `wrangler deploy --env hosted` | `cf deploy --mode hosted` | ci.yml 8c, ops runbook | same dry-run; parity-asserted vs `wrangler.jsonc` `env.hosted` |
| `wrangler deploy -c wrangler.restore.jsonc` | `cf deploy --mode restore` | ops runbook, cloudflare.config.ts | dry-run shows `maruhi-restore` + `* * * * *` cron + `RestoreDrillDO`/`PRODUCTION_PROJECT_CHAIN` DO bindings |
| `wrangler delete -c wrangler.restore.jsonc` | `cf workers delete maruhi-restore --force` | SELF_HOSTING | `cf workers delete --help` surface only |
| `wrangler dev` / `wrangler dev --port` | `cf dev --port` | apps/site preview, apps/web preview, both e2e spawns | `cf dev` boots and serves HTTP 200 on :8794; **web e2e 36/36 and site e2e 12/12 pass under `cf dev` + Playwright** |
| `wrangler login` | `cf auth login` | docs | `--help` surface only |
| `wrangler secret put X` | **kept on wrangler** (`wrangler secret put [X] [--env hosted]`) | SELF_HOSTING, AUTH_SPEC | cf's `workers secrets update` only accepts the value inline via `--text` — argv/`ps`/shell-history exposure, a real regression for a secrets manager. Reviewer-flagged; reverted. `cf workers secrets list` still used (no value exposure) |
| `wrangler secret list` | `cf workers secrets list` | docs | `--help` surface only |
| `wrangler d1 create maruhi` | `cf d1 create --name maruhi` | `db:create`, docs | `--help` surface only |
| `wrangler d1 migrations apply DB --remote/--local` | `cf d1 migrations apply <id> [--local] --dir drizzle --pattern 'drizzle/*/migration.sql'` | `db:migrate` family, CI | `--local` run applied `20260926225739_init/migration.sql` to the local D1 sim (verified via `d1_migrations` row); **cf takes the database UUID, not the binding name** — `scripts/d1-id.ts` resolves it from cloudflare.config.ts |
| `wrangler d1 execute --file` | `scripts/d1-import.ts` (`cf d1 import` init→PUT→ingest→poll) | ops restore flow | `--help`/`cf schema` surface + script run verified to the auth wall (cf spawned as `node apps/server/node_modules/.bin/cf` at repo root, JSON envelope parse, URL-redacted error path). `cf d1 query` has no `--file`; the script reproduces wrangler's multipart import protocol |
| `wrangler d1 export` | `scripts/d1-export.ts` (`cf d1 export --output-format polling` loop + signed-url fetch) | ops-backup.yml | `--help`/`cf schema` surface + script run verified to the auth wall (cf spawned as `node apps/server/node_modules/.bin/cf` at repo root, JSON parse, URL-redacted error output); the script owns the bookmark poll + download wrangler used to hide |
| `wrangler d1 info` | `cf d1 get <id>` | ops-backup.yml trip-wire | `--help` surface only; size field name unverifiable locally → parses `database_size ?? file_size` (+ `result.*`) |
| `wrangler r2 bucket create` | `cf r2 buckets create-by-name` | docs | `cf schema r2 buckets …` |
| `wrangler r2 bucket lifecycle add` | `cf r2 buckets lifecycle update <name> --rules <json> -f` | docs | `cf schema` shows `rules` is a JSON-array string; exact per-rule field names (`expire_objects`/`abort_multipart_uploads`) are API-doc parity, **not locally verifiable** |
| `wrangler r2 bucket dev-url get` | `cf r2 buckets domains managed list` | docs | `--help` surface only |
| `wrangler r2 object put/get` | `cf r2 objects put <key> --bucket-name --file` / `get <key> --bucket-name [--text]` | ops-backup.yml, docs | `cf schema r2 objects …`; positional is the object key, bucket via `--bucket-name` |
| `wrangler tail` | **kept on wrangler** (documented) | SELF_HOSTING | `cf` beta has no tail command — noted in docs |

### Behavior notes worth knowing

- **`--dir` is the migration-name anchor**: `cf d1 migrations` records names relative to `--dir` (`drizzle/…/migration.sql` under `--dir drizzle`); the pattern must start with the dir prefix. `--dir drizzle --pattern 'drizzle/*/migration.sql'` reproduces wrangler's `migrations_dir`+`migrations_pattern` exactly.
- **`cf d1` requires an RFC-4122-shaped UUID**, so the self-host placeholder changed `00000000-0000-0000-0000-000000000000` → `00000000-0000-4000-8000-000000000000` (still visually a placeholder, now passes ID validation) in `cloudflare.config.ts` **and** `wrangler.jsonc` (kept in parity by the check script).
- `cf dev` runs the same workerd/wrangler engine (`[wrangler:info]` logs) — local state moved `.wrangler/state` → `~/.config/cloudflare/state`; `WRANGLER_SEND_METRICS` is still meaningful (cf delegates internals to wrangler), so CI sets `CF_SEND_TELEMETRY: "false"` alongside it.
- `wrangler types` → `cf workers types` writes `worker-configuration.d.ts` at the package root (not `.cloudflare/types/`); it is generated/unconsumed by tsconfig → gitignored, not committed.

### Repo gates (all green)

`bun run check` full pass: check:english → oxfmt → oxlint → tsc → ImportLint → fallow → React Doctor → **vitest 146 files / 5072 tests**; plus `bun scripts/check-hosted-config.ts` (wrangler.jsonc ↔ cloudflare.config.ts parity), `cf deploy --dry-run` ×3 modes (server) + ×1 (site), `db:migrate:local`, `cf dev` smoke, web e2e 36/36, site e2e 12/12.

### What stays on wrangler (partial migration)

- **Test harness**: `@cloudflare/vitest-plugin` reads only `wrangler.jsonc` — kept as drift-checked mirror; `packages/crypto/wrangler.jsonc` same role.
- **Product surface**: `maruhi sync`/`ci run` exec driver and site recipe docs emit `wrangler` commands for **end users'** vendor CLIs (apps/cli `sync-*`, site `deploy-targets`/`github-actions` mdx, test shims) — product behavior, out of scope. Follow-up candidate: a `cf` preset (`cf workers secrets bulk` exists).
- **`wrangler tail`**: no `cf tail` in beta — documented.
- **`wrangler secret put`**: cf's `workers secrets update` takes values only via `--text` (argv/history exposure); stdin registration stays on wrangler — documented.
- **cf internals**: `cf deploy`/`cf dev` delegate builds to workspace wrangler (`wrangler-dist/cli.js`) — devDeps keep `wrangler@4.136.1` + `cf@1.0.0-beta.5` (exact pins).

### Risks / gaps (unverified by definition)

- Remote-side behavior verified by command surface only (`--help`, `cf schema`, `--dry-run`, local sim): `cf workers secrets update`, `cf d1 create/query/get`, `cf d1 import/export` (scripted), `cf r2 buckets objects lifecycle`, `cf workers delete`, `cf pages deploy`. The first real `bun run deploy`/`ops-backup` run should be watched.
- `cf d1 get` JSON size field name assumed `database_size`/`file_size` (both parsed) — trip-wire step in ops-backup.yml fails safe (empty → step errors, does not silently pass zero).
- Second commit pins `miniflare>undici` to 7.29.1 via a scoped override (the existing `@scalar/json-magic>undici` precedent): miniflare exact-pins the vulnerable 7.29.0 and the `bun audit` step was already failing on main — this fixes it properly rather than extending the `--ignore` list by 10 GHSA ids.
- Ops scripts (`d1-export.ts`, `d1-import.ts`) spawn `node` on the pinned bin `apps/server/node_modules/.bin/cf` with cwd at the repo root — `bun <file>` doesn't put `.bin` on PATH (reviewer-caught), `bun x cf` at root would resolve `cf@latest` under the isolated linker (also reviewer-caught), and cf inside apps/server tries to load cloudflare.config.ts which requires Node. Raw `cf d1` API calls need no project config. Thrown errors redact URL-shaped values (`redactUrls`) so a signed export URL can never land in Actions logs.
- SELF_HOSTING.md's 2026-08-10 real-deploy verification was against wrangler 4.120; the cf re-expression is not yet verified against a real account (documented in the guide header).
- `cf` is beta — command surface may shift before 1.0; pins are exact to contain that.

Link to Devin session: https://app.devin.ai/sessions/cb13b7ea0a09457887d17acacc9e97e9
Open in Devin Desktop: https://app.devin.ai/desktop/session/cb13b7ea0a09457887d17acacc9e97e9?variant=devin
Requested by: @lightsound
