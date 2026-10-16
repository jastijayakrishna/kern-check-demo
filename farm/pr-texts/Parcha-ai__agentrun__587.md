# feat(pi-durable-agent): the agent home follows its repo at a sha

## Why

An agent's definition and skills can live in a git repo (an `agent.json` and its skill files), with the agent home as their cache. Nothing recorded which commit the cache was read from, or which commit a run's skills came from. So a run could start on skills older than the ones the host meant, and after the fact nobody could say which version of the agent a run used.

## What

The package still does not read git. The host reads the definition and the skill files at a commit and passes them in with the commit's sha: 40 or 64 lowercase hex digits, a SHA-1 or SHA-256 commit. Anything else is refused as `invalid`.

- **New singleton kind `agent.source`**: `{ sha, refreshedAt }`, the commit the cached definition and skills were read from.
  - It is written in the same commit as the files it describes.
  - It is absent for a home not tied to a repo, every home made before this. The change is additive: no format version change.
- **`createAgentHome(dir, { definition, skills, sha })`** writes `agent.source` in the creation commit.
- **`refreshAgentHome(home, { sha, definition, skills })`** is a host step: one commit under the home's lock.
  - It validates the way creation does.
  - The definition's `id`, if given, must be the agent's, and `identity.name` follows the new `name`.
  - The skill set is replaced: a skill path not in the new set is retired with pi-durable's `retireDoc`.
  - At the sha the home already has, it changes nothing and returns `{ changed: false }`: a sha names one content.
  - **`from`** makes it a compare-and-swap, checked under the lock before anything is written:
    - the home's sha must equal `from`, or the refresh is refused `stale`, naming both shas;
    - `from: null` means the home has no sha yet;
    - omitting `from` means no check;
    - the same-sha no-op applies after the check.

    A host that read an older commit cannot move the cache back over a newer one. Whether one commit follows another is the host's call, from git, not the package's.
- **`startRun`** records the home's sha on the run and returns it as `RunStart.sha`.
  - The sha is read under the same lock as the skills it copies into `work/.agents/skills`, so the recorded sha always names the copied skills.
  - With `options.sha`, a cache at another commit, or at none, is refused with the new `AgentHomeError` code `stale`. The run starts only after the host refreshes.
- **`carryBack`** keeps the sha on the run record.
- **Export:** `agent.source` is on `EXPORTABLE_KINDS`, so the existing guard test classifies it. An exported run keeps its sha, and its `host` is still stripped.
- Types `AgentSource` and `RunRecord.sha` are exported, and `AgentHomeState` gains `source?`.
- A README section, "Following the agent's repo", and a changes fragment.

## Before / After

| | Before | After |
|---|---|---|
| Which commit the cached definition and skills came from | Not recorded | `agent.source.sha`, written in the same commit as them |
| Which commit a run's skills came from | Not recorded | `sha` on the run record and on `RunStart` |
| Updating the cache from the repo | No API; a host would rewrite documents itself | `refreshAgentHome`, one commit, skills replaced as a set |
| A run asked at a commit the cache does not have | Starts on whatever is cached | Refused, `stale`, until the host refreshes |
| Two hosts refreshing from different commits | Last writer wins, possibly moving the cache back | `from` makes a refresh conditional on the sha the host read |

## Evidence

- `@parcha/pi-durable-agent`: build, typecheck, and 66/66 tests on Node 22.23.2 and on Node 24.21.0. That is the 56 existing tests plus 10 new ones.
- One commit, checked on pi's own records:
  - The tests read the agent store's `durable_metadata` and `document_revisions` through a read-only connection.
  - A refresh advances the store by exactly one commit, and in that commit `agent.source`, the definition, the identity and both kept or new skills changed. The removed skill was retired in the same commit.
  - Creation is one commit, and a same-sha refresh adds none.
- Mutations, each failing at least one test:
  - the sha dropped from the run record;
  - a refresh that keeps an absent skill;
  - `startRun` skipping the sha check;
  - `agent.source` written in its own commit after a refresh's;
  - `agent.source` written in its own commit at creation;
  - a refresh that ignores the same sha;
  - the `from` check removed;
  - the same-sha no-op moved ahead of the `from` check;
  - `from: null` treated as no check.
- `node scripts/changes.mjs --check`: valid. `npm run export:source`: passed, 0 findings.

## Test plan

- [x] `npm run build -w @parcha/pi-durable-agent && npm run typecheck -w @parcha/pi-durable-agent && npm test -w @parcha/pi-durable-agent` (Node 22 and 24)
- [x] Create with a sha keeps `agent.source`; `startRun` records it and returns it; `carryBack` keeps it
- [x] A mismatched sha, and a sha for a home with none, are refused `stale` and start nothing
- [x] A refresh replaces the definition and skills (one removed, one new), renames the identity and moves `agent.source`, all in one commit; another agent's id is refused; a same-sha refresh changes nothing and commits nothing
- [x] A run started before a refresh keeps its sha and its workspace skills; the next run gets the new ones
- [x] `projectForExport` keeps `agent.source` and a run's sha, and strips its host
- [x] Bad sha shapes are refused by create, refresh and `startRun`
- [x] `from`:
  - a matching `from` refreshes;
  - a mismatched one, and `null` on a home with a sha, are refused `stale` with nothing written and no commit;
  - `null` on a home without a sha refreshes;
  - an omitted `from` does not check.
- [x] Nine mutations
- [ ] CI: the verify matrix and the pi version legs

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- codesmith:footer -->
---
<a href="https://app.blacksmith.sh/Parcha-ai/codesmith/agentrun/pr/587?autoLogin=true&ref=codesmith_pr_footer"><picture><source media="(prefers-color-scheme: dark)" srcset="https://pr-comments-assets.blacksmith.sh/codesmith/view-with-codesmith-dark-v3.svg"><source media="(prefers-color-scheme: light)" srcset="https://pr-comments-assets.blacksmith.sh/codesmith/view-with-codesmith-light-v3.svg"><img alt="View with [code]smith" src="https://pr-comments-assets.blacksmith.sh/codesmith/view-with-codesmith-dark-v3.svg"></picture></a> <a href="https://backend.blacksmith.sh/track/enable-autofix?expires=1794717459&installation_model_id=431113&pr_number=587&ref=codesmith_pr_footer&repository=Parcha-ai%2Fagentrun&return_to=https%3A%2F%2Fgithub.com%2FParcha-ai%2Fagentrun%2Fpull%2F587&signature=31c63080525fc012c76722d987888088dc5b0fed4a57b0eaf8a2f8e1067ecb91"><picture><source media="(prefers-color-scheme: dark)" srcset="https://pr-comments-assets.blacksmith.sh/codesmith/autofix-with-codesmith-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://pr-comments-assets.blacksmith.sh/codesmith/autofix-with-codesmith-light.svg"><img alt="Autofix with [code]smith" src="https://pr-comments-assets.blacksmith.sh/codesmith/autofix-with-codesmith-dark.svg"></picture></a>
<sup>Need help on this PR? Tag <code>@codesmith-bot</code> with what you need.</sup>

<!-- codesmith:autofix:disabled -->
<!-- /codesmith:footer -->
