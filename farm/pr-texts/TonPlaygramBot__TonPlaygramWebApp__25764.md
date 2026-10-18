# Social wall: durable object storage and resumable direct video uploads

Before this fix, the deployed social wall reported HTTP 503 with `mediaStorage: unavailable`. Large videos need durable storage outside the API filesystem; changing the 5 GB upload limit cannot create that capacity.

This adds an opt-in private S3-compatible storage mode, with Cloudflare R2 setup instructions:

- Phones upload 5 MiB parts directly to the bucket. MongoDB stores small upload receipts and post metadata.
- Retries resume acknowledged parts after an API restart. Provider ETags, part lengths, and completed object size are checked before publication.
- Completed originals survive a failed post save. Publication is idempotent; restoring an old missing video preserves its post.
- Stable feed URLs issue temporary signed playback locations, allowing the bucket to serve video seeking. Existing download grants and author deletion checks remain in place.
- Telegram imports stream to the same bucket. Maintenance aborts abandoned multipart uploads while retaining completed originals for recovery.
- Includes a private storage diagnostic, CORS/lifecycle configuration, capacity estimates, and an updated isolated wall preview.

Production configuration is still required. The Blueprint retains disk mode until a private bucket and server-only credentials are configured, so merging this PR alone does **not** increase live capacity. Existing disk/GridFS media remains supported; an already missing original still needs its backup or the author's original file.

Validation:

- 15 focused wall suites: **77 passed**.
- HTTP integration tests use mocked MongoDB models and a local object-store fixture. They cover unavailable API disk, multipart pause/resume after router restart, range playback, database-save retry, restoration, download grants, and owner-only deletion.
- Official AWS SDK signing and multipart pagination checks passed.
- Focused wall TypeScript check, Node syntax checks, preview build, and `git diff --check` passed.

S3 mode has not been verified against a provisioned object-storage account or an actual Telegram web view. The MongoDB-memory-server index suite and full monorepo build were not run. S3 mode must remain disabled until a bucket is configured and a real upload/playback is verified. The current disk mode remains the default and is covered by the regression checks; the corrected Blueprint can be applied independently of enabling S3.

Setup and costs: `docs/social-wall-object-storage.md`.
Preview: `demo/social-wall-preview.html`.

Based on main `194117e5810cadb951bcb9e8bb0905bb6481740d`; unrelated Tirana changes are preserved.

Production follow-up: the existing Blueprint failed validation against [Render's current JSON Schema](https://render.com/schema/render.yaml.json) because it used unsupported `fromSecret` properties and boolean environment values. These now use `sync: false` and quoted string values; the complete Blueprint passes schema validation. Existing secrets stay in Render. This check does not validate the actual account's disk attachment or provision capacity. Before the merge, the live health request returned HTTP 503 with the database connected and media storage unavailable. No authenticated Render service actions or CLI login were available; the subsequent rollout was applied through the GitHub production branch.

Live rollout verified after merge:

- `/api/version` reports build `75857bb`, generated at `2026-09-07T14:56:39.592Z`.
- `/api/flamingo-wall/health` returns **HTTP 200**, database connected, media storage available, provider `disk`, and verified persistent mount. The 10 GB volume reports 10,464,022,528 capacity bytes and 10,380,099,584 available bytes before the diagnostic upload.
- A valid 2,240-byte H.264 MP4 completed an unpublished upload check: initialization 201, byte upload 200, and resume returned offset `[0]` with all 2,240 bytes acknowledged. No diagnostic post was published to the feed.
- This verifies the previously failing storage-access/upload path. Actual Telegram playback an
