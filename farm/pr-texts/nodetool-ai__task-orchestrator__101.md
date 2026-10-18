# feat(runner): bake nodetool's env (npm install + Playwright) into the worker image

Agents currently pay a cold `npm ci` (nodetool's install is **~5 GB**) plus `npx playwright install` on the first action of *every* run, because the Fly runner image bakes only a git *mirror* — no `node_modules`, no browsers. This pre-warms the primary target repo at build time so runs start ready to go.

> Note: an accidental `readTurnEndState` change (a stray working-tree edit) was removed, and the branch was rebased onto current `main`, so this PR is purely the prewarm. Playwright/Chromium **is** baked — it adds only a few hundred MB, negligible next to the ~5 GB npm install.

## Image — `Dockerfile.fly-runner` + `scripts/build-prewarm.sh`
- **Base node 24 → node 22** to match nodetool's `engines` (`>=22 <23`). Its baked `node_modules` ships native modules (better-sqlite3) whose ABI must match the node the agent runs. Verified safe: task-orchestrator's own worker is pure JS (postgres.js, no native, no engines pin).
- Add nodetool's **native build toolchain** (`build-essential`, `pkg-config`, `libsecret-1-dev`, `python3-pip`). The runtime CLIs (ffmpeg, poppler, qpdf, pandoc, …) were already mirrored.
- `build-prewarm.sh`: clone the repo (reusing the blobless mirror as a `--reference`), full `npm ci`, `npm run build:packages`, and **Playwright Chromium + OS deps** into `PLAYWRIGHT_BROWSERS_PATH`. Chromium-only because that's the sole project in nodetool's `playwright.config.ts`. Never fatal — a missing repo/token or a failed step leaves the image usable (runs pay the cold install), mirroring `build-repo-cache.sh`.

## Runtime — `lib/prewarm.ts` + `lib/worktree-env.ts` + `lib/runs.ts`
- `containerCheckoutAt` (the single clone funnel) calls `applyPrewarmToCheckout`, which symlinks the baked `node_modules` tree (root **+ every nested workspace dir**) into the per-run checkout — **only when the checkout's git origin matches** the prewarmed repo, so it can never bleed into a different project.
- `linkNodeModulesTree` / `discoverNodeModulesDirs` generalize the worktree linker from top-level-only to the whole monorepo tree; `isolate-env` still gives a worktree a private install by unlinking every `node_modules` symlink.

## Pipeline
`PREWARM_REPO` (default `nodetool-ai/nodetool`) + `PREWARM_BUST` build-args wired into the push-to-main and nightly workflows so the baked deps refresh with the mirror.

## Test plan
- [x] `__tests__/prewarm.test.ts`: origin-match gating (links on match incl. ssh/case/`.git` variants; **no-op on a different repo**; no-op with no image / missing marker).
- [x] Extended `__tests__/shared-worktree-artifacts.test.ts`: discovers/links the full monorepo tree, prunes inside `node_modules`, never clobbers a private isolate-env dir, propagates nested workspace dirs into worktrees, unlink removes the whole tree.
- [x] `npx tsc --noEmit -p .` clean; full suite **988 passed** / 1 skipped.
- [ ] **Requires a real runner-image build + one live run to validate** end-to-end (image size, `npm ci` under node 22, Playwright resolution from a worktree).

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01ERytf1oyF5LHQUEgaA965q
