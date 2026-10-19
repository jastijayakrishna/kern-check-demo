# Update dependency @angular/compiler to v22.2.3

This PR contains the following updates:

| Package | Change | [Age](https://docs.renovatebot.com/merge-confidence/) | [Adoption](https://docs.renovatebot.com/merge-confidence/) | [Passing](https://docs.renovatebot.com/merge-confidence/) | [Confidence](https://docs.renovatebot.com/merge-confidence/) |
|---|---|---|---|---|---|
| [@angular/compiler](https://redirect.github.com/angular/angular) ([source](https://redirect.github.com/angular/angular/tree/HEAD/packages/compiler)) | [`22.2.2` → `22.2.3`](https://renovatebot.com/diffs/npm/@angular%2fcompiler/22.2.2/22.2.3) | ![age](https://developer.mend.io/api/mc/badges/age/npm/@angular%2fcompiler/22.2.3?slim=true) | ![adoption](https://developer.mend.io/api/mc/badges/adoption/npm/@angular%2fcompiler/22.2.3?slim=true) | ![passing](https://developer.mend.io/api/mc/badges/compatibility/npm/@angular%2fcompiler/22.2.2/22.2.3?slim=true) | ![confidence](https://developer.mend.io/api/mc/badges/confidence/npm/@angular%2fcompiler/22.2.2/22.2.3?slim=true) |

---

### Release Notes

<details>
<summary>angular/angular (@&#8203;angular/compiler)</summary>

### [`v22.2.3`](https://redirect.github.com/angular/angular/blob/HEAD/CHANGELOG.md#2223-2026-10-14)

[Compare Source](https://redirect.github.com/angular/angular/compare/v22.2.2...v22.2.3)

##### common

| Commit                                                                                           | Type | Description                                       |
| ------------------------------------------------------------------------------------------------ | ---- | ------------------------------------------------- |
| [fafec77b5d](https://redirect.github.com/angular/angular/commit/fafec77b5d4e6dfc89aad72db9c132d3dfe46ba6) | fix  | harden param encoding against prototype pollution |

##### compiler

| Commit                                                                                           | Type | Description                                                                |
| ------------------------------------------------------------------------------------------------ | ---- | -------------------------------------------------------------------------- |
| [54f3de517c](https://redirect.github.com/angular/angular/commit/54f3de517c2e4cda264eca5f2d143a1f6967c7a9) | fix  | check `@boundary` blocks in the control flow content projection diagnostic |
| [5e50658fd2](https://redirect.github.com/angular/angular/commit/5e50658fd23983dd27ef89a67cea26910af6fd79) | fix  | compare the operand in ReadTemporaryExpr.isEquivalent                      |
| [b6f9cc5d70](https://redirect.github.com/angular/angular/commit/b6f9cc5d7013f8f136b38cccfe486264200f04f5) | fix  | do not scope comments placed inside of a selector                          |
| [35a02f8097](https://redirect.github.com/angular/angular/commit/35a02f8097724f4b6e83e1c9c008da8f1fc7f127) | fix  | harden JIT against prototype pollution                                     |
| [08075e8aa0](https://redirect.github.com/angular/angular/commit/08075e8aa03800bc1b8ae793fb3d52761cdd28b6) | fix  | support dots in class binding names                                        |
| [c7a72c2bf2](https://redirect.github.com/angular/angular/commit/c7a72c2bf2213d881496e70933fc61bdaaa00621) | fix  | support popover property bindings                                          |

##### compiler-cli

| Commit                                                                                           | Type | Description                                  |
| ------------------------------------------------------------------------------------------------ | ---- | -------------------------------------------- |
| [fa21d083fe](https://redirect.github.com/angular/angular/commit/fa21d083fe92e67a2a070059b850b9a32a08cef9) | fix  | inline tcb when depending on local directive |

##### core

| Commit                                                                                           | Type | Description                                                          |
| ------------------------------------------------------------------------------------------------ | ---- | -------------------------------------------------------------------- |
| [b5208f9fc3](https://redirect.github.com/angular/angular/commit/b5208f9fc3a77a9631c2f38c30c38c777a642839) | fix  | avoid deleting idle bucket created during another bucket's drain     |
| [90af679c3b](https://redirect.github.com/angular/angular/commit/90af679c3b585515651b138667b8eaf3df652968) | fix  | do not swallow compilation errors in computeStandaloneComponentScope |
| [eca5fa4665](https://redirect.github.com/angular/angular/commit/eca5fa466508ef68014cbebb0cafd63947f9eda7) | fix  | don't crash initEventReplay when two apps share an APP_ID            |
| [e59a2303df](https://redirect.github.com/angular/angular/commit/e59a2303dfb4f3242552d382bbeebf6a38446856) | fix  | error when destroying embedded view with animations                  |
| [a23941fe75](https://redirect.github.com/angular/angular/commit/a23941fe7547634c9f1160541b3a2265e284f624) | fix  | keep activeConsumer and currentInjector constant using Store helper  |
| [913ae7421f](https://redirect.github.com/angular/angular/commit/913ae7421f609c6ad375219045e9ab3f3b0eba73) | fix  | skip nested tick from onMicrotaskEmpty while a tick is running       |

##### forms

| Commit                                                                                           | Type | Description                                                       |
| ------------------------------------------------------------------------------------------------ | ---- | ----------------------------------------------------------------- |
| [cc515b8b23](https://redirect.github.com/angular/angular/commit/cc515b8b2331df643e7ff80915efc402bc97d3bb) | perf | use addEventListener to avoid unconditional CD scheduling on blur |

##### migrations

| Commit                                                                                           | Type | Description                                         |
| ------------------------------------------------------------------------------------------------ | ---- | --------------------------------------------------- |
| [d04f214d04](https://redirect.github.com/angular/angular/commit/d04f214d04678f0dbb0b769a53d1f15ece09c4a2) | fix  | normalize .d.ts paths in output migration field IDs |

##### router

| Commit                                                                                           | Type | Description                           |
| ------------------------------------------------------------------------------------------------ | ---- | ------------------------------------- |
| [f9a4f751f0](https://redirect.github.com/angular/angular/commit/f9a4f751f0ad0f3f22d49430475d6d57fa29fd3f) | fix  | check abort signal state on subscribe |

<!-- CHANGELOG SPLIT MARKER -->

</details>

---

### Configuration

📅 **Schedule**: (UTC)

- Branch creation
  - At any time (no schedule defined)
- Automerge
  - At any time (no schedule defined)

🚦 **Automerge**: Disabled by config. Please merge this manually once you are satisfied.

♻ **Rebasing**: Whenever PR becomes conflicted, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

---

 - [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

---

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job log](https://developer.mend.io/github/prettier/prettier).
<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiI0NC4xNTYuMyIsInVwZGF0ZWRJblZlciI6IjQ0LjE1Ni4zIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6WyJkZXBlbmRlbmN5Il19-->

