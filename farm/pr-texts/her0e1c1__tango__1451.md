# refactor(settings): consolidate preferences in page model (No issue)

## Related issue

None.

## Summary

Settings previously wired preference state and auto-save in the Page while a separate form hook synchronized external theme changes. Consolidate form initialization, dark-mode synchronization, and auto-save in `useSettingsPageModel`, so the Page only consumes the prepared form and limits.

Write the effects and preference updates directly in the Page model without wrapper hooks or action files. Preserve existing auto-save, theme synchronization, and route shortcuts. All changes stay within `src/pages/settings/`.

## Testing

- `mise run check` passed: static checks and 730 unit tests across 126 files.
- Mandatory reviewer found no issues in the final implementation.

