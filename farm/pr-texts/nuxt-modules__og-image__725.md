# fix(runtime): pass cache TTL to the storage driver

### 🔗 Linked issue

Part of #724 (the TTL and docs suggestions; the default store itself is unchanged).

### ❓ Type of change

- [x] 📖 Documentation (updates to the documentation or readme)
- [x] 🐞 Bug fix (a non-breaking change that fixes an issue)
- [ ] 👌 Enhancement (improving an existing functionality)
- [ ] ✨ New feature (a non-breaking change that adds functionality)
- [ ] 🧹 Chore (updates to the build process or auxiliary tools and libraries)
- [ ] ⚠️ Breaking change (fix or feature that would cause existing functionality to change)

### 📚 Description

Runtime cache entries store an `expiresAt`, but it's only checked when the same key is read again (`useOgImageBufferCache`). Images that are never requested again stay in storage until it's cleared. On sites with many dynamic OG images, this is unbounded growth: in #724, a crawler pushed a server from about 0.5 GB to its 8 GB limit.

- **`src/runtime/server/util/cache.ts`:** `setItem` now gets `{ ttl: Math.max(maxAge, 60) }`, so drivers that support expiry (Redis, Cloudflare KV, and others) drop unread entries themselves. The 60-second floor is Cloudflare KV's minimum `expirationTtl`; without it, a per-image `cacheMaxAgeSeconds: 30` would make KV writes fail. Reads still honour `expiresAt`, so shorter lifetimes behave as before.
- **Docs (Runtime Cache guide):** a warning that the default in-memory store has no size limit and ignores TTLs, with an `lru-cache` `maxSize` example for capping it, plus a line under *Cache Time* that the TTL is passed to the driver.
- **`test/unit/cache-ttl.test.ts`:** checks the TTL passed on write and the 60-second floor. Both tests fail without the change. They pass with it, alongside `cache-degrade` and `image-event-handler` (13 tests).

This doesn't change the default in-memory store, which still grows without limit unless it's configured. Making the default size-bounded (for example, `lru-cache` with a `maxSize`) would fix that for everyone, but it changes default behaviour and adds a dependency, so I've left that decision to you. It's suggestion 2 in #724.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
