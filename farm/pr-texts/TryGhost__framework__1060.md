# Removed the GELF logging transport

## Why

Nothing uses the `gelf` logging transport:
- Ghost(Pro) doesn't enable it.
- Nothing in Ghost or Ghost-Moya configures it.

Its dependencies, `gelf-stream` and `gelfling`, haven't been published since 2022.

## What changed

- **Removed from `@tryghost/logging`:** `setGelfStream()`, the `gelf` options, the `Transport`/`GelfOptions` types, and the `gelf-stream` dependency (which also drops `gelfling` from the lockfile).
- **Removed transports share one path:** a `REMOVED_TRANSPORTS` list now covers both `gelf` and `elasticsearch`. #1052 had skipped `elasticsearch` with its own check, which is now folded into this list. A configured transport on the list is skipped instead of throwing "invalid transport", so existing self-hosted configs still boot.
- **One warning per transport:** each removed transport warns (`GHOST_LOGGING_TRANSPORT_REMOVED`) once per process, not once per logger or per duplicate entry.

## Testing

- The GELF tests and #1052's elasticsearch test are replaced by one test. It checks that both removed transports are skipped, no streams are created for them, and only one warning is emitted per transport across duplicate entries and a second logger.
- Ran the `@tryghost/logging` tests (48), plus `pnpm lint` and `pnpm format:check`. All pass, and coverage is above the thresholds.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_0155DGdr754WaUA9CNSSk7uK
