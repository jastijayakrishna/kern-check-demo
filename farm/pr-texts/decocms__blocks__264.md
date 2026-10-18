# feat(scaffold): add Props interface with seo and github to generated site.ts

## Summary

- The deco-migrate scaffold now generates a `Props` interface in `src/apps/site.ts` with CMS-editable fields: `seo`, `github`, `platform`
- This is picked up automatically by `generate-schema.ts`'s third pass (PR #257) which scans `src/apps/` and emits them to `manifest.blocks.apps`
- Without a `Props` interface, the Studio site tab opened but showed no editable fields

## Problem

The existing scaffold generated `src/apps/site.ts` with only `Platform` and `AppContext` — no `Props` interface. When `generate-schema.ts` (with the third pass from #257) scanned this file, it produced an empty schema for `site/apps/site.ts`.

As a result, the Studio Content > Site tab showed the app entry but rendered no form fields.

## github field

The `github` block (owner, repo, branch, team) enables team access management from the Studio site tab — a common need for store projects.

## Test plan
- Run deco-migrate on a fresh deco.cx site
- Check that `src/apps/site.ts` contains a `Props` interface
- Run `npm run generate:schema` and confirm `meta.gen.json` contains `site/apps/site.ts` in `manifest.blocks.apps` with `seo` and `github` properties

Generated with [Claude Code](https://claude.com/claude-code)

<!-- This is an auto-generated description by cubic. -->
---
## Summary by cubic
Scaffold now generates a CMS-editable `Props` interface in `src/apps/site.ts` and a default `Site` export. `generate-schema.ts` now always registers the site app, merging or falling back to built-in `seo`, `github`, and `platform` fields so the Studio Site tab always shows a form.

- **New Features**
  - Adds `seo` fields (title, description, favicon, image, titleTemplate, noIndexing) and `github` settings (owner, repo, branch, team).
  - Ensures the site app is included in `manifest.blocks.apps` even without `Props`; merges built-in fields when present and emits a base64 alias for manifest lookup.

<sup>Written for commit cef5587ac605631334606c57ba439b787afa9e12. Summary will update on new commits.</sup>

<a href="https://cubic.dev/pr/decocms/deco-start/pull/264?utm_source=github" target="_blank" rel="noopener noreferrer" data-no-image-dialog="true"><picture><source media="(prefers-color-scheme: dark)" srcset="https://www.cubic.dev/buttons/review-in-cubic-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://www.cubic.dev/buttons/review-in-cubic-light.svg"><img alt="Review in cubic" src="https://www.cubic.dev/buttons/review-in-cubic-dark.svg"></picture></a>

<!-- End of auto-generated description by cubic. -->


