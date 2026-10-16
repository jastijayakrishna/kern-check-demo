# Fix navigation font color inheritance in sidebar items

### Motivation

- Navigation item text and icon colors were not inheriting the community `ui_config` `fontColor` because components contained hard-coded color classes that override the themed value.

### Description

- Replaced hard-coded Tailwind color classes on navigation links and buttons with `text-inherit` so they inherit the nav font color from `navTextStyle`/CSS variables (changed in `src/common/components/organisms/navigation/NavigationItem.tsx`).
- Removed explicit color classes from the edit pencil icon to avoid forcing a gray color (changed in `src/common/components/organisms/Navigation.tsx`).
- Adjusted footer/social link and small-footer text classes to `text-inherit` so those elements also respect the configured nav font color (changed in `src/common/components/organisms/Navigation.tsx`).

### Testing

- Started the dev server with `yarn dev`, which reported Next.js ready (server started successfully).  
- Attempted an automated visual check via Playwright screenshot, but the Playwright run timed out and did not complete.  
- No unit tests or snapshot tests were run as part of this change.

------
[Codex Task](https://chatgpt.com/codex/tasks/task_e_697913d69e588325a1f24dccb0a970de)
