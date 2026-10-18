# fix: flag duplicate action_id within a block

## Summary

Fixes #66. Two interactive elements sharing an `action_id` inside the same block validated clean, so a builder could hand a user a payload Slack will reject. Adds `findDuplicateActionIds`, wired into `validateBlockKit` alongside the other caveat helpers.

Uniqueness is scoped **per block**, not per payload — `state.values` is keyed `block_id` then `action_id`, so the same `action_id` in two different blocks stays legal and is not flagged.

The repro from the issue now returns:

```
blocks[0].elements[1].action_id must be unique within the block — '123' appears at elements[0] and elements[1]
```

(em dash, matching `findDuplicateBlockIds`; the issue's sample used a hyphen.)

## Type of change

- [x] Bug fix (non-breaking change that fixes an issue)
- [ ] New feature (non-breaking change that adds functionality)
- [ ] Breaking change (fix or feature that would cause existing behavior to change)
- [ ] Schema update (changes to `src/slack-block-kit.schema.json`)
- [ ] Docs / chore (no runtime change)

## Changes

- New `src/helpers/find-duplicate-action-ids.ts`. One namespace per block, collected from `elements` / `actions` / `element` / `accessory` — covering `actions.elements[]`, `context_actions.elements[]`, `card.actions[]`, `input.element`, `section.accessory`.
- Exported from `src/helpers.ts`; called from `validateBlockKit` next to `findDuplicateBlockIds`.
- README: intro line, à-la-carte import example, helpers table, cross-payload-rules coverage line.
- Tests: unit coverage in `test/find-duplicate-action-ids.test.ts`, wiring + the "legal across blocks" case in `test/validate-block-kit.test.ts`, and a fast-check termination property alongside the other walkers.

Two calls beyond the issue's scope list, worth a look:

- **`container.child_blocks` recursion.** The issue didn't list it, but the same bug is reachable inside a container, and each child block carries its own `block_id` — so each child opens its own namespace rather than sharing the container's. Same treatment as `carousel` → cards.
- **Depth cap (`MAX_WALK_DEPTH = 50`).** Recursion keys off `type` alone, not schema validity, so a hand-crafted `container` → `container` → … payload would otherwise blow the stack. Matches the cap in `check-focus-on-load-uniqueness` / `check-number-input-bounds`.

Non-string `action_id` values are skipped, so malformed payloads fall through to the schema error rather than producing a confusing duplicate message.

## Testing

- [x] `pnpm test` passes (515 tests, 21 files)
- [x] `pnpm typecheck` passes
- [x] `pnpm lint` passes
- [ ] `pnpm validate-schema` passes (if the schema changed) — schema unchanged
- [x] Added or updated tests under `test/` covering the change

## Schema changes

None — `src/slack-block-kit.schema.json` is untouched. JSON Schema can't express per-property uniqueness across sibling items, which is the same reason `findDuplicateBlockIds` lives in the helper set.

## Checklist

- [x] Commit messages follow [Conventional Commits](https://www.conventionalcommits.org/) (required for release-please)
- [x] Public API changes are reflected in `README.md`
- [x] No secrets, tokens, or sample tenant data committed

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- codesmith:footer -->
---
<a href="https://app.blacksmith.sh/TightknitAI/codesmith/slack-block-kit-validator/pr/67"><picture><source media="(prefers-color-scheme: dark)" srcset="https://pr-comments-assets.blacksmith.sh/codesmith/view-with-codesmith-dark-v2.svg"><source media="(prefers-color-scheme: light)" srcset="https://pr-comments-assets.blacksmith.sh/codesmith/view-with-codesmith-light-v2.svg"><img alt="View with [code]smith" src="https://pr-comments-assets.blacksmith.sh/codesmith/view-with-codesmith-dark-v2.svg"></picture></a> <a href="https://backend.blacksmith.sh/track/enable-autofix?expires=1788455401&installation_model_id=13354&pr_number=67&repository=TightknitAI%2Fslack-block-kit-validator&return_to=https%3A%2F%2Fgithub.com%2
