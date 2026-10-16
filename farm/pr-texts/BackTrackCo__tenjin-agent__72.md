# feat(install): three-question walkthrough with auto-wired free-verb allowlist

Rebuilds the interactive install around three decisions (publishing, permissions, wallet) with one line of consequence per option, replacing the security-essay walkthrough. Two keypresses on a typical machine, three on a fresh one.

- Publishing question reworded and re-ordered: Auto is the recommended interactive default (agent publishes clean pieces; the harness's own permission dialog is the per-publish yes/no). Stored default for non-interactive installs stays review, so a piped or CI install never lands on auto silently.
- New: install offers to write the 9 free-verb rules into ~/.claude/settings.json (permissions.allow); none can spend USDC or open the keystore, and three send or store data (search, outcome, read) so agents stop getting denied on tenjin search. The writer is consent-gated, additive-only, idempotent, skips unparseable files, and is structurally incapable of adding spend/publish/keystore verbs: the rule list is a hardcoded constant, the writer takes no rule argument, and a test pins it equal to doctor's documented safe tier plus asserts the forbidden-verb list. --allow-free-verbs wires it headless.
- Prompts render via @clack/prompts (bundled devDep; runtime dependencies stay {}), behind the existing injectable prompt seams so tests never touch clack. Non-interactive/--json contract unchanged except the new data.permissions report.
- Walkthrough no longer prints the full allowlist block or the --base-url/session-key essays; doctor's permissions output is unchanged. README/docs restructure is #73, stacked on this branch, and the two are a coupled pair: merging this PR without #73 leaves the README describing the old install output, so merge #72 then #73 in the same sitting.

Verified: typecheck, lint, prettier, build, full vitest suite green (1449 passed, 36 new).

🤖 Generated with [Claude Code](https://claude.com/claude-code)
