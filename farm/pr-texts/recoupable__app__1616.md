# feat: migrate room segment lookup to dedicated chats api

## Summary
- migrate `useChatSegment` to dedicated `GET /api/chats/{id}/segment`
- use bearer auth via `useAccessToken`
- respect API override via `useApiOverride`
- map dedicated response shape (`segment_id`) to existing hook contract (`segmentId`)
- remove local route `app/api/roomSegment/route.ts`

## Validation
- `pnpm exec eslint hooks/useChatSegment.ts`
- `rg -n "/api/roomSegment|roomSegment" --glob "!**/node_modules/**"`
