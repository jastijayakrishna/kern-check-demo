# fix(shared): emit equal-sized S3 multipart parts from buffered uploader

<!-- aws-preview-pin:start -->
🟡 **Live preview: [pr-16754.preview.langfuse.com](https://pr-16754.preview.langfuse.com)**
<!-- aws-preview-pin:end -->

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## What does this PR do?

The buffered S3 multipart uploader flushed the entire accumulated buffer whenever it crossed `partSizeBytes`. Incoming stream chunks vary in size, so non-final parts could have different lengths.

AWS S3 accepts that. Stricter S3-compatible endpoints (notably GCS XML multipart) reject completion with `InvalidPart: All non-trailing parts must have the same length`, which failed blob-storage and core-data exports on the buffered path.

This change slices exact `partSizeBytes` parts and carries the remainder forward. Only the final part may be smaller.

## Type of change

- [x] Bug fix (non-breaking change which fixes an issue)

## Mandatory Tasks

- [x] Make sure you have self-reviewed the code.

## Checklist

- Code follows the style guidelines of this project
- Comments document the equal-part constraint for S3-compatible endpoints
- No documentation update required (internal uploader behavior)
- Lint passed for `@langfuse/shared` and `worker`
- Tests prove non-final parts are exactly `partSizeBytes` for uneven chunks and oversized chunks

## Impacted packages

- `@langfuse/shared` — `BufferedStreamUploader`
- `worker` — regression tests in `bufferedStreamUploader.test.ts`

## Verification

- `pnpm --filter worker run test bufferedStreamUploader.test.ts` — `Tests  42 passed (42)`
- `pnpm --filter @langfuse/shared run lint` — clean
- `pnpm --filter worker run lint` — clean
- Pre-commit `turbo run lint` — `Tasks:    7 successful, 7 total`

Skipped a targeted web test: this path is worker-only (`uploadFileBuffered` for blob-storage, batch export, and core-data S3 export). No web UI or tRPC surface changed.
<!-- CURSOR_AGENT_PR_BODY_END -->

Linear Issue: [LFE-15739](https://linear.app/clickhouse/issue/LFE-15739/buffered-s3-multipart-upload-emits-unequal-non-final-parts-invalidpart)

<div><a href="https://cursor.com/agents/bc-da1f817e-03ae-43c6-a6c6-2a748a2a75c4?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-da1f817e-03ae-43c6-a6c6-2a748a2a75c4&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>



<!-- greptile_comment -->

<details open><summary><h3>Greptile Summary</h3></summary>

This PR updates the buffered multipart uploader to emit uniformly sized non-final parts while retaining excess bytes for subsequent parts.
- Replaces whole-buffer flushing with exact-size slicing and a final remainder flush.
- Adds regression coverage for uneven input chunks and single oversized chunks.
</details>


<details><summary><h3>Confidence Score: 4/5</h3></summary>

The permitted non-integer multipart-size configuration can now make sufficiently large batch exports fail, so this should be fixed before merging.

The new explicit `Buffer.concat` length is reached from a configuration schema that permits fractional MiB values, and Node rejects the resulting non-integer byte length before any upload retry is scheduled.

**Files Needing Attention:** packages/shared/src/server/services/BufferedStreamUploader.ts
</details>

<details><summary>Prompt To Fix All With AI</summary>

``
