# Add safe-area CSS tokens for notch-aware mobile layout

## Summary
Introduces CSS custom properties for safe-area insets to standardize notch/status-bar clearance across the app. Replaces hand-rolled `calc(env(safe-area-inset-top) + Npx)` expressions with reusable tokens, ensuring consistent spacing and simplifying future maintenance.

## Key Changes
- **CSS tokens** (`src/index.css`): Added `--safe-top`, `--safe-bottom`, `--header-top`, `--masthead-top`, and `--overlay-top` with documented purposes and fallback values for desktop browsers
- **Viewport configuration** (`index.html`): Added `viewport-fit=cover` to enable edge-to-edge rendering and activate safe-area inset values; added theme-color and Apple mobile web app metadata
- **Capacitor config** (`capacitor.config.ts`): Set `contentInset: "never"` on iOS to prevent WKWebView from adding its own inset, and configured warm cream background color (#E6E0CC) across platforms
- **Component updates**: Replaced all inline safe-area calculations with CSS token references in:
  - `ListingDetail.tsx` (3 header sections + 2 overlay buttons)
  - `EventDetail.tsx` (1 header + 2 overlay buttons)
  - `SpecialDetail.tsx` (1 header + 2 overlay buttons)
  - `PageHeader.tsx` (default top padding)
  - `HomeMasthead.tsx` (masthead spacing)
  - `PolicyPageLayout.tsx` (back button area)
  - `RefineDrawer.tsx` (drawer header)
  - `BottomNav.tsx` (safe-area bottom inset for home indicator)

## Implementation Details
- The `max(...)` floor in token definitions ensures sensible gaps (22px, 28px, 16px) in desktop/preview environments where safe-area insets resolve to 0
- Bottom navigation bar now grows by `--safe-bottom` to accommodate the home indicator without overlapping content
- All changes maintain visual consistency while enabling the app to render edge-to-edge under the status bar/notch

https://claude.ai/code/session_01GaroNBVeoMfSJYTWyDZzNP
