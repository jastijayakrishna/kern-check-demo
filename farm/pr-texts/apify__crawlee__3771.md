# feat(impit-client): add `cacheClients` option to disable `Impit` client reuse

`ImpitHttpClient` always reused cached `Impit` instances, which might be undesirable, as described in #3769. This change introduces an explicit cache toggle so callers can opt out of client reuse.

Adds `cacheClients?: boolean` to `ImpitHttpClient` constructor options (default: `true`), with JSDoc on the new option.

```ts
const httpClient = new ImpitHttpClient({
  cacheClients: false,
  // other impit options...
});
```

Fixes #3769
