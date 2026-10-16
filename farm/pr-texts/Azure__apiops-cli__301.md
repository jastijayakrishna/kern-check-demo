# Improve extract and publish log readability: tier grouping, timing, and per-resource retry reporting

Extract and publish output was a flat, hard-to-scan stream. Extract silently dropped APIs that had no spec or operations. Neither command reported elapsed time. Retry warnings showed raw millisecond delays with no resource or attempt number, and they appeared between PUT lines.

### Publish output (before → after)

```
PUT namedvalue/src-nv-plain
Server error 503, retrying after 1175.1730686888397ms
PUT tag/tag1
--- Summary ---
2 creates/updates, 0 patches, 0 deletes, 0 skipped
```
```
── Tier 1: Independent resources (2) ──
PUT namedvalue/src-nv-plain (2 retries)
PUT tag/tag1
Tier 1 completed in 3.2s

--- Summary ---
2 creates/updates, 0 patches, 0 deletes, 0 skipped
2 retries across 1 resource
Completed in 12.3s
```

### Extract (`src/cli/extract-command.ts`)
- The `Extracted N <Type>(s)` / `Failed …` lines are grouped under `Tier N: <label>` headings.
- Every API is listed. APIs without a spec, operations or revisions show as `definition only`.
- The total line includes duration: `Total: 96 resources extracted, 0 errors in 12.3s`. The time covers extraction plus moving the files into the output directory.
- JSON `summary.elapsedMs` added.

### Publish (`src/services/publish-service.ts`, `src/cli/publish-command.ts`)
- Each tier gets a header and a `Tier N completed in …` line; delete tiers get the same, labelled `Delete tier N`.
  - The header count is the number of descriptors scheduled in the tier, after skipping auto-generated named values and children already published by their parent API or product.
  - It can differ from the number of PUT lines, because publishing an API or product also emits lines for its children.
- `PublishResult` gains optional `elapsedMs`, `totalRetries` and `retriedResources`; `PublishActionResult` gains `retries`. The existing function body moved into `runPublishPipeline` so these fields are filled on every return path.
- Text summary adds the retry line (only when retries occurred) and `Completed in …`.
- JSON summary adds `totalRetries`, `retriedResources` and `elapsedMs`; each action adds `retries`.

### Retries (`src/clients/apim-client.ts`)
- New message format: `Server error 503 on PUT namedValues/nv-1 (attempt 1/4), retrying in 1.2s`. The same format applies to 429s, network failures, and delete conflicts.
- `describeRequestTarget(url)` shortens ARM URLs to the path below the APIM service and drops query strings, so storage signatures never appear in logs.
- New `src/lib/retry-tracker.ts` counts retries per resource using `AsyncLocalStorage`, which keeps counts correct while resources publish in parallel.
  - Publish wraps each resource in `trackRetries()`.
  - The client calls `recordRetry()` on every retry.
  - Inside a tracked scope the retry message is logged at debug level; outside one it stays a warning.

### Shared helpers
- `src/lib/format-duration.ts`: formats times as `1.2s` or `2m 5.0s`.
- `TIER_LABELS` in `src/lib/dependency-graph.ts`, used by both extract and publish.

### Review notes
- **Behaviour change:** during publish, the individual retry messages only appear at `--log-level debug`. Extract and other callers still show them as warnings.
- **JSON mode:** publish already wrote PUT lines to stdout in `--format json` mode. The tier headers follow the same path; that existing problem is not fixed here.
- Per the repo's code-review requirement, this PR still needs the CodeReviewer step from `.squad/ceremonies.md`.

<!-- START COPILOT CODING AGENT SUFFIX -->

- Fixes #162
