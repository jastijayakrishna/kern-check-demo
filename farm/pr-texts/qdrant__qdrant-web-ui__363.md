# Fix incorrect API endpoint in payload index "Equivalent Requests" preview

The Create Collection form displayed `PUT /collections/{name}/payload_indexes` in the "Equivalent Requests" preview for payload indexes — an endpoint that doesn't exist and returns 404. The correct Qdrant API endpoint is `PUT /collections/{name}/index`.

## Change

- **`CreateCollectionDialog.jsx`**: Fix template literal URL from `/payload_indexes` to `/index` in `convertToRequest`

```diff
- result += `\nPUT /collections/${collectionName}/payload_indexes \n`;
+ result += `\nPUT /collections/${collectionName}/index \n`;
```

Note: the actual API calls executed by the UI were already correct (via `qdrantClient.createPayloadIndex()`); only the display preview was wrong.

<!-- START COPILOT CODING AGENT TIPS -->
---

⚡ Quickly spin up Copilot coding agent tasks from anywhere on your macOS or Windows machine with [Raycast](https://gh.io/cca-raycast-docs).
