# fix(youtube): search.list SINGLE key — remove cross-project quota rotation (ToS)

**CP512 P0 security.** `resolveSearchApiKeys` returned `YOUTUBE_API_KEY_SEARCH` + `_2..N` and `searchVideos` rotated to the next project's key on 403/429 quota — the YouTube ToS *"spread requests across projects to exceed quota"* violation (prod alarm 7/1, 8 active SEARCH keys). James disabled _2..8 in Console; this removes the code path that would use them.

- `resolveSearchApiKeys`: **single key** (YOUTUBE_API_KEY_SEARCH, legacy fallback); _2..N ignored. Return stays `string[]` (len 0|1) → callers unchanged.
- `searchVideos`: **drop the rotation loop**; use the first key only; on 403/429 surface the error (no spill). Trace + G5 alert preserved.
- Quota-exhaustion behavior: trend-collector already defers (no rotation); wizard/add-cards surface error to caller.
- videos.list untouched (VIDEOS pool = separate single key, CP492).
- Tests: single-key resolution + _2..N ignored + legacy + empty.

⚠️ **Order: deploy this BEFORE deleting the _2..8 Secrets (James).** Post-deploy: James runs 1 mandala-gen test.

BE tsc clean.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
