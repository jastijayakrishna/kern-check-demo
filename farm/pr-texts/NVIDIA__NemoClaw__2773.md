# feat(cli): add `share mount/unmount/status` for SSHFS-based file sharing

## Summary

- Adds `nemoclaw <name> share mount/unmount/status` commands that use SSHFS over OpenShell's existing SSH proxy to mount the sandbox filesystem on the host
- Bidirectional file sharing — edits on host appear instantly in the sandbox and vice versa
- Adds `openssh-sftp-server` to `Dockerfile.base` (88KB, SFTP subsystem required by SSHFS)
- Fixes pre-existing flaky test timeouts in `service-env.test.ts` and `cli.test.ts`

### Why SSHFS?

Upstream OpenShell has no `--mount`/`--volume` support, and the maintainer confirmed on NVIDIA/OpenShell#925 that k3s+Docker is being deprecated — so upstream mount support is not coming. SSHFS reuses the existing SSH proxy infrastructure without any upstream changes.

### Usage

```console
$ nemoclaw my-assistant share mount
✓ Mounted /sandbox → ~/.nemoclaw/mounts/my-assistant
  Edit files at ~/.nemoclaw/mounts/my-assistant — changes appear in the sandbox instantly.

$ nemoclaw my-assistant share status
● Mounted at ~/.nemoclaw/mounts/my-assistant

$ nemoclaw my-assistant share unmount
✓ Unmounted ~/.nemoclaw/mounts/my-assistant
```

### Prerequisites

- `sshfs` on the host (`sudo apt-get install sshfs` on Linux, `brew install macfuse && brew install sshfs` on macOS)
- Sandboxes built before this change need `nemoclaw <name> rebuild` to get `openssh-sftp-server`

Closes #2631

## Test plan

- [x] `npm run build:cli` — compiles cleanly
- [x] `npm test` — 154 files passed, 2926 tests passed
- [x] Command registry tests updated (48 commands, 16 sandbox action tokens)
- [x] CLI dispatch test: `share` recognized as valid action, usage help shown on bare `share`
- [x] Manual E2E: mount via SSHFS, write from host → read in sandbox, write in sandbox → read on host, unmount
- [x] `--dump-commands` includes all 3 share commands (docs parity CI)
- [x] Pre-update sandbox error: detects missing sftp-server and suggests rebuild
- [ ] Base image rebuild (CI-triggered after merge) installs `openssh-sftp-server`

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **New Features**
  * Added `share mount`, `share unmount`, and `share status` sandbox commands to mount, unmount, and inspect sandbox directories via SSHFS.

* **Documentation**
  * Added CLI reference entries with usage, examples, defaults, prerequisites, and guidance for rebuilding older sandboxes after SFTP updates.

* **Tests**
  * Updated tests to exercise the new share commands and extended relevant test timeouts.

* **Chores**
  * Base image now includes a pinned SFTP server package to support SSHFS.
<!-- end of auto-generated comment: release notes by coderabbit.ai -->
