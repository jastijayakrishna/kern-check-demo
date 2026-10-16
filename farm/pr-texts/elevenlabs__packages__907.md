# feat(scribe): support disabling logging via enableLogging

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## description

Closes #545. Threads the realtime Scribe `enable_logging` query param through the SDKs so callers can opt into zero retention mode.

- `enableLogging?: boolean` on `BaseOptions` in `@elevenlabs/client`, appended to the WebSocket URI as `enable_logging=true|false`. Omitted entirely when unset, so the server default (logging enabled) still applies.
- `enableLogging?: boolean` on `ScribeHookOptions` in `@elevenlabs/react`, forwarded in both the microphone and manual-audio branches. Resolved with `??` so `connect({ enableLogging: false })` can disable logging for a single session even when the hook was created with `enableLogging: true`.

Confirmed against the backend repo: `/v1/speech-to-text/realtime` takes an `enable_logging` query param (bool, default `true`), and there is no `disable_logging` on the public API — `disable_logging` exists only internally as the derived/inverted value.

That also settles the naming. @kraenhansen raised `disableLogging: true` as affirmative-language alternative on #680, but `disable_logging` is an internal-only concept, so mirroring it in a public option would name something the API does not expose. `enableLogging` matches the query param, the Python SDK, and the LiveKit plugin, and is consistent with how this file already mirrors API names (`noVerbatim` → `no_verbatim`).

### second commit

`22baef6` renames `disable_logging` to `enable_logging` in the Scribe `session_started` config schema. The published [`/v1/speech-to-text/realtime` contract](https://elevenlabs.io/docs/api-reference/speech-to-text/v-1-speech-to-text-realtime) reports `enable_logging` in `MessagesSessionStartedConfig` and has no `disable_logging`. `disable_logging` was hand-written into `scribe.asyncapi.yaml` when the file was created in #328 and is referenced nowhere else in the repo, so nothing consumes it today — the internal derived value is the likely source of the mistake. It matters here because this is how a caller would confirm zero retention mode took effect.

One thing worth a second pair of eyes from someone with backend access: this is the field name in the `session_started` *response payload*, not the query param. The published contract says `enable_logging`, but if the handler happens to serialize the internal config object into that message, it could emit the derived `disable_logging` instead. Confirming which model backs that payload would close it out; the commit is separable if you would rather not take it on faith.

Not touched: the same schema declares `vad_commit_strategy` where the published contract says `commit_strategy`. Same class of drift, unrelated to this issue.

## testing

Added unit tests, run with `pnpm exec vitest --browser.headless`:

```
 ✓ src/scribe/scribe.test.ts > builds URI with enable_logging='false' when enableLogging is false
 ✓ src/scribe/scribe.test.ts > builds URI with enable_logging='true' when enableLogging is true
 ✓ src/scribe/scribe.test.ts > omits enable_logging when enableLogging is not set
 ✓ src/scribe.test.tsx > useScribe > passes enableLogging through to the client
 ✓ src/scribe.test.tsx > useScribe > lets connect() disable logging for a session enabled at the hook level
```

Full suites pass: 160 tests in `@elevenlabs/client`, 133 in `@elevenlabs/react`, plus `turbo check-types lint` for `client`, `react`, and `types`.

The client-side assertions inspect the URI the mock server actually received. The existing `builds URI with ...` tests only put the expected query string in the `new Server(...)` URL, which `mock-socket` strips via `trimQueryPartFromURL` before matching, so those tests pass regardless of the query params that get built. I verified the new ones fail when the param name is misspelled, when the boolean is inverted, and when the `undefined` guard is removed.

<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-0c8d57df-cc8c-4112-ad2c-4429d3c7a2bd"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-0c8d57df-cc8c-4112-ad2c-4429d3c7a2bd"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
