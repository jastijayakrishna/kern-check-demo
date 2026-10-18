# Restore Racing Royal tire barriers and portrait brake layout

### Motivation
- Align mobile controls for portrait play by placing the BRAKE control in the same vertical column as BOOST to match phone UX expectations.
- Replace the hard track-edge walls with the previous go-kart tire barriers to reuse familiar visuals and make edges read better on the current tracks.
- Improve road readability by deepening the asphalt tint while keeping the existing PBR asphalt textures.

### Description
- Move the on-screen `BRAKE` button into a new right-side pedal column directly above the `BOOST` control in `webapp/src/games/kartroyale/BaseKartRoyale.tsx` and add a `.kr-pedal-column` container.
- Add responsive brake styling and adjusted sizing in `webapp/src/games/kartroyale/kart-royale.css` so the brake visually lines up with the boost across portrait breakpoints and small widths.
- Replace instanced solid walls with instanced tire geometry in `webapp/src/games/kartroyale/renderer.ts`, creating `TorusGeometry`-based tire instances and dark tread inserts with alternating colors and some stacked tires for variety and performance.
- Slightly darker/asphalt tint applied to the road material so the existing diffuse/normal/roughness textures read more clearly without changing texture assets.

### Testing
- Ran `git diff --check` and confirmed no whitespace/index issues (passed).
- Ran `npx eslint --no-ignore --no-warn-ignored` against the modified files (`src/games/kartroyale/BaseKartRoyale.tsx` and `src/games/kartroyale/renderer.ts`) and fixes passed (no new lint errors in those files).
- Built the app with `npm run build` and the production build completed successfully.
- Ran a portrait smoke screenshot attempt at 390x844 using Playwright; browser dependencies were installed as part of the run but the Racing page remained on its loading fallback rather than entering the playable race (smoke check exercised the page load but did not reach an in-race state).
- Type-check (`npx tsc --noEmit`) reported an unrelated pre-existing error in `lib/prismMaterial.ts` and did not block the targeted changes.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6aa2864af75083298c1a7964581e922d)
