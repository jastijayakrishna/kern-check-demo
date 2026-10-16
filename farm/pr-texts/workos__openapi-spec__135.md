# Mount agent sub-resource tags onto the Agents service

## Summary

The agent endpoints in the monorepo were retagged per sub-resource (`agents.registrations`, `agents.blueprints`, `agents.instances`, `agents.sessions`, `agents.blueprints.tokens`) to make room for the blueprints docs nav. Once that spec syncs here, the SDK generator would derive one service per tag (`AgentsRegistrations`, `AgentsBlueprints`, ...) and split the `client.agents.*` SDK surface.

Add a wildcard mount rule to fold them back onto `Agents`:

```ts
'Agents*': 'Agents',
```

This is the upstream version of the local rule the docs snippet generator already carries in `packages/docs/scripts/generate-sdk-snippets.ts` (`localMountRules`), whose comment says to move it into this policy package. No tag changes are needed in the monorepo — the API reference nav keys off the operation's tag independently of SDK mounting.

Verified with `npx oagen resolve` against the monorepo's current `open-api-spec.yaml`: all 15 agent operations mount on `Agents` with unchanged operation names, and `npm test` passes.


Link to Devin session: https://app.devin.ai/sessions/2bc6383e342647a89ca261e9ff487bb1
Open in Devin Desktop: https://app.devin.ai/desktop/session/2bc6383e342647a89ca261e9ff487bb1?variant=devin
Requested by: @m0tzy
