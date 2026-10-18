# fix(deployer): resolve metadata for exported packages

Fixes #18849.

This updates deployer package metadata resolution to first resolve the package entry from the importing project, then read package.json directly from the resolved package root. That keeps .mastra/output/package.json pinned to the installed package version even when the package exports map does not expose ./package.json.

I also added a regression test for a package that exports its entry point but hides package.json.

Checks run:
- pnpm --filter ./packages/deployer test src/build/package-info.test.ts src/build/plugins/node-modules-extension-resolver.test.ts
- pnpm --filter ./packages/deployer lint
- pnpm --filter ./packages/deployer build:lib

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## ELI5
This change makes the deployer check the installed package’s real folder first, instead of asking for `package.json` through the package export map. That way, it records the correct version even when a package hides its `package.json` file.

## Summary
- Fixed deployer metadata resolution so external package versions are read from the resolved package root on disk.
- Avoided relying on `<pkg>/package.json` export resolution, which can fail for packages that don’t expose that subpath.
- Added a regression test for a package that exports its entry point but hides `package.json`, confirming the correct root path and version are captured.
- Updated the changeset to note the patch release and the dependency version fix.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->
