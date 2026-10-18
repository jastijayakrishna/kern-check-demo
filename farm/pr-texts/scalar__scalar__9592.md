# fix(api-client): respect per-operation security in the auth dropdown

The auth dropdown listed every scheme from `components.securitySchemes` for every operation, so users could pick auth a request does not accept — even on operations that opt out with `security: []`.

The OpenAPI spec is clear that an operation's `security` is the source of truth:

> Lists the required security schemes to execute this operation. The name used for each property MUST correspond to a security scheme declared in the Security Schemes under the Components Object.

> This definition overrides any declared top-level `security`. To remove a top-level security declaration, an empty array can be used.

Defining a scheme under `components.securitySchemes` only declares it — it does not make it usable on a request. So in the reference docs and the request modal the dropdown now offers only what the operation declares:

- `security: []` → no auth offered (e.g. the `Login` endpoint)
- a subset (e.g. `[{ BearerJwt: [] }]`) → only that scheme; others are no longer shown as "Available"
- multiple alternatives (e.g. `[{ ApiKey: [] }, { BearerJwt: [] }]`) → all of them selectable

The standalone client keeps letting you attach any defined scheme (`createAnySecurityScheme`), since that is an explicit testing affordance.

A follow-up PR will tidy the "Required" vs alternative labeling (OR-alternatives are currently all labeled "Required").

## Ticket

Fixes #7400

<!-- CURSOR_SUMMARY -->
---

> [!NOTE]
> **Medium Risk**
> Changes request/auth UX in shared api-client logic; wrong gating could hide valid schemes or still expose invalid ones, but scope is limited to option building with solid regression tests.
> 
> **Overview**
> The auth dropdown no longer surfaces every entry in `components.securitySchemes` when the operation’s `security` should be authoritative (reference docs and the request modal).
> 
> **`getSecuritySchemeOptions`** now builds the “Available authentication” list from all defined schemes **only when** `canAddNewAuth` is true (standalone client via `createAnySecurityScheme`). When that flag is false, users see only schemes declared on the operation: **`security: []`** yields no options, a single declared scheme excludes the rest, and multiple OR-alternatives all remain selectable.
> 
> Standalone client behavior is unchanged—arbitrary schemes can still be attached for testing. Tests were adjusted for the new semantics and regression coverage was added for issue **#7400**.
> 
> <sup>Reviewed by [Cursor Bugbot](https://cursor.com/bugbot) for commit 988a8a7648246e24bae918a4921befe6e754a430. Bugbot is set up for automated code reviews on this repo. Configure [here](https://www.cursor.com/dashboard/bugbot).</sup>
<!-- /CURSOR_SUMMARY -->
