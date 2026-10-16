# fix: installed skill consumer compat

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary
- bump the npm package to `0.0.9` and update the changelog because template conversions touch shipped source
- bump the phase skill version to `0.0.16`
- enforce Oxlint's `prefer-template` rule globally
- convert existing string concatenations in source, tests, and tooling to template literals
- use template literals in consumer-installed scanner and eval fixtures
- read the skill version from canonical `SKILL.md` when generated `metadata.json` is omitted by an installer
- add regression coverage for the metadata-free installed layout
- regenerate scanner goldens, metadata, bundle sizes, and packaged skill artifacts

## Verification
- `node scripts/check-package-version.mjs "04267a1571b439f68524045a2a41fcc64917f963"` (`0.0.8 -> 0.0.9`)
- `pnpm validate` (51 files, 812 tests passed)
- `pnpm size`
- pre-commit lint, formatting, and artifact generation completed
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-f303984e-3c1e-4bbf-bc3d-ac13ceb7a16c?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-f303984e-3c1e-4bbf-bc3d-ac13ceb7a16c&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
