# feat: implement artifacts.list() and add filename param to artifacts.get()

## Summary

Adds SDK support for the new `GET /v1/artifacts/list` endpoint (vlm-lab PR #2001) and extends `artifacts.get()` to accept a `filename` parameter.

**New types** in `src/client/types.ts`:
```typescript
type ArtifactSource = "store" | "manifest" | "workspace";

interface ArtifactListItem {
  object_id: string;
  filename: string | null;
  source: ArtifactSource;
}

interface ArtifactListResponse {
  namespace_id: string;
  items: ArtifactListItem[];
}
```

**`Artifacts.get()`** — new optional `filename` in `ArtifactGetParams` (mutually exclusive with `objectId`):
```typescript
const data = await client.artifacts.get({ filename: "report.pdf", sessionId: "..." });
```

**`Artifacts.list()`** — accepts `ArtifactListParams` with `sessionId` or `executionId`:
```typescript
const response = await client.artifacts.list({ sessionId: "..." });
response.items.forEach(item => console.log(item.object_id, item.filename, item.source));
```

Tests cover all new paths including mutual-exclusivity validation for both `get()` and `list()` (20 tests total).

Link to Devin session: https://app.devin.ai/sessions/13d55013533b4c8d826104e377b2cabb
Requested by: @dineshreddy91
