# fix(daemon): replay session metadata after reconnect

## Summary

- persist each authoritative daemon event/session metadata snapshot beside its local session row
- replay converged snapshots after every successful Control Plane register, covering turns completed before the control client reaches READY
- retain terminal phase and timestamp when later asynchronous metadata enrichment arrives
- repair pre-upgrade rows with identity/classification-only metadata so historical status and execution config are never reconstructed from current agent settings

## Why

Relay ingress remains local-first while the Control Plane client is CONNECTING or REGISTERING. During that window, event/session is intentionally a no-op. A fast turn can therefore start and finish before READY, leaving no later milestone to create session_meta. The protected session deep link then stays a 404 and the visibility control never has persisted ownership metadata to render.

The replay sends metadata only. Transcript bodies remain daemon-local, and the Control Plane still performs the normal webchat owner classification and authorization checks. Persisted snapshots preserve nonstandard terminal sessions such as memory dreams across daemon restarts, while later display-name enrichment cannot downgrade a terminal snapshot to plan.

## Validation

- pnpm --filter @agentconnect.md/daemon exec vitest run test/daemon-smoke.test.ts -t "session metadata snapshots|dream terminal metadata|display names are resolved"
- pnpm --filter @agentconnect.md/daemon typecheck
- pnpm exec eslint packages/daemon/src/daemon.ts packages/daemon/src/store/local-store.ts packages/daemon/src/cp/client.ts packages/daemon/test/daemon-smoke.test.ts
- GitHub Actions: Build, Check, Unit Test, both Integration test shards, Sandbox (Linux), Semantic PR
- pre-push eslint .

Created by Codex . GPT-5

