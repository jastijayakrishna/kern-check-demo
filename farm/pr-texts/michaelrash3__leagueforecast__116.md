# Refactor UI: unify card styles, update dashboard, and remove Predictions/Matchup views

### Motivation

- Simplify and modernize the app UI by consolidating dashboard functionality, trimming redundant views, and harmonizing card/spacing styles across components.

### Description

- Replace the old `ForecastDashboard` with a refreshed `DashboardView`, update copy and actions (e.g. view labels, header text, and primary buttons) and change several labels such as "Forecast" → "Projection" and "Forecast field" → "Gold cutoff".
- Remove the standalone `PredictionsView` and `MatchupAnalyzer` code and strip the `predictions` and `matchup` entries from view lists and share/type unions so they are no longer exposed in `VIEW_LABELS`, `VIEW_ORDER`, `SHARE_VIEWS`, and `ActiveShareView`.
- Harmonize component styling by replacing many `rounded-3xl`/large card classes with `rounded-2xl`/`rounded-xl`, adjust paddings and some layout classes for consistency, and apply these changes across `App.tsx` and several components (`ClinchingPathsPanel`, `CompareDrawer`, `SeasonTimelinePanel`, `WeeklyRecap`, etc.).
- Tweak small UI behaviors and structure such as changing button targets (linking forecast actions to the schedule), renaming components and sections (e.g. "Game Forecasts" → "Game Projections"), and using the shared `card` container where appropriate.

### Testing

- TypeScript build (`yarn build` / `tsc`) was run and completed successfully.
- Automated unit tests (`yarn test`) were executed and passed.
- Lint checks (`yarn lint`) were run and passed.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a3a16e1ec38832ab087feee8a726b53)
