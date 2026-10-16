# action: skip profiling gracefully on credential-less fork pull requests

## Summary

`pull_request` runs from forked repositories receive neither repository secrets (`api_token` resolves empty) nor an `id-token: write` grant, so both auth paths are structurally unavailable — today the action fails the contributor's job with a confusing token error for zero benefit. This adds `src/fork-run.js` with `resolveForkSkip({apiToken, eventName, eventPath, repository})`, called from `run()` in `src/action.js` only inside the existing `TOKEN === ""` branch:

```js
if (TOKEN === "") {
    const forkSkip = await resolveForkSkip({ … })
    if (forkSkip.skip) {
        core.notice(forkSkip.reason)   // one clear notice; job continues
        return false                    // post step no-ops via jibrilStarted state
    }
    throw new Error("Input 'api_token' is required. …") // unchanged
}
```

Skip fires only when ALL of: event is `pull_request` (never `pull_request_target`, which does get secrets), `head.repo.full_name` differs from `GITHUB_REPOSITORY` (case-insensitive), no `api_token`, and OIDC unavailable (`GARNET_ACTION_ENABLE_OIDC_AUTH` off or no `ACTIONS_ID_TOKEN_REQUEST_URL`/`_TOKEN`). Detection never throws — any read/parse/shape problem returns "do not skip", falling back to current behavior. The post step already no-ops cleanly when `jibrilStarted` state is absent (nothing installed, nothing to upload).

### Behavior matrix

| Context | api_token | OIDC grant + flag | Behavior |
|---|---|---|---|
| fork `pull_request` | empty | unavailable | **NEW: single `core.notice`, exit success; post no-ops** |
| fork `pull_request` | provided | — | unchanged (normal run) |
| fork `pull_request` | empty | available + flag on | unchanged (falls through to auth path) |
| `pull_request_target` | empty | — | unchanged (existing token error) |
| same-repo, any event | empty | unavailable | unchanged (existing token error) |
| unexpected payload shape | empty | — | unchanged (fallback, never throws) |

Tests (`test/fork-run.test.js`): all six matrix rows plus a `run()`-level fork-skip test and a spawned `src/post.js` no-op test (exit 0, no `::error`). `npm run validate` green on Node 24; `dist/` rebuilt with ncc and committed.

### Stack position
Top of the stack: **#122 → #124 → #126 → #125**. Based on #126; merge last. Its own diff is `src/fork-run.js`, `src/action.js`, `test/fork-run.test.js`, and `dist/`.

Rebasing onto #122 required a real integration in `src/action.js`: #122 replaced the bare `TOKEN === ""` throw with `resolveControlPlaneAuth()` / `requireApiToken()`. The fork check now runs before auth resolution and only when `api_token` is empty, so #122's OIDC ladder and error text are untouched:

```js
if (TOKEN === "") {
    const forkSkip = await resolveForkSkip({ apiToken: TOKEN, eventName, eventPath, repository })
    if (forkSkip.skip) { core.notice(forkSkip.reason); return false }
}
const controlPlaneAuth = await resolveControlPlaneAuth({ apiURL: API, apiToken: TOKEN, useOIDCAuth })
```

`resolveForkSkip` already declines to skip when OIDC is actually available (`GARNET_ACTION_ENABLE_OIDC_AUTH=true` plus a granted `ACTIONS_ID_TOKEN_REQUEST_URL`/`_TOKEN`), so with #122's flag on, an OIDC-capable run always reaches the exchange; the skip only fires for `pull_request` runs from forks with no credential path at all.


Link to Devin session: https://app.devin.ai/sessions/131f3ed18255411ab6c052d0c81f79b8
Requested by: @jadoonf
