# feat(sql-pg): expose TCP keepalive settings

A PostgreSQL outage investigation reproduced queries hanging on an existing TCP connection that received neither responses nor a close/reset, even though fresh connections worked. `connectTimeout` only covers startup.

```diff
 query bytes acknowledged; existing TCP connection silently lost (no response or FIN/RST)
- query stays pending
+ configured keepalive probes go unanswered
+ socket reports an error
+ pool retires the dead connection
+ subsequent queries can acquire a healthy connection
```

Add opt-in `keepAlive` settings for idle delay, probe interval, and probe count on native TCP connections, including TLS, cancellation sockets, and pool replacements. Timings accept Effect durations; keepalives remain disabled unless configured.

_This PR was raised with assistance from Codex ( GPT 6.1 Sol )_

Closes EFF-2075
