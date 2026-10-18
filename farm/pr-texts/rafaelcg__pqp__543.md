# Watch party: past broadcasts for owners and mods, keep a replay

## Summary

"Transmissões anteriores": a history panel for a watch-party channel's owner and moderators (whoever holds `START_WATCH_PARTY` or `MANAGE_CHANNELS` on the channel) to find yesterday's broadcasts and watch one back.

**Server (`restarts-api`):**
- `GET /api/channels/:channelId/watch-party/history?limit=20` — sessions for the channel, newest first: `sessionId` (the broadcast's `started_at` in epoch ms, as a string), `startedAt`, `endedAt` (null if still live), `durationSeconds`, `presenter` (best-effort, see below), `replayAvailable`, `keepReplay`. No `peakViewers` field — nothing durable records a viewer count anywhere in the schema, so it's omitted rather than invented.
- `PATCH /api/channels/:channelId/watch-party/history/:sessionAt` — `{ keepReplay: boolean }`, same permission, 409 once the segments are already gone (in either direction). Flipping it on writes `keep_replay` to **every** `hls_sessions` row of the broadcast (every ladder rung, the mic archive, the camera pip), so the retention sweep keeps or drops the whole thing together rather than dropping a companion rendition while the "primary" one survives.
- `GET /api/channels/:channelId/watch-party/history/:sessionAt/replay` — mints a master playlist URL for an ended, still-available broadcast, using the exact same viewer-token machinery as a live stream (`hls-viewer-token.ts`, 60-minute TTL).
- The path segment is `:sessionAt`, not `:sessionId` — the router requires anything ending in `Id` to be a UUID and 404s otherwise, and a timestamp never is.

**Design notes** (all documented in `server/src/voice/hls-history.ts` and the new "Past broadcasts (replay)" section of `docs/WATCH_PARTY.md`):
- A "broadcast" is a group of `hls_sessions` rows sharing `(channel_id, started_at)` — the file groups by that pair, the same mental model the rest of the doc already uses for "a session".
- The presenter is a best-effort join against `channel_sessions.host_user_id` (the closest party row at/before `started_at`), because `hls_sessions` itself carries no user id, only an ephemeral peer id — the schema comment says reconciling the two is future work. No match is `presenter: null`, never a guess.
- `replayAvailable` mirrors the retention sweep's own predicate exactly (the negation of `dueSessions`' WHERE clause in `hls-cleanup.ts`), not `cleaned_at IS NULL` alone — approximating that way would repeat the "finished session answering as if live" incident this file already documents.
- Replay is served on its **own path** (`GET /api/voice/hls-replay/:channelId/:startedAt(/:rung)`), not a mode on the live playlist proxy: the live proxy deliberately refuses anything with `ended_at` set (a fix for a real production incident), and this feature doesn't loosen that. It rewrites LiveKit's existing `-index.m3u8` accumulated VOD playlist (already written beside the live rolling one) into signed URLs, guarded by its own headerless capability door mirroring the live one's.

**Retention interaction, tested:** `server/src/api/watch-party-history.test.ts` (Postgres-backed, `TEST_DATABASE_URL`) covers permission denial (a plain member is 403'd, a moderator granted `START_WATCH_PARTY` via a channel overwrite gets through), 404/409 edges, `keepReplay` writing every rung, and the retention interaction itself: setting `keepReplay: true` while a broadcast is still within the default window, then advancing `ended_at` past it and confirming `sweepHlsSessions()` does **not** clean it — and that turning it back off makes it due again.

**Client:**
- `watch-party-history-dialog.tsx` — its own dialog, own fetch, own player mount. Does **not** touch `watch-party-panel.tsx` or `watch-party-transmission.tsx` (rewritten elsewhere).
- Opened from a new history icon in the channel header, next to the settings gear, shown only for a `watch_party` channel and only with the permission above. Deliberately independent of `ChannelSettingsDialog`, which is `MANAGE_CHANNELS` / `MANAGE_ROLES` only and would otherwis
