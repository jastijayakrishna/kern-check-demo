# Fix slow Tirana startup and recover failed character downloads

The user's Street Career screenshot shows HTTP 502 for living/operator.glb; Battlefield also remains on loading. The model exists in the repository. Investigation additionally measured ~31 seconds just importing the battlefield layout before the menu can appear.

This patch:
- Retries transient core GLB downloads with deadlines, cancellation and binary/size validation.
- Shares character loading across both FPS modes and tries the existing suited-agent rig if the operator remains unavailable. Persistent outages produce an explicit error.
- Applies bounded downloads to required city and held-weapon assets, and disposes partial city results when startup fails.
- Replaces repeated full-city road, obstacle, furniture, bridge and institution scans with spatial lookups while retaining exact geometry tests and source-order ties.
- Allows terminal.local only in development, fixing a canonical-host redirect that had sent the browser preview to production with port 4173. Production wallet-origin enforcement is unchanged.

Validation:
- Local fresh-process layout import: 31,035 ms baseline (second baseline 27,928 ms) → 8,221 ms. These are initialization measurements, not phone FPS or total download times.
- All 113 spawn/extraction records, force-vehicle placements, and complete street-prop/collider/railing/mapped-place outputs match baseline.
- 10 startup/download/lobby tests passed, including simulated 502 recovery, cancellation, timeout, invalid responses, backup rig selection and spatial-query equivalence.
- 64 related city-source, street-detail and full-body career regression checks passed.
- Scoped TypeScript and production build passed; the final development-host exception was exercised in the browser.
- Actual browser: lobby selectors → Battlefield menu → deployed operation with character and AK-47 → pause → return to lobby. Gameplay screenshot inspected.

Limits:
The cloud browser uses software compatibility rendering (~1–2 FPS). Full Street Career WebGL play and real-phone performance remain unverified. The production cause of Render's 502 has not been determined; its connector requires user workspace confirmation before logs can be read. Local download recovery and successful deployment into a local match do not prove the production outage resolved.

The previous preview connection failure was traced to the app's canonical redirect, correcting its earlier classification as a preview infrastructure issue. Details are in docs/tirana-startup-recovery.md.

