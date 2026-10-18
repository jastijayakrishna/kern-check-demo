# fix: show SFW minor-flagged content at mature browsing levels

## Problem

The `disableMinor` browsing-settings addon (fires when the browsing set includes R/X/XXX) enforced a blanket `minor != TRUE`, dropping **every** row whose `minor` boolean is true — including fully SFW (`nsfwLevel` PG/PG-13) content such as clothed anime child characters. On `.com` the browsing level is capped to SFW so `disableMinor` never fires and the content shows; on `.red` mature levels are allowed, `disableMinor` fires, and the SFW content is hidden. Reporters browsing `.red` at a mature level saw it missing (FD #66144 / #66064 / #65925).

Not caused by the blocked-browsing-tags work (PR #3041) — the example content carries the `minor` boolean but none of the blocked child tags.

## Policy (ClickUp 868kbr0dt)

Hide minor-flagged content **only when it is also mature** (`nsfwLevel` > PG-13). SFW minor content (PG / PG-13) is visible at **all** browsing levels. `.red` retains full content-level control including SFW-only.

## Change

Replace the blanket `minor` filter with an nsfwLevel-gated one at every enforcement site. Boundary: SFW = `sfwBrowsingLevelsFlag` / `sfwBrowsingLevelsArray` = {PG (1), PG-13 (2)}; mature = R/X/XXX. New rule: hide the row only if `minor` **and not** SFW.

- SQL: `(minor != TRUE OR (nsfwLevel & sfwBrowsingLevelsFlag) != 0)`
- Meili: `((NOT minor = true) OR nsfwLevel IN [1,2])`
- Client: drop iff `minor && minorDisabled && !hasSafeBrowsingLevel(nsfwLevel)`

### Enforcement sites changed

**Server — `src/server/services/image.service.ts`**
- `getAllImages` (DB) `:1457` — `(i."minor" != TRUE)` → `(i."minor" != TRUE OR (i."nsfwLevel" & sfwBrowsingLevelsFlag) != 0)`
- `getImagesFromSearchPreFilter` (Meili) `:3158` — `(NOT minor = true)` → `((NOT minor = true) OR nsfwLevel IN [sfw])`
- `getImagesFromBitdexPreFilter` (Meili helpers) `:3806` — `_not(_eq('minor',true))` → `_or(_not(_eq('minor',true)), _in('nsfwLevel', sfw))`
- `getImagesFromSearchPostFilter` (Meili) `:4025` — `(NOT minor = true)` → `((NOT minor = true) OR nsfwLevel IN [sfw])`
- `getImagesForPosts` (DB, post feed) `:5409` — `(i."minor" = false OR i."minor" IS NULL)` → adds `OR (i."nsfwLevel" & sfwBrowsingLevelsFlag) != 0`

**Server — `src/server/services/model.service.ts`**
- `getModelsRaw` (DB) `:444` — `${pSql}."minor" = false` → `(${pSql}."minor" = false OR (${pSql}."nsfwLevel" & sfwBrowsingLevelsFlag) != 0)`

### Additional enforcement paths found beyond the spec's list

The spec enumerated only the 6 server sites. Grepping broadly surfaced a **load-bearing client-side layer** that would have re-dropped the now-served SFW-minor rows, making the fix invisible in the UI. Gated for consistency (same policy, same fail-closed semantics):

- `src/components/HiddenPreferences/useApplyHiddenPreferences.ts` — the post-fetch feed filter (`filterPreferences`). 9 `minor && minorDisabled` drop sites across models, model images, images, article covers, collection covers + images, bounty images, post images, and model3d — each now `&& !hasSafeBrowsingLevel(nsfwLevel)`. This is the "post feeds / collection feeds" path. Without it the server changes have no visible effect.
- `src/pages/search/images.tsx` and `src/components/AutocompleteSearch/AutocompleteSearch.tsx` — raw Meili InstantSearch filter strings (`'minor != true'`) → `(minor != true OR nsfwLevel IN [sfw])`.

The search-index service wrappers (`image-search.service.ts`, `model-search.service.ts`) only set `disableMinor: true` and delegate to the covered functions — no separate predicate, no change needed.

## Safety reasoning

This LOOSENS a minor-content filter, so the failure mode hunted was any path letting a **minor + mature** row through.

- **SFW flag is exactly {PG, PG-13}** (`sfwBrowsingLevelsArray`), bit-disjoint from every mature bit (R/X/XXX) — unit-tested. The bitwise `& sfw != 0` / `IN [1,2]` tests cannot match a mature-only row.
- **NULL / 0 nsfwLevel fails closed to HIDDEN.** SQL: `NULL & flag → NULL`, and `false OR NULL → NULL` → WHERE drops the row; `0 & flag → 0
