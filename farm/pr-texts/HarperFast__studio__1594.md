# fix(rum): drop private-repo SSH deploy failures from Error Tracking, redact repo URLs

No linked issue: the RUM signal embeds a customer's private repository URL, so it was
deliberately not filed publicly. Details below use `acme-corp/billing-service` in place of
the real one.

## Problem

Deploying a component from a private git repository surfaces an `SSEOperationError` whose
message is Harper's:

```
Failed to deploy private repository git@github.com:acme-corp/billing-service.git: SSH access
failed. Verify the repository URL, configure an SSH key on this Harper instance, ensure the
key has access to the target repository, and confirm the host is present in the
ssh/known_hosts file.
```

RUM recorded **8 of these in the 24h to 2026-07-30** (`env:prod`, one customer, one session),
and Error Tracking opened an issue for them. Two things are wrong with that:

1. **It isn't a Studio bug.** Every remediation step in the message is on the *instance* —
   install an SSH key, grant it access to the repo, add the git host to the instance's
   `ssh/known_hosts`. Nothing in Studio changes in response, so the issue can only ever be
   closed as customer configuration.
2. **It carries customer-identifying data.** The message embeds the private repo's owner and
   name, which Error Tracking then retains and makes searchable.

## Treatment

**Drop the event** (`shouldKeepEvent`). This is the same class as the expected states already
dropped there — 401s, timeouts, instance-endpoint 5xx. Matched on the
`Failed to deploy private repository` prefix rather than the SSH remediation sentence, so a
reworded message still drops; a generic `Failed to deploy component: …` is still kept.

**Redact customer URL paths anyway** (`redactErrorText`, new). Dropping this message keeps
*this* URL out of Datadog, but other deploy failures that stay kept — a repo 404, a bad ref,
npm auth output — quote the same `package` reference, and the drop rule depends on Harper's
wording. So redaction is a backstop, not a substitute.

The first cut of it asked "is this URL a repository?" and answered with a forge list, a
`git.`/`gitlab.`/`github.` hostname convention, a `.git` suffix and a git protocol check.
Review found the holes, and they share a root — that list never finishes. A GitLab or Gitea
self-hosted at `scm.acme-corp.com` matches none of it; neither does a `git+https:` remote;
neither does `https://api.github.com/repos/<owner>/<repo>`, which is Studio's own lookup while
the deploy form is being filled in.

So it's inverted: **Harper's domains are the short list we control, so keep the path only for
those and reduce every other URL to scheme + host + `<redacted>`.** Credentials are stripped
from any URL's userinfo (an https private-repo remote can carry a token there — strictly worse
than a repo name), and query/fragment go with the path (a `?ref=` can name a private branch).
scp-style remotes (`git@host:owner/repo.git`) aren't URLs and keep their own rule.

```
Failed to deploy git@github.com:acme-corp/billing-service.git: exit code 128
  -> Failed to deploy git@github.com:<redacted>: exit code 128

Failed to deploy https://scm.acme-corp.com/acme-corp/billing-service: 404 not found
  -> Failed to deploy https://scm.acme-corp.com/<redacted>: 404 not found

Request failed with status code 500 https://api.harper.fast/HDBInstance/ins-123/operation
  -> unchanged
```

Harper API endpoints stay triageable and Studio's asset URLs stay source-mappable — that is
what the allowlist (`harper.fast`, `harperfabric.com`, `harperdb.io` by suffix, plus
`localhost`) is there to protect. Two accepted costs: a stack frame from an embedded
third-party script now reads `https://static.reo.dev/<redacted>`, which still attributes it by
host; and a URL whose path is just `/` is left alone rather than gaining a `<redacted>` that
hides nothing.

**Compose in `beforeSend`** (new module): filter first, then redact `error.message`,
`error.stack` and `error.resource.url`. Order matters — the third-party attribution in
`shouldKeepEvent` inspects the raw stack, so it must run before any frame is rewritten (there's
a test pinning that). `error.resource.url` is in scope because a failed lookup carries the same
identity in a different field: a 404 on a private repo would otherwise ship the repo name
verbatim beside a redacted message. Only the reported copy is rewritten; the UI renders the
error object itself.

**Compensate in the UI.** With RUM now silent on this failure, `DeployProgress` is the only
place it surfaces, so it links to Config > SSH Keys beneath Harper's remediation text.
`onNavigateAway` lets `RedeployApplicationModal` close first — it's controlled by global
watched state, not the route, so it would otherwise sit over the SSH Keys page. The import
flow is unchanged: its toast already shows the full remediation text, and
`ImportAuthorization` links to SSH Keys and warns on key/host mismatch before submit.

## Testing

`npx vitest run` → 267 files / 2003 passing; `tsc -b`, `dprint check`, `oxlint` clean.

New coverage: the drop rule (including the reworded variant and a generic deploy failure that
must stay); redaction of a self-hosted forge under a custom domain (including a nested group
path), `git+https:`/`git+ssh:` remotes, and Studio's own GitHub/npm lookups; what must *not* be
redacted (Harper endpoints, Studio stack frames on a Harper subdomain, a bare host with no
path, an email followed by a colon); `error.resource.url` redacted for a lookup but left intact
for an instance operation endpoint; the filter-before-redact ordering; and the guidance link's
href and dismiss behaviour.

Not browser-verified: reaching that UI needs a real failing private-repo deploy against a
Harper >= 5.1 instance, which the preview can't produce, so the unit tests are the
verification.

## Notes, out of scope

**RUM `resource` events carry the same identity, unredacted.** `beforeSend` only rewrites error
events here. Resource events are a live vector, not a hypothetical one: a 7-day RUM query
returns `resource` events for `github.com` URLs that name a customer's repo path (CI badge
images), and `getGitHubRepo` / `findNpmPackageName` fetch `api.github.com` and
`registry.npmjs.org` with the owner/repo or package the customer typed. Extending redaction to
`resource.url` would close it, but it changes what every third-party resource looks like in the
RUM performance views, so it's a call for the team rather than a quiet addition to this PR.

**The global `errorHandler` splits messages on the first `:`**, so this failure currently toasts
with the title `Failed to deploy private repository git@github.com` and the rest as the
description. That's generic behaviour for any colon-bearing message, not specific to this path.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
