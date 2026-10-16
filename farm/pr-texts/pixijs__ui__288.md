# fix: build-umd script trips the lint gate

`xs lint` runs with `--max-warnings 0`, and the progress line `scripts/build-umd.mjs` prints is a bare `console.log`. So every pull request currently fails lint on a file it didn't touch:

```
/home/runner/work/ui/ui/scripts/build-umd.mjs
  57:1  warning  Unexpected console statement  no-console

✖ 1 problem (0 errors, 1 warning)

ESLint found too many warnings (maximum: 0).
```

Silenced with the same disable comment style already used in the repo, keeping the output — it's useful when the UMD bundle is rebuilt.

### Why this wasn't caught

`.github/workflows/testing.yml` runs `on: [pull_request]` only, so nothing lints main after a merge. #286 was green when it was opened and main has been red since it landed.

Worth considering adding `push` to that trigger, so main going red surfaces immediately rather than through the next contributor's PR.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
