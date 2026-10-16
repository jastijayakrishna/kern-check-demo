# feat: add transform v2 handler runtime

## Summary
- Add transform v2 handler ZIP runtime for Browser Flow v2 capture manifests.
- Add CLI/library option gating, public handler types, schema-aware relationship/data-group output, and docs.
- Preserve v1 `--scripts-zip` behavior while documenting the new v2 package contract.

## Test plan
- npm run test -- tests/unit/commands/transform.test.ts tests/unit/lib/commands.test.ts tests/unit/lib/transform-v2.test.ts
- npm run build
- npm run lint
- npm run format:check


Made with [Cursor](https://cursor.com)
