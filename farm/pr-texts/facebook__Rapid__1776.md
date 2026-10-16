# Fix `this` context in missing_role validation fix onClick handlers

Quick fixes for `missing_role` validation (set as inner/outer, remove from relation) were broken — clicking them threw `TypeError: can't access property "data", this.issue is undefined`.

The `onClick` handlers were written as arrow functions, which capture `this` lexically (undefined in module scope) instead of binding to the `ValidationFix` instance at call time. Since `entity_issues.js` invokes them as `d.onClick()`, they need to be regular functions so `this` resolves to the `ValidationFix` instance (which has `.issue` set).

## Change

`modules/validations/missing_role.js` — two handlers changed from arrow to regular functions:

```js
// Before (broken): arrow function captures `this` from lexical scope → undefined
onClick: () => {
  const oldMember = this.issue.data.member;  // TypeError
  ...
}

// After (fixed): regular function receives `this` = ValidationFix instance
onClick: function() {
  const oldMember = this.issue.data.member;  // works correctly
  ...
}
```

Affects both the `makeAddRoleFix` handler (set as inner/outer) and the remove-from-relation handler.

<!-- START COPILOT ORIGINAL PROMPT -->



<details>

<summary>Original prompt</summary>

> 
> ----
> 
> *This section details on the original issue you should resolve*
> 
> <issue_title>Validation fixes are broken</issue_title>
> <issue_description>### Description
> 
> 
> the `missing_role` validation (and maybe others?) quick fixes don't work.
> 
> 
> I suspect the issue was introduced in facebook/Rapid#961 which replaced the `onClick` `function` at https://github.com/facebook/Rapid/blob/main/modules/validations/missing_role.js#L95 with a `=>` style func, which given the use of `this` seems problematic.
> 
> ### Screenshots
> 
> <img width="529" height="76" alt="Image" src="https://github.com/user-attachments/assets/c66540d2-b24b-4551-8c59-eb488e2134a0" />
> 
> ### Version
> 
> 2.5.5
> 
> ### What browser are you seeing the problem on? What version are you running?
> 
> Firefox v141.0
> 
> ### The OS you're using
> 
> mac
> 
> ### Steps to reproduce
> 
> create a multipolygon relation and don't add inner/outer roles, when you click the fix to add inner or outer, nothing happens and you get an error in the console.
> 
> 
> 
> ### The browser URL at the time you encountered the bug
> 
> https://rapideditor.org/edit#map=20.82/37.50696/-77.43077&background=USGS-Imagery&id=r-1
> 
> ### The auto-detected useragent string for your browser (leave blank if you're manually filling this form out)
> 
> Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:141.0) Gecko/20100101 Firefox/141.0</issue_description>
> 
> ## Comments on the Issue (you are @copilot in this section)
> 
> <comments>
> </comments>
> 


</details>



<!-- START COPILOT CODING AGENT SUFFIX -->

- Fixes facebook/Rapid#1729

<!-- START COPILOT CODING AGENT TIPS -->
---

✨ Let Copilot coding agent [set things up for you](https://github.com/facebook/Rapid/issues/new?title=✨+Set+up+Copilot+instructions&body=Configure%20instructions%20for%20this%20repository%20as%20documented%20in%20%5BBest%20practices%20for%20Copilot%20coding%20agent%20in%20your%20repository%5D%28https://gh.io/copilot-coding-agent-tips%29%2E%0A%0A%3COnboard%20this%20repo%3E&assignees=copilot) — coding agent works faster and does higher quality work when set up for your repo.
