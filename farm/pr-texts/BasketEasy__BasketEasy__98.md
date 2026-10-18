# Fail fast and log on Redis connection issues in scoresheet OCR queue

ioredis's default retryStrategy reconnects forever, so a bad or
unreachable REDIS_URL silently hangs every queue command (enqueue,
worker polling) instead of erroring — a scoresheet upload looked
"stuck" with no log output to explain why.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_016Cow3jXDSxT8jxnF7DHyZx
