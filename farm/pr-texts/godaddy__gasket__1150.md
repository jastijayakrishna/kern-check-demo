# Convert gasket-utils to ESM with CommonJS compatibility

## Summary

Convert gasket-utils package from CommonJS to ESM while maintaining backward compatibility:

- Migrate from Jest to Vitest for better ESM support
- Add SWC build configuration for CommonJS output
- Update package exports to support both ESM and CommonJS consumers

## Changes

- Convert all lib files to ESM syntax (import/export)
- Add Vitest configuration and update test files
- Configure SWC to generate CommonJS build in cjs/ directory
- Update package.json exports with conditional exports for both module systems

## Test plan

- [x] All gasket-utils tests pass with Vitest
- [x] Build generates proper CommonJS files with .cjs extensions
- [x] Fix Jest mocking issues in create-gasket-app (follow-up needed)

🤖 Generated with [Claude Code](https://claude.ai/code)
