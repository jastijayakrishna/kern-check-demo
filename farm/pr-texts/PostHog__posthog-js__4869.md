# feat(replay): apply URL masking to JSON-LD payloads

## Problem

Captured JSON-LD can retain URLs in allowed fields such as `category` and `availability`. These values currently bypass replay URL privacy settings, including custom URL masking callbacks.

## Changes

Use the shared `isUrl()` helper from `@posthog/core` to detect URL prefixes, then apply `_maskReplayUrl` during JSON-LD sanitization to retained strings that start with `http://`, `https://`, `//`, `/`, `./`, or `../`, after trimming whitespace. This includes nested entities and scalar arrays. For example, a URL in `Product.category` now uses the same query parameter masking, hash removal, and custom callback as a replay page URL.

Keep the existing property allowlist. The fixed `@context`, normalized `@type`, and captured DOM IDs retain their existing sanitization. Ordinary text, bare relative paths such as `Books/Fiction`, and URLs embedded in prose stay unchanged. Parsing every string against a base URL would classify ordinary text as a relative URL.

A rejected URL is omitted. A callback exception drops that script's capture. Masking happens before output size checks and deduplication, within the existing sanitizer traversal. This change is independent of #4864.

Validation:

- 505 tests pass across the core utility, JSON-LD capture, and lazy recorder suites (one existing test is skipped), including primitive and boxed strings, nested fields, scalar arrays, URL forms, rejected URLs, callback exceptions, output limits, deduplication, and both current and deprecated URL callbacks.
- The production build, targeted lint, formatting, and `git diff --check` pass.
- Against base `21d407a13`, production `array.js` changes by -1 minified byte / +9 gzip bytes (0.01%), and `array.full.js` adds 230 minified bytes / 80 gzip bytes (0.04%).
- The separate `test:typecheck` command stops on missing ambient type definitions for `dompurify` and `dotenv`. The package dependencies and test compiler configuration are unchanged.

## Release info Sub-libraries affected

### Libraries affected

- [x] posthog-js (web)
- [x] @posthog/types
- [x] @posthog/core

## Checklist

- [x] Tests for new code
- [x] Accounted for the impact of any changes across different platforms
- [x] Accounted for backwards compatibility of any changes (no breaking changes!)
- [x] Took care not to unnecessarily increase the bundle size

### If releasing new changes

- [x] Ran `pnpm changeset` to generate a changeset file

## 🤖 Agent context

**Autonomy:** Human-driven (agent-assisted)

Codex used local source inspection, shell tools, Vitest, and the production build. It checked the JSON-LD specification with web search. The implementation uses explicit URL prefixes to avoid treating ordinary text as a relative URL, and reuses the existing sanitizer traversal to limit code and bundle growth. A human must review this PR before merge.
