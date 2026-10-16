# Add support for Angular bindings API with twoWayBinding

## Overview

This PR implements support for Angular's native bindings API in Angular Testing Library, addressing the suggestion in #526 that ATL's current input/output interfaces may be unnecessary with Angular's new approach.

## What's New

Angular introduced a native bindings API that allows direct binding of inputs and outputs when creating components with `TestBed.createComponent()`:

```typescript
// Angular native approach
TestBed.createComponent(MyComponent, {
  bindings: [
    inputBinding('value', () => 'test-value'),
    outputBinding('click', (event) => console.log(event)),
    twoWayBinding('name', signal('initial'))
  ]
});
```

This PR adds seamless support for this pattern in ATL while maintaining full backward compatibility.

## Usage Examples

### New Bindings API
```typescript
import { render, screen } from '@testing-library/angular';
import { inputBinding, outputBinding, twoWayBinding, signal } from '@angular/core';

await render(MyComponent, {
  bindings: [
    inputBinding('value', () => 'test-value'),
    inputBinding('greeting', () => 'hello'),  // supports aliases
    outputBinding('clicked', clickHandler),
    twoWayBinding('name', signal('initial'))  // two-way binding with signals
  ],
});
```

### Traditional API (Still Supported)
```typescript
await render(MyComponent, {
  inputs: { value: 'test-value', greeting: 'hello' },
  on: { clicked: clickHandler },
});
```

### Mixed Usage
```typescript
// Both approaches can coexist with intelligent warnings
await render(MyComponent, {
  bindings: [inputBinding('value', () => 'test-value')],
  inputs: { greeting: 'hello' }, // Warning: ignored due to Angular limitations
  on: { clicked: clickHandler }, // Works alongside bindings
});
```

## Benefits

1. **Native Angular Integration** - Uses Angular's official bindings API
2. **Better Performance** - Bindings are handled natively by Angular, avoiding manual setup overhead
3. **Improved Type Safety** - Leverages Angular's built-in type checking for bindings
4. **Future-Proof** - Aligns with Angular's recommended testing patterns
5. **Zero Breaking Changes** - Existing code continues to work unchanged
6. **Two-Way Data Binding** - Full support for bidirectional data flow with signals

## Implementation Details

- Added `bindings?: Binding[]` option to `RenderComponentOptions`
- Modified `createComponent()` to use `TestBed.createComponent(component, { bindings })` when bindings are provided
- Smart logic handles mixed usage scenarios with helpful warnings
- Users import binding functions directly from `@angular/core`
- Added comprehensive tests validating input binding, output binding, two-way binding, and mixed usage scenarios
- Support for writable signals with re-rendering scenarios

## Binding Types Supported

- **`inputBinding()`** - Bind input values, including with writable signals for dynamic updates
- **`outputBinding()`** - Listen to component outputs
- **`twoWayBinding()`** - Bidirectional data binding with writable signals

## Mixed Usage Behavior

Due to Angular's limitations, inputs and outputs behave differently when mixing approaches:

- **Inputs**: Angular prevents mixing `setInput()` with `inputBinding()`, so bindings take complete precedence (with warning)
- **Outputs**: Both `outputBinding()` and traditional `on` listeners work together
- **Warnings**: Helpful messages guide users toward consistent usage patterns

## Migration Path

Users can gradually adopt the new bindings API:
- **Immediate**: Continue using existing `inputs`/`on` APIs - no changes required
- **Gradual**: Start using `bindings` for new tests while keeping existing tests unchanged  
- **Future**: Eventually migrate to bindings API for consistency with Angular's patterns

This provides a smooth transition path while giving users access to Angular's modern testing capabilities.

Fixes testing-library/angular-testing-library#546

<!-- START COPILOT CODING AGENT SUFFIX -->

Fixes testing-library/angular-testing-library#546

<!-- START COPILOT CODING AGENT TIPS -->
---

💬 Share your feedback on Copilot coding agent for the chance to win a $200 gift card! Click [here](https://survey3.medallia.com/?EAHeSx-AP01bZqG0Ld9QLQ) to start the survey.
