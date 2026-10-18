# Integrate CareerAI UI template into Next.js app

### Motivation
- Bring the supplied static CareerAI front-end template into the existing Next.js App Router app so users can preview Job Search, Draft Studio, and Saved views as native pages and components. 
- Preserve existing backend, auth, and data patterns while implementing the UI as client components and keeping any backend wiring untouched.

### Description
- Converted the static template into reusable client components and pages, adding `CareerNav`, `CareerIcon`, `JobCard`, `JobSearchPage`, `DraftStudioPage`, `SavedJobsPage`, `useSavedJobs` and shared template data in `components/career/*` and mapped them to routes `/jobs`, `/applications`, and a new `/saved` page. 
- Added scoped template styling to `app/globals.css` (prefixed `career-*`) and integrated the template header/navigation into the dashboard shell via `components/ui/AppShell.tsx`. 
- Kept backend/auth placeholders intact while adapting the sign-in placeholder to a lint-friendly form; saved-job state is implemented as a browser-local hook (`useSavedJobs`) and draft edits are local template revisions until backend AI/persistence is implemented. 
- Updated ESLint/TS config compatibility (`eslint.config.mjs`, `tsconfig.json`) and updated `middleware.ts` route matcher so the new `/saved` route is included in coarse route matching.

### Testing
- Ran linting with `npm run lint` which passed after updating the ESLint config. (success)
- Ran type checking with `npm run typecheck` using `tsc --noEmit`, which passed. (success)
- Ran unit tests with `npm run test` (Vitest), all tests passed. (success)
- Built the production bundle with `npm run build` (Next.js), the build completed successfully and pages compiled. (success)

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a5050d7dc58833189102d86afda52bc)
