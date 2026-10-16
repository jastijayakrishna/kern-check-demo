# fix: autoincrement unpublished npm version on release publish

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Problem

Publishing a GitHub release fails when `package.json` still has a version that is already on npm:

```
npm error You cannot publish over the previously published versions: 1.4.8
```

That happened on the `v1.5.0` release: the tag was `1.5.0`, but `package.json` was still `1.4.8`.

## Change

The release workflow now chooses an unpublished version before `npm publish`:

1. Prefer the GitHub release tag (`v1.5.0` → `1.5.0`) when it is valid semver.
2. Otherwise use `package.json`.
3. If that version is already on the registry, increment the **patch** until it is free.
4. Apply the version once in the build job and share it with both npm and Nexus publish jobs.

`package.json` is also bumped to `1.5.0` so it matches the intended release.

## How to publish next time

- Create a GitHub release tagged with the version you want (`v1.5.0`, `v1.6.0`, …).
- You no longer need to remember to bump `package.json` first.
- Use a new major/minor in the **tag** when you want more than a patch bump.
- Re-running a release whose version is already on npm publishes the next patch (for example `1.5.0` → `1.5.1`).

## Tests

Unit tests cover tag vs `package.json` vs already-published versions. Live registry check: `v1.5.0` resolves to `1.5.0` because npm latest is still `1.4.8`.

<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-8da0e77e-2585-4d88-b8c7-6c5f723f8173?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-8da0e77e-2585-4d88-b8c7-6c5f723f8173&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
