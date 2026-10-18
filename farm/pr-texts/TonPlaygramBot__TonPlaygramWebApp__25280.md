# Match Murlan Royale characters to Domino Royal

### Motivation
- Ensure Murlan Royale uses the same seated human roster as Domino Royal for a consistent seven-player experience while preserving extra character models for Pool Royale.

### Description
- Consolidated the full character catalog into `CHARACTER_THEME_CATALOG` and derived `MURLAN_CHARACTER_THEMES` by filtering that catalog to the seven Domino roster IDs in `webapp/src/config/murlanCharacterThemes.js`.
- Added `POOL_ROYALE_CHARACTER_THEMES` as an export that preserves the complete catalog for Pool Royale usage.
- Updated `webapp/src/config/poolRoyaleInventoryConfig.js` to import `POOL_ROYALE_CHARACTER_THEMES` and keep Pool Royale character options unchanged.
- Changes are limited to configuration-level mappings and do not modify runtime character-loading logic.

### Testing
- Ran a Node assertion that verifies `MURLAN_CHARACTER_THEMES` contains the expected 7 IDs and that `POOL_ROYALE_CHARACTER_THEMES` is larger, and the assertion passed (`Murlan roster: 7; Pool catalog: 14`).
- Performed a production build with `npm run build`, which completed successfully and produced the application `dist` artifacts.
- Executed `git diff --check` to validate there are no diff-check issues reported by the change tooling.
- Ran `npm run lint` targeted at the edited files and observed pre-existing ESLint formatting/semicolon errors in the repository that are unrelated to the functional change and did not block the build.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a7161767ecc8329b7bf2dcc803886c6)
