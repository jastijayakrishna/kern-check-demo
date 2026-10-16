# Fix drawio -xf png parsing, point SECURITY.md at GitHub reporting, fix the Windows portable asset name

Found while the jgraph/drawio wiki was being rewritten as a developer guide.

## CLI: `drawio -xf png file` treated `png` as an input file

`parseDrawioArgs` expands short-flag clusters (`-xa`, `-xfpng`) for commander.js compatibility. When the cluster ended in a flag that takes a value, it applied the empty attached string as that value and moved on. So for `-xf png file`:

- the format fell back to `pdf`;
- `png` became a positional input;
- the export stopped with `Error: input file/directory not found: png`.

commander.js, which these clusters copy, takes the next argument in that case. The cluster now does the same, using the rule a lone `-f` already follows: the next token is the value unless it starts with `-`.

**Tests:** I added three cases to `src/test/cli-args.test.js` (`-xf png`, `-xo out.pdf` and `-xf -a`). `npm test`: 262 pass. Without the fix, the first two fail.

**Manual:** `electron . -xf png test.drawio` from source:

| Parser | Result |
|---|---|
| Before | `Error: input file/directory not found: png` |
| After | `test.drawio -> test.png`, a 124×64 PNG |

## SECURITY.md

It said "If you discover a security vulnerability in axios", which was copied from axios's policy. It also pointed to huntr, which no longer takes reports for projects like this. It now follows the jgraph/drawio policy:

- reports go through GitHub private vulnerability reporting, which is enabled on this repo (`/security/advisories/new`);
- vulnerabilities in the core editor can also be reported to jgraph/drawio.

## README

- **Windows portable build:** the x64 asset has been `draw.io-<version>-windows.zip` since May 2025 (d2b655b, f1f18b8; see the v32.3.0 assets), not `-windows-no-installer.exe`. The arm64 portable `-no-installer.exe` still exists, so that entry is unchanged.
- **Release steps:** the "To release" steps (Travis, AppVeyor, manual `signtool`, re-uploading `-no-installer.exe`) no longer match how releases are made. They are replaced by a pointer to `doc/RELEASE_PROCESS.md`.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
