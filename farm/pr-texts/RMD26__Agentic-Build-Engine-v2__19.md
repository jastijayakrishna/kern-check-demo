# security: rotate PROXY_HEADER and inject it via env instead of hardcoding

## Summary

Follow-up to #15. The `PROXY_HEADER` shared value was hardcoded in the frontend shim (`frontend/vertex-ai-proxy-interceptor.js`) and had leaked into git history, so it needed rotating. Rather than re-hardcode a fresh value into tracked source (which would just reintroduce the problem #15 fixed), the shim now reads it from a build-time env var:

```js
// before
'X-App-Proxy': 'KYcpAhHGTSJSbZUJUIJYyE369qTxlqN0',

// after
const PROXY_HEADER = import.meta.env.VITE_PROXY_HEADER; // inlined by Vite at build
...
'X-App-Proxy': PROXY_HEADER,
```

The fresh value is set locally in the git-ignored `backend/.env.local` (`PROXY_HEADER`) and `frontend/.env.local` (`VITE_PROXY_HEADER`) — the two must match. This PR contains **no secret values**.

Changes:
- `frontend/vertex-ai-proxy-interceptor.js`: read `VITE_PROXY_HEADER` (warns if unset); drop the hardcoded value.
- Add `frontend/.env.example` (`VITE_PROXY_HEADER`); note in `backend/.env.example` that the two headers must match.
- Untrack `frontend/dist/` — build output that PR #15 gitignored but left tracked; the committed bundles also still contained the old header.
- README: document the rotate-and-set-both flow.

Verified: `VITE_PROXY_HEADER=<new>` → `npm run build` inlines the new value into `dist/` and the old value is absent from the bundle.

## Action still required by maintainer
`import.meta.env.VITE_PROXY_HEADER` is inlined into the browser bundle, so it is still shipped to clients and is **not** a real auth mechanism (called out in #15). Keep the backend bound to `127.0.0.1`. For any non-local deployment, add real per-user authentication.

## Note
Build requires Node `20.19+`/`22.12+` (Vite 8); Node 20.18 on the base image fails with a rolldown native-binding error. Built with Node 22.12. Not changed here, but worth pinning the engine in a future PR.


Link to Devin session: https://app.devin.ai/sessions/e4cfc7173a7f4418b7577c06dd28f8c1
Requested by: @robert2687

## Summary by Sourcery

Rotate the proxy header by moving its value out of hardcoded frontend code into environment configuration shared between frontend and backend, and remove previously committed build artifacts containing the old value.

Enhancements:
- Update the frontend proxy shim to read the shared header value from a build-time environment variable and log when it is missing.
- Clarify README security guidance around using matching PROXY_HEADER/VITE_PROXY_HEADER values and their limitations as an auth mechanism.

Build:
- Add a frontend .env.example file documenting VITE_PROXY_HEADER configuration.
- Stop tracking the built frontend dist/ assets that previously contained the old proxy header value.

Documentation:
- Expand README setup and security instructions to cover both backend and frontend env files and the proxy header rotation process.
