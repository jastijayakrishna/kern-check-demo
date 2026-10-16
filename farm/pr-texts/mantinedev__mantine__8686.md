# Fix TagsInput duplicate checking bypass with splitChars

TagsInput bypassed duplicate checking when using `splitChars`. Entering "One,one,ONE" created three tags instead of preventing case-insensitive duplicates, and custom `isDuplicate` functions were ignored.

**Root cause**: `getSplittedTags` used `Set` for deduplication, which is case-sensitive and doesn't support custom duplicate checking logic.

**Changes**:

- **`get-splitted-tags.ts`**: Accept `isDuplicate` and `onDuplicate` parameters; implement proper duplicate checking loop with case-insensitive default comparison
- **`TagsInput.tsx`**: Pass duplicate checking functions to `getSplittedTags` in both keydown and paste handlers; clear search input on duplicate detection when `allowDuplicates=false`
- **Tests**: Add coverage for duplicate checking with splitChars (default and custom), Enter key behavior, and custom `isDuplicate` functions

**Behavior change**:
```tsx
// Before: creates ["One", "one", "ONE"]
<TagsInput onDuplicate={callback} />
// User types: One,one,ONE

// After: creates ["One"], calls callback twice
<TagsInput onDuplicate={callback} />
// User types: One,one,ONE
```

Custom `isDuplicate` functions now work consistently with splitChars:
```tsx
<TagsInput 
  splitChars={['|']} 
  isDuplicate={(val) => val.startsWith('test')}
/>
// "test-1|test-2|hello" → only "hello" added
```

<!-- START COPILOT ORIGINAL PROMPT -->



<details>

<summary>Original prompt</summary>

> 
> ----
> 
> *This section details on the original issue you should resolve*
> 
> <issue_title>TagsInput bipassed when splitChars in used</issue_title>
> <issue_description>### Dependencies check up
> 
> - [x] I have verified that I use latest version of all @mantine/* packages
> 
> ### What version of @mantine/* packages do you have in package.json?
> 
> 8.3.14
> 
> ### What package has an issue?
> 
> @mantine/core
> 
> ### What framework do you use?
> 
> Next.js
> 
> ### In which browsers you can reproduce the issue?
> 
> Chrome
> 
> ### Describe the bug
> 
> Hello hope you are well,
> 
> The ` <TagsInput />` component [should not allow](https://github.com/mantinedev/mantine/blob/9c9b2c20b91b327bf9b0ff34ab4e0ac0cdd0bee3/packages/%40mantine/core/src/components/TagsInput/TagsInput.tsx#L272) you to enter in `One,one,ONE` (yielding ["One", "one", "ONE"]), but it does. If you `<TagsInput splitChars={["|"]}/>` (but don't use that character) and use returns to enter in your tags, it will complain about the all the successive entries). If you customize `isDuplicate()` to console.log when it fires, it does not fire with splitChar is used firing vanilla. For this I am using no specified props and then just the spitChars in the second example.
> 
> Thank you, be safe.
> 
> 
> ### If possible, include a link to a codesandbox with a minimal reproduction
> 
> _No response_
> 
> ### Possible fix
> 
> _No response_
> 
> ### Self-service
> 
> - [ ] I would be willing to implement a fix for this issue</issue_description>
> 
> ## Comments on the Issue (you are @copilot in this section)
> 
> <comments>
> </comments>
> 


</details>



<!-- START COPILOT CODING AGENT SUFFIX -->

- Fixes mantinedev/mantine#8685

<!-- START COPILOT CODING AGENT TIPS -->
---

✨ Let Copilot coding agent [set things up for you](https://github.com/mantinedev/mantine/issues/new?title=✨+Set+up+Copilot+instructions&body=Configure%20instructions%20for%20this%20repository%20as%20documented%20in%20%5BBest%20practices%20for%20Copilot%20coding%20agent%20in%20your%20repository%5D%28https://gh.io/copilot-coding-agent-tips%29%2E%0A%0A%3COnboard%20this%20repo%3E&assignees=copilot) — coding agent works faster and does higher quality work when set up for your repo.
