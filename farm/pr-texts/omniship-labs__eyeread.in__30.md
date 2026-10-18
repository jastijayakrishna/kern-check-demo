# fix: retry DB load on startup to prevent blank script list

## Summary

- On some cold starts, the Tauri SQLite plugin isn't ready before the first DB call fires, causing \`dbPromise\` to cache a rejection — all subsequent \`fetchScripts\` calls return the same failed promise and scripts never appear
- **\`store.js\`**: clear \`dbPromise\` on failure so the next call gets a fresh attempt instead of the cached rejection
- **\`MainWindow.jsx\`**: wrap the initial load in a retry loop (up to 5 attempts, 300 ms × attempt back-off); falls through to an empty ready state rather than hanging forever if all retries fail
- **\`.githooks/pre-commit\`**: committed hook that runs ESLint + prettier on staged JS/JSX files and re-stages the result, wired up via a \`prepare\` npm script so every contributor gets it automatically on \`npm install\`

## Test plan

- [ ] Cold-start the app several times and confirm scripts always appear
- [ ] Confirm the app still renders (empty state) even if the DB is completely unavailable
- [ ] Clone fresh, run \`npm install\`, confirm \`.git/config\` has \`hooksPath = .githooks\`
- [ ] Stage a poorly-formatted JS file, commit, confirm prettier fixes and re-stages it

🤖 Generated with [Claude Code](https://claude.com/claude-code)
