# Add opt-in Apple Silicon CPU temperature sampling

## What changes

The CPU tile can show Apple Silicon CPU temperature measured by the optional third-party tool macmon. The Screen privacy checkbox is off by default. Fremkit does not install macmon; the user installs it separately and then enables the checkbox.

After consent, the server reads only `/opt/homebrew/bin/macmon` or `/usr/local/bin/macmon`, requesting one background sample at most once every 10 seconds while the system channel is active. The first reading starts in a neutral state. Polling never waits for macmon. A failed refresh keeps the last good sample until it is 30 seconds old, then rejects it. The channel reports `cpu.tempSource` and `cpu.tempError`; the CPU tile explains missing, failed, invalid or unsupported readings and uses the existing system temperature when available. Disabling consent stops subsequent macmon reads.

The system provider is registered where the config store is available. The branch is rebased on the account-email privacy setting from #25 and preserves both independent switches. This PR is separate from the disk, memory, swap and uptime changes in #16.

## Validation

- `pnpm typecheck` and `pnpm build` passed after the rebase.
- Server tests: 1,407 passed with `test/app.test.ts` excluded locally because its external favicon request timed out in this environment. UI tests: 385 passed.
- Focused thermal and uptime tests: 25 passed.
- Hardware temperature accuracy and the XENEON tile layout have not been verified with macmon installed. The live Fremkit installation was not changed for this PR.
