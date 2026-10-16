# fix: guard encoded example routes by matched route ID

## Summary

The example app's `protectedRoutesHandle` (`example/src/hooks.server.ts`) matched request paths without normalizing percent-encoded segments, so encoded variants could miss the guard's prefix checks. This change normalizes the path before matching.

_Please review before merging._
