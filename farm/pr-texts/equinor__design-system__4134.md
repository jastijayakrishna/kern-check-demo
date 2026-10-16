# fix(eds-core-react)!: Improve onChange handler typing for TextField component and remove multiline support

## Problem

When using `onChange` handlers with `TextField` component, developers had to manually specify event types, which created unnecessary boilerplate and reduced developer experience:

```typescript
// Before - manual typing required ❌
<TextField
  onChange={(event: ChangeEvent<HTMLInputElement>) => {
    console.log(event.target.value)
  }}
/>
```

This was caused by the `TextField` type definition using a union type that prevented TypeScript from properly inferring event types.

## Solution

### Simplified TextField Implementation

Simplified `packages/eds-core-react/src/components/TextField/TextField.tsx`:

- **BREAKING CHANGE**: Removed `multiline` prop support from TextField - users should now use the `Textarea` component directly for multiline input
- Removed `rowsMax` and `textareaRef` props
- Removed Field proxy component that switched between Input and Textarea
- TextField now directly extends `InputHTMLAttributes<HTMLInputElement>`
- Simplified to only render `Input` component (much closer to native input behavior)

### Reverted Complex Changes

- Reverted `packages/eds-utils/src/utils/overridableComponent.ts` to original simple implementation
- Removed complex `IntrinsicElementFromHTMLElement` helper type
- Kept type definitions clean and straightforward

### Type Inference Validation

- Updated TextField story to demonstrate automatic type inference without manual type annotations
- TypeScript compiler validates type inference during build process
- Removed runtime tests that don't validate compile-time type inference

## Result

TextField now properly types onChange handlers without manual type annotations:

```typescript
// After - automatic type inference ✅
<TextField
  onChange={(event) => {
    console.log(event.target.value) // TypeScript knows event.target.value is a string
  }}
/>
```

For multiline text input, users should now use the `Textarea` component directly:

```typescript
// Use Textarea for multiline
<Textarea
  onChange={(event) => {
    console.log(event.target.value) // Also properly typed
  }}
/>
```

## Migration Resources

To help with the breaking change, comprehensive migration resources have been provided:

### 1. Migration Guide (`MIGRATION_TEXTFIELD_MULTILINE.md`)
- Complete step-by-step migration examples
- Before/after code comparisons for various scenarios
- Component API comparison table
- Manual review checklist
- Testing guidelines

### 2. Automated Codemod (`textfield-to-textarea.codemod.js`)
- jscodeshift-based codemod for automatic migration
- Transforms TextField with multiline to Textarea
- Handles imports, refs (textareaRef → ref), and prop updates
- Usage: `npx jscodeshift -t textfield-to-textarea.codemod.js --parser=tsx src/`

### 3. Codemod Documentation (`CODEMOD.md`)
- Detailed usage instructions and examples
- What the codemod handles and limitations
- Manual review requirements
- Testing and rollback procedures

### 4. Search Prompts (`SEARCH_PROMPTS.md`)
- Ready-to-use commands for grep, ripgrep (rg), ag
- IDE-specific search patterns (VSCode, WebStorm, Sublime, Atom)
- Git history searches
- CI/CD integration examples

## Quick Migration

**Find TextField with multiline:**
```bash
rg "TextField.*multiline" src/
```

**Auto-migrate:**
```bash
npx jscodeshift -t textfield-to-textarea.codemod.js --parser=tsx src/
```

**Manual migration:**
```typescript
// Before (deprecated)
<TextField multiline label="Description" />

// After
<Textarea label="Description" />
```

## Testing

- ✅ All 434 tests pass
- ✅ TypeScript compilation validates type inference works correctly
- ✅ TextField story demonstrates automatic type inference
- ✅ Build completes successfully
- ✅ Simpler implementation with ~40 lines of complex type logic removed
- ✅ Migration resources thoroughly documented

Fixes equinor/design-system#4133

<!-- START COPILOT CODING AGENT SUFFIX -->



<details>

<summary>Original prompt</summary>

> 
> ----
> 
> *This section details on the original issue you should resolve*
> 
> <issue_title>bug(eds-core-react): onChange handler requires manual event typing for TextField and Input components</issue_title>
> <issue_description>When using onChange with components like <TextField> and <Input> from @equinor/eds-core-react, the event type does not infer automatically.
> 
> Example:
> // Required for EDS components
> onChange={(e: ChangeEvent<HTMLInputElement>) => foo(e.target.value)}
> 
> // Works without explicit typing for a native input
> onChange={(e) => foo(e.target.value)}
> 
> This makes the API feel brittle — developers must manually specify ChangeEvent<HTMLInputElement> or risk incorrect typing.
> 
> Expected behavior:
> Event typing should be inferred automatically, as it is with the native <input> element. Developers should be able to write:
> 
> onChange={(e) => foo(e.target.value)}
> 
> without TypeScript errors.
> 
> Additional context:
> Another developer confirmed experiencing similar typing issues with <Input /> props like onChange, value, and others in @equinor/eds-core-react.
> 
> Possible cause / suggested fix:
> Type inference might be lost due to overly generic prop definitions (e.g., React.ChangeEventHandler<any>). Updating the component’s prop typing to use React.ChangeEventHandler<HTMLInputElement> or proper generics should restore native inference behavior.
> 
> 
> The fix to this issue should be probably tested with unit tests. 
> </issue_description>
> 
> <agent_instructions>The suggested solution should follow good software principles like DRY and SOLID</agent_instructions>
> 
> ## Comments on the Issue (you are @copilot in this section)
> 
> <comments>
> </comments>
> 


</details>

Fixes equinor/design-system#4133

<!-- START COPILOT CODING AGENT TIPS -->
---

💬 We'd love your input! Share your thoughts on Copilot coding agent in our [2 minute survey](https://survey3.medallia.com/?EAHeSx-AP01bZqG0Ld9QLQ).
