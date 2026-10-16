# Use dynamic year in footer copyright

Footer copyright year was hardcoded to `2025`, requiring manual updates each year.

## Change

- Replaced static year with `new Date().getFullYear()` in `Footer.tsx`

```tsx
// Before
&copy; 2025 Appwrite. All rights reserved.

// After
&copy; {new Date().getFullYear()} Appwrite. All rights reserved.
```

<!-- START COPILOT CODING AGENT TIPS -->
---

✨ Let Copilot coding agent [set things up for you](https://github.com/appwrite/arena/issues/new?title=✨+Set+up+Copilot+instructions&body=Configure%20instructions%20for%20this%20repository%20as%20documented%20in%20%5BBest%20practices%20for%20Copilot%20coding%20agent%20in%20your%20repository%5D%28https://gh.io/copilot-coding-agent-tips%29%2E%0A%0A%3COnboard%20this%20repo%3E&assignees=copilot) — coding agent works faster and does higher quality work when set up for your repo.
