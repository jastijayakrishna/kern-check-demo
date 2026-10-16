# Normalize icon export naming 

Several icon exports in `src/icons` used names that didn’t consistently follow the `*Icon` convention. This PR standardizes most of the updated icon index exports to `*Icon`-suffixed names, while restoring `ChevronLeft` and `ChevronRight` to their original unsuffixed exports based on review feedback.

- **Exports updated**
  - `src/icons/AccessTime/index.ts` → `AccessTimeIcon`
  - `src/icons/Fullscreen/index.ts` → `FullScreenExitIcon` and `FullScreenIcon`
  - `src/icons/GroupAdd/index.ts` → `GroupAddIcon`
  - `src/icons/MesheryOperator/index.ts` → `MesheryOperatorIcon`
  - `src/icons/Barchart/index.ts` → `BarChartIcon`

- **Reverted to original state (per feedback)**
  - `src/icons/ChevronLeft/index.ts` → `ChevronLeft`
  - `src/icons/ChevronRight/index.ts` → `ChevronRight`
  - `src/icons/ChevronLeft/ChevronLeft.tsx` and `src/icons/ChevronRight/ChevronRight.tsx` remain with original `ChevronLeft`/`ChevronRight` symbol names.

- **Feedback alignment**
  - Kept single `default as` export entries per line in each updated icon index file.
  - Reverted `src/__testing__/Icons.test.tsx` to its previous state.

```ts
export { default as AccessTimeIcon } from './AccessTimeIcon';
export { default as ChevronLeft } from './ChevronLeft';
export { default as ChevronRight } from './ChevronRight';
```
