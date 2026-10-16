# feat: add ending_at to Schedule

This PR adds an optional `ending_at` property to the Schedule interfaces in the knock-node SDK.

### Changes
- Added `ending_at?: string | null` to the `Schedule` interface
- Added `ending_at?: string` to `CreateSchedulesProps` interface (which is also inherited by `UpdateSchedulesProps`)

### Implementation Details
- The property is optional and requires no validation in the SDK
- Format follows the same pattern as other date fields (ISO-8601 string)
- No breaking changes to existing functionality

### Testing
- Existing tests continue to pass
- No additional tests were needed as the property is optional and follows the same pattern as other date fields

### Link to Devin run
https://app.devin.ai/sessions/78a792caa098421fb3045c0423cd7d56
