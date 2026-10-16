# feat(cli): show active team in `vc whoami`

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary

`vc whoami` previously printed only the logged-in username. This PR adds the actively-selected team to the interactive output, with a distinction between:

- the **globally-selected team** (the one chosen via `vc switch`, stored in `currentTeam` in the global config), and
- a **local override** (the team inferred from a `.vercel/project.json` or linked repo in the current directory).

If the local override and the global selection conflict, the output makes that clear so the user can see which team their commands will actually run under and why.

## Behavior

### TTY output

Before:

```
> acme-team
```

After, when you're on the globally-selected team:

```
> Logged in as rauchg
> Active team: acme-team (Acme Inc.)
```

After, when the linked project overrides the globally-selected team:

```
> Logged in as rauchg
> Active team: other-team (Other Team)
> Local override: scope is set to other-team by the linked project in this directory (globally selected: acme-team).
```

### Non-TTY output

**Unchanged.** We still print just the logged-in `user.username` followed by a newline so existing pipelines like `vc whoami | pbcopy`, CI scripts, and tests that assert on stdout keep working. Team information is available via `--format json`.

### `--format json`

- Always includes `team` (or `null` for personal scope).
- When a local override applies, also includes `localOverride: true` and `globalTeam`.

```json
{
  "username": "rauchg",
  "email": "rauchg@example.com",
  "name": "Guillermo Rauch",
  "team": { "id": "team_abc", "slug": "other-team", "name": "Other Team" },
  "localOverride": true,
  "globalTeam": { "id": "team_xyz", "slug": "acme-team", "name": "Acme Inc." }
}
```

## Implementation notes

- Extended `ScopeContext` with a `globalTeam` field so commands can tell the globally-selected team apart from a team resolved via a project link. The existing `team` field continues to represent the effective team after local overrides are applied.
- `whoami` now calls `getScope` with `resolveLocalScope: true` and compares `team` vs `globalTeam` (ignoring cases where the user passed an explicit `--scope`/`--team` flag) to decide whether to show the local-override notice.
- Added unit tests for: personal scope, globally-selected team, linked-project override, non-TTY output (still prints username), and JSON output with/without a local override.

## Changeset

`.changeset/whoami-show-active-team.md` (patch bump for `vercel`).

<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-3b3e3e93-d04c-4192-98dd-e176c1e38f42"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-3b3e3e93-d04c-4192-98dd-e176c1e38f42"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
