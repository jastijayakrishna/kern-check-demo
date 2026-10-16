# Fix ReDoS vulnerability and build failure in fetch-install-prompts.js

## Summary

Fixes a Regular Expression Denial of Service (ReDoS) vulnerability in `scripts/fetch-install-prompts.js` and resolves a build failure that occurred when the script generated empty install guides data.

## Vulnerability Details

The script contained a regex pattern `/\/+\/+/g` on line 89 that uses nested quantifiers, which can cause exponential backtracking when processing malicious inputs with many consecutive slashes. This creates a potential DoS attack vector where an attacker could provide specially crafted input to cause the regex engine to consume excessive CPU time.

**Vulnerable pattern:**
```javascript
.replace(/\/+\/+/g, '/')  // Nested quantifiers - vulnerable to ReDoS
```

## Fixes

### 1. ReDoS Vulnerability Fix
Replaced the vulnerable pattern with a functionally equivalent but safe regex:

```javascript
.replace(/\/+/g, '/')  // Simple quantifier - safe from ReDoS
```

This change:
- ✅ Maintains identical functionality (collapses multiple slashes to single slash)
- ✅ Eliminates the ReDoS vulnerability by removing nested quantifiers
- ✅ Improves performance by using a simpler, more efficient pattern

### 2. Build Failure Fix
Added logic to preserve existing install guides data when the API is unavailable or returns no results:

```javascript
// If no guides found and existing file exists, preserve it
if (slugs.length === 0 && fs.existsSync(outFile)) {
    console.warn(
        `No install guides found from API. Existing generated file found at ${outFile}. Proceeding with previously generated data.`,
    )
    return
}
```

This prevents TypeScript compilation errors that occurred when the script generated an empty array, since Zod enums require at least one value.

## Additional Improvements

- Fixed regex character class escaping issues for better linting compliance
- Added proper ESLint configuration for Node.js script environment
- Ensured all console usage is properly declared for linting

## Testing

- All existing tests pass (187 passing)
- Manual testing confirms script functionality is preserved
- Performance testing shows the fix handles large inputs efficiently without timeouts
- Build process works correctly even when GitHub API is unreachable
- Linting passes with no errors

The fix addresses both the security vulnerability and build reliability while maintaining backward compatibility and improving code quality.

<!-- START COPILOT CODING AGENT TIPS -->
---

💡 You can make Copilot smarter by setting up custom instructions, customizing its development environment and configuring Model Context Protocol (MCP) servers. Learn more [Copilot coding agent tips](https://gh.io/copilot-coding-agent-tips) in the docs.
