# Auto-skip release validation columns from PR labels on main release tabs

Release validation rows were always initialized with empty `Validated` cells, even when PR labels explicitly indicate validation should be skipped. This update adds label-driven auto-skip behavior for main release tabs and leaves all `pre-` tabs unchanged.

## Description

- ~**Main-release-only auto-skip**~
  - ~Applies skip logic only when writing to non-`pre-` tabs (main release tabs after rename).~
  - ~`pre-*` tabs do not get automatic `Skipped` values.~

- **Supported skip labels**
  - Global: `skip-release-validation`
  - Granular: `skip-release-validation[android|ios|design|chrome|firefox]`
  - `design` skips both validation columns for the repo type.

- **Repo-aware label filtering**
  - Mobile ignores extension-only labels: `[chrome]`, `[firefox]`
  - Extension ignores mobile-only labels: `[android]`, `[ios]`
  - Invalid labels are ignored, not errored.

- **Comments column for auto-skips**
  - Uses the existing template `Comments` column (column J), rather than adding a new comment column.
  - When any validation cell is auto-skipped, the skip reason and effective labels are written to that existing `Comments` column.

- **Sheet range updates**
  - Header updates remain `A2:H2` (renaming validated columns for platform-specific labels).
  - Row read/append ranges use `A3:J` / `A4:J` so existing `Design Validation` and `Comments` columns are preserved and the auto-skip note is written in `Comments`.

## Example

```js
// Extension main-release row with labels:
// skip-release-validation[chrome], skip-release-validation[design]
[
  /* ...A-F... */,
  'Skipped', // Validated (Chrome)
  'Skipped', // Validated (Firefox) via [design]
  '', // Design Validation (existing template column)
  'Release validation automatically skipped due to PR labels: skip-release-validation[chrome], skip-release-validation[design]' // Comments (existing template column)
]
```

<!-- START COPILOT CODING AGENT TIPS -->
---

✨ Let Copilot coding agent [set things up for you](https://github.com/MetaMask/github-tools/issues/new?title=✨+Set+up+Copilot+instructions&body=Configure%20instructions%20for%20this%20repository%20as%20documented%20in%20%5BBest%20practices%20for%20Copilot%20coding%20agent%20in%20your%20repository%5D%28https://gh.io/copilot-coding-agent-tips%29%2E%0A%0A%3COnboard%20this%20repo%3E&assignees=copilot) — coding agent works faster and does higher quality work when set up for your repo.

<!-- CURSOR_SUMMARY -->
---

> [!NOTE]
> **Medium Risk**
> Medium risk because it changes how the post-merge tracker writes Google Sheets rows (expands to columns A–J and mutates validation/comment cells) based on PR labels, which could affect reporting if label parsing or column indexing is wrong.
> 
> **Overview**
> Adds label-driven auto-skip behavior to the post-merge validation tracker so PRs labeled `skip-release-validation` (or granular `skip-release-validation[...]`) automatically get `Skipped` populated in the relevant *Validated* columns and a reason written into the existing *Comments* column.
> 
> Updates sheet read/append ranges from `A3:H`/`A4:H` to `A3:J`/`A4:J` and extends generated rows to include the extra `Design Validation` and `Comments` columns, preserving template columns while inserting the auto-skip note.
> 
> <sup>Written by [Cursor Bugbot](https://cursor.com/dashboard?tab=bugbot) for commit d8b84622c2659bccde19b1d7e973a1816f66c9c3. This will update automatically on new commits. Configure [here](https://cursor.com/dashboard?tab=bugbot).</sup>
<!-- /CURSOR_SUMMARY -->
