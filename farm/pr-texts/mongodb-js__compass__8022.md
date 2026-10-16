# fix(compass-indexes): include _id in create index field suggestions COMPASS-9771

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Description

The create index modal builds the field-name combobox options from schema autocomplete fields. Previously `_id` was filtered out; that filter is removed so `_id` appears like any other field and users can define compound indexes that include `_id`.

Field names are derived with `schemaFields.map((field) => field.name)` inside the existing `useMemo`.

### Checklist

- [ ] New tests and/or benchmarks are included
- [ ] Documentation is changed or added
- [ ] If this change updates the UI, screenshots/videos are added and a design review is requested
- [ ] If this change could impact the load on the MongoDB cluster, please describe the expected and worst case impact
- [ ] I have signed the MongoDB Contributor License Agreement (https://www.mongodb.com/legal/contributor-agreement)

## Motivation and Context

Addresses **COMPASS-9771**. Creating a compound index that includes `_id` is valid in MongoDB; excluding it from suggestions was an unnecessary limitation.

- [ ] Bugfix
- [x] New feature
- [ ] Dependency update
- [ ] Misc

## Open Questions

None.

## Dependents

None.

## Types of changes

- [ ] _Backport Needed_
- [ ] Patch (non-breaking change which fixes an issue)
- [x] Minor (non-breaking change which adds functionality)
- [ ] Major (fix or feature that would change existing functionality)
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-90da14af-c38f-44f4-8042-391ae5be99cd"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-90da14af-c38f-44f4-8042-391ae5be99cd"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
