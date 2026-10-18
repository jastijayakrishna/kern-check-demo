# Re-apply Head-to-Head (Mode 2) after outage investigation

## Summary
Re-applies #77 (reverted by #78 after a production outage).

Root-caused the outage before re-applying: cloned the repo into a scratch directory, checked out the exact merged commit (f4f3ed7) from #77, ran `npm ci` to get the exact locked dependency versions Cloudflare's build used (including `vite@8.1.5`, which my local `node_modules` had drifted from — still on a stale `8.1.3`), built it, and served it. **It renders correctly** — same commit, same exact dependency versions Cloudflare used, no blank page.

That rules out the code and the build tooling as the cause. Whatever broke the previous deploy was specific to Cloudflare's edge serving of that one deployment (Pages Functions layer, header rules, or a one-off deploy glitch), not anything reproducible from source. Re-applying with the expectation this was a transient deploy issue, not a real regression — will watch the live site closely right after this merges.

## Test plan
- [x] `npm run test` (162/162), `npx vite build` clean
- [x] Exact commit + exact locked deps (vite 8.1.5) verified working via a from-scratch clone + `npm ci` + `vite preview`, outside the original build environment
- [ ] Matt: merge, then we both watch eyewallanalytics.com closely as the deploy goes out

🤖 Generated with [Claude Code](https://claude.com/claude-code)
