# fix: don't set nuxt 2 legacy config for nuxt 4+

Fixed Nuxt framework detection to properly handle v4+ versions by using modern config as default and consistent naming.

## Problem
Nuxt v4+ projects were incorrectly falling back to legacy v2 configuration due to version detection logic that only matched exactly version 3. This caused Nuxt v4 projects to use older commands like `nuxt generate` instead of modern commands like `nuxt build`.

## Solution
- **Default Configuration**: Uses modern Nuxt 3+ config as class defaults
- **Override Logic**: Only overrides to legacy commands for v2 projects
- **Version Detection**: Changed from exact equality (`=== 3`) to greater-than-or-equal (`>= 3`) comparison
- **Consistent Naming**: All versions use 'Nuxt' name for consistency
- **Test Coverage**: Added comprehensive tests for v2, v3, and v4 scenarios

## Implementation Details

### Default Class Configuration (Modern)
```typescript
name = 'Nuxt'                   // Consistent name for all versions
dev.command = 'nuxt dev'        // Modern dev command
build.command = 'nuxt build'    // Modern build command
```

### Override Logic for Legacy Versions
```typescript
// Override with legacy commands only for major version < 3
if (version < 3) {
  this.build.command = 'nuxt generate'
  this.dev.command = 'nuxt'
}
// Name always stays 'Nuxt' - never overridden
```

### Code Quality Improvements
- Simplified condition logic without empty branches
- Accurate comments that match implementation
- Test structure with explicit version fixtures instead of 'latest'
- Clear separation between modern and legacy test cases

## Behavior Matrix
| Package | Version | Name | Build Command | Dev Command |
|---------|---------|------|---------------|-------------|
| `nuxt` | v2.x | "Nuxt" | `nuxt generate` | `nuxt` |
| `nuxt` | v3.x+ | "Nuxt" | `nuxt build` | `nuxt dev` |
| `nuxt3` | any | "Nuxt" | `nuxt build` | `nuxt dev` |
| `nuxt-edge` | v2.x | "Nuxt" | `nuxt generate` | `nuxt` |
| `nuxt-edge` | v3.x+ | "Nuxt" | `nuxt build` | `nuxt dev` |

## Test Results
All 6 tests pass covering:
- ✅ Modern config: nuxt3, nuxt v3+, nuxt-edge v3+ → 'Nuxt', `nuxt build`, `nuxt dev`
- ✅ Legacy config: nuxt v2, nuxt-edge v2 → 'Nuxt', `nuxt generate`, `nuxt`

This ensures Nuxt v4+ projects get the correct modern build configuration while maintaining consistent naming and backward compatibility for v2 projects.

<!-- START COPILOT CODING AGENT TIPS -->
---

✨ Let Copilot coding agent [set things up for you](https://github.com/netlify/build/issues/new?title=✨+Set+up+Copilot+instructions&body=Configure%20instructions%20for%20this%20repository%20as%20documented%20in%20%5BBest%20practices%20for%20Copilot%20coding%20agent%20in%20your%20repository%5D%28https://gh.io/copilot-coding-agent-tips%29%2E%0A%0A%3COnboard%20this%20repo%3E&assignees=copilot) — coding agent works faster and does higher quality work when set up for your repo.
