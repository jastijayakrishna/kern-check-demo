# fix(mobile): fall back to bundle-done when the screenshot reach-home marker is lost

## Summary

Third and final robustness fix for the iOS screenshot capture (follows #3484, #3485). Even with the log now line-buffered (#3485), the upload run still flaked ~2 shards per run — iPhone and iPad alike.

Root cause (now visible in the log dump): **`ERR_STREAM_UNABLE_TO_PIPE` is Metro's own error**, thrown after the bundle finishes when its log-forwarding pipe breaks. Once it fires, no further app console.logs are captured — so the `$screen /home` marker never lands and the shard fails at "did not reach the home screen", **even though the screenshot build did auto-sign-in and reach home**.

Fix: the `… Bundled 12345ms …` line lands *before* the pipe breaks, so it's a reliable "JS loaded" signal. When the marker times out but the bundle finished (and the app has had the full reach-home window to sign in + render), **proceed** instead of failing the shard. A genuinely stuck app is still caught downstream when the flow's taps/links hit a blank screen; a bundle that never finished stays a hard failure.

## Release Notes

- [x] No release note needed (internal / tooling change)

## Test plan
- `vp test run mobile-screenshots.test` — 40 pass, incl. a new `metroBundleFinished` case.
- `vp check` — clean.

## After merge
Re-run `mobile-screenshots-ios` (upload: true) — shards should stop flaking on the Metro log-forwarding race.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_012KV6NHZAQUPLz5EigLLd7p
