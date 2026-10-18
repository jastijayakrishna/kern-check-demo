# fix(editor): stop a concurrent photo-swap from reverting a caption edit

## Problem

Feedback `d6b2b24d` (Philip Abraham, `movebetter`): "The caption changed without clicking regenerate. It was shorter and without the dashes... the text changed and added dashes and more writing. I believe it occurred when I changed the photo and zoomed in."

A Facebook single-photo post is archetype `visual` → SlideEditor → CaptionPanel.

## Root cause (a stale-echo cache race)

SlideEditor fires **independent** `content_items` PATCHes for a caption edit (`{content}`) and a photo swap (`{mediaUrls}`) / zoom (`{slides,…}`) — separate `useUpdateContentItem` calls, no ordering guarantee. Every PATCH echoes the **full row** (`select=*`). If the photo-swap echo is read server-side before the caption commits, its `content` is the *pre-edit* value. `useUpdateContentItem.onSuccess` did `setQueryData(detail, echo)` — blindly writing that whole stale echo into the cache, reverting the caption. CaptionPanel's re-seed effect then saw `content` regress and clobbered the textarea back to the longer/em-dashed generated caption; a later blur could persist it.

The **DB never loses the edit** — the two PATCHes write *different columns* (`content` vs `media_urls`), so the row ends consistent. This was purely a client-cache artifact of overwriting with a full echo.

## Fix

`mergePatchedContentRow(prev, echo, patch)` merges into the detail cache **only the columns the patch actually wrote** (camelCase→snake_case, matching `api/_routes/db/content.js`'s `allowed` map) plus the authoritative `updated_at`/`moment`. A media-only PATCH can no longer overwrite `content`. Server side-effect columns (`approved_by`, `model_marked_at`, …) are reconciled by the existing `contentItems.all` invalidation refetch.

- **Regenerate unaffected** — separate `useRegenerateContentItem` hook (invalidate-only, no `setQueryData`).
- Both PATCH orderings now converge with neither edit lost.

## Verification

- `tests/lib/mergePatchedContentRow.test.js` — 6 cases incl. the exact race; **mutation-proven** (reverting to the naive whole-row replace fails 4/6).
- `lint` / `typecheck` / `build` green.
- Live repro + fix confirmation on a disposable draft in prod pending post-deploy (Chrome).

🤖 Generated with [Claude Code](https://claude.com/claude-code)

