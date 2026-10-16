# [code-infra] Update all builtin module imports to use node: protocol and enforce with ESLint using eslint-plugin-n

This PR updates all Node.js builtin module imports throughout the repository to use the modern `node:` protocol, changing imports like `import fs from 'fs'` to `import fs from 'node:fs'` and `require('path')` to `require('node:path')`. Additionally, it adds ESLint enforcement using the community-standard `eslint-plugin-n` package to prevent future violations.

## Changes Made

### Import Updates
Updated 33 import statements across 23 files to use the `node:` protocol for builtin modules including:
- `fs` and `fs/promises`
- `path` 
- `os`
- `util`
- `child_process`
- `url`
- `zlib`
- `module`

### ESLint Enforcement
Added comprehensive ESLint enforcement using `eslint-plugin-n` and its `prefer-node-protocol` rule:

1. **Added `eslint-plugin-n`**: Industry-standard ESLint plugin for Node.js best practices
2. **Repository-level enforcement**: Added `n/prefer-node-protocol` rule to main repository ESLint config (`eslint.config.mjs`)
3. **Clean configuration**: Replaced custom `no-restricted-imports` implementation with proven community plugin

## Files Updated

### Packages
- **babel-plugin-resolve-imports**: Updated CommonJS `require('path')` and ES module imports in test files
- **babel-plugin-minify-errors**: Updated CommonJS `require('fs')` and `require('path')` plus test file imports
- **bundle-size-checker**: Updated ES module imports across worker, CLI, config loader, builder, and upload utility files
- **code-infra**: Updated CLI command files

### Apps
- **code-infra-dashboard**: Updated util and zlib imports in Netlify function

### Root Files
- `babel.config.js`: Updated CommonJS `require('path')`
- `update-netlify-ignore.mjs`: Updated fs, child_process, and path imports
- `eslint.config.mjs`: Added repository-wide enforcement rule using `eslint-plugin-n`

## Benefits

1. **Modern Node.js best practice**: The `node:` protocol was introduced in Node.js 14.18.0 and became stable in later versions
2. **Explicit builtin identification**: Makes it clear which imports are Node.js builtins vs. external packages
3. **Community-standard enforcement**: Uses established `eslint-plugin-n` instead of custom rules
4. **Future compatibility**: Aligns with Node.js ecosystem evolution and tooling expectations
5. **Comprehensive coverage**: Rule covers all builtin modules including submodules like `fs/promises`

## Validation

- ✅ All packages build successfully
- ✅ ESLint and Prettier checks pass with new rule enforcement
- ✅ CLI tools functionality verified
- ✅ Repository-wide ESLint enforcement verified through testing

The changes maintain full backward compatibility while adopting modern Node.js import conventions and ensuring consistency through automated enforcement using industry-standard tooling.

<!-- START COPILOT CODING AGENT TIPS -->
---

💡 You can make Copilot smarter by setting up custom instructions, customizing its development environment and configuring Model Context Protocol (MCP) servers. Learn more [Copilot coding agent tips](https://gh.io/copilot-coding-agent-tips) in the docs.
