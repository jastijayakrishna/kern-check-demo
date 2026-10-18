# fix(mobile): keep Metro screenshot log line-buffered (tee, not file redirect)

## Summary

Follow-up to #3484. That PR redirected Metro's output to the reach-home marker log with `> FILE` (to dodge the `ERR_STREAM_UNABLE_TO_PIPE` from the old `stdio:'inherit'`). But writing to a **regular file** makes `bunx` block-buffer the forwarded child output, so the log stayed **empty** until a flush that never came during the wait — so **every** iOS shard (iPhone + iPad) timed out at "did not reach the home screen" with an empty Metro-log dump (seen in the upload run 28765725642).

Fix: go back to `| tee` — a **pipe** stays line-buffered, so the `$screen /home` marker lands promptly. Keep `stdio:'ignore'` (not the old `inherit`) so this detached process never shares the runner's stdout, which was the real `ERR_STREAM_UNABLE_TO_PIPE` source.

Verified locally on the iPad: Metro log populates (2 `$screen /home` markers), reach-home succeeds, 6 distinct shots captured.

## Release Notes

- [x] No release note needed (internal / tooling change)

## Test plan
- `vp test run mobile-screenshots.test` — pass.
- Local iPad capture: Metro log populated, reach-home OK, kiosk shot lit.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_012KV6NHZAQUPLz5EigLLd7p
