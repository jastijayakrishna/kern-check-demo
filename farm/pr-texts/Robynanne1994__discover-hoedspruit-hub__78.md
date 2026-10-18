# Add search and improve segmented control UI in FollowList

## Summary
Enhanced the FollowList page with client-side search functionality and redesigned the followers/following segmented control with improved visual styling.

## Key Changes
- **Search functionality**: Added a search input that filters connections by display name or username in real-time
- **Segmented control redesign**: Replaced underline-style tabs with a modern pill-style segmented control featuring:
  - Rounded background track with subtle color
  - Active state with brown background and white text
  - Smooth transitions between states
  - Updated typography using the 'Nohemi' font family
- **Find people button**: Added a "UserPlus" icon button in the page header (visible only on own profile) that navigates to the people search page
- **Empty state handling**: Added specific messaging when search returns no results vs. when there are no connections at all
- **Color and typography updates**: Added new color token for the segmented control track and new font family constant for headings

## Implementation Details
- Search is case-insensitive and matches against both `display_name` and `username` fields
- Search state resets when switching between followers/following tabs
- Uses `useMemo` to optimize filtering performance
- Maintains accessibility with proper `aria-label` and `aria-current` attributes
- Responsive button styling with flexbox layout for the search input

https://claude.ai/code/session_016sYXYnQZgGrGgQqxjaM3pf
