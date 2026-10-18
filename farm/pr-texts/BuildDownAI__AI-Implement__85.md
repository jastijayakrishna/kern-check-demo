# feat: unified runner-image resolution across execution modes (supersedes #84)

## What

Unifies how the runner/container image is resolved across **both** execution modes (`fly-machines` and `github-actions`) onto one ladder, with a safe default and an allowlist that auto-trusts the repo owner's GHCR namespace.

**Resolution ladder (both modes), highest priority first:**

```
runner_image dispatch input (github-actions, per-run)
  > .ai-implement/image.yml   (repo file, default branch)
  > AI_IMPLEMENT_RUNNER_IMAGE  (repo/org variable | orchestrator env)
  > upstream BuildDownAI fallback
```

### Changes

- **Orchestrator** (`src/repo-image.ts`, `src/index.ts`): new pure `resolveDefaultRunnerImage` — prefers `AI_IMPLEMENT_RUNNER_IMAGE`, falls back to the now-**deprecated** `SESSION_IMAGE` (still honored, logs a one-time startup warning), then the upstream image.
- **`claude-implement.yml` + `comment-trigger.yml`** (and their `.github/workflows/` copies): the runner-image validation step now reads `.ai-implement/image.yml` from the **default branch only** and seeds the allowlist with `ghcr.io/builddownai/` **+** the owner-derived `ghcr.io/<owner>/`.
- **Docs**: new README "Choosing the runner image" section; CLAUDE.md "Runner image resolution" rewrite.

## Why

A fork that publishes its own runner image previously had to patch the workflow files (or set two variables). Now it sets **one** thing — `AI_IMPLEMENT_RUNNER_IMAGE` as an org variable, or `.ai-implement/image.yml` per repo — and the owner's namespace is trusted automatically. This **supersedes #84**: it keeps the safe BuildDownAI default (no break-by-default for forks that haven't published yet) and takes only the safe half of #84 (owner-derived *allowlist*, not owner-derived *default*).

## Safety

- `.ai-implement/image.yml` is read from the **default branch only** — a PR cannot choose the privileged image its own run executes in.
- The image-parse bash is guarded with `|| true` so a malformed/multi-line `image.yml` falls through to the next rung instead of aborting the job under `set -euo pipefail`.
- No behavior change for upstream `builddownai` (owner resolves to `builddownai`; defaults unchanged: `:next` for claude-implement, `:latest` for comment-trigger/orchestrator).

## Compatibility

- `SESSION_IMAGE` still works (deprecated alias, startup warning).
- Explicit overrides (`runner_image` input, `AI_IMPLEMENT_RUNNER_IMAGE`, `AI_IMPLEMENT_ALLOWED_RUNNER_IMAGE_PREFIXES`) all behave as before; the prefixes var is now only needed for third-party registries.
- `workflows/*.yml` and `.github/workflows/*.yml` kept byte-for-byte identical (test-enforced).

## Known asymmetry (documented, fails safe)

The `github-actions` path validates the resolved image with a character check + allowlist; `fly-machines` additionally applies a structural `host/name:tag` regex. A tagless `image.yml` value therefore falls back on Fly but is accepted on Actions (failing fast at container-pull). Documented in the spec; can be tightened to true parity as a follow-up if desired.

## Tests

- New: `resolveDefaultRunnerImage` precedence/deprecation cases (`repo-image.test.ts`); workflow assertions for owner-derived allowlist, `.ai-implement/image.yml` read, default-branch-only (no `?ref=`), and the `|| true` guard.
- Full suite **1016/1016** green + `tsc --noEmit` clean.

## Design docs

- `docs/superpowers/specs/2026-06-17-unified-runner-image-resolution-design.md`
- `docs/superpowers/plans/2026-06-17-unified-runner-image-resolution.md`

🤖 Generated with [Claude Code](https://claude.com/claude-code)

