# fix: shell-quote review diff base in git diff commands

### Motivation
- Auto-detected repository trunk names were being written into the review `diffBase` and interpolated directly into shell `git diff` commands, opening a command-injection vector when branch names contain shell metacharacters. 
- The fix hardens command construction to ensure untrusted branch names cannot inject shell payloads while preserving existing review behavior for `HEAD` and `--staged` bases.

### Description
- Quote `diffBase` using `shellQuote()` before embedding it into shell command strings in `buildGitDiffCommand` (`src/common/utils/git/diffParser.ts`).
- Import `shellQuote` from `src/common/utils/shell` and use the quoted `diffBase` for both merge-base and three-dot branch diff paths, retaining current logic for `HEAD` and `--staged` cases.
- Add a focused unit test `should shell-quote diffBase to prevent command injection` asserting malicious branch-like inputs are emitted as quoted literals (`src/common/utils/git/diffParser.test.ts`).

### Testing
- Added a unit test in `src/common/utils/git/diffParser.test.ts` that verifies `buildGitDiffCommand("main;touch /tmp/pwned", false, "", "diff")` emits a quoted branch literal, but the test runner was not executed locally. 
- Attempting `bun --version` failed in this environment because Bun is not installed and automatic download is blocked by the network tunnel, so `make test` / `bun test` and `make static-check` were not run here.

------
[Codex Task](https://chatgpt.com/codex/tasks/task_b_69b3f18bd848832ea5196d4b0d361b55)
