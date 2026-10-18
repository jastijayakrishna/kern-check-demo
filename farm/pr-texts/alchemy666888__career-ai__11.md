# Customize marketing homepage with responsive landing page

### Motivation
- Replace the minimal placeholder marketing page with a polished, responsive landing page that better represents the AI Job Search product and provides clear CTAs and metadata for search/social sharing.

### Description
- Replaced the marketing homepage component at `app/(marketing)/page.tsx` with a new landing page component that includes hero copy, product proof points, a workspace preview panel, workflow cards, primary/secondary CTAs linking to `/dashboard` and `/jobs`, and a `metadata` export for page `title` and `description`.
- Added responsive landing styles to `app/globals.css` under `.landing-*` selectors that reuse the app's existing `career-btn` visual system and match existing brand colors and layout patterns.
- Preserved all application routes and functionality; no changes to API routes, deployment configuration, or core route logic.
- Files changed: `app/(marketing)/page.tsx`, `app/globals.css`.

### Testing
- Ran `npm run lint` and the lint step completed successfully.
- Ran `npm run typecheck` (`tsc --noEmit`) and typechecking passed.
- Ran `npm run build` (`next build`) and the production build completed successfully with static pages generated and no build errors.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a50669cdaa48331905a65dac926504d)
