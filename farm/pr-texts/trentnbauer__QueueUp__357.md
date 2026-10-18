# Fix DLC filter, modal drag-close, replay filter, add list view (#354, #342, #334, #344)

## Summary

Four independent fixes/features, one per commit:

- **#354** - "Hide DLC" toggle didn't hide DLC in the collection review screen (e.g. Borderlands 2). `searchGames` already applied the filter; `getCollectionGames`/`collectionGamesIntake`/`/api/games/collections/:id` never received it. Now threaded through end-to-end, same opt-out default as search.
- **#342** - Click-and-hold inside a modal (e.g. selecting text), dragging out, and releasing outside closed the modal. Every modal's backdrop used a plain `onClick`, which fires based on where `mouseup` lands. Added `closeOnBackdropMouseDown` (keys off `mousedown`, requires the press itself to start on the backdrop) and applied it to all 10 modals sharing this pattern.
- **#334** - Added a "Replay" filter pill (was missing from `STATUS_FILTER_ORDER`), and replay-queued games now also show under the Completed/Beaten strip, same as Done games, hidden from the main grid by default but revealed by selecting its filter pill (matching the existing Playing/Done/Dropped pattern).
- **#344** - New per-browser "Shelf & room layout" setting (Profile Settings) to swap the Personal Shelf/rooms between the existing artwork grid and a new compact list view (`GameListRow`) showing review score, squad votes, ownership fraction, and time-to-beat per row. Defaults to Artwork.

## Test plan

- [x] `npm test` - 169 tests pass
- [x] `tsc --noEmit` on both `web` and `server` - no new errors
- [x] Verified live: ran the dev server against a seeded local DB, drove it with Playwright -
  - Backdrop drag-release-outside no longer closes the modal; a genuine outside click still does
  - List view toggle in Profile Settings works; list rows render review score/votes/ownership/time-to-beat and open the same detail modal as the artwork card
  - Replay status shows in the detail modal's status picker and the filter pill list

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01TL7AVdeMpr4MWYSQdiZYb6
