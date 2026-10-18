# Tirana Streets + Racing Royal: three modes, social Explore and Grand circuits

## Actual integration in Tirana Streets and Racing Royal

This PR changes the real game entries, server service, shared scene adapters and racing simulation wrapper. It is not an offline social mockup or an asset-only proposal. **Keep draft: full application, actual-game and two-device media verification remain release blockers.**

### Three modes

- Tirana Streets lobby: **Battlefield**, **Career mode**, **Explore**. Battlefield retains the current wave/extraction and paid multiplayer operation. Career retains the existing nine-mission driving/combat campaign and saves. City Stories remains a secondary link. This is not a newly authored GTA VI campaign or a feature-parity claim.
- Racing Royal: **Multiplayer racing**, **Career mode**, **Explore together**. The existing multiplayer/AI-practice lobby remains available. The explicit career view uses the current KartRenderer, original cup slots and original career save key, with a new Grand cup appended.
- Existing paid online/table URLs retain priority and never enter the free social path. No stake amounts, payment/reward settlement, original starting grids or race time limit are changed.

### Shared Explore city and existing human characters

Both game entries connect to the same new **four-person, server-authoritative, peaceful city instances** via the existing registered game socket/service attachment. Walking, driving, existing traffic and mapped city collision are reused; combat, purchases, wanted dispatch and rewards are stripped.

The server resolves profile names/photos/social identifiers from the user store, bounds chat and signaling, fences requests by client session, supports room invitation links, session blocking and operator report callbacks. The People panel invokes the existing friend-request API only after an explicit click; friendship still requires acceptance. Original city rooms/career service is preserved byte-for-byte as `legacyTiranaStreets.js`.

Existing Chess/RPM and Adrian/Maya models are selected through the shared catalog/rig loader. Profile avatars/initials or opted-in camera video appear as **face-mounted identity panels**, not UV-remapped face skins or face scans. Existing embedded human materials and licences are retained; no new model binaries or fonts are included.

### Live voice/video: explicit consent, not automatic capture

Dedicated Explore WebRTC signaling uses the existing shared socket and configured TURN environment settings. Camera/microphone start off. Join Voice or Go Live requests browser permission; every signal requires current mutually opted-in room members and matching server-issued media epochs. Stale/cancelled capture results are stopped before use. Muting retains call membership without falsely advertising a live microphone. Stop, page hide, disconnect and unmount stop capture and close peers. Remote audio offers a playback gesture when browser autoplay is blocked.

**Not verified end-to-end:** camera permissions, remote resource loading, two-device calls/TURN, runtime animation/head alignment or physical-phone performance. Rooms are single-process and memory-backed, not a persistent MMO or multi-replica room architecture. Reports currently reach an operator log callback, not a durable moderation queue; session blocking is not a platform-wide block list.

### Bigger tracks and correctly oriented turn helpers

- Original five circuit IDs and original simulation retained unchanged in `legacySimulation.mjs`.
- New **Lana–Pyramid Grand** combines the exterior of the two adjacent shipped mapped race paths, removing their shared corridor. Every returned edge already exists in those paths. Calculated length: **1,993.973 m** in the existing approximate metre frame, about 37.7% longer than Lana and 102.7% longer than Pyramid. Registered in the actual track list and a stable new career cup slot.
- Optional per-district Grand candidates require connected eligible source roads, at least 1.4× the previous circuit length and at most 2.2 km
