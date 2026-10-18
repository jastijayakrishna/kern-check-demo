# Fix claude.ai MCP connector: OAuth rate-limit bucket, CORS, resource identifier

## Problem

Connecting Lion Reader as a custom connector on **claude.ai** fails with:

> Couldn't register with Lion Reader's sign-in service. You can try again, or add an OAuth Client ID in the connector settings. If this persists, share this reference with support: "ofid_…"

This is a generic error that masks a failure anywhere in the discovery → register → authorize → token chain. Claude Code connects fine because its client is more lenient than the claude.ai web connector.

## Investigation

I reproduced the full flow against production. Everything works from a normal host (discovery `200`, DCR `201`, TLS chain valid, redirect URIs accepted). Research (cross-checked against Anthropic's docs + issue-tracker traces) confirmed claude.ai runs discovery/registration/token **server-to-server from a shared proxy egress range** — so this is **not** a CORS problem. Two concrete defects remained, plus a defense-in-depth gap:

## Fixes

**1. Rate limiting (primary suspect).** `/oauth/register`, `/oauth/authorize`, and `/oauth/token` all shared the strict per-IP `expensive` bucket (capacity 10, refill 1/s) with login/subscribe — key `rate_limit:expensive:ip:{IP}`. claude.ai proxies these from a shared egress IP and re-registers on every connect, so that bucket returns `429`, surfaced as "Couldn't register." Adds a dedicated generous `oauth` bucket (capacity 60, refill 6/s) for these endpoints.

**2. CORS.** Adds a shared MCP/OAuth CORS helper + `OPTIONS` preflight to `.well-known/*`, `/oauth/register`, `/oauth/token`, and `/api/mcp`, exposing `WWW-Authenticate`. Not what breaks claude.ai (server-side), but required by in-browser MCP clients (MCP Inspector "Quick OAuth", playgrounds), which previously got no `Access-Control-Allow-Origin`.

**3. Resource identifier.** The protected-resource metadata advertised the bare origin as `resource`, but per MCP 2025-06-18 / RFC 9728 it must be the canonical MCP endpoint URL (`${issuer}/api/mcp`). Now:
- PRM `resource` = the `/api/mcp` URL; `authorization_servers` stays the origin.
- Audience binding accepts **both** the new value and the origin (`getAcceptedResourceIdentifiers()`), so tokens minted before this change keep working until they expire.
- The `WWW-Authenticate` `resource_metadata` URL is built from the issuer, not by appending to the (now path-bearing) resource.
- The metadata is also served at the path-inserted `/.well-known/oauth-protected-resource/api/mcp` location for RFC 9728 clients.

## Caveat

Without production logs filtered to Anthropic's egress range I can't *prove* which suspect is the root cause (the error is generic). #1 is the most concrete/likely fix and lowest-risk. All three are safe, additive, and spec-improving.

## Tests
- Unit: `oauth` bucket separateness + generosity, list-form `isResourceForThisServer`, CORS helpers, new metadata shape.
- `pnpm typecheck`, `pnpm lint`, and `pnpm test:unit` (1931) pass. Integration/e2e run in CI (Docker unavailable in this env).
- Updated `docs/DESIGN.md`.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
