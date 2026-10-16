# [7.x backport] feat: Allow specifying startLine in code frame

Backport PR #17070 to ensure parser error code frames honor parser `startLine/startColumn` when consuming code that is part of a larger source. This prevents mismatched line numbers in error output.

- **code-frame numbering and markers**
  - Add `startLine` option to `@babel/code-frame` and adjust line/marker calculations accordingly.
- **parser error framing**
  - Pass `startLine` to `codeFrameColumns` and offset columns when `startColumn` is specified.
- **coverage**
  - Add regression tests for `startLine` handling in both `@babel/code-frame` and `@babel/core` parse errors.

Example:

```js
parseSync("const* a = 1;", {
  parserOpts: { startLine: 3, startColumn: 3 },
  highlightCode: false,
  configFile: false,
  babelrc: false,
});

// code frame now reports line 3 with correct gutter/marker alignment
```

<!-- START COPILOT CODING AGENT TIPS -->
---

✨ Let Copilot coding agent [set things up for you](https://github.com/babel/babel/issues/new?title=✨+Set+up+Copilot+instructions&body=Configure%20instructions%20for%20this%20repository%20as%20documented%20in%20%5BBest%20practices%20for%20Copilot%20coding%20agent%20in%20your%20repository%5D%28https://gh.io/copilot-coding-agent-tips%29%2E%0A%0A%3COnboard%20this%20repo%3E&assignees=copilot) — coding agent works faster and does higher quality work when set up for your repo.
