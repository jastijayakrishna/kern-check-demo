# [No issue] Improve list and settings readability

## Related issue

None.

## Summary

Narrow list rows truncated ordinary deck names and study progress beside the action buttons. Give deck content the full row width on mobile, allow two lines for deck and card text, and place card tags below the study count on small screens.

Let deck section headings wrap, add breathing room between settings labels and help text, and place the language selector below its explanation.

## Testing

- `mise run check` passed, including 730 unit tests.
- All 49 stories passed across the six affected component suites, including interaction and accessibility checks.
- Visually checked 320px and 375px mobile previews and 1280px desktop routes, long text/tags, English/Japanese, and light/dark themes. Verified Continue opens the study route.
- Required reviewer review completed with no findings.

