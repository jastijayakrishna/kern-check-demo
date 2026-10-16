# fix: apply Steady teletext code as Set At, not Set After

## Summary
- The Steady control code (0x09) now takes effect on the cell where it appears ("Set At") instead of the next cell ("Set After")
- When Hold Graphics is active, the held graphic at the Steady code position no longer incorrectly flashes

Fixes #611

## Before / After

Test sequence: `CLS:VDU &91,&88,&BF,&BF,&9E,&89,&BF,&BF`
(Red graphics, Flash, two full blocks, Hold Graphics, Steady, two more blocks)

Captured during flash-on phase. The cell at position 5 contains the Steady code with Hold Graphics active.

| Before (bug) | After (fix) |
|---|---|
| ![before](https://raw.githubusercontent.com/mattgodbolt/jsbeeb/claude/fix-teletext-steady-set-at-611/tests/integration/teletext/before_steady_set_at_flash_1.png) | ![after](https://raw.githubusercontent.com/mattgodbolt/jsbeeb/claude/fix-teletext-steady-set-at-611/tests/integration/teletext/expected_steady_set_at_flash_1.png) |
| 5 cells blanked — Steady cell incorrectly flashes | 4 cells blanked — Steady cell shows held red graphic |

## The fix
`render()` captures `prevFlash` before processing control codes, then uses it for the flash blanking decision. Flash (0x08) is correctly "Set After" so it uses the old state. But Steady (0x09) is "Set At" — when flash transitions from on→off (which only happens via Steady), we now update `prevFlash` to reflect the new state.

## Test plan
- [x] Added integration test with image comparison capturing flash-on phase
- [x] Added `runToFlashState()` helper to TestMachine for deterministic flash timing
- [x] All existing teletext tests pass
- [x] Full test suite passes (unit, integration, CPU)
- [ ] Compare against real BBC hardware: `CLS:VDU &91,&88,&BF,&BF,&9E,&89,&BF,&BF`

🤖 Generated with [Claude Code](https://claude.com/claude-code)
