# refactor(content-sidebar): convert ActivityMessage to TypeScript

# Description
Convert ActivityMessage component from Flow to TypeScript

## Changes
- Renamed ActivityMessage.js to ActivityMessage.js.flow (preserving Flow types)
- Created ActivityMessage.tsx with TypeScript types
- Properly removed original .js file
- Added LoadingIndicatorSize import to fix size prop type

## Type Changes
- Converted Flow's React.Node to TypeScript's React.ReactNode
- Changed SyntheticMouseEvent to React.MouseEvent
- Added specific types for getUserProfileUrl parameters
- Made onTranslate type more specific with proper parameter types

## Testing
- All TypeScript compilation checks pass
- All lint checks pass
- All tests pass (937 test suites, 9913 tests)

## Notes
- Following instructions, external component types are handled implicitly
- Only modified files within activity-message directory

Link to Devin run: https://app.devin.ai/sessions/29674c71a8134e87b61140b94104e0da
Requested by: tjuanitas@box.com
