# chore(format): align oxfmt with sanity-io/ui (^0.71.0, config), pre-commit hook on lefthook

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
Brings oxfmt in line with sanity-io/ui's `main`: the same version, the same config, and the same scripts and CI wiring. The pre-commit hook moves from husky and lint-staged to lefthook, set up like sanity-io/sanity's. Supersedes #1919.

## Commits

1. **`chore(deps): update oxfmt to ^0.71.0`**: the catalog goes from ^0.63.0 to ui's ^0.71.0, with ui's oxfmt resolution: oxfmt 0.71.0 and `tinypool` 2.2.0, the same versions and integrity hashes as ui's lockfile. There's a patch changeset for `@sanity/plugin-kit`, whose optional `oxfmt` peer uses the catalog.
2. **`chore(format): align the oxfmt config with sanity-io/ui`**: root `oxfmt.config.ts` now ignores `storybook-static/**` and `CHANGELOG.md`, like ui's `.oxfmtrc.json`. `.vscode/settings.json` points `oxc.fmt.configPath` at `oxfmt.config.ts` instead of the `.oxfmtrc.json` that #1565 deleted. AGENTS.md records the parity with ui and the exceptions.
3. **`chore: drop the husky and lint-staged pre-commit hook, like sanity-io/ui`**: superseded by commit 6, which brings the hook back on lefthook.
4. **`chore(format): drop the oxfmt preset's .changeset/*.md override, like sanity-io/ui`**: the `@sanity/plugin-kit/oxfmt` preset loses its Prettier-era `singleQuote: false` override for `.changeset/*.md`, as ui's `.oxfmtrc.json` did when ui switched Changesets to oxfmt formatting (sanity-io/ui#2957). It gets a patch changeset for `@sanity/plugin-kit`, since the preset is published. This part moved here from #2046 because it's formatter config. AGENTS.md now explains how changesets get quoted.
5. **`chore(format): run pnpm format`**: requotes this PR's own changeset from commit 1. Everything else already passed under oxfmt 0.71.
6. **`chore: run oxfmt on staged files with lefthook, like sanity-io/sanity`**: see below.

## Pre-commit hook: husky and lint-staged → lefthook

