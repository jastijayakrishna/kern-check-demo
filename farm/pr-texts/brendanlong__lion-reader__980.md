# Ignore pinch-zoom and mid-pan swipes for article navigation

## Problem

The next/previous article swipe recorded a single touch's start/end point and navigated on any qualifying horizontal motion. That meant **pinch-to-zoom** and **panning around a zoomed-in article** both triggered navigation, making zoomed reading frustrating on touch devices.

## Fix

Two guards added to `useSwipeGesture`:

1. **Multi-touch cancellation** — if a gesture ever has more than one active touch, it is never treated as a navigation swipe (covers pinch-zoom and other two-finger gestures). The flag resets only once all fingers lift.
2. **Edge-gated navigation** — capture the visual viewport pan position at `touchstart`. When the article is pinch-zoomed, only navigate if the swipe started against the edge it moves toward:
   - swipe-left → next requires the viewport at the **right** edge
   - swipe-right → previous requires the **left** edge

   When the article isn't zoomed, the visual viewport fills the layout viewport so both edges read true and behavior is unchanged. Degrades to the unzoomed default when the `visualViewport` API is unavailable (SSR/older browsers).

New pure, testable helpers `getViewportEdges` / `isSwipeNavigationAllowed` live in `EntryContentHelpers`, with unit tests in `tests/unit/frontend/components/entry-swipe-navigation.test.ts`.

## Testing

- `pnpm test:unit` — all pass (new swipe-navigation cases included)
- `pnpm typecheck` — clean

The edge math is DOM-read-in-hook / pure-logic-in-helper, so the branching is covered by unit tests. Manual verification on a real touch device with a zoomed article is worth a spot-check before merge.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
