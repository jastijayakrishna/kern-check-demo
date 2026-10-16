# make perf benchmark script more reliable

The `perf-check` CI job fails intermittently due to race conditions in server readiness detection.

### Bugs fixed

- **`lsof()` was a no-op**: `.toString` (property reference) instead of `.toString()` (method call) — the check always returned truthy (the function itself), never validating anything. Also now wrapped in try/catch since `lsof` exits non-zero when no process is found.

- **Hardcoded `sleep(5000)` replaced with HTTP polling**: New `waitForServer(url)` polls with `fetch()` every 500ms until the server responds, up to a 30s timeout. Eliminates the timing race entirely.

- **Server processes were fire-and-forget**: `startVitePreview()` return values are now stored with `.catch()` handlers to surface unexpected exits.

### Before/After

```js
// Before: always truthy — this is a reference to the toString function, not a call
return execSync(`lsof -i :${port} -P -n`).toString;

// After
return execSync(`lsof -i :${port} -P -n`).toString();
```

```js
// Before: fixed delay, then broken check
await sleep(5000);
let controlLsof = await lsof(port);

// After: poll until actually ready
await waitForServer(url, { timeout: 30_000, interval: 500 });
```
