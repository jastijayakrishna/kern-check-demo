# Season History: every season's champions on one line

From a user request: after jumping twenty years ahead there was no way to see who had won anything without opening twenty separate pages.

A new page at **/season-history**, in the sidebar just above Club History. One line per season, newest first:

| | |
|---|---|
| Continental Cup / Shield | winning club, crest and full name |
| International | that offseason's World Cup winner, or every confederation champion, each with a short code (WC / EUR / SAM / AFR / ASI / NAM / OCE) and the full name and score in its title |
| One column per top flight | that country's champion, as a three-letter club code linking to `/club/:tid/:season` |

A toggle swaps the country columns between **league champions** and **domestic cup winners**. Showing both at once is a column per country twice over, roughly 2,000px of table against ~1,300 for either alone.

## How it's built

`core/seasonSummary.ts` is pure, derived and rng-free, with **no persisted field and no migration**, so an existing dynasty shows its whole back catalogue on load.

The continental and international halves go through **`trophyNewsBySeason`** rather than a second walk over the same records. Two surfaces disagreeing about who won the Continental Cup in season N is exactly what a second walk costs, and that function already handles the two things a fresh implementation gets wrong: reading the **live** cup as well as the archive (a cup is archived at the rollover, so the archive alone hides the club season's biggest result until the user clicks Advance), and filing an international tournament under the club season it **followed**, which is the convention the awards and the News Feed already use. `TrophyNews` gained an optional `confederation` field for the column's short label; the News Feed ignores it.

**Super cups are dropped** even though the trophy map carries them: thirteen more columns for the smallest trophy, and — the sharper reason — a super cup is played in the *preseason*, so counting one would open a row for the new season on matchday 0 with nothing else in it yet.

A row exists for every `seasonHistory` season plus any later one with a decided winner, which is what puts the **season in progress** on the page the moment a continental final is played, marked "(now)" with its league columns still empty.

## Two things found by running it, not by reading it

- **The sticky season column was transparent.** Bootstrap's `.table > :not(caption) > * > *` sets `background-color: var(--bs-table-bg)`, which this theme maps to `transparent`, and it out-specifies a lone class — so the country columns scrolled straight *through* the year. Needs `.sh-table > tbody > tr > .sh-season`. Same family as the unmapped-`--bs-` traps CLAUDE.md documents.
- **`.sh-intl-col`'s min-width is what keeps row height independent of the viewport.** A confederation offseason decides up to six championships that share one cell; uncapped, the column collapsed to 155px at 1280 and a three-line row became a five-line one on a narrower screen. 19rem is measured: the widest it can be with the shipped twelve-country world still fitting 1680px unscrolled, and wide enough for the longest pair ("NAM United States" beside "EUR England") to share a line.

Country cells are abbreviations with **no crest**, deliberately: a crest fallback is 3 elements, so twelve columns over 100 seasons is ~5,000 extra nodes on the page family whose one known failure mode is DOM weight.

## Verification

- `test/core/seasonSummary.test.ts` (11) and `test/ui/seasonHistoryRender.test.tsx` (7), including the spectator save, the season in progress, super cups never opening a row, and confederation labelling.
- Scoped suite: `test/ui` plus the news-related core tests, **64 files / 462 tests green**. Typecheck clean.
- Driven in a browser on a real save jumped eight seasons ahead: World Cup years, confederation years, the season-1 row with no continental cup yet, both toggle views, click-through to a club season, and 390px through 16
