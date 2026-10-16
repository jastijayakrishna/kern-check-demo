# Add dynamic label support to F1 create-issue command (CYPACK-680)

## Summary

Adds dynamic label support to the F1 testing framework's create-issue command, enabling testing of label-based features like model selection and routing.

- Add `--labels` flag to CLI accepting comma-separated label names
- Labels are created dynamically on first use (no seeding required)
- Labels persist across issues and can be reused

## Changes

### CLI (`apps/f1/src/commands/createIssue.ts`)
- Added `-l, --labels <labels>` option accepting comma-separated label names
- Labels are parsed, trimmed, and passed to the RPC server

### RPC Server (`packages/core/.../CLIRPCServer.ts`)
- Extended `CreateIssueParams` to include optional `labels?: string[]`
- Updated `handleCreateIssue` to resolve label names to IDs using `findOrCreateLabel()`

### Issue Tracker Service (`packages/core/.../CLIIssueTrackerService.ts`)
- Added `findOrCreateLabel(name: string)` method for dynamic label creation
- Added `generateLabelColor(name: string)` helper using hash-based color assignment

## Usage

```bash
# Single label
./f1 create-issue --title "Test" --labels sonnet

# Multiple labels
./f1 create-issue --title "Test" --labels sonnet,feature,urgent
```

## Test Plan

- [x] All 5 acceptance criteria validated
- [x] 7 new label-specific tests added and passing
- [x] All 13 core package tests passing
- [x] Full package test suite passing (285+ tests)
- [x] TypeScript typecheck passing across all packages
- [x] Biome linting passing

Resolves CYPACK-680

🤖 Generated with [Claude Code](https://claude.com/claude-code)
