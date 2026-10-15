# fix(utils): include execution context in timeout errors

## Proposed changes

When an async test or hook exceeds its deadline, `executeAsync` currently throws only `Error('Timeout')`. Include the effective deadline, runnable identity and WDIO retry attempt, for example:

`Timeout after 59997ms in "navigation switches windows" (WDIO attempt 1/1)`

Capture the title and attempt before calling the test so the error retains the original identity if the framework advances its runnable. Prefer the full runnable title, then its title, the callback name and finally `unknown test or hook`. Check that `fullTitle` is callable and escape the title with `JSON.stringify`.

The deadline calculation, 3 ms buffer, retry policy and original error propagation are unchanged. The attempt count is explicitly WDIO's; native framework retries are separate. This adds execution context, not tracking of the blocked WebDriver command or cancellation of a timed-out body.

Follow-up to [the timeout diagnostics request in #15603](https://github.com/webdriverio/webdriverio/pull/15603#discussion_r4024809469).

## Types of changes

- [x] Polish (an improvement for an existing feature)

## Checklist

- [x] I have read the [CONTRIBUTING](https://github.com/webdriverio/webdriverio/blob/main/CONTRIBUTING.md) doc
- [x] I have added tests that prove my fix is effective or that my feature works
- [x] I have added the necessary documentation (if appropriate; no new public API)
- [x] I have added proper type definitions for new commands (if appropriate; no new commands)

## Backport Request

- [x] This change is solely for v9 and does not need to be back-ported

## Validation

- Frozen-lockfile installation and package compilation passed.
- 504 tests across wdio-utils, Mocha, Jasmine and Cucumber passed; no type errors.
- Full repository ESLint and `git diff --check` passed.
- Fake-timer regressions cover deadline precedence, original runnable identity, full-title method binding, hook titles, non-callable metadata, named/anonymous callbacks, Jasmine's deadline and exhausted WDIO retries. The initial six regressions failed against the old message before implementation.

## Further comments

AI disclosure: OpenAI Codex implemented, reviewed and locally validated this contribution for this account.
