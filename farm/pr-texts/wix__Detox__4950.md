# fix(android): quote adb device serials

## Description

- This pull request addresses the issue described here: #4937

In this pull request, I have quoted the device serial used by shell-built ADB commands. This keeps mDNS/Wi-Fi serials with characters like parentheses from being parsed by the shell, while leaving the spawned ADB paths unchanged because they already pass the serial as an argument array.

## Verification

- `corepack yarn workspace detox jest src/devices/common/drivers/android/exec/ADB.test.js --runInBand`
- `corepack yarn workspace detox eslint src/devices/common/drivers/android/exec/ADB.js src/devices/common/drivers/android/exec/ADB.test.js`
- `git diff --check`

---

> _For features/enhancements:_
 - [ ] I have added/updated the relevant references in the [documentation](https://github.com/wix/Detox/tree/master/docs) files.

> _For API changes:_
 - [ ] I have made the necessary changes in the [types index](https://github.com/wix/Detox/blob/master/detox/index.d.ts) file.

This was implemented with Codex assistance, with the patch kept to the shell-command serial quoting path and reviewed against the existing ADB unit tests.
