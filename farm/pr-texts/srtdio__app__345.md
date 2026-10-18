# Add Mentions filter to Activity screen

## What

Adds a **Mentions** state chip to the Activity screen. Unlike the other state chips (which slice the newest 50-row page client-side), Mentions filters **server-side** by `event_type='mention'`, so older mentions are never hidden behind the newest-page cap.

Chip order is now: **All, Unread, Mentions, Snoozed**.

## Files changed

- **`src/components/pages/activity/data.ts`**
  - Extended `ActivityState` union with `'mentions'`.
  - Added a `'mentions'` branch to `filterByState`: mentions that are read **and** unread, excluding snoozed, input order (newest-first) preserved.
  - Added an optional `eventType` arg to `fetchActivityEntries`; when present it adds `.eq('event_type', eventType)` while keeping `created_at DESC`, the keyset `before` cursor, and `ACTIVITY_PAGE_SIZE` unchanged.
  - The mention preview body is resolved from the comment already joined via `COMMENT_EVENTS` (mention was already in that set) — **no new fetch**; `@[uuid]` tokens resolve to `@Name` via the existing `resolveBodyMentions`.
  - Added `segmentSelfMentions` (pure, boundary-aware) so only the viewer's own `@name` is accented.
  - Added a single canonical `MENTION_EVENT_TYPE` constant typed against `InboxEventTypeValue` (tracks `INBOX_EVENT_TYPES`; no free-floating literal).
- **`src/components/pages/activity/ActivityFilterBar.tsx`** — chip order + Mentions chip; count folded into the label exactly as the Unread chip does (hidden when zero, no clamp — matching the existing Unread behaviour, which has no clamp).
- **`src/lib/inbox/inbox-reads.ts`** — added `fetchUnreadMentionCount`, a HEAD count mirroring `fetchInboxUnreadCount` (same workspace/user/read_at/deleted_at/snooze predicates) plus `.eq('event_type', MENTION_EVENT_TYPE)`.
- **`src/components/pages/ActivityPage.tsx`** — refetches and resets pagination when the chip changes to/away from Mentions (via `eventType` in the loader deps; scope stays client-side); loads the mention count and refreshes it after mark-read and mark-all-read; passes the viewer's display name to the card; Mentions empty state with `IconAt`.
- **`src/components/pages/activity/ActivityCard.tsx`** — for `mention` rows only, renders the resolved comment body as a two-line-clamp preview (`overflow-wrap: anywhere`) under the target line, accenting the viewer's own `@name` with the existing `font-medium text-accent`. No layout change to non-mention rows.
- **Tests** — `data.test.ts` (mentions filter branch; `segmentSelfMentions`; `fetchActivityEntries` event_type query filter + keyset pagination preserved; mention preview body resolution), `inbox-reads.test.ts` (`fetchUnreadMentionCount`), and prop updates in `ActivityCard.test.tsx`. Wired into the existing root vitest config; no new workflow, no config changes.

## Light / dark parity

Confirmed for every changed surface — all use existing theme-aware tokens, no hardcoded hex, no `dark:` literals:
- **Mentions chip** — reuses the `Chip` component and its existing selected styling; count is plain label text. Reads correctly in both modes.
- **Mention preview line** — `text-fg-2` (unread) / `text-fg-3` (read) for body text; self `@name` uses `font-medium text-accent`. All three tokens are defined for light and dark.
- **Mentions empty state** — `EmptyState` + `IconAt`, token-driven text. Inherits parity.

Touch targets unchanged (chips use `size="tap"`, rows keep `min-h-[44px]`); no new animation.

## `?comment=` deep-link verification

**Works end to end.** `entityHref` already appends `?comment=${payload.comment_id}` for post/brief mention rows (verified, unchanged). Both consumers focus the target: `PostDetailPage` captures `?comment=` → `focusCommentId` → hands to `Comments`, which flashes the row and lands the mobile layout on the Feedback tab; `BriefDetailPage` does the same scroll-to-and-flash. Nothing to fix.

## Found but not fixed (out of scope)

- Threaded mention rows: when multiple mentions collapse onto the same post/brief, only the **lead** card shows the bo
