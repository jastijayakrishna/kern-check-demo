# fix: make airport runways read as light concrete strips

## What

Follow-up to #104. You reported not seeing landing strips at Boston Logan — the airport *was* rendering, but the first palette put runway/taxiway/apron all in a narrow mid-grey band, so it read as one uniform grey blob.

Spread the palette by luminance so runways pop:
- **runway** → light concrete `#c4c8d0`
- **stopway** → `#9a8f7e`
- **taxiway** → mid grey `#74777e`
- **taxilane** → `#676a72`
- **apron/helipad fill** → dark tarmac `#54565c`

## Verified in the running app

Loaded the dev build at Boston Logan and confirmed the runways/taxiways now render as distinct light strips against the dark apron (before/after below is night-and-day). Test updated to assert runway luminance > taxiway.

Full suite green, `tsc` clean.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
