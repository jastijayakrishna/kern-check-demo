# fix(grove-content-drafter): open draft requests every 15 min, not nightly

## Before you open this PR

- [x] Self-contained — no unmerged dependencies
- [x] Ran the smallest local verify that proves this change
- [x] Expect CI to be green

## What & why

The Odoo product form tells whoever clicks **Request draft**: *"the drafter polls every 15 min; expect a draft within ~20 min."* But `content-draft-request`, the job that opens the Paperclip issue for Sora, ran **once a day at 07:00 UTC**. A request could sit up to about 24 hours with nothing on the board.

Hit on 2026-09-30: American Chestnut (`product.template` 93) was requested at 20:22Z, and Josh saw nothing in Paperclip. It was picked up only after a manual `POST /api/plugins/:id/jobs/:jobId/trigger` at 22:10Z; the drafter's Odoo user signed in at that exact second. `content-draft-sweep` (every 20 min) only harvests replies for issues that already exist, so it can't cover this gap.

- `content-draft-request` schedule changes from `0 7 * * *` to **`*/15 * * * *`**. This is safe:
  - the request run is idempotent: a product-scoped `originId` (`pt#<id>`) allows only one open request per product, and the drafted-version marker means a product+version is never redone;
  - each run stays capped by `maxDraftsPerRun`.
- Manifest version `0.2.0` → **`0.2.1`**, per the "bump on every manifest change" convention. `dist/manifest.js` is rebuilt; `dist/worker.js` came out byte-identical. The README cadence line is updated.

**To take effect:** reinstall the plugin on Paperclip, using the delete + install path for plugin updates. The live instance is `agenticos.grove-content-drafter`, id `f071f43f-…`, currently v0.2.0. Afterwards, confirm the `content-draft-request` job reads `*/15 * * * *` and its `nextRunAt` is within 15 minutes.

## Verification

- `pnpm run typecheck`: clean.
- `pnpm run test`: 6 files, **41 passed**.
- `pnpm run build`: `dist/manifest.js` shows `version: "0.2.1"` and `schedule: "*/15 * * * *"`. The diff is the manifest, its bundle and the README only.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
