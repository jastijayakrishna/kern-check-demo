# feat: Update client-sdk user cache with user-specific caching and 30 day TTL

## Overview
This PR updates the client-side SDK cache to address several shortcomings in the current implementation:

1. Standardizes the default cache TTL to 30 days across all client-side SDKs (previously 7 days in JS SDK)
2. Implements user-specific caching, allowing configs to be cached and retrieved per user ID
3. Maintains backward compatibility with existing cached configs
4. Migrates from old cache format to new format
5. Removes `saveUser` / `loadUser` from `CacheStore.ts` that was only ever saved not loaded.
6. Keeps the anon user_id consistent between identifyUser calls
7. Adds an `expirary_date` to keys stored in storage, cleans up old expired keys.

Fixes #1081.

---

💡 You can make Copilot smarter by setting up custom instructions, customizing its development environment and configuring Model Context Protocol (MCP) servers. Learn more [Copilot coding agent tips](https://gh.io/copilot-coding-agent-tips) in the docs.
