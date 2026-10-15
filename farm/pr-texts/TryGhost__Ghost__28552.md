# Fixed flaky automations E2E test (another attempt)

closes https://linear.app/ghost/issue/NY-1341
ref 4250b43c67f8a95b62eb64bc68f9cbe52718088a

This test waits for `DomainEvents` to be flushed. But in this test, it flushed too early, which caused assertions to fail because automations polling wasn't finished.

This was because our helper, `oneAtATime`, returned immediately. That meant the `DomainEvents` settle would happen immediately, which caused the problem.

This fixes that by making `oneAtATime` return a promise.