This mirrors how sanity-io/sanity replaced husky and lint-staged (sanity-io/sanity#12755, then sanity-io/sanity#12767 and sanity-io/sanity#12953):

- **`lefthook` ^2.1.14** as a root devDependency, sanity's range. It resolves to 2.1.14, as in sanity's lockfile.
- **`allowBuilds: lefthook: true`** in `pnpm-workspace.yaml`, as in sanity. Lefthook's own install script runs `lefthook install` during `pnpm install`, and it skips when `CI` is set, which covers GitHub Actions and Vercel. There's no root `postinstall` script: sanity dropped its `lefthook install --reset-hooks-path` postinstall in #12767 for this package build.
- **`lefthook.yml`** with sanity's layout: a parallel `pre-commit` with two jobs that run oxfmt on staged files with `stage_fixed: true`. The jobs are `format-scripts` (`*.{js,jsx,ts,tsx,mjs,cjs,mts,cts}`) and `format-other` (`*.{md,yml,yaml,css,json,jsonc}`).
  - `mts`, `cts` and `jsonc` are additions to sanity's globs. They cover this repo's `.mts`, `turbo.jsonc` and `knip.jsonc` files, which the old lint-staged glob partly covered.
  - sanity's `oxlint --fix` line is left to the oxlint alignment (#2049).
- **Direct binary calls:** the jobs call `node_modules/.bin/oxfmt` instead of sanity's `pnpm oxfmt`. Running pnpm in a hook triggers pnpm 12's implicit install, which flips the lockfile's peer toggle (see AGENTS.md). sanity switched to `pnpm oxfmt` in #12953 because lefthook doesn't put `node_modules/.bin` on `PATH`; the path solves that too.
- **Lockfile:** `pnpm-lock.yaml` gains only lefthook 2.1.14 and its platform packages (100 lines). A plain install would also have bumped the Studio's `next` overrides from `6.17.0-next.108` to `6.17.0-next.112`, so I resolved it through a local registry proxy that served the locked versions as `next`, as AGENTS.md describes. The lockfile has no `localhost` or `tarball:` entries.
- **Docs:** AGENTS.md documents the hook, `LEFTHOOK=0`, the one-time reset for clones that ran husky, and `pnpm --config.verify-deps-before-run=false <script>` for local runs. README's note that formatting also runs in a pre-commit hook is back.

## Merges with `main`

`main` is merged in, not rebased, so nothing was force-pushed. After each merge, `pnpm-lock.yaml` is `main`'s lockfile regenerated with pnpm 12.6.0, invoked directly so `packageManagerDependencies` stays, minus the peer toggle that AGENTS.md describes.

- **#2039 (lock file maintenance):** only the lockfile conflicted.
- **#2048 (pnpm 12.6.0):** `package.json` conflicted next to the removed `lint-staged` block. The resolution keeps both sides: `main`'s `packageManager: pnpm@12.6.0` and `vercel` ^60.1.3, without the block. A follow-up commit restores `main`'s side of the peer toggle, which the regeneration had flipped.
- **#2046 (themer move):** only the lockfile conflicted. `pnpm format` then requoted #2046's three changesets in a separate commit: `dashboard-widget-vercel-xstate`, `shared-deps-sanity-ui-icons-motion` and `themer-plugins-monorepo`, 45 frontmatter lines, quote-only. The new `plugins/@sanity/themer` package and `dev/storybook` already passed.
- **#2053 (Version Packages):** it released and deleted those three changesets, so the modify/delete conflicts resolve to `main`'s deletions. It didn't change the lockfile, and `pnpm format` changes nothing after the merge.

`pnpm-lock.yaml` differs from `main` only by this PR's own changes:

- oxfmt and its bindings go from 0.63.0 to 0.71.0, and `tinypool` from 2.1.0 to 2.2.0.
- husky, lint-staged and their four exclusive dependencies are removed.
- lefthook 2.1.14 and its platform packages are added.

No other version moves, and the Studio stays on `6.17.0-next.108`.

## How it compares with ui

- **Options:** identical, overrides included (`printWidth`, `semi`, `singleQuote`, `bracketSpacing`, `quoteProps`, `sortImports`, `sortPackageJson`). They come from the `@sanity/plugin-kit/oxfmt` preset.
- **Ignore patterns:** `dist/**`, `storybook-static/**`, `pnpm-lock.yaml` and `CHANGELOG.md` in both. Two differences remain:
  - `turbo/**/*.hbs` is plugins-only (the turbo generator templates).
  - ui's `**/sanity.types.ts` is left out. In ui it was for `apps/docs/sanity.types.ts` and has matched nothing since the docs app went static. Here, `pnpm typegen` formats `dev/test-studio/sanity.types.ts` on purpose: the test studio runs typegen with `formatGeneratedCode: false` and then `pnpm format`. Ignoring the file would make the next TypeGen PR unformat it.
- **Config file:** plugins keeps `oxfmt.config.ts` re-exporting the published preset instead of ui's `.oxfmtrc.json`. #1565 made that switch so the preset is exactly what the monorepo formats with, and plugin-kit's `verify-package` expects plugins to use it. oxfmt, the Oxc extension and Changesets' formatter detection all read `oxfmt.config.ts`. See the open question.
- **Scripts and CI:** the `format` script is identical to ui's (`oxfmt . --no-error-on-unmatched-pattern`). Neither repo checks formatting on PRs, and both run the same shared `format-if-needed.yml` on `main`, so no workflow changes are needed. `oxfmt .` also formats `.github/workflows/*.yml`, which that workflow can't push, and 0.71 changes none of them. ui has no pre-commit hook; this repo keeps one, on lefthook.
- **VS Code:** ui points `oxc.fmt.configPath` at its config file, but plugins pointed it at a file that doesn't exist. I drove `oxfmt --lsp` directly: with the old setting, the editor silently formats with oxfmt's defaults (double quotes, semicolons, bracket spacing, unsorted imports), and with `oxfmt.config.ts` it matches `pnpm format`.

## Changesets

- **Changesets formats what it writes with oxfmt.** `.changeset/config.json` sets `"format": "oxfmt"` (from #2046). I called `@changesets/write` (what `changeset add` uses) directly. With the override it writes `"@sanity/plugin-kit": patch`; without it, `'@sanity/plugin-kit': patch`, the same as `pnpm format`.
- **`changeset version` is unaffected.** It only hands `CHANGELOG.md` files to the formatter. This PR ignores those, and oxfmt skips them and exits 0 thanks to `--no-error-on-unmatched-pattern`.
- **`changeset status` parses the single-quoted frontmatter.** It lists this PR's two changesets for `@sanity/plugin-kit` 10.0.11.

## What to expect after merging

- **Renovate changesets get a follow-up format PR, as in ui.** The shared Renovate changesets workflow uses `mscharley/dependency-changesets-action`, which always writes double quotes and has no formatting option. After a Renovate PR merges, the Auto format workflow opens (or updates) a `chore(format): 🤖 ✨` PR that requotes the changeset. ui has had one after most Renovate merges since sanity-io/ui#2957: sanity-io/ui#2971, sanity-io/ui#2980, sanity-io/ui#2986, sanity-io/ui#2998, sanity-io/ui#3002, sanity-io/ui#3013 and sanity-io/ui#3024.
- **Clones that ran husky need a one-time reset.** They still have `core.hooksPath=.husky/_`. There, `lefthook install` refuses to install and prints how to fix it, and `pnpm install` continues. Until the reset, husky's leftover runner does nothing, so commits simply aren't formatted. `git config --unset core.hooksPath && pnpm install` fixes it.

## Related PRs

- **#1919** (Renovate, oxfmt ^0.71.0): superseded. This PR has the same bump, with the lockfile regenerated on current `main`, plus the config alignment. Close it if Renovate doesn't once this merges.
- **#2046** (themer move) and **#2048** (pnpm 12): merged, and merged into this PR.
- **#2049** (oxlint) conflicts with this PR in `pnpm-workspace.yaml`, where its `oxlint` catalog lines sit next to `oxfmt`. Keep both sides. It could also add sanity's `oxlint --fix` line to the `format-scripts` job, calling `node_modules/.bin/oxlint` directly.
- **#2050** (vitest 5) conflicts only in `pnpm-lock.yaml`.
- **#2051** (tsdown) doesn't conflict.
- Whichever PR lands later merges `main` and regenerates the lockfile without committing the peer toggle.

## What Cody needs to do

- Add the `🤖 bot` label: the agent's label tool couldn't edit PRs in this repository.
- Triage Socket's alert. It flags `lefthook@2.1.14`'s install script (`node postinstall.js`) as a low-priority warning. That script is what installs the hook: `allowBuilds: lefthook: true` enables it, as in sanity-io/sanity, and it skips when `CI` is set. Mark it as acceptable risk if you agree. Socket's required checks pass either way.
- After merging, tell contributors to run `git config --unset core.hooksPath && pnpm install` once, so lefthook replaces husky's hook.
- Merge the Renovate follow-up format PRs as they come, as in ui.
- No Vercel, secrets or ruleset changes, and no new secrets or env vars.

## Open question

**`.oxfmtrc.json`:** should plugins switch to ui's JSON config file, too? That would mean no longer re-exporting the plugin-kit preset, and it would reverse #1565. I kept `oxfmt.config.ts`, since the formatting result is already the same as ui's.

## Verification

- **The hook**, tested on throwaway commits, with `pnpm-lock.yaml` untouched each time:
  - Staged TS and JSON files get formatted and re-staged.
  - A tracked `.vscode/settings.json` (its folder is gitignored) is re-staged without the `[FAILED]` that lint-staged printed.
  - A staged `CHANGELOG.md`, which oxfmt ignores, passes as-is.
  - In a partially staged file, only the staged hunk is formatted and the unstaged hunk is kept.
  - The commit that adds the hook ran it on its own files in 0.4 seconds.
- **Clones that ran husky:** with `core.hooksPath=.husky/_`, `lefthook install` exits 1 with instructions and installs nothing, as described above.
- **Local checks** at the head commit, with pnpm 12.6.0 on Node 24.21 and `CI=true` (lefthook's install script skips):
  - `pnpm install --frozen-lockfile`, which leaves `pnpm-lock.yaml` untouched
  - `oxfmt --check` (2,018 files)
  - `oxlint` and `knip`
  - the full turbo build (54 tasks)
  - `vitest run` (235 files, 1,509 tests)
  - `pnpm test:browser` (4 files, 7 stories)
- **CI** is fully green at the head commit (`123af257`): build, lint, knip, all four test shards, coverage, `storybook-test`, both e2e browsers, Bugbot, and both Vercel checks, whose installs run lefthook's install script. The branch is up to date with `main`.
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-0b8c4f47-d9af-5929-8254-d25847e7e2dd?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-0b8c4f47-d9af-5929-8254-d25847e7e2dd&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
