# Add optional `alias` array to repository dispatch success payload

Repository dispatch success events can include deployment aliases, but the client payload type did not model that field. This PR updates the payload contract so consumers can read aliases in a typed way.

- **Payload type update**
  - Added optional `alias?: string[]` to `DispatchDataDeploymentStatusEvent` in `packages/repository-dispatch/src/data/deployment.ts`.
  - Keeps backward compatibility by making the field optional.

- **Documentation update**
  - Updated the package payload example in `packages/repository-dispatch/README.md` to include `alias` and show a success-state payload.
  - Aligns docs with the event shape expected by consumers.

- **Release metadata**
  - Added a changeset for `@vercel/repository-dispatch` patch release.

```ts
export interface DispatchDataDeploymentStatusEvent extends DispatchDataCommon {
  url: string;
  id: string;
  alias?: string[];
  state: DeploymentState;
}
```
