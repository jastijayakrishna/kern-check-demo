# Repair Tirana Streets Explore and restore Racing Royal AI/online garage with kart missions

## Actual repairs to Tirana Streets and Racing Royal

Based on merged #25785 / `ed2043ef984e9824c0ed5cedd58e184676e17ee7`. **24 changed files. Keep draft until full application and browser/device/network checks pass.** No separate demo or production deployment.

### Explore: reproduced failures, then fixes

Three regressions failed against the previous actual TypeScript classes. Pausing inserted a wall-clock sequence much larger than subsequent CityInput counters, causing the server to reject movement as stale. The pause state also was not immediately published to the UI.

The transport now owns one monotonic input counter. Pause, the People panel and network availability are separate input states. Escape/blur/visibility and the visible resume button stay synchronized. Registration/rejoin is coalesced; only one heartbeat/listener set survives. Late joins after disposal leave their own client session. Public-room reconnect, visible connection state and an explicit Reconnect action are added. Explicit invitations do not silently redirect to another room. Valid snapshots recover from transient request errors.

Camera/microphone consent, server authentication and room authorization remain unchanged. Media does not automatically restart. Optional decoration failure no longer permanently disables the existing base city.

### Racing Royal restored, plus kart missions

- The default route again opens the original BaseKartRoyale garage with **VS AI / MULTIPLAYER / CAREER** tabs, kart selection, original cameras and controls. The extra mode-selection screen is removed.
- Kart Missions and Explore are accessible through buttons in the original online-lobby slot; dedicated career/Explore URLs remain available. Paid online/table/code URLs retain priority. An AI URL opens the original garage without overriding its own initial-tab behavior.
- Four sequential device-local kart-race goals: Skënderbej time qualification, clean driving in Blloku, Lana podium and Grand endurance. These are full races with extra goals, **not open-world delivery missions**. First-completion XP uses a separate save key; no TPG rewards.
- Independent touch/keyboard owners prevent releasing boost/brake from cancelling held steering. Pause, pointer cancellation, blur and race finish clear controls.
- Original kart dynamics, original five route geometries/IDs, cup save key and multiplayer settlement rules remain unchanged. Optional-mode recovery boundaries are added to both game entries.

### Startup, human loading and city scope

Whole-WORLD automatic detour generation is removed from synchronous startup. The five original circuits and source-backed Lana–Pyramid Grand remain. Unvalidated automatic per-district Grand variants are no longer advertised/accepted; authoring helpers and stored records remain.

Street Career and shared Explore prioritize the existing bundled Chess/RPM, Adrian, Maya and soldier GLBs. A requested avatar can fall back to an already-loaded role-compatible human. No new model binaries, fonts, arbitrary reskins or permission changes.

Existing city PBR buildings, lane/crossing/post/grass/tree layers remain connected. This repair improves loading resilience; it is not a new high-resolution asset pack, altitude correction or satellite survey. Battlefield operation opponents are not reskinned.

## Validation executed

**191 passed, 0 failed, 0 skipped**: prior 142 focused cases unchanged, plus 29 input/lifecycle/task/fallback tests and 20 driving/compatibility checks.

The actual checked-in kart physics drove **six AI karts on six circuits at all three difficulties**: 18 races and **108 successful finishes** before the unchanged 480-second limit. No mocked steering/collision response or teleports. This is headless simulation, not full-city visual-clearance or online-racing validation.

Strict TypeScript public-contract test passed against the existing declarations; eight changed JSX/TS/TSX files passed transpilation syntax checks. These are not a full
