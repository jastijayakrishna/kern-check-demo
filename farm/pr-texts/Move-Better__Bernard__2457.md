# fix(regenerate): strip Instagram SLIDES block from caption on regenerate (P0)

## P0: Instagram "Regenerate Text" dumps the `---SLIDES---` JSON into the caption

Three staff feedback reports (movebetter, 2026-07-29, Philip Abraham III): regenerating text on an Instagram carousel produced a concise caption **plus** the raw `---SLIDES---` separator and the entire carousel JSON array in the caption box. If approved, that garbage would publish to Instagram.

### Root cause
`api/_routes/content-items/regenerate.js` split model output on a stale `---OVERLAY---` marker the atom prompt **no longer emits** (grep confirms zero emitters repo-wide). Every Instagram atom appends `---SLIDES---` + a JSON deck (`atomPrompts.js`). Only the first-draft path (`draftAtom.js`) knew to split on it; `regenerate.js` was a drifted second copy of the parse — same class as #2278.

### Fix
- Extract the split into a single shared `parseCaptionAndSlides()` (`api/_lib/producer/slidesBlock.js`), imported by **both** `draftAtom.js` and `regenerate.js` so they can't diverge again.
- Regenerate now also **refreshes** `content_items.slides` from the new deck (not merely strips it), and only overwrites `slides` on a successful parse — a non-Instagram platform or a truncated JSON never wipes an existing deck.
- Dropped the now-dead `---OVERLAY---` / HOOK/SUBHEAD/CTA branch.

### Verification
Ran the **real** parser against the 3 corrupted production rows (their stored `content` is exactly the raw-model shape):

| row | caption before → after | deck |
|---|---|---|
| eccbc519 | 1792 → 627 | 4 slides parsed |
| 9c34f441 | 1959 → 709 | 4 slides parsed |
| 8bcd86de | 2133 → 2029 | null (stored JSON was itself DB-truncated — graceful) |

All captions clean (no `---SLIDES---`, no JSON). New `tests/lib/slidesBlock.test.js` pins the caption-never-retains-SLIDES invariant; **confirmed it reddens** when the split is reverted to the old `---OVERLAY---` marker (5/6 fail). Full suite green (847 tests), lint + typecheck + build + 277/277 bundle smoke pass.

### Follow-up (not in this PR)
The 3 affected rows still hold polluted `content` in the DB — they need a manual re-regenerate (or cleanup) after this ships.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

