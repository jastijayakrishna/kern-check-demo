# Reduce RSC payload by omitting default apiHost and useProjectHostname

Omit `apiHost` and `useProjectHostname` from the `SanityLiveClientComponent` props when they equal their defaults (`"https://api.sanity.io"` and `true`), same pattern already used for `token` and `includeDrafts`. Reduces RSC payload size for faster page loads.

- **Both condition entry points** (`react-server`, `next-js`): conditionally pass `undefined` instead of the default values
- **Shared constant**: extracted `defaultApiHost` to `shared/constants.ts` for consistency across conditions
- **Tests**: added explicit assertions that default `apiHost` and `useProjectHostname` are omitted from the client component config
- **Changeset**: patch
