# Fix @expo/cli format check failure in instantiateMetro

A formatting regression in `@expo/cli` caused the workspace format job to fail on `src/start/server/metro/instantiateMetro.ts`. This PR applies the required `oxfmt` formatting update in that file only.

- **Scope**
  - `packages/@expo/cli/src/start/server/metro/instantiateMetro.ts`

- **Change**
  - Reflowed a multiline type assertion/property access expression to match `oxfmt` output.
  - No behavioral or logic changes.

- **Representative diff**
  ```ts
  -      environment: (graph.transformOptions.customTransformOptions as ExpoCustomTransformOptions | undefined)
  -        ?.environment,
  +      environment: (
  +        graph.transformOptions.customTransformOptions as ExpoCustomTransformOptions | undefined
  +      )?.environment,
  ```
