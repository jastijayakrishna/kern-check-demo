# Re-anchor starter patch on the rewritten chat template and hand it to agent-native

Template syncs into `main` fail at the starter-patch step ([run 37627091103](https://github.com/BuilderIO/builder-agent-native-starter/actions/runs/37627091103)) with `expected snippet not found in AGENTS.md`. [agent-native#6872](https://github.com/BuilderIO/agent-native/pull/6872) rewrote the chat template's `AGENTS.md`, its `package.json` scripts, and the `storing-data`, `adding-a-feature` and `frontend-design` skills, and it deleted `self-modifying-code`. That broke 20 replacements and assertions. `main` is stuck on the core 0.202.0 sync until this merges.

This is the third repair PR for this kind of drift in about 10 days, after #409 and #413. So this PR also hands the patch to agent-native: [BuilderIO/agent-native#6930](https://github.com/BuilderIO/agent-native/pull/6930) adds the identical patch as `starters/fusion/`, runs it in agent-native CI on every PR that touches the Chat template or core, and copies it here on every mirror.

## Commit 1: re-anchor on #6872's rewrite

**Mechanical re-anchors**
- **`AGENTS.md`:** the intro, the `navigation` line, and the multi-app-workspace paragraph now anchor on the single `## Core rules` heading, which upstream lowercased. I updated the `CLAUDE.md` duplicate check to the new heading too, because the old one could no longer fire.
- **`package.json`:** the db scripts anchor only on the `test` line.
- **`adding-a-feature`:** the copy/i18n paragraph is re-anchored. The starter's English-inline wording is unchanged.

**Places where upstream now contradicts the starter**
- **`AGENTS.md` "Building a domain app":** upstream tells the agent to:
  - edit `Sidebar.tsx` and `Header.tsx`
  - keep `/home` as Chat
  - not rewrite `README.md`

  The starter deletes those files and the `/home` route, and `DEVELOPING.md` asks for the README rewrite. Both paragraphs are replaced with blank-canvas guidance. I also dropped the rooms-specific "overlap rejection, cancellation freeing the slot" wording.
- **`build-an-app`:** it picks `edit-points-chat.md` from `scaffold.template: "chat"`, which the starter still reports. The `chat` line now sends agents to `AGENTS.md`, `DEVELOPING.md` and `drizzle/START_HERE.md`. The file is added to `owned.txt`.
- **`storing-data`:** upstream says "the Chat and default starters do not ship that Drizzle Kit setup". The managed Drizzle scaffold is again the only migration owner.
- **`self-modifying-code` (deleted upstream):** its four replacements are gone. The batch-verification table moves into a `## Verification` section in `DEVELOPING.md`.
- **`frontend-design`:** the starter's "no brand system" paragraph is re-anchored onto the new design-system paragraph. Two replacements are dropped because upstream removed or now covers what they patched.

## Commit 2: convert to TypeScript and match agent-native's copy
- **`apply.mjs` becomes `apply.ts`:** agent-native allows no new `.mjs` sources.
  - `sync.yml` already sets up Node 24, which runs `.ts` directly.
  - `verify-starter-patch.yml` now sets up Node 24 too.
- **The content is byte-identical to agent-native's `starters/fusion/`:**
  - oxfmt formatting
  - Agent-Native branding
  - UTM-tagged links in the shipped README
  - `coercion-ok` notes on two catches that intentionally treat failure as absent
- **The README states the new rule:** edit the patch in agent-native, because the mirror overwrites this directory.

## Verification
Done on a local copy of the `template` tree:
- The `verify-starter-patch.yml` script passes. That covers the pristine tree, idempotence, and migration from the current `main`.
- A fresh patched tree also passes the steps `sync.yml` runs afterwards:
  - `pnpm install --no-frozen-lockfile`, which resolves `@agent-native/otel@0.1.0`
  - `pnpm typecheck`
  - `pnpm build`
  - `agent-native doctor` reports no findings.
- `apply.ts` passes strict `tsc` against `@types/node`.

## Rollout
Merge this before agent-native#6930, or at the same time. After both merge, run "Sync template into main" here, or wait for the next `template` push, to pick up the 0.203.0 sync.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01RUDitSt3FB37KqMKfQgkJj
