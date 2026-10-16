# @uppy/companion: enforce SSRF protection in WebDAV provider

Fixes #6640

The WebDAV provider never applied Companion's SSRF protection:

1. `allowLocalIPs: !allowLocalUrls` was inverted, so with the default `allowLocalUrls: false` local IPs were allowed.
2. The agent was set under `[`${protocol}Agent`]`, but `URL#protocol` includes the colon (`'http:Agent'`), so the webdav client ignored it and used a default agent.

Now both `httpAgent` and `httpsAgent` are passed with the correct flag (this also covers http↔https redirects). Added a regression test that verifies a loopback WebDAV server receives no request unless `allowLocalUrls` is enabled; it fails without this fix.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
