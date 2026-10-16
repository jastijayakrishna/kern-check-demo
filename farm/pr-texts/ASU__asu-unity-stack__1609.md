# fix(app-webdir-ui): update catalog URL to new domain

### Description

Updated ASU class search URL from legacy `webapp4.asu.edu/catalog/classlist` endpoint to new `catalog.apps.asu.edu` domain in the app-webdir-ui package.

**Changed:**
- `packages/app-webdir-ui/src/QuickLinks/index.js` - Updated href in QuickLinks component
- Added JSDoc documentation comment to QuickLinks component

```jsx
// Before
<a href="https://webapp4.asu.edu/catalog/classlist">ASU class search</a>

// After
<a href="https://catalog.apps.asu.edu">ASU class search</a>
```

## Checklist

- [x] Tests pass for relevant code changes

## Important Reminders
<!-- Add meaningful tests -->
<!-- Remove tests that do not provide value -->

### Links

- [Unity reference site](https://asu.github.io/asu-unity-stack/)
- [UDS Guidelines](https://zeroheight.com/9f0b32a56/p/96ab23-getting-started)

<!-- START COPILOT CODING AGENT SUFFIX -->



<!-- START COPILOT ORIGINAL PROMPT -->



<details>

<summary>Original prompt</summary>

> replace all instances of "https://webapp4.asu.edu/catalog/classlist" with "https://catalog.apps.asu.edu" and make sure the commit message follows the convention "fix: <package-updated>" for the corresponding package it updates. Have a separate commit for each package you update


</details>



<!-- START COPILOT CODING AGENT TIPS -->
---

✨ Let Copilot coding agent [set things up for you](https://github.com/ASU/asu-unity-stack/issues/new?title=✨+Set+up+Copilot+instructions&body=Configure%20instructions%20for%20this%20repository%20as%20documented%20in%20%5BBest%20practices%20for%20Copilot%20coding%20agent%20in%20your%20repository%5D%28https://gh.io/copilot-coding-agent-tips%29%2E%0A%0A%3COnboard%20this%20repo%3E&assignees=copilot) — coding agent works faster and does higher quality work when set up for your repo.
