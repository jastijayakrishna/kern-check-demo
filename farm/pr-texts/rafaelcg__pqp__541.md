# Watch party: stream left, chat right by default for the audience

## Summary

A seatless viewer watching a watch party (live, ended, or not-yet-started — the stage, the "it ended" card and the holding screen all share one pane) now gets a Twitch-shaped default: the stream takes most of the width, the channel's own chat is pinned to about 340px on the right, and it stacks on a phone-width pane the same way `CallSplit` already stacks everything else. The seated surface — host, co-hosts, anyone on stage — is untouched; it keeps the call's shared proportional split.

**The layout rules:**
- Desktop: stream left (majority of the width), chat column right, ~340px by default, resizable by dragging the existing divider (persisted once dragged).
- Phone / narrow pane: stacks — stream on top, chat below.
- Native fullscreen: unaffected (already documented and tested — the chat's column goes away entirely, theatre-mode overlay only).
- "Party ended" and "not started yet" screens draw inside the same pane arrangement, so the layout doesn't jump around as the stream starts/stops.

**The toggle:** reuses the existing header icon toggle (`data-call-split-toggle`) rather than forking a new control. It already persists to `localStorage` (`pqp:call-split`) and already drives the "put the chat away" affordance; this PR only gives it audience-appropriate copy ("Chat beside the stream" / "Chat below the stream", pt-BR "Chat do lado da transmissão" / "Chat embaixo da transmissão") instead of the call-oriented wording, and makes sure it applies to the audience surface at all (previously the shared `side` fraction — 62% to the stage — was correct for a call but left an audience's chat far wider than a Twitch column on any big monitor).

**Not touched, on purpose:**
- `watch-party-panel.tsx` / `watch-party-transmission.tsx` (PR #538 rewrites them).
- `hls-watch-player.tsx` — the delay badge, viewer count, quality selector and fullscreen control were already drawn as an overlay with idle-hiding chrome (Twitch-style already); no changes needed there.
- The member/roster sidebar already steps aside while a live picture is showing (`memberSidebar.suspend`, pre-existing).
- The chat column reuses `MessageList` / `MessageComposer`'s existing "stream" variant — no forked chat component.

## What changed, mechanically

- `client/src/lib/call-split.ts`: a third `CallSplitKind`, `"watch-audience"`, with its own `watchAudienceSide` preference field. Left unset, the default is computed fresh against the live pane width (`watchAudienceDefaultSide`) so the chat reads as a fixed ~340px column rather than a proportion of an arbitrary window; once a viewer drags the divider it freezes into an ordinary stored fraction, same as every other split. The two watch kinds (`"watch"`, the seated surface, and `"watch-audience"`) still share one stored orientation (`watchOrientation`), so flipping the toggle while watching doesn't flip back the moment you take a seat.
- `client/src/components/layout/call-split.tsx`: threads the new kind through the fraction/commit logic.
- `client/src/App.tsx`: `splitKind` now distinguishes the seated surface from the audience one by whether this account holds a seat in the room; the places that keyed off `splitKind === "watch"` for chrome shared by both surfaces (stream-shaped chat variant, the toggle's copy) now read a new `isWatchPartySplit`.
- `client/src/locales/{en,pt-BR}/translation.json`: two new keys for the toggle's audience-facing copy.
- `docs/WATCH_PARTY.md`: addendum to "The layout" documenting the new default and explicitly noting it revises an earlier recorded decision ("no watch-party-specific number was introduced").

## Tests

- `client/src/lib/call-split.test.ts` (pure functions): desktop → side-by-side with the chat at exactly `MIN_WATCH_CHAT_WIDTH_PX`, phone-width pane → stacked, `fullscreen` shape → stacked, the default recomputing per width vs. a dragged fraction freezing, round-trip through `loadCallSplit`/`saveCallSplit`.
- `client/src/components/layout/call-split.test.tsx` (rendered 
