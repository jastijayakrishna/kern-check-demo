# Rebuild Activity card layout to the approved prototype

## What

Full layout rewrite of `ActivityCard` to match the approved prototype. Not a set of tweaks: the card is now a **flex row** with a 3px lead rail and a content column beside a full-height media tile flush to the card's right edge. Only two files changed.

## Layout

- **Container:** `flex overflow-hidden rounded-xl border bg-panel transition-colors`, `border-accent-line` when unread / `border-border` when read.
- **Rail (child 1):** `w-[3px] shrink-0`, `bg-accent` (accent tone) or `bg-border-strong` (neutral). `aria-hidden`. No opacity modifier.
- **Inner column (child 2):** `min-w-0 flex-1`, holds the content row and the footer.
- **Content row (Row A):** `flex items-stretch`, is the clickable button (opens the group; keyboard handler unchanged).
  - **Actor line:** `mb-1.5 flex items-center gap-[7px]` — avatar, inline event glyph (size 14, `text-accent`/`text-fg-3`), short actor text (`truncate text-xs font-medium text-fg-3`), and the unread dot moved here (`ml-auto h-1.5 w-1.5 shrink-0 rounded-full bg-accent`).
  - **Title:** on its own full-width row, no glyph beside it — `truncate text-[15px] font-semibold leading-[1.3] text-fg`.
  - **Body / mention preview:** `mt-[3px] line-clamp-2 text-sm leading-[1.4] text-fg-2` (mention preview keeps its existing condition and `mentionPreview` call).
  - **Meta:** `mt-2 flex items-center gap-1.5` — mono timestamp + panel-2 scope chip, with the Snoozed indicator as a matching second chip.
  - **Media tile:** `flex min-h-[104px] w-24 shrink-0 self-stretch`, no radius/padding/margin, flush to the card edge.
- **Footer (Row B):** unchanged condition (>1 entry) — `h-px bg-border` divider, restyled `+N more` / `Show less` button, expanded list re-padded (`pl-[14px]`) to line up under the title, every row `min-h-[44px]`.

## Actor line helper

Added a local `actorLine(item, who)` in `ActivityCard.tsx` (not in `data.ts`). It returns a short, entity-free line derived from the existing `actorEntry` logic: `commented` / `mentioned you` / `resolved a thread` / `sent N points` (existing `pointsAdded` + local singular/plural) / `asked a question` / `reopened a point`, `Moved to {toStage}` (no actor), `Ready for review`, and the bare actor name (or `activityLine(item)` with no actor) for everything else.

## Avatar size

Avatar has no 20px option (`sm:24, md:26, lg:32, xl:48`). Used **`size="sm"`**, which renders **24px** — the nearest available to the 20px spec.

## Media tile / Thumbnail

The media wrapper is a flex container, so `Thumbnail` (a flex child, default `align-items: stretch`) is stretched to the full row height, which overrides its `aspect-square` and yields the required non-square 96px-wide fill. No edit to `Thumbnail` was needed; `fallback={leadFallback(lead)}`, `cache`, `presignEnabled`, `aspect` and `alt` are all passed exactly as before.

## Removed

`ActivityRowMenu` is no longer rendered (import + usage deleted). Its file is untouched. `onSnooze` / `onMarkRead` stay in `ActivityCardProps`; they're simply not destructured, so `ActivityPage.tsx` compiles unchanged and no unused-var lint fires.

## CSS verification (every added class confirmed in `dist/assets/index-*.css`)

All **PRESENT**, none absent:

`flex` · `overflow-hidden` · `rounded-xl` · `border` · `bg-panel` · `transition-colors` · `border-accent-line` · `border-border` · `w-[3px]` · `shrink-0` · `bg-accent` · `bg-border-strong` · `min-w-0` · `flex-1` · `cursor-pointer` · `items-stretch` · `hover:bg-panel-2` · `py-[14px]` · `pl-[14px]` · `pr-3` · `mb-1.5` · `items-center` · `gap-[7px]` · `text-xs` · `font-medium` · `text-fg-3` · `truncate` · `text-accent` · `ml-auto` · `h-1.5` · `w-1.5` · `rounded-full` · `text-[15px]` · `font-semibold` · `leading-[1.3]` · `text-fg` · `mt-[3px]` · `line-clamp-2` · `text-sm` · `leading-[1.4]` · `text-fg-2` · `[overflow-wrap:anywhere]` · `mt-2` · `gap-1.5` · `font-mono` · `h-5` · `rounded-md` · `bg-panel-2` · `px-2` · `text-[11px]` · `gap-1` · `min-h-[104px]` · `w-24` · `self-stret
