# Add local-dev-only light/dark theme toggle to application header

## JIRA Ticket

<!-- Please include the primary JIRA ticket reference (e.g., PROJECT-123). -->

## Summary

Adds a light/dark theme toggle to the chat-bot header to make it easier to check dark mode during local development. The button is rendered only when `NODE_ENV === 'development'`, so production and staging builds never show it.

- **`ThemeToggleButton`** (`components/navigation/theme-toggle-button.tsx`): new component using `next-themes`. It shows a sun or moon icon and is hidden below the `md` breakpoint.
- **`ApplicationHeader`**: renders the toggle immediately before the profile menu, in both the regular and compact layouts. On mobile it stays hidden through `md:` CSS only, so it still renders in the DOM in dev.
- **`ClientProvider`**: `enableSystem` is now `false`, so the app always starts in light. Previously a dark OS preference could pick dark on first load.

The `enableSystem` change applies in every environment, not just local dev. Users who relied on OS-based theme detection will now get light.

The toggle's aria-labels are hardcoded English and are not routed through `next-intl`.

## Screenshots (if appropriate)

<!-- If there are UI changes, please add screenshots here. -->
