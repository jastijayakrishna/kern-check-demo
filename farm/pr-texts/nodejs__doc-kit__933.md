# fix(metadata): use short deprecation anchors

## Description

Use short `DEP####` codes as metadata slugs for headings on the deprecations page. This keeps duplicate handling in the existing stateful slugger, preserves ordinary slugging outside `deprecations`, and avoids emitting a duplicate legacy HTML alias when the primary slug is already short.

This changes web and Orama links from long heading-derived fragments to stable links such as `#DEP0001`. Legacy JSON and `llms.txt` outputs are byte-identical to the base for the tested deprecations source.

Assisted-by: OpenAI Codex

## Validation

- Node.js v24.14.0
- `npm ci` (0 vulnerabilities)
- focused metadata parser test: 27 passed
- `node --run test:ci`: 512 passed, 0 failed
- `node --run lint`: 0 errors, 2 pre-existing warnings in `useOrama.mjs`
- `node --run format:check`
- `changeset status --since=main`
- `node --run test:e2e`: 4 passed
- generated Node.js deprecations source at `e6e6f677b34ba0fc87e897512feee11e4d2c0ca4` with `legacy-html`, `legacy-json`, `web`, `orama-db`, and `llms-txt`; short anchors were verified in legacy HTML, web, and Orama, with legacy JSON and `llms.txt` unchanged from base

## Related Issues

Fixes #790

### Check List

- [x] I have read the Contributing Guidelines and made commit messages that follow the guideline.
- [x] I have run `node --run test` and all tests passed.
- [x] I have checked code formatting with `node --run format:check` and `node --run lint`.
- [x] I have covered the new functionality with unit tests.
