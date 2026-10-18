# Remove rounded card corners

### Motivation
- Replace the app's large rounded card visuals with square edges so card surfaces read as straight/squared rather than curved.
- Make the card appearance consistent by centralizing the corner style and removing the prominent `rounded-2xl` look across panels and dialogs.

### Description
- Changed the shared card token in `src/styles/tokens.ts` from `rounded-2xl` to `rounded-none` so usages of `card` now render square corners.
- Replaced `rounded-2xl` with `rounded-none` on many top-level containers, panels, dialogs, and cards across the app including `src/App.tsx` and component files such as `ClinchingPathsPanel.tsx`, `CommandPalette.tsx`, `CompareDrawer.tsx`, `HelpTip.tsx`, `ModelHealthPanel.tsx`, `OnboardingTour.tsx`, `SeasonTimelinePanel.tsx`, `ShortcutsHelp.tsx`, `Toast.tsx`, and `WeeklyRecap.tsx` (12 files modified in total).
- Left smaller rounded tokens (e.g. `rounded-xl`, `rounded-full`, `rounded-lg`) intact where they provide micro-UI affordances; the change targets larger card/container surfaces only.

### Testing
- Ran type checking with `npm run typecheck`, which completed successfully.
- Built the production bundle with `npm run build`, which produced a successful build.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a3a81b15f80832a80ac537578c0d9dc)
