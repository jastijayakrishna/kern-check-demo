# Add selected Unicorn rules to ESLint

Adds ESLint Unicorn 56.0.0 for the project's Node 20 / ESLint 8 setup and enables 18 selected rules alongside the existing custom checks.

- Allow `err` and `error`, including prefixes and suffixes such as `errReading`, `errorReading`, `readErr`, and `readError`. Preserve the existing `catch(err)` in `FindFile`.
- Initialize `VscodeError` through `new Error(message)` and remove the redundant message assignment.
- Resolve the selected lint findings, including using `join('|')` for static variable names. Preserve named regex captures and parser behavior. Keep `no-useless-undefined` configured with `checkArrowFunctionBody: false`.
- Add `.gitattributes` and `.editorconfig` so Git stores LF and working copies/editor saves use CRLF on every platform. Normalize this PR's files and document verification for local and cloud agents in `AGENTS.md`.

Validation of the final tree, unchanged by rebasing onto the latest master: all 561 tests in 19 suites pass; full ESLint checks 82 files with zero errors and zero warnings (the existing React-version detection notice remains). All nine changed regex literals passed 1,048,828 comparisons of matches and captures, including all UTF-16 code units in representative contexts. Catch-name acceptance/rejection and VscodeError message inheritance were also checked directly. Verified LF in Git and CRLF without BOM in all 19 changed files, including checkout with `core.autocrlf=false`. Parser fixtures and generated declarations are unchanged.

Copilot's untyped JSDoc concern was checked against the original PR base, current master, and this branch. In all three, `@param options` is unmatched and produces no warning; the original `(?:...)` group was neither optional nor an alternative. Ten direct parser cases produced identical metadata and warnings, so the review thread was resolved without changing parser acceptance.
