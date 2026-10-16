# Skip AWS discovery when running Frigg start locally

## Summary

- set the Frigg start CLI command to pass an environment flag that skips AWS discovery while running serverless offline
- gate serverless template discovery logic on the new FRIGG_SKIP_AWS_DISCOVERY flag so local runs avoid remote AWS lookups

## Testing

- npm test --workspace @friggframework/devtools -- serverless-template.test.js _(fails: existing Jest suites in frigg-cli currently break on virtual mocks and AWS SDK configuration)_

---

https://chatgpt.com/codex/tasks/task_e_68d57cd7c2a48321914f144c7bf5d5ce

<!-- GITHUB_RELEASE PR BODY: prerelease-version -->

# Version

Published prerelease version: `v2.0.0-next.41`

<details>
<summary>Changelog</summary>

#### 🚀 Enhancement

- `@friggframework/devtools`
    - Skip AWS discovery when running Frigg start locally [#431](https://github.com/friggframework/frigg/pull/431) ([@seanspeaks](https://github.com/seanspeaks))
- `@friggframework/core`, `@friggframework/devtools`, `@friggframework/eslint-config`, `@friggframework/prettier-config`, `@friggframework/schemas`, `@friggframework/serverless-plugin`, `@friggframework/test`, `@friggframework/ui`
    - feat: add KMS decrypt capability check to health endpoint [#428](https://github.com/friggframework/frigg/pull/428) ([@d-klotz](https://github.com/d-klotz) [@seanspeaks](https://github.com/seanspeaks))

#### Authors: 2

- Daniel Klotz ([@d-klotz](https://github.com/d-klotz))
- Sean Matthews ([@seanspeaks](https://github.com/seanspeaks))

</details>

<!-- GITHUB_RELEASE PR BODY: prerelease-version -->
