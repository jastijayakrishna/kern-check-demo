# Fix the leaderboard stats button and list /k spotters with their last spot

## What

- **/leaderboard**: pressing a tab re-rendered the boards for whoever pressed the button, so "Mijn stats" showed the presser's stats instead of the command user's. The tab custom ids now carry the invoker's user id (`leaderboard:<view>:<userId>`) and the stats tab is labelled with their display name ("Stats van …"). Buttons on messages from before this change carry no user id and keep the old behaviour.
- **/k**: the spotters are now a markdown list, one line per spotter with their count and most recent sighting as a relative timestamp, linked to the original message when it can be jumped to. The summary header loses its "— laatst …" (each line has its own) and the caption loses "N× gespot in deze server", which disagreed with the summary count because it included the spot being recorded. `Sightings.countForLicense` and `LicenseViewData.spotCount` became dead and were removed — one query fewer per /k.
- **Startup**: a malformed `heartbeatUrl` made `https.get` throw synchronously before the interaction listeners were attached, leaving a logged-in bot that answered nothing. The heartbeat now catches its own errors and starts after the listeners.

## Tests

- New coverage for the user id in the tab custom ids, the display-name label, and the per-spotter list format.
- `npx jest`: 162 passed, `tsc --noEmit` and `eslint` clean.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01Xyn9AonyvuMYqmmQs8vRjF
