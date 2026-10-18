# [Fix] Batch pending Fast session steering

## Summary
- accumulate same-user follow-ups while the Fast/OpenCode session is running
- flush the ordered block at real native pickup boundaries: prompt-active, assistant-completed, or tool-completed
- preserve each message as its own canonical transcript entry
- submit accumulated, bounded message blocks and attachments as native OpenCode steers
- leave multi-message overflow queued for the next bounded steer
- defer an oversized singleton to the durable whole-turn fallback instead of hot-retrying native steering
- keep other participants and later messages behind the authorization boundary
- log accepted native-steer batch sizes for diagnosis

## Validation
- 178 focused provider/Fast tests covering event-boundary accumulation, bounded chunking, oversized-singleton fallback, ordering, images, authorization boundaries, retries, and steering races
- lint:fast, check-types:fast, knip, and targeted formatting all pass
- full GitHub CI, CodeQL, Docker build, compatibility checks, and Roomote code review all pass on commit 0a6153a; review found no new issues
- exact-head real Slack + Brave proof in #dan-tests: while one Fast turn was running, four rapid Boundary 1–4 messages produced one native steer with followUpCount=4
- all four durable rows have attempts=0 and the same delivered_at timestamp; OpenCode stores one ordered user block containing Boundary 1–4; the visible Slack reply incorporated all four updates
- no fixed debounce or quiet-window timeout is used
