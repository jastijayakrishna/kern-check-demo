# fix(daemon): audit and write workspace git config through the runner

Closes the remaining in-scope gap of #815, flagged on #835.

## What

`assertSafeWorkspaceGitConfig` and `writeRepoHelperConfig` were the last two helpers reaching local git directly — both took a cwd and built their own simple-git. Both now take a `GitRunner`, and all eight call sites pass one from the seam.

For the audit this is not merely inconsistent, it is **the check running on the wrong machine**. It exists to reject a checkout-owned network override or executable setting *before* the daemon runs git on that checkout. So it has to read the config that the guarded git will actually read — and for a cluster workspace that config lives on the sandbox pod. Auditing this daemon's disk would have reported safe while the real config was hostile: a security check that passes by looking somewhere else.

## The test

Pinned in both directions, because only one of them is the interesting one:

- clean local checkout + runner reporting `filter.generated.process` → **must refuse** (it follows the runner)
- **unsafe** local checkout + runner reporting clean → **must pass** (this is what proves the local disk is no longer consulted)

Reverting the helper to read a cwd fails that test along with every other audit test in the file.

## Verification

- 330 tests across the git-injection, workspace, session-manager, shim, cluster and daemon-hook suites
- typecheck, eslint, prettier, build clean; shim bundle still `node:`-only

## #815 after this

The migration is complete: no workspace git path reaches simple-git outside the seam. What remains there is not migration work but two open decisions, recorded on the issue — `setWorkspaceGitRunnerResolver` still has no production caller (that is the cloud wiring, not this seam), and `env` remains a trusted input on the exec channel, which cannot be filtered without moving credential-helper and `hooksPath` policy into the shim.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
