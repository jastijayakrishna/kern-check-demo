# fix(debugger): explain missing worker entry point

### What does this PR do?

Makes the Dynamic Instrumentation worker failure for a missing entry point explicit. Previously it showed up only as an opaque `MODULE_NOT_FOUND` worker error.

```diff
 worker.on('error', error)
-  logWorkerError(error)                       // reason=unknown
+  if error.code is MODULE_NOT_FOUND and error.requireStack is empty
+    // Node.js could not find the worker entry point itself, not one of its dependencies
+    print startup diagnostic naming the missing file
+    report reason=worker_entry_point_not_found
+  else
+    logWorkerError(error)
```

The new diagnostic goes through the existing startup-log writer, so users see it without `DD_TRACE_DEBUG`, and `DD_TRACE_STARTUP_LOGS=false` turns it off:

```
DATADOG TRACER DIAGNOSTIC - Generic Error: Dynamic Instrumentation is disabled, because its worker thread could not load <path>/devtools_client/index.js. Make sure dd-trace is installed as regular files on disk and is not bundled into the application.
```

### Motivation

Part of [DEBUG-6006](https://datadoghq.atlassian.net/browse/DEBUG-6006). The telemetry fields added in #10393 show that 6.20.x users hit `name=Error code=MODULE_NOT_FOUND` from the worker's bootstrap. The stack contains only Node's module loader frames, with no dd-trace frames, meaning the worker's entry file doesn't exist on disk. This happens when dd-trace is bundled, when some of its files aren't deployed, or when it's loaded from a virtual file system the worker can't read (the worker starts with `execArgv: []` and no `NODE_OPTIONS`). Users got no explanation.

The check runs on the worker error instead of an `existsSync` before spawning, because a virtual file system can report the file as present on the main thread even though the worker can't load it.

### Additional Notes

**Why an empty `requireStack` is specific:** Node's CJS loader (v18.20.8, v22.23.2, v24.21.0) builds `requireStack` by walking up from the requesting parent module, so it's empty only when a module is loaded without a parent. Normal `require()`, `require.resolve()`, `createRequire()` and `--require` preloads all have one; only the worker's entry point is loaded without one. None of the worker's 82 modules call `Module._load` or `_resolveFilename` directly. I checked the error shape against real workers on Node 18, 22 and 24.

**Evidence**

- **Before:** a bundled app with `DD_DYNAMIC_INSTRUMENTATION_ENABLED=true` printed nothing. Telemetry reported `worker thread error name=Error code=MODULE_NOT_FOUND reason=unknown`.
- **After:** the same esbuild-bundled app prints the diagnostic above. Telemetry reports `reason=worker_entry_point_not_found`.

New tests use real worker threads for both sides of the boundary:

```text
missing entry file  -> reason=worker_entry_point_not_found, diagnostic printed
missing dependency  -> reason=unknown, no diagnostic
```

Breaking the check deliberately in each direction fails the matching test.

**Validation**

- `./node_modules/.bin/mocha packages/dd-trace/test/debugger/index.spec.js`: 54 passing
- `npm run test:debugger`: 840 passing
- `npx eslint` on the changed files: passed

**Merge danger:** easy to revert. Only the failure path of a worker that can't load its entry point changes. The visible effect is one new stderr line for affected users, who can turn it off with `DD_TRACE_STARTUP_LOGS=false`.

🤖 Generated with [Claude Code](https://claude.com/claude-code)


[DEBUG-6006]: https://datadoghq.atlassian.net/browse/DEBUG-6006?atlOrigin=eyJpIjoiNWRkNTljNzYxNjVmNDY3MDlhMDU5Y2ZhYzA5YTRkZjUiLCJwIjoiZ2l0aHViLWNvbS1KU1cifQ
