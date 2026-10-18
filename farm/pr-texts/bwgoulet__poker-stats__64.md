# Fix player stat tooltips

### Motivation

- The player detail page relied on native `title` hints which were non-interactive and not accessible, so stat explanations were not discoverable or usable on keyboard/touch devices. 

### Description

- Add a reusable client component `src/components/ui/StatTooltip.tsx` that renders an accessible tooltip trigger and content, exposing ARIA attributes via `useId` and supporting hover, focus, click/tap, blur, and Escape to close. 
- Replace inline `title`-based hints on `src/app/players/[playerId]/page.tsx` for headline and detail stats with the new `StatTooltip` control so each stat shows an interactive help icon and tooltip. 
- The tooltip uses a help icon from `lucide-react`, toggles visibility with internal state, and keeps the tooltip constrained for small viewports.

### Testing

- `npm run lint` (TypeScript typecheck) completed successfully. 
- `npm test` (Vitest) ran and the full test suite passed (`37` tests passed). 
- `npx vitest run test/normalize-workbooks.test.ts` passed on retry for the targeted spec. 
- `npm run build` produced a successful Next.js production build.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a992bc1cf888332a8ed8aba893e4e5d)
