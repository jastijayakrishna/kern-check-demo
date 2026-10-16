# Update default catalog from dcp55 to dcp56 for HCA

### Ticket

### Reviewers

@.

### Changes

- Modified `CATALOG` constant from `"dcp55"` to `"dcp56"` in `site-config/hca-dcp/dev/config.ts`
- Modified `CATALOG` constant from `"dcp55"` to `"dcp56"` in `site-config/hca-dcp/ma-prod/config.ts`

### Definition of Done (from ticket)

Both dev and ma-prod environments now reference the latest dcp56 catalog.

### QA steps (optional)

Verify the configurations load correctly in their respective environments with the updated catalog reference.

### Known Issues

None.

<!-- START COPILOT ORIGINAL PROMPT -->



<details>

<summary>Original prompt</summary>

> 
> ----
> 
> *This section details on the original issue you should resolve*
> 
> <issue_title>Make dcp56 the default catalog for HCA</issue_title>
> <issue_description>Similar to DataBiosphere/data-browser#4577 we need to updat the default catalog for dev and ma-prod config.ts files to update the default catalog from dcp55 to dcp56. Both constants need to be updated.
> 
> Configuration updates:
> 
> Update the CATALOG constant from "dcp55" to "dcp56" in site-config/hca-dcp/dev/config.ts to use the latest data catalog.
> Update the CATALOG constant from "dcp55" to "dcp56" in site-config/hca-dcp/ma-prod/config.ts to use the latest data catalog.</issue_description>
> 
> ## Comments on the Issue (you are @copilot in this section)
> 
> <comments>
> </comments>
> 


</details>



<!-- START COPILOT CODING AGENT SUFFIX -->

- Fixes DataBiosphere/data-browser#4626

<!-- START COPILOT CODING AGENT TIPS -->
---

✨ Let Copilot coding agent [set things up for you](https://github.com/DataBiosphere/data-browser/issues/new?title=✨+Set+up+Copilot+instructions&body=Configure%20instructions%20for%20this%20repository%20as%20documented%20in%20%5BBest%20practices%20for%20Copilot%20coding%20agent%20in%20your%20repository%5D%28https://gh.io/copilot-coding-agent-tips%29%2E%0A%0A%3COnboard%20this%20repo%3E&assignees=copilot) — coding agent works faster and does higher quality work when set up for your repo.
