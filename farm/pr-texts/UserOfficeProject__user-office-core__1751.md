# refactor: improve experiment status action logging

Mirrors the logging hardening applied to the proposal status action engine in `improve-status-action-logging`, extending it to `experiment/statusActionEngine`.

## Changes

- **`logger` import** — adds `@user-office-software/duo-logger` import
- **`groupLogContext`** — built per group with `workflowStatusConnectionId` and `experimentPks` (no `callIds`/`proposalPks`)
- **Per-action `.catch` handlers** — attached to `emailActionHandler` and `rabbitMQActionHandler` invocations, each logging with action-specific message and `logContext` (`groupLogContext` + `actionId`)
- **Top-level `.catch`** — catches unexpected failures in the outer `Promise.all` and logs via `logger.logException`

```ts
const groupLogContext = {
  workflowStatusConnectionId,
  experimentPks,
};
// ...
emailActionHandler(statusAction, experiments).catch((error) =>
  logger.logException('Error executing email status actions', error, logContext)
);
// ...
Promise.all([...]).catch((error) => {
  logger.logException('Error executing experiment status action engine', error);
});
```
