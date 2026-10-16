# feat(playground): add lifecycle actions for One playgrounds

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary

Implements playground lifecycle actions (favorite/pinned/locked/visibility/delete/fork) for v0play, enabling owners to manage their saved playgrounds and non-owners to fork public playgrounds.

Fixes #828

## Changes

### Composable API (`useOnePlaygrounds.ts`)

New exports:
- `currentMeta` - reactive state for favorite/pinned/locked/visibility
- `currentOwner` - owner user ID from API responses
- `isOwner` - computed that compares current user to owner
- `patchMeta({ favorite?, pinned?, locked?, visibility?, title? })` - partial POST for meta-only updates
- `destroy()` - DELETE with guards (throws if favorite or locked)
- `fork(getContent)` - create owned copy with defaults, navigate to new playground

Updated:
- `create()` now accepts `{ visibility }` option
- `save()` passes visibility through to create

### UI

**Save Dialog** (`PlaygroundSaveDialog.vue`):
- Added visibility toggle (Public/Private) when creating new playgrounds
- Default remains public, user can choose private before save

**File Menu** (`PlaygroundMenuBar.vue`):
- Owner actions (when linked + owner):
  - Make Public/Private toggle
  - Favorite/Unfavorite toggle
  - Pin/Unpin toggle
  - Lock/Unlock toggle
  - Delete (with confirm, disabled when favorited or locked)
- Non-owner action (when linked + not owner):
  - Fork (creates owned copy, navigates to new playground)

**Icons** (`icons.ts`):
- Added: `star`, `star-outline`, `pin`, `pin-outline`, `lock`, `lock-open`, `visibility-public`, `visibility-private`, `delete`, `fork`

## API Notes

- Uses partial POST from api#99 - only sends changed fields
- Meta patches are separate from content autosave to avoid races
- Fork creates with defaults: favorite/pinned/locked false, visibility public
- Delete requires unfavorite + unlock first (guards match play behavior)

## Testing Checklist

- [ ] Linked owner playground: toggle favorite/pin/lock/visibility → partial POST; reload preserves values
- [ ] Create can be private; Open → Saved still opens private owned playgrounds
- [ ] Non-owner on public playground: Fork creates owned copy, navigates to new ID
- [ ] Delete confirms; success clears association; favorite/locked cannot delete
- [ ] Content autosave and meta patch do not clobber each other
- [ ] Unlinked (hash-only) playground: lifecycle actions hidden
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-00f55c1a-de43-4889-a565-30e07983216d?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-00f55c1a-de43-4889-a565-30e07983216d&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
