# Kart Royale: rearrange touch pedals and replace track walls with tire instancing

### Motivation
- Improve touch control ergonomics by grouping brake and boost into a dedicated pedal column for mobile players.
- Refresh track visuals by replacing blocky wall instancing with tires and tire-tread instanced meshes for better appearance and material control.

### Description
- Move the brake button into a new `.kr-pedal-column` next to the boost button in `BaseKartRoyale.tsx` and adjust touch control markup accordingly.
- Add `.kr-pedal-column` and `.kr-brake` styles and responsive size tweaks in `kart-royale.css`, and introduce the `.rr-pedals` helper in `explore.css` and `RacingCareerGame.tsx` to keep pedal layouts consistent across screens.
- Update renderer in `renderer.ts` to change road color and replace the previous wall instanced mesh with instanced `tires` and `tireTreads`, including new geometries, materials, colors, instance counts, transforms, and shadow settings.
- Wire up instance matrices and colors for tires/treads and ensure the curb and start/checker geometry remain intact.

### Testing
- Ran the frontend build with `yarn build` which completed successfully.
- Executed the automated test suite with `yarn test` and it passed without failures.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6aa2864af75083298c1a7964581e922d)
