# Improve Murlan Royale card handling animation

### Motivation
- Make character card pickup/place actions more natural for human players by involving both hands and smoothing the timing. 
- Preserve existing card layout and final table placement while improving the pickup, carry and release phases for better visual fidelity.

### Description
- Added the left arm/hand to the animated bone set by updating `CHARACTER_ACTION_BONE_KEYS` to include `leftUpperArm`, `leftForeArm`, and `leftHand`.
- Introduced coordinated pose variants (`supportHandGesture`, `pinchFingers`, `pickupGesture`, `carryGesture`, `singlePlaceGesture`, `releaseGesture`) and used `buildPoseVariant` to construct realistic reach/pinch/carry/place/release poses for the play action in `runCharacterAction`.
- Reworked the `PLAY` action timing into sequential phases (pickup → carry → place → release → recover) and adjusted thrown card interpolation so the acting hand remains visually attached to the card during the transition.
- Kept all existing card meshes, table anchors and community layout logic unchanged while only modifying character bone poses and action timing in `webapp/src/pages/Games/MurlanRoyaleArena.jsx`.

### Testing
- Ran ESLint on the modified file with `npx eslint --no-ignore --no-warn-ignored src/pages/Games/MurlanRoyaleArena.jsx` and it passed.
- Built the webapp with `npx vite build --emptyOutDir=false` and the build completed successfully.
- Attempted an automated portrait capture using Playwright at `390×844`, but the headless Chromium instance terminated during the WebGL run so the screenshot could not be produced; the change was still validated by local lint/build checks.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6aa8c736ff0083298c6406db42410db2)
