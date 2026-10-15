# fix(shared): type JWT aud as string or string array

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Description

Types the `aud` claim on JWT OAuthAccess token payloads & the `aud` field on SDK IdpOAuthAccessToken output.

Also fixes incorrect `millisecond` comments to `second`.

Manually tested w/

```
pnpm --filter @clerk/backend test:node src/tokens/__tests__/verify.test.ts

```

& 

```
# installed sdk
npm i https://pkg.pr.new/@clerk/backend@9585

# verified `aud` is now returned
import { createClerkClient } from '@clerk/backend'

const res = await clerk.idpOAuthAccessToken.verify(token)
//res.aud is present; [ 'http://localhost:8787/mcp' ]
```



## Checklist

- [x] `pnpm test` runs as expected.
- [x] `pnpm build` runs as expected.
- [x] (If applicable) [JSDoc comments](https://jsdoc.app/about-getting-started.html) have been added or updated for any package exports
- [ ] (If applicable) [Documentation](https://clerk.com/docs) has been updated

## Type of change

- [x] 🐛 Bug fix
- [x] 🌟 New feature
- [ ] 🔨 Breaking change
- [ ] 📖 Refactoring / dependency upgrade / documentation
- [ ] other:


Linear Issue: [AIE-1629](https://linear.app/clerk/issue/AIE-1629/javascript-type-rfc-8707-audience-claims-in-jwt-payloads)

<div><a href="https://cursor.com/agents/bc-14a35554-dc9c-44e9-ac20-6c10844ed864?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-14a35554-dc9c-44e9-ac20-6c10844ed864&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
