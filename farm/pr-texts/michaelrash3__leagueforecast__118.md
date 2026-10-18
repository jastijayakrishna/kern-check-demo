# Remove rounded edges sitewide

### Motivation

- Enforce the new design direction that all UI surfaces must have square corners (zero rounded edges) across the entire app, including buttons, pills, tabs, cards, modals, charts, and the header logo container. 
- Make the header logo match the League Forecast tab/title asset and ensure the icon itself has square outer corners.

### Description

- Replaced non-zero Tailwind `rounded*` utilities with `rounded-none` across components and views to remove rounded corners sitewide (many edits in `src/` including `App.tsx` and component files). 
- Updated shared style tokens in `src/styles/tokens.ts` to use square variants for `pill`, `card`, `tab`, and all `button` styles so component-level utilities are unified. 
- Added a global base-layer guard in `src/index.css` that forces `border-radius: 0 !important` on `*`, `::before`, and `::after` to prevent reintroduction of rounded corners. 
- Squared the app icon by removing the SVG rectangle `rx` radius in `public/icon.svg`, and swapped the header LF text block to render the shared `/icon.svg` image in the header for consistent branding. 

### Testing

- Ran type checking with `npm run typecheck` and it completed successfully. 
- Ran linting with `npm run lint` and it completed successfully. 
- Built the production bundle with `npm run build` and the Vite build completed successfully. 
- Executed an automated scan (Python) across `src/` and `public/` to verify there are no remaining non-`rounded-none` Tailwind `rounded*` classes, and the scan passed.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a3abcdc9b08832ab820425709a17427)
