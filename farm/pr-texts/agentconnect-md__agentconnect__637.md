# fix(sessions): stabilize hook source and participant header

## Summary

- hydrate direct session-detail responses with stable hook kind and display metadata so GitHub identity is correct on the first render
- keep the detail mapping compatible with control planes that do not yet return hook metadata
- replace the duplicate agent participant dropdown with involved human avatars whose names appear on hover
- cover direct webhook and GitHub detail hydration end to end

## Verification

- Web test suite: 858 passed
- Control Plane integration suite: 978 passed
- focused session-metadata integration test: 8 passed
- Control Plane and Web typechecks
- focused ESLint and Prettier checks
- pre-push full-repository lint

Created by Codex . GPT-5
