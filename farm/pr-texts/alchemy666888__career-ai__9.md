# Add CareerAI workspace: job search, saved jobs, and AI draft studio

### Motivation
- Introduce a career-focused workspace to browse jobs, save positions locally, and draft/tailor CVs and cover letters with a lightweight AI preview and editor UI.
- Replace several simple placeholder pages with composed components to provide a cohesive CareerAI experience and shared navigation.
- Simplify layout wrapper to allow page-level shells for the career pages and add local persistence for saved jobs.

### Description
- Added a set of career components and pages: `CareerNav`, `JobSearchPage`, `DraftStudioPage`, `SavedJobsPage`, `JobCard`, `useSavedJobs`, `data`, and `icons` under `components/career/*` and new route `app/(dashboard)/saved/page.tsx` to render the saved jobs view.
- Reworked `app/(dashboard)/jobs/page.tsx` and `app/(dashboard)/applications/page.tsx` to mount the new `CareerNav` and page components (`JobSearchPage` and `DraftStudioPage`), and updated `app/(auth)/signin/page.tsx` to use a `<form>` with a submit `button` for sign-in flow.
- Added extensive UI styles and responsive rules to `app/globals.css` to support the career workspace, and added a small localStorage-backed hook `useSavedJobs` for browser-local saved job persistence.
- Updated shared pieces: removed `AppShell` wrapping in `app/(dashboard)/layout.tsx` so pages control their layout, added a `Saved` link to `components/ui/AppShell.tsx`, simplified `middleware.ts` and extended its `matcher` to include `/saved`, replaced the eslint flat config with `eslint-config-next` imports in `eslint.config.mjs`, and adjusted TypeScript environment/`tsconfig.json` and `next-env.d.ts` entries for Next.js types and JSX settings.

### Testing
- Ran TypeScript checks with `tsc --noEmit`, which passed without type errors.
- Ran ESLint (`eslint .`) with the updated config, which completed without lint failures for the changed files.
- No automated unit or integration tests were added in this change.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a5050d7dc58833189102d86afda52bc)
