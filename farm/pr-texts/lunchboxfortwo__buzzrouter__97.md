# Bounce every address that resolves to nothing

Three defects in how an addressed message reported failure. All in `src/shared-channels/`.

### 1. A bare `@name` gave no feedback

`explicit` treated the bracket form as the only unambiguous routing intent, so `@trustysqire hello` (a typo for `@trustysquire`) stayed local and was indistinguishable from a message that had been sent.

Checking the regex first, as asked: both forms are anchored with `^\s*`, so `see @[hive] for details` and `ask @bob about it` already parse as `null`. **Position, not brackets, is what separates addressing from mentioning** — `explicit` was buying nothing except the silence. It is removed; anything that parses is routing intent and bounces when it resolves to nothing. A mid-sentence or trailing mention still never parses, so it can never bounce (covered by tests).

### 2. An unknown user was not validated

`@community/nosuchperson hi` was delivered with `@nosuchperson` prepended as plain text — mentioning nobody, with neither end told.

The check belongs on the **destination** session (the user lives in the destination community, and `getProfileName` caches pubkey→name on the actor's own relay). `readRosterRoles()` is the right source for membership because it is relay-signed; only the pubkey→name step is a guess, and it is the same guess a human reading `@bob` in that channel makes.

**Cost, stated plainly:** there is no filter that answers "is anyone here called bob", so a correct check is one roster read plus one profile read per member. The cheapest correct option, and what is implemented:

- the name index is cached per connection for 5s, so a burst costs one build, not one per message;
- one build at a time per community, so concurrent messages share it instead of each starting a roster read;
- a build is abandoned **whole** past a 4s budget (a half-built index would deny members it had not reached yet), and profile names stay cached on the connection so the next attempt gets further and a large community converges;
- **anything unknowable delivers, never bounces**: no live session for that community, an unreadable roster, or a build that ran long. Our own connection being unhealthy is not evidence about their roster.

A member may also be addressed by pubkey.

### 3. The bounce text was stale

`↳ BuzzRouter: no community named "X" is connected here…` used the attribution format replaced in #88. Now, in the grammar delivered messages carry, and naming the half that failed:

```
BuzzRouter: not delivered to @trustysqire — no connected community has that name.
BuzzRouter: not delivered to @destination/nosuchperson — @destination is connected, but nobody there is named nosuchperson.
```

### Loop safety

A notice is an ordinary kind-9 the bridge reads back. It carries `br notice`, which is **not** a projection marker, so `hasBuzzRouterProjectionMarker` does not catch it — the bridge-authored pubkey check in `canonicalizeSourceEvent` is what does. As a second stop the text opens with `BuzzRouter:` rather than an `@`, so it parses as unaddressed chat regardless. A test asserts all three and feeds a real notice back through the subscription.

### Tests

`npm run typecheck`, `npm test` (609 passing), and `npm run build` pass. New unit tests cover each behaviour and its negative: mid-sentence/trailing mention and unaddressed chat neither route nor bounce; unknown community bounces; unknown user bounces; a known user (any casing) and a pubkey deliver; an unreadable roster does not bounce; one roster read per burst and per concurrent burst; a long build is abandoned rather than bouncing on a partial index; a notice cannot be re-ingested. The two cost/safety tests were mutation-checked — reverting the in-flight dedupe and the deadline makes them fail.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01GMAEvM5zBNvpw7KywwqTe7
