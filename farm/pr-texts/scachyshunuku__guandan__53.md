# Fix game history panel padding and freeze header on scroll

## Summary
- The desktop history side panel had no visible bottom margin unless scrolled all the way to the end, since the padding lived inside the scrollable content itself. Reserves a permanent gap below the scrollable region instead, so it's always visible.
- The "History" heading now stays pinned to the top of the panel while the list scrolls underneath it, with its own divider that stays fixed in place too.
- Slightly darkened the entry divider lines (`border-slate-100` → `border-slate-200`) for better contrast.

## Verification
- `npx jest` — 1639/1639 tests passing.
- Exercised `/mocks/game-preview` with agent-browser at both desktop (scrollable side panel) and mobile (natural stacked flow) widths, checking scroll position top/mid/bottom in each.

Desktop panel, mid-scroll — bottom margin and frozen header/divider both visible:

![final_check.png](https://github.com/user-attachments/assets/b5aa0b1b-d489-4bae-b0a7-e45434f3f1b8)

Frozen header + divider close-up while scrolled:

![sticky_divider_zoom.png](https://github.com/user-attachments/assets/c27775fe-84be-44c2-8e8d-00390d5b4a87)

## Review order
1. `src/components/game/GameHistory.tsx` — divider color + bottom padding on the list.
2. `src/app/game/[id]/page.tsx` — the panel layout fix (mirrored in the mock preview page below).
3. `src/app/mocks/game-preview/page.tsx` — same layout fix, for the dev-only preview route.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
