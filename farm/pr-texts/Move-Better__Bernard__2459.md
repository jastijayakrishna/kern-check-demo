# fix(auto-attach): default text-first drafts to a photo, not a video

## Problem

Feedback (P1, Philip Abraham III, `movebetter`): *"Drafted a linkedin post but reel template and editor came up."*

A media-less LinkedIn draft got a 25.2s video (`IMG_4614.mov`) auto-attached at draft-creation time (confirmed: `updated_at` ~780ms after `created_at` — the auto-attach signature). `resolveArchetype` then correctly routes any single-visual platform + video to `lvideo` → the reel/timeline editor. **The resolver is right** (SlideEditor is photo-only and would silently drop the video, per #2174/#2307) — the bug is upstream: auto-attach picked a *video* for a post the user drafted as text/photo.

Root cause: `mediaKindForDraft('linkedin')` returns `null` (= "either kind"), so auto-attach's `searchClips` ranked photos and videos together on similarity and grabbed a video.

## Fix

New `autoAttachKindForDraft(piece)`: for the single-photo-default social platforms (the `visual`-archetype set — linkedin, facebook, gbp, x, threads, bluesky, mastodon, pinterest, reddit, discord, slack), **auto-attach defaults to a photo**. Instagram stays dual (a Reel is an expected IG format).

This is a **photo-*default*, not a capability block** — LinkedIn/Facebook/X/GBP all support native video. Video stays one manual click away in the picker, which keeps showing both kinds (`mediaKindForDraft`, used by the manual suggest panel + the DraftContextPanel hint, is **unchanged**). If no photo clears the confidence bar, the draft is left media-less (the existing amber "needs media" cue) rather than getting a surprise video.

Product direction (photo-only auto-attach + all single-visual text platforms, IG excluded) confirmed with Q.

## Files
- `src/lib/platformMediaKind.js` — `autoAttachKindForDraft` + `PHOTO_DEFAULT_AUTOATTACH`
- `api/_lib/autoAttachMedia.js` — use it in place of `mediaKindForDraft` (covers both the inline draft path and the `attach-draft-media` cron)
- `src/lib/editorArchetype.js` — export `PLATFORM_ARCHETYPE` so the set is drift-guarded against the archetype map
- `tests/lib/autoAttachKind.test.js` — behavior + a **self-maintaining** drift guard (any new `visual` platform missing from the set fails the test)

## Verification
- typecheck, lint (0 warnings), **850 tests**, build, **277/277 bundle smoke** — all green.
- Drift guard **proven to fail** (removed `linkedin` from the set → red with the exact message), then restored.
- **OLD-vs-NEW on movebetter's live library** (real embeddings + vector search, "Neck pain" draft): OLD (`kind:null`) → 3 candidates, all videos, picked a video (the exact reported `IMG_4614.mov`). NEW (`kind:photo`) → 0 candidates cleared the bar → draft left media-less (needs-media cue), never the reel editor.

## Notes
- The one existing wrong draft (`69d0cede-…`) still carries its video (a valid on-topic post that now correctly opens the reel editor). This PR prevents future surprises; that row is left as-is — the user can keep or swap it manually. Say the word to reset it to media-less.
- For "Neck pain" specifically, no photo in the 524-photo library scored ≥0.45, so that draft shows the needs-media cue rather than an auto-photo — the intended honest-gap behavior (no filler). If media-less drafts become common, the `AUTO_ATTACH_MIN_SCORE` bar (0.45) is the lever.

Fixes feedback `f7fc5daf-c017-470e-b513-7bb20c463252`.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

