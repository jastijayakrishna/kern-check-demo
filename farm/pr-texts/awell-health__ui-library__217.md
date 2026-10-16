# feat(calcom): add calOrigin prop for enterprise custom domains

# feat(calcom): add calOrigin prop for enterprise custom domains

## Summary
Adds support for Cal.com enterprise custom domains (e.g., `joinavela.cal.com`) by introducing an optional `calOrigin` prop to `CalDotComScheduling` and `CalDotcomActivity` components.

This prop is passed through to the `@calcom/embed-react` `<Cal>` component, which natively supports the `calOrigin` parameter for specifying custom booking domains.

**Part of a 3-repo change:**
- **ui-library** (this PR): Adds the `calOrigin` prop
- **awell-extensions**: Adds `calOrigin` as an extension setting
- **hosted-pages**: Extracts and passes `calOrigin` from settings

## Review & Testing Checklist for Human
- [ ] Verify that `@calcom/embed-react` handles `undefined` calOrigin correctly (should default to `https://cal.com`) - the prop is passed without a fallback default
- [ ] Test the Cal.com embed with an actual custom domain (e.g., `joinavela.cal.com`) to confirm bookings work correctly
- [ ] Coordinate merge order: this PR should be merged and published before the hosted-pages PR can pass CI
- [ ] Confirm backward compatibility: existing usage without `calOrigin` should continue working unchanged

**Recommended test plan:**
1. After publishing this version, update hosted-pages to use the new ui-library version
2. Configure a test Cal.com extension with `calOrigin: "https://joinavela.cal.com"` 
3. Verify the booking widget loads from the custom domain

### Notes
- The `@calcom/embed-react` library (v1.5.x) confirms `calOrigin?: string` in its type definitions
- No unit tests added for the new prop - relies on existing component behavior

Link to Devin run: https://app.devin.ai/sessions/578adba6f85d4605b20d35fc46f7eb16
Requested by: jonathan@awellhealth.com
