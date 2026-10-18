# feat: add hover/focus feedback to account-menu profile avatar

## What Does This PR Do?

- Adds the same hover-opacity/focus-ring feedback already applied to the header trigger avatar (Xchange-Taiwan/X-Talent-Tracker#691) to the larger avatar in the opened account menu's profile-header row, in both `UserDropdown` (desktop) and `MobileUserMenu` (mobile)
- Adds tests asserting the profile-header avatar carries the `group-hover`/`group-focus-visible` classes, scoped via `data-testid="profile-header-button"` rather than matching on className

## Demo

http://localhost:6006/?path=/story/layout-header-userdropdown--mentor-session

## Screenshot

N/A

## Anything to Note?

**Not a misplaced fix — read this before flagging scope.** Ticket #691's original acceptance criteria (header trigger avatar) already shipped and merged: Xchange-Taiwan/X-Talent-Frontend#1134 (`feat/691-header-avatar-hover`, merged as commit `30891a73`). That trigger avatar (`size-[30px]`, in `DropdownMenuTrigger`/`SheetTrigger`) already has `group-hover:opacity-80` / `group-focus-visible:ring-2` — untouched by this PR's diff.

This PR is a deliberate, separate follow-up: after #1134 shipped, a reviewer pointed out that the *other* avatar shown inside the opened menu (the `size-14` one next to the user's name in the profile-header row) still had no hover/focus feedback, and asked for the same treatment there too. That is the only element this diff touches (`UserDropdown.tsx:99-121`, `MobileUserMenu.tsx:94-115`) — intentionally, not by mistake.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01SBXFntsszSujdiKRS5hA6f
