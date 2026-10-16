# feat(slack): add care flow link to Slack messages

## Summary

Automatically appends a link to the care flow in every Slack message sent via the `sendMessageToChannel` action. The URL is constructed based on the `AWELL_ENVIRONMENT` environment variable:

- Sandbox: `https://care.sandbox.awellhealth.com/pathway/{pathwayId}/activity-feed`
- Production (empty env): `https://care.awellhealth.com/pathway/{pathwayId}/activity-feed`

The link appears at the end of the message using Slack's link formatting: `<url|View Care Flow>`

### Additional Changes

- Updated the Slack extension `icon_url` to use the new Slack icon: `https://res.cloudinary.com/dre4xxcrk/image/upload/v1769185115/Slack_icon_2019_jr0cmr.svg`

## Review & Testing Checklist for Human

- [ ] **Verify URL format is correct** - The URL pattern uses `https://care.{environment}.awellhealth.com/...` for non-empty environments and `https://care.awellhealth.com/...` for production. Confirm this matches the actual care app URL structure.
- [ ] **Confirm always-on behavior is desired** - Every Slack message will now include this link with no option to disable. Verify this is the intended behavior.
- [ ] **Test in actual environment** - Ensure `AWELL_ENVIRONMENT` is properly set in the extension server so URLs point to the correct environment.
- [ ] **Verify Slack message rendering** - Test that the `<url|View Care Flow>` syntax renders correctly as a clickable link in Slack.
- [ ] **Verify new icon displays correctly** - Check that the updated Slack icon renders properly in the extension UI.

**Recommended test plan:** Deploy to sandbox, trigger a care flow that sends a Slack message, and verify the link appears correctly and navigates to the right care flow page.

### Notes

Link to Devin run: https://app.devin.ai/sessions/12062dfcc1d3462188b4d47bf0ff56c4
Requested by: thomas@awellhealth.com
