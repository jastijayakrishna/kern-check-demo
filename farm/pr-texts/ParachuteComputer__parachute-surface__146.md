# fix(surface-host): CLI mints a surface:admin token instead of presenting the operator token

## The bug (reproduced live on the gitcoin box)

`parachute-surface add <local-path>` (and `list`/`remove`/`reload`/`dev`/`provision-schema`) fail against a deployed surface daemon with:

```
HTTP 401 {"error":"unauthorized","message":"hub JWT audience mismatch: expected \"app\", got \"operator\""}
```

This blocked the clean external-surface-add workflow (had to hand-place a surface in `~/.parachute/surface/uis/` to work around it).

## Root cause

The CLI (`bin/parachute-surface.ts`) authenticated by presenting the on-disk operator token (`~/.parachute/operator.token`) directly:

```ts
function bearerToken(): string | undefined { return readOperatorToken(); }
```

That token is `aud: "operator"` carrying host-authority scopes (`parachute:host:*`, `hub:admin`, …). The daemon's admin auth (`src/auth.ts`) requires a hub-issued **`aud: "surface"`** token with a `surface:*` scope. The daemon tries its accepted audiences in order (`["surface", "app"]`); the last one tried (legacy `"app"`) is what the error text surfaces — but the real requirement is `aud: "surface"`.

The daemon's requirement is **correct** and shared by every other caller: the hub credential-delivery path (`POST /surface/api/credential`) and the admin SPA both present `aud: "surface"` `surface:admin` tokens. The CLI was the lone outlier presenting the wrong-audience operator credential.

## The fix (principled — no auth weakening)

The CLI now exchanges the operator credential for a short-lived `surface:admin` token at the hub's `POST /api/auth/mint-token` (new `src/cli-token.ts`), then presents that.

This is the ecosystem's **capability-attenuation** model — the exact path the admin SPA uses (session → mint → present):

- The operator token holds `parachute:host:auth` (default "admin" scope-set), which per the hub's `canGrant` **rule 1** may mint any *requestable* scope.
- `surface:admin` **is** requestable (only `parachute:host:*` are non-requestable — `hub/src/scope-explanations.ts`).
- The hub's `inferAudience(["surface:admin"])` → `"surface"`, exactly what the daemon validates.

The daemon's admin auth is **unchanged** — no extra accepted audience, no widened scope. A caller with no operator token, or one lacking minting authority, still can't reach the admin API.

### Why not the alternative (daemon accepts the operator token directly)?

The operator token IS a legitimate host-admin credential, so accepting it was on the table. Rejected because:
1. It would introduce a **new direct-trust path** (module trusting `aud: "operator"` + a host scope mapped to module-admin) — precisely the ad-hoc credential coupling the auth-unification arc retired (pvt_* → attenuation).
2. The operator scope-set carries `vault:admin`/`scribe:admin` but **not** `surface:admin`, so a clean version would *also* need a hub-repo change to the operator scope-set, and would lag 90-day operator-token rotation on deployed boxes.
3. Minting works on the gitcoin box **today** — the existing operator token already holds `parachute:host:auth`, so no hub change and no token rotation needed.

## Behavior
- **No operator token** → request goes out unauthenticated; daemon answers 401 (same as before this credential existed).
- **Mint failure** (expired token, hub unreachable, insufficient authority) → actionable message + non-zero exit (e.g. *"the operator token lacks minting authority (parachute:host:auth); run `parachute auth rotate-operator`"*).

## Tests
- New `src/__tests__/cli-token.test.ts` — 10 cases via injected `fetchFn`: request shape (URL/method/Bearer/scope/`expires_in`), trailing-slash trim, no-token → `undefined`, and every `CliTokenError` surface (hub_unreachable / 401 / 403 / bad_response).
- `src/__tests__/cli.test.ts` hardened to a hermetic `PARACHUTE_HOME` + blank `PARACHUTE_HUB_TOKEN` so the verb-routing/connection-error assertions don't depend on a developer's real operator token + a live hub.
- **665 pass, 0 fail** (`bun test src/`); `tsc --noEmit` clean; biome clean.

## 
