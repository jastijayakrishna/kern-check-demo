# Fail fast with a descriptive error when an updater image is missing from the catalog

GHES release bundles can pin a Dependabot action whose `docker/containers.json` predates an ecosystem the backend already accepts (e.g. Conda in GHES 3.21.X). When that happens, `updaterImageName()` returns `undefined`, which reaches `validImageRepository()`'s `.startsWith()` call and throws an uncaught `TypeError`, surfaced only as a generic `Error fetching updater images`.

## Changes

- **Guard against undefined updater images** — in `src/main.ts`, immediately after resolving `updaterImage` (from `params.updaterImage` or `updaterImageName(details['package-manager'])`), fail the job early with a descriptive error naming the unsupported package manager if no image was resolved, instead of proceeding into the pull/registry-validation path.
- **Regression test** — added a case in `__tests__/main.test.ts` covering a package manager with no catalog entry, asserting the job fails without attempting any image pulls and reports a descriptive error to the Dependabot service.

## Example

```ts
let updaterImage =
  params.updaterImage || updaterImageName(details['package-manager'])

if (!updaterImage) {
  await failJob(
    apiClient,
    'Error fetching updater images',
    new Error(
      `No updater image is configured for package manager '${details['package-manager']}' in this action revision`
    ),
    DependabotErrorType.Image
  )
  return
}
```

This turns an opaque, uncaught `TypeError` into a clear, actionable diagnostic that identifies the affected package manager, without changing behavior for any ecosystem already present in the image catalog.
