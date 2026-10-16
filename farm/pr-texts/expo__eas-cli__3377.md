# [build-tools] Poll lockscreen state and retry unlock until it clears

# Why

The Cuttlefish device may remain locked after an initial `KEYCODE_MENU` event which blocks reaching the home screen, so the unlock flow must verify the real lock state instead of blindly sending HOME. See https://exponent-internal.slack.com/archives/C02VC9BLMQW/p1769703880840729?thread_ts=1763747642.435979&cid=C02VC9BLMQW.

# How
- Updated `packages/build-tools/src/steps/functions/startCuttlefishDevice.ts` to poll `adb shell dumpsys window` and check `mDreamingLockscreen` before deciding the device is unlocked.
- Implemented a retry loop that sends `adb shell input keyevent 82` while the lockscreen remains active, waits 1s between attempts, and uses a 30 second deadline for the unlock attempts.
- When unlock is detected the code now sends `adb shell input keyevent 3` to return to the home screen and logs success, and it logs warnings on query failures or on timeout.

# Test Plan

- Ran `yarn typecheck` which completed successfully.
- Ran `yarn lint --fix` which completed successfully.

------
[Codex Task](https://chatgpt.com/codex/tasks/task_e_698374b75b88832890754e697e58e5ea)
