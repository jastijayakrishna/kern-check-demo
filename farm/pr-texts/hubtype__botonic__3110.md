# Export client session type and update package

## Description

Exports the `ClientSession` type from the `@botonic/react` package, allowing it to be imported directly by consumers. The package version has been incremented (patch) and the `CHANGELOG.md` updated.

## Context

The `ClientSession` type was not directly accessible from the `@botonic/react` package, limiting its use for type-checking and integration in external modules. This change makes the type publicly available for improved type safety and developer experience.

## Approach taken / Explain the design

1.  **Export `ClientSession` from context**: Added `ClientSession` to the named exports in `packages/botonic-react/src/webchat/context/index.tsx`.
2.  **Re-export `ClientSession` from webchat entry point**: Added `ClientSession` to the named exports in `packages/botonic-react/src/webchat/index.ts`.
3.  **Update package version**: Bumped `@botonic/react` version from `0.40.0` to `0.40.1` (patch).
4.  **Update CHANGELOG**: Added a new entry for version `0.40.1` in `packages/botonic-react/CHANGELOG.md`.

## To document / Usage example

The `ClientSession` type can now be imported directly:

```typescript
import { ClientSession } from '@botonic/react'

const mySession: ClientSession = {
  user: {
    id: 'user-123',
    name: 'Test User'
  }
}
```

## Testing

The pull request...

- doesn't need tests because... **This change involves exporting a type and updating package metadata. The export chain was verified manually during development.**

---
<a href="https://cursor.com/background-agent?bcId=bc-e5e4caee-fab6-44f7-89c2-b3d6949273f9"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/open-in-cursor-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/open-in-cursor-light.svg"><img alt="Open in Cursor" src="https://cursor.com/open-in-cursor.svg"></picture></a>&nbsp;<a href="https://cursor.com/agents?id=bc-e5e4caee-fab6-44f7-89c2-b3d6949273f9"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/open-in-web-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/open-in-web-light.svg"><img alt="Open in Web" src="https://cursor.com/open-in-web.svg"></picture></a>
