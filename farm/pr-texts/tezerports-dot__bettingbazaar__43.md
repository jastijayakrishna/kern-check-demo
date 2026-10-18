# UI: Enterprise shell + dark theme, branding assets, responsive nav and results analytics

### Motivation
- Modernize and unify the three web panels (user/merchant/admin) with a polished enterprise dark theme and consistent branding assets. 
- Improve navigation usability on small screens with responsive drawers and clearer active state styling. 
- Consolidate page routing to a registry-driven model for the user panel and reduce duplicated routing logic. 
- Enhance the game results UX with richer streak analytics and an expandable results panel.

### Description
- Added brand assets for all panels: `brand-wordmark.svg` and `brand-splash.svg` under each panel's `public/brand/` directory and switched several UI areas to reference the new assets (e.g. header and loading screens). 
- Reworked admin layout (`admin-panel/src/components/Layout.tsx`) to a responsive enterprise sidebar (larger desktop width, hidden on small screens), mobile drawer overlay, updated header, new color tokens and active/hover styling, and replaced text logo with the wordmark SVG. Also added global admin CSS tokens in `admin-panel/src/styles/globals.css`. 
- Rebuilt merchant layout (`merchant-panel/src/components/Layout.tsx`) into a compact enterprise-style shell with persistent left nav (`MerchantNav`), responsive drawer, online-status controls, motion/animation (`framer-motion`), and merchant theme CSS in `merchant-panel/src/index.css`. 
- Refactored user app routing and shell: introduced `UI_PAGE_REGISTRY.tsx` for centralized page definitions, replaced direct route imports with registry-driven routes in `user-panel/src/App.tsx`, and added a new `EnterpriseShell` component (`user-panel/src/components/Shell/EnterpriseShell.tsx`) that provides the unified layout, right rail, and mobile sheet. 
- Revamped game results UI in `user-panel/src/components/Game/ResultsPanel.tsx` to show a compact strip plus an expandable analytics view, added streak-profile calculation (`buildStreakProfile`) and new visual summaries. 
- Updated user header (`user-panel/src/components/Layout/Header.tsx`) to use the new wordmark asset by default and adjusted logo sizing and wallet UI styles. 
- Added panel-wide theme CSS for user/admin/merchant shells to centralize colors, backdrop gradients, reduced-motion handling, scroll/padding tweaks and card/input styling in `user-panel/src/index.css`, `merchant-panel/src/index.css`, and `admin-panel/src/styles/globals.css`.

### Testing
- Performed TypeScript type-checks with `tsc --noEmit` for the modified packages and they completed without type errors. 
- Executed production builds (`npm run build`) for the affected panels and the builds succeeded. 
- Ran a smoke build verification by starting the app bundles and loading key screens (login, dashboard, game page) to confirm the new shells, drawers, and brand assets render; no runtime errors were observed.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a59ba93d78c8331a540a2bd73638357)
