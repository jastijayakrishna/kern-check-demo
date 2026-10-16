# feat(sandbox/e2b): refresh sandbox lifetime on every provider.get()

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary

Adds `keepAliveMs` to E2B sandbox config so each `provider.get()` call extends the sandbox lifetime, preventing E2B from killing sandboxes mid-run during long agent loops while preserving the kill-on-abandon safety net.

`withSandbox` is invoked exactly once per tool call, so:

- Active sessions refresh the lifetime by `keepAliveMs` on every tool call (sandbox equivalent of a Temporal activity heartbeat).
- An abandoned sandbox still dies `keepAliveMs` after the last tool call.
- Consumers can keep `timeoutMs` short without tuning against worst-case run length.

## API surface

`keepAliveMs` is **provider-level only** — every sandbox managed by the provider refreshes by the same amount on each `get()`. Per-create overrides are intentionally not exposed; we'll add them if a real use case shows up.

`withSandbox` gains an opt-in `translateSandboxNotFound` flag (off by default) that converts a `SandboxNotFoundError` into a structured tool response, plus an optional `sandboxNotFoundToolResponse` for callers that want to localize or customize the message.

## Commits

### `feat(sandbox/e2b): add keepAliveMs to refresh sandbox lifetime on get()`

- New `keepAliveMs?: number` on `E2bSandboxConfig`.
- `E2bSandboxProvider.get(sandboxId)` forwards `{ timeoutMs: keepAliveMs }` to `Sandbox.connect()` when configured.
- New `src/adapters/sandbox/e2b/README.md` documenting the keep-alive pattern.
- New unit test file `src/adapters/sandbox/e2b/keep-alive.test.ts`.

### `feat(tool-router): opt-in translation of SandboxNotFoundError in withSandbox`

Optional `translateSandboxNotFound` flag on `withSandbox` translates `SandboxNotFoundError` from `manager.getSandbox()` into a structured tool-handler response instead of letting it bubble out. **Off by default** in the SDK — the consumer flips it on alongside the dep bump. New `WithSandboxOptions` type re-exported from `zeitlich`.

### `docs(sandbox/e2b): clarify timeoutMs is a lifetime, not an idle timeout`

JSDoc fix: `E2bSandboxConfig.timeoutMs` and `E2bSandboxCreateOptions.timeoutMs` previously read "Sandbox idle timeout in milliseconds", which is misleading on E2B (it's a sandbox lifetime — kills regardless of activity).

### `refactor(sandbox/e2b): drop per-create keepAliveMs override`

Per reviewer feedback: speculative API surface with no real caller. Removes the `keepAliveOverrides` Map / helper, `keepAliveMs` propagation from `create()`/`restore()`/`fork()`, override cleanup in `destroy()`, `keepAliveMs` from `E2bSandboxCreateOptions` (kept on `E2bSandboxConfig`), and corresponding tests.

This subsumes the earlier `fix(sandbox/e2b): honour per-call keepAliveMs in restore() and fork()` commit on this branch — that fix is no longer needed because per-create overrides no longer exist.

### `fix(sandbox/e2b): narrow connect() catch to genuine not-found errors`

The catch-all in `E2bSandboxProvider.get()` previously converted every E2B SDK error — auth failures, network blips, 5xx, validation — into `SandboxNotFoundError`. Combined with `translateSandboxNotFound`, that meant transient infra problems would silently soften into a misleading "sandbox is gone" tool response.

Narrow the catch to the SDK's `SandboxNotFoundError` class (and to deprecated parent `NotFoundError` as a defensive fallback). Re-throw everything else. Tests assert both:
- A real SDK `SandboxNotFoundError` is translated into our `SandboxNotFoundError`.
- A non-not-found error (e.g. `ECONNRESET`) propagates unchanged.

### `fix(tool-router): rewrite SandboxNotFound tool response message`

The previous "The session cannot continue" message was wrong — `withSandbox` returns a normal tool response, the agent sees it next turn, execution continues. New message:

> Error: the execution environment for the &lt;toolName&gt; tool is no longer available, so this tool call could not be completed.

### `docs(sandbox/e2b): clarify connect() timeoutMs is monotonic-extend`

Verified the "only extends when longer" claim against `node_modules/e2b/dist/index.d.ts:6573-6582` and the live SDK docs at `e2b.dev/docs/sdk-reference/js-sdk/v2.14.1/sandbox`. The SDK's `SandboxConnectOpts.timeoutMs` JSDoc says verbatim:

> For running sandboxes, the timeout will update only if the new timeout is longer than the existing one.

So `connect()` with `timeoutMs` is correctly monotonic. README quotes that line, calls out the no-shrink-via-connect rule, and points at `Sandbox.setTimeout` / `SandboxApi.setTimeout` for shrink semantics.

### `feat(tool-router): allow custom sandboxNotFoundToolResponse` *(new)*

New optional `sandboxNotFoundToolResponse?: string` on `WithSandboxOptions`. When set (and `translateSandboxNotFound` is `true`), this string is returned verbatim as the tool response instead of the default English message. Use this to localize, match agent persona, or give the model more specific recovery instructions. No callback form and no full `{ toolResponse, data }` form — defer those until a real caller needs them.

## Acceptance criteria

- [x] New `keepAliveMs` option documented on `E2bSandboxConfig`.
- [x] `E2bSandboxProvider.get()` forwards `timeoutMs` to `connect()` when configured.
- [x] Unit test covers the keep-alive path and the no-keep-alive path.
- [x] Catch in `get()` only converts genuine not-found errors; transient errors propagate.
- [x] `withSandbox` exposes `sandboxNotFoundToolResponse` for custom messaging.
- [x] No behavioural change for consumers that don't set `keepAliveMs` / `translateSandboxNotFound`.
- [x] Public API change is additive only.

## Testing

- ✅ `npx vitest run src/adapters/sandbox/e2b/keep-alive.test.ts` — 5/5 pass
- ✅ `npx vitest run src/lib/tool-router/auto-append-sandbox.integration.test.ts` — 17/17 pass (2 new tests for `sandboxNotFoundToolResponse`: custom string used when translate is on; ignored when translate is off)
- ✅ `npm run typecheck` — clean
- ✅ `npm run lint` — 0 errors
- ✅ `npm run build` — succeeds

One pre-existing unrelated failure in `src/lib/subagent/subagent.integration.test.ts > "fn-explicit sandbox outputs win over captured session outputs"` reproduces on `main` without these changes — not introduced by this PR.

<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-4ce96978-2a5f-421a-9678-6116eb84a40c"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-4ce96978-2a5f-421a-9678-6116eb84a40c"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
