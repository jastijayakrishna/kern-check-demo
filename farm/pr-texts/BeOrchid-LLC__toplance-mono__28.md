# Ship corridors with the deploy

## The gap #26 left

[#26](https://github.com/BeOrchid-LLC/toplance-mono/pull/26) added the export. The **runtime image never carried it** — the Dockerfile copies `drizzle/`, `migrate.mjs`, `sql-objects.sql` and `seed.sql`, so a deployed container can migrate its own database and still have no corridors to serve.

The only way to load them was handing someone a production connection string. That's the wrong shape of answer: the credential leaves Coolify, and it becomes a manual step somebody forgets.

## What changes

`corridors.sql` rides along in the image, and the post-deployment runner applies it.

Unlike the seed beside it, this runs on **every** deploy. It can, because it's additive by construction — every insert is `on conflict do nothing` on the corridor's natural key.

That property is the whole reason it's allowed to be a deploy step. Staging is where the 47 drafts get reviewed; a release step that reset someone's approvals would make the queue worthless.

Ordered after the seed so both starting points converge: on an empty database the seed writes its four and this skips those four on conflict; on a populated one the seed is skipped and this fills the gaps.

## Verified against three databases

| starting state | seed | this step | result |
|---|---|---|---|
| empty | writes 4 | adds 48 | 52 corridors, 5 live, 631 reqs |
| 4 corridors | skipped | adds 48 | 52 corridors, 5 live, 631 reqs |
| 52 corridors | skipped | adds 0 | unchanged |

And the one that actually matters. Between two deploys I approved `za/work` and rejected `jp/tourism` with a reason, then redeployed:

```
before   approved za/work · rejected jp/tourism · pending za/tourism
after    approved za/work · rejected jp/tourism (fee missing) · pending za/tourism
         52 corridors, 6 live
```

Both decisions intact, the reviewer's corridor still live, count unchanged.

684 tests pass, typecheck and lint clean.

## After merge

Redeploy staging. Corridors arrive with the release — no connection string, no manual step.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
