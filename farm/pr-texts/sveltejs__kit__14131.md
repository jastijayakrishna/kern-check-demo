# fix: support multiple cookies with the same name across different paths and domains

Fixes #13947

When setting multiple cookies with the same name but different paths or domains using `event.cookies.set()`, only the last cookie was retained. This happened because the internal `new_cookies` object used just the cookie name as the key, causing cookies with different paths/domains to overwrite each other.

## Example of the issue

```js
// Server load function
export const load = (event) => {
  event.cookies.set('key', 'value1', { path: '/foo/' });
  event.cookies.set('key', 'value2', { path: '/bar/' });
  // Only the second cookie would be sent in set-cookie headers
}
```

Previously, this would only result in one `set-cookie` header:
```
set-cookie: key=value2; Path=/bar/; HttpOnly; SameSite=Lax
```

Now it correctly sends both:
```
set-cookie: key=value1; Path=/foo/; HttpOnly; SameSite=Lax
set-cookie: key=value2; Path=/bar/; HttpOnly; SameSite=Lax
```

## Solution

- **Unique key generation**: Cookies are now stored internally using unique keys combining domain, path, and name in the format `${domain || ''}${path}?${name}`
- **Most specific path wins**: The `cookies.get()` method implements proper cookie precedence by selecting the cookie with the most specific matching path, following standard browser behavior
- **Backward compatibility**: Existing code continues to work unchanged - `cookies.get(name)` automatically finds the most appropriate cookie

## Behavior

```js
// Set cookies with same name but different paths
cookies.set('session', 'user_root', { path: '/' });
cookies.set('session', 'user_admin', { path: '/admin' });

// cookies.get() returns the most specific matching cookie
cookies.get('session'); // returns 'user_admin' when on /admin path
                        // returns 'user_root' when on / path

// Works with domains too
cookies.set('token', 'main', { path: '/', domain: 'example.com' });
cookies.set('token', 'sub', { path: '/', domain: 'sub.example.com' });
// cookies.get('token') returns the appropriate value based on current domain
```

The solution ensures consistent behavior whether cookies are freshly set during the current request or read from existing request headers.

<!-- START COPILOT CODING AGENT TIPS -->
---

✨ Let Copilot coding agent [set things up for you](https://github.com/sveltejs/kit/issues/new?title=✨Set+up+Copilot+instructions&body=Configure%20instructions%20for%20this%20repository%20as%20documented%20in%20%5BBest%20practices%20for%20Copilot%20coding%20agent%20in%20your%20repository%5D%28https://gh.io/copilot-coding-agent-tips%29%0A%0A%3COnboard%20this%20repo%3E&assignees=copilot) — coding agent works faster and does higher quality work when set up for your repo.
