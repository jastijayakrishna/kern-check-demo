# Claim org installs /user/installations omits, and say why a repo is missing

## What

`GET /user/installations` is keyed to one OAuth token's visibility and can omit an organization installation outright — an org that restricts third-party access, or a member who is not an app manager, both read as a clean absence. Both claim paths treated that silence as a denial:

- `apps/auth/src/server-context.ts` — `reconcileGitHubInstallations`
- `apps/server/src/github-operations.ts` — `GitHubOperations.refresh` (the path behind the mobile repo picker)

So the org installation stayed unclaimed and its repositories never reached the picker, which showed nothing and explained nothing.

## Membership fallback

`GitHubAppClient.organizationMembership` (`GET /user/memberships/orgs/{org}`) asks the user's own token whether they belong to the account that owns the install. It is consulted only when the listing omits an Organization install, and it can only ever ADD a claim:

- `active` → claim
- `404` (definitive non-member) → the listing's refusal stands
- `unknown` — 403 (the App manifest deliberately requests no organization permissions, so GitHub may simply close this endpoint), 5xx, network error → prior behaviour, unchanged

The unavailable-listing precedent is untouched: it still claims without asking. The monolith asks with the rotated token rather than the expired one, and never takes an installation row another identity already owns.

## Picker

`explainMissingRepo` (`apps/mobile/sources/buzz/room-repo-picker.ts`) names the reason a typed `owner/repo` is absent, rendered under the connect card: owner not connected, owner-grant-needed, installation suspended, installation revoked, selected-repositories install that excludes it, or a stale listing.

## Tests

- `apps/auth/src/github.test.ts` — every membership answer, including the refusals that must not read as denials, and org-login path encoding
- `apps/auth/src/server-github-installation-routes.test.ts` — omitted org claims on active membership, stays unclaimed on denial, and an unverifiable membership does not block the unavailable-listing precedent
- `apps/server/src/github-operations.test.ts` — same three, plus "never takes an installation another identity owns"; the membership stub rejects the expired token, so it pins the rotated-token fix
- `apps/mobile` — `explainMissingRepo` cases and the rendered reason line

`apps/auth` is green (134/134) and `github-operations.test.ts` is green (27/27). This sandbox has no npm, so `node_modules` was assembled from another checkout; the remaining `apps/server` integration/latency and `nativeFingerprint` failures reproduce identically on the untouched tree and are that environment, not this change.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
