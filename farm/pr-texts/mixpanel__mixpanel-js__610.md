# Fix fetch response body race: use deferred promise in initFetchObserver

`Promise.all` in `initFetchObserver` captured a stale `Promise.resolve(undefined)` reference for `responseBodyPromise` — the async reassignment inside the fetch `.then` handler happened too late, so network events were emitted before `tryReadFetchBody` resolved, leaving `responseBody` always `undefined`.

## Changes

- **`src/recorder/rrweb-network-plugin.js`** — Replace the eagerly-resolved `responseBodyPromise` with a deferred whose resolver is captured before `Promise.all` runs. Call `responseBodyResolve()` in both branches of the response-body check (body-recorded and body-skipped), so `Promise.all` always settles. `return originalFetchPromise` is untouched — the app's `await fetch()` resolves at headers-received time, not body-read time.

  ```js
  // Before (stale reference — Promise.all never waited for body)
  var responseBodyPromise = Promise.resolve(undefined);
  // ...inside fetch .then:
  responseBodyPromise = tryReadFetchBody(res).then(...); // too late

  // After (stable deferred — Promise.all waits correctly)
  var responseBodyResolve;
  var responseBodyPromise = new Promise(function(resolve) {
      responseBodyResolve = resolve;
  });
  // ...inside fetch .then:
  if (shouldRecordBody('response', options.recordBodyUrls, req.url)) {
      tryReadFetchBody(res).then(function(body) {
          networkRequest.responseBody = body;
          responseBodyResolve();
      });
  } else {
      responseBodyResolve();
  }
  ```

- **`src/recorder/rrweb-network-plugin.js`** — Export `initFetchObserver` to enable unit testing.

- **`tests/unit/rrweb-network-plugin.js`** — Add regression test: installs the observer on a fake `win` with a `Response` body and a matching `recordBodyUrls.response` pattern; asserts `cb` receives a request with `responseBody` equal to the actual response text. This test fails against the pre-fix code.

<!-- START COPILOT CODING AGENT SUFFIX -->



<!-- START COPILOT ORIGINAL PROMPT -->



<details>

<summary>Original prompt</summary>

Fix GitHub issue #607 (Linear MULTI-745): "Session Replay: fetch response bodies often empty due to Promise.all race in network plugin".

## The bug

In `src/recorder/rrweb-network-plugin.js`, function `initFetchObserver` (the patched `fetch` wrapper, roughly lines 490–592 on `master`).

- Line ~511 declares `var responseBodyPromise = Promise.resolve(undefined);`
- Line ~557 builds `Promise.all([requestBodyPromise, responseBodyPromise, originalFetchPromise])`, and that `.then` chain is what emits the recorded network event (it reads `networkRequest.responseBody` at line ~578).
- But `responseBodyPromise` is **reassigned asynchronously** inside the fetch `.then` handler (line ~543–548): `responseBodyPromise = tryReadFetchBody(res).then(function(body){ networkRequest.responseBody = body; });`

Because that reassignment happens *after* `Promise.all(...)` already captured the original `Promise.resolve(undefined)` reference, `Promise.all` never waits for the response-body read. The event is emitted as soon as `originalFetchPromise` resolves (headers processed), while `tryReadFetchBody(res)` is usually still in flight — so `networkRequest.responseBody` is still `undefined` and the recorded event has an empty response body.

The **request** body is unaffected: `requestBodyPromise` is reassigned *synchronously* (line ~522–527) *before* `Promise.all`, so its reassignment is captured. This asymmetry is the tell — the fix must only touch the response-body path.

## Required fix — use a deferred promise (do NOT fold into originalFetchPromise)

There are two candidate fixes. Use the **deferred-promise** one, NOT the "return `tryReadFetchBody(res)` from the fetch `.then`" one.

Reason: `initFetchObserver` returns `originalFetchPromise` to the *caller* (line ~586) — it IS the promise the application `await`s from its own `fetch()` call. If you fold the body read into `originalFetchPromise` (make it `return tryReadFetchBody(res).then(() => res)`), you delay the application's own fetch resolution by up to the body-read timeout (`tryReadFetchBody` has a 500ms internal timeout). Session-replay instrumentation must never delay the app's fetch. Note `tryReadFetchBody` already `clone()`s the response before reading, so it does not consume the app's response stream — the only risk is the timing/delay, which the deferred approach avoids.

Implement it like this (keep the existing "await concurrently so we don't delay the fetch response" comment and the `Promise.all` structure intact):

1. Replace the `var responseBodyPromise = Promise.resolve(undefined);` declaration with a deferred whose resolver is captured in the enclosing scope:
   ```js
   var responseBodyResolve;
   var responseBodyPromise = new Promise(function(resolve) {
       responseBodyResolve = resolve;
   });
   ```
2. Inside the fetch `.then` handler, replace the reassignment block with code that resolves the deferred in ALL branches (so `Promise.all` can never hang):
   ```js
   if (shouldRecordBody('response', options.recordBodyUrls, req.url)) {
       tryReadFetchBody(res).then(function(body) {
           networkRequest.responseBody = body;
           responseBodyResolve();
       });
   } else {
       responseBodyResolve();
   }
   ```
   (`tryReadFetchBody` always resolves — it never rejects — so `responseBodyResolve` will always be called on this path.)
3. Leave `Promise.all([requestBodyPromise, responseBodyPromise, originalFetchPromise])` at line ~557 unchanged — it now references a stable deferred that resolves only after the response body has actually been read into `networkRequest.responseBody`.
4. Leave `requestBodyPromise` exactly as-is (it already works — synchronous reassignment before `Promise.all`). Keep `return originalFetchPromise;` at the end unchanged so the app's fetch resolution is not delayed.

Verify the failure/edge paths still behave as before: if the real `fetch` rejects (network error) or the synchronous `try` block throws, `originalFetchPromise` rejects, so `Promise.all` rejects and the existing `.catch` at line ~582 logs — the pending `responseBodyPromise` is simply abandoned (harmless). No event should be emitted on those paths, matching current behavior.

## Regression test (add if feasible)

`initFetchObserver` is not currently exported, so `tests/unit/rrweb-network-plugin.js` only covers the exported utils. Add coverage for this race in whichever way fits the repo's conventions best:

- Preferred: export `initFetchObserver` (and/or `initNetworkObserver`) from `src/recorder/rrweb-network-plugin.js`, then in `tests/unit/rrweb-network-plugin.js` add a test that installs the observer on a fake `win` whose `fetch` resolves to a `Response` with a JSON body and whose `performance` provides a matching entry, with `recordBodyUrls.response` matched to the URL. Assert the `cb` receives a request whose `responseBody` equals the response text (this test must FAIL before the fix and PASS after). If a fake `performance.getEntriesByName` entry ...

</details>
