# Add `originalUrl` to findings in `findForUrl`

When we perform a scan, we may end up on a different url than the intended one (due to redirects for login or otherwise). The 'find' action only adds the scanned url (the url we land on) to the findings. There are situations where we need to preserve the original/intended url. 

The ideal approach would be to call the existing 'url' field: 'scannedUrl', and populating the 'url' field with the original/intended url. The problem with this approach is it't not backward compatible. Existing codebases would have to account for this change. Instead, I decided to introduce a new 'originalUrl' field that captures the intended url that was supposed to be scanned. This leaves the existing url field as-is and doesnt disrupt existing codebases.

### Copilot summary
Findings only carried the URL the page ended up on (`page.url()`). If the page redirected, for example to a login page, the URL we were asked to scan was lost. This PR records that URL on every finding as `originalUrl`.

- **`findForUrl.ts`**: `addFinding` now sets `originalUrl: url`, where `url` is the configured URL passed to `page.goto`. It is the last property in the `findings.push({...})` call, so a plugin-supplied `originalUrl` can't overwrite it.
- **`types.d.ts`**: `Finding` gains an optional `originalUrl?: string`.
- **Tests**: a new case in `findForUrl.test.ts` checks that findings carry the configured URL.

```ts
findings.push({...findingData, screenshotId, originalUrl: url})
```

`Finding.url` is unchanged. It is still the post-redirect URL from `page.url()`.
