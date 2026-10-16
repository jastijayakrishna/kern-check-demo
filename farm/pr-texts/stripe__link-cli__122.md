# feat(sdk): migrate WebBotAuthResource to POST /web_bot_auth/sign

## Motivation

Web Bot Auth signing now has a dedicated endpoint `POST /web_bot_auth/sign`  rather than being bundled into another endpoint.

The `WebBotAuthResource` SDK class (added in #105) was pointing at the old combined endpoint. This PR updates it to call the dedicated signing endpoint, keeping the SDK in sync with the current API.

## What changed

**`packages/sdk/src/resources/web-bot-auth.ts`**
- `credentialsEndpoint` renamed to `signEndpoint`
- Endpoint URL updated: `${apiBaseUrl}/v1/agent_identity/credentials` => `${apiBaseUrl}/web_bot_auth/sign`
- JSDoc and error messages updated to reflect the new endpoint

**`packages/sdk/src/resources/__tests__/web-bot-auth.test.ts`**
- URL assertion updated to `https://api.link.com/web_bot_auth/sign`
- Test fixture updated to remove `identity_token`: the signing endpoint returns `{ web_bot_auth: {...} }` only
- Error message assertion updated to match

## What did not change

The response parsing logic is unchanged. The signing endpoint wraps the signature block identically to before: `{ "web_bot_auth": { signature, signature_input, signature_agent, authority, expires_at } }`. The request body is also unchanged: `{ "url": "<target url>" }`.

There is no behavior change for callers of `WebBotAuthResource.getHeaders()`.

## Test plan

- [x] updated tests
