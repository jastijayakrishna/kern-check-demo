# feat: add connection create and update commands

## Summary

Adds `workos connection create` and `workos connection update <id>` for provisioning and migrating SSO connections via the Connections API, plus a `connections` alias for the resource (kept out of metric fragmentation via `command-aliases.ts`).

- Body assembly: `--data '<json>'` and `--file <path|->` (stdin) provide the raw request body; top-level flags `--org/--organization-id`, `--name`, `--external-id`, `--type` override/merge on top. Nested `saml_options` / `oidc_options` / `attribute_maps` are passed through the raw JSON body. Non-object JSON bodies are rejected with `invalid_json_body` (type-narrowed via an `isJsonObject` guard — no casts).
- `workos-api.ts`: add `PATCH` to `WorkOSRequestOptions['method']` and send JSON bodies for PATCH.
- `workos-client.ts`: new `connections.create(body)` / `connections.update(id, body)` raw methods.
- `connection create` requires `organization_id`; `connection update` rejects an empty body. Both support human and `--json` output and reuse the standard API-key resolution and error handling.

These endpoints are feature-gated server-side (`connections-api-migrations-capabilities-api`) and return 404 unless enabled for the team.

Part of https://linear.app/workos/issue/ENT-6443 — companion docs PR in workos/workos.

## Test plan

- `bun run typecheck`, `bun run lint`, `bun run format:check`, `bun run build` — clean.
- `bun run vitest run src/commands/connection.spec.ts src/lib/workos-api.spec.ts` — new specs cover request construction, flag/JSON precedence, `--file`/stdin parsing, invalid JSON, empty update body, API errors, and JSON output mode.


Link to Devin session: https://app.devin.ai/sessions/9151860048f44f5084cd0fe314e8722c
Requested by: @qbalin
