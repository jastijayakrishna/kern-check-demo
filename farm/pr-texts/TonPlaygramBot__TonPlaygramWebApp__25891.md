# Checkers: add Chess human characters and physical token handling

Checkers currently moves tokens without the human characters used by Chess Battle Royal. This adds the same character catalogue, owned/equipped character selection, seated rig, material treatment, and calibrated finger pickup and placement.

- Reuse the existing bundled Chess human for the default player and rival; share the model and pose code between both games.
- Use the shared 1.6-second reach, grip, lift, carry, place, release, and withdrawal sequence for each checker move and each capture-chain jump.
- Keep captured tokens visible until placement, delay the AI until the hand withdraws, and defer character replacement during a move.
- Render the player's real skinned arms in the close camera view and restore the full body in 2D. Fit the opponent's head and board into portrait screens while preserving square coordinates and touch mapping.
- Include a React/Three.js/TypeScript movement preview source and verification notes in docs/checkers-human-characters.md.

Validation: all 55 Checkers/Chess Node regression tests passed, including contact with the actual GLB skeleton, extreme board positions, portrait projection, and 12 complete AI matches with 154 captures. A separate 75-case comparison confirmed that the shared ordinary poses match the previous Chess implementation. Strict TypeScript checks and the Vite production build passed; Vite reports the existing large-chunk warning. Rebased onto latest main dcb32d8 without conflicts.

Draft because live browser verification was blocked by this session's browser policy. Before release, verify character/chair fit, finger contact, capture chains, character changes, 2D/3D switching, optional remote character models, and online play from both seats on a portrait phone. Automated geometry checks do not establish mobile visual quality or GPU performance.
