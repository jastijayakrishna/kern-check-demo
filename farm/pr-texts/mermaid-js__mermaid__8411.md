# Update dependency katex to ^0.18.0 [SECURITY]

This PR contains the following updates:

| Package | Change | [Age](https://docs.renovatebot.com/merge-confidence/) | [Confidence](https://docs.renovatebot.com/merge-confidence/) |
|---|---|---|---|
| [katex](https://katex.org) ([source](https://redirect.github.com/KaTeX/KaTeX)) | [`^0.16.47` → `^0.18.0`](https://renovatebot.com/diffs/npm/katex/0.16.47/0.18.2) | ![age](https://developer.mend.io/api/mc/badges/age/npm/katex/0.18.2?slim=true) | ![confidence](https://developer.mend.io/api/mc/badges/confidence/npm/katex/0.16.47/0.18.2?slim=true) |

---

### KaTeX: Existing prototype pollution can bypass trust restrictions
[CVE-2026-103923](https://nvd.nist.gov/vuln/detail/CVE-2026-103923) / [GHSA-238p-pmpm-9mq7](https://redirect.github.com/advisories/GHSA-238p-pmpm-9mq7)

<details>
<summary>More information</summary>

#### Details
##### Impact

KaTeX can act as a read-side prototype pollution gadget in applications where `Object.prototype` has already been polluted, or where an attacker can influence the prototype of the renderer options object. (KaTeX does not enable said prototype pollution. This advisory applies when combining KaTeX with other vulnerable software that allows for prototype pollution.)

Affected versions may treat inherited properties from `Object.prototype` as renderer options, internal setting metadata, or namespace entries. In particular, an inherited `trust` value will be treated as though the application explicitly enabled trusted rendering, rather than using the documented default of `false`.

With attacker-controlled mathematical expressions, this can produce links capable of user-interaction cross-site scripting or load attacker-selected external resources. Exploitation requires the consuming application to insert KaTeX output into a web page without a separate sanitizer. (KaTeX does not execute scripts merely by rendering an expression.)

Other inherited settings can alter rendering behavior or resource limits. Inherited setting metadata can affect how defaults and supplied options are processed, while inherited namespace properties can be mistaken for defined macros or other internal values.

##### Patches

Upgrade to KaTeX v0.18.2 to remove this vulnerability.

##### Workarounds

- Address any prototype-pollution vulnerability in the application or its dependencies.
- `delete Object.prototype.trust`, `delete Object.prototype.default`, and `delete Object.prototype.processor` before calling KaTeX
- Do not allow untrusted input to control the renderer options object or its prototype.
- Sanitize KaTeX-generated HTML before inserting it into a document.

##### Details

KaTeX previously used ordinary JavaScript property access in the following contexts:

- Renderer settings could be inherited from the prototype of the options object.
- Internal `default` and `processor` setting metadata could be inherited from `Object.prototype`.
- Namespace lookup could treat inherited properties as built-in definitions.
- Namespace group restoration could preserve an inherited property as though it had been an explicitly defined value.

The fix adds own-property checks to each of these paths. Inherited properties are no longer accepted as renderer settings, setting metadata, namespace definitions, or values to be restored after a group ends.

##### For more information

If you have any questions or comments about this advisory:

- Open an issue or security advisory in the [KaTeX repository](https://redirect.github.com/KaTeX/KaTeX/)
- Email us at [katex-security@mit.edu](mailto:katex-security@mit.edu)

#### Severity
- CVSS Score: 2.1 / 10 (Low)
- Vector String: `CVSS:4.0/AV:N/AC:L/AT:P/PR:N/UI:A/VC:N/VI:N/VA:N/SC:L/SI:L/SA:N`

#### References
- [https://github.com/KaTeX/KaTeX/security/advisories/GHSA-238p-pmpm-9mq7](https://redirect.github.com/KaTeX/KaTeX/security/advisories/GHSA-238p-pmpm-9mq7)
- [https://nvd.nist.gov/vuln/detail/CVE-2026-103923](https://nvd.nist.gov/vuln/detail/CVE-2026-103923)
- [https://github.com/KaTeX/KaTeX/pull/4260](https://redirect.github.com/KaTeX/KaTeX/pull/4260)
- [https://github.com/KaTeX/KaTeX/commit/0adf7e77db6915d991803b29699f82b1ccf8d4f4](https://redirect.github.com/KaTeX/KaTeX/commit/0adf7e77db6915d991803b29699f82b1ccf8d4f4)
- [https://github.com/KaTeX/KaTeX/releases/tag/v0.18.2](https://redirect.github.com/KaTeX/KaTeX/releases/tag/v0.18.2)
- [https://github.com/advisories/GHSA-238p-pmpm-9mq7](https://redirect.github.com/advisories/GHSA-238p-pmpm-9mq7)

This data is provided by the [GitHub Advisory Database](https://redirect.github.com/advisories/GHSA-238p-pmpm-9mq7) ([CC-BY 4.0](https://redirect.github.com/github/advisory-database/blob/main/LICENSE.md)).
</details>

---

### Release Notes

<details>
<summary>KaTeX/KaTeX (katex)</summary>

### [`v0.18.2`](https://redirect.github.com/KaTeX/KaTeX/blob/HEAD/CHANGELOG.md#0182-2026-08-08)

[Compare Source](https://redirect.github.com/KaTeX/KaTeX/compare/v0.18.1...v0.18.2)

##### Bug Fixes

- prevent prototype pollution in settings ([#&#8203;4260](https://redirect.github.com/KaTeX/KaTeX/issues/4260)) ([0adf7e7](https://redirect.github.com/KaTeX/KaTeX/commit/0adf7e77db6915d991803b29699f82b1ccf8d4f4))

### [`v0.18.1`](https://redirect.github.com/KaTeX/KaTeX/blob/HEAD/CHANGELOG.md#01811-2026-10-01)

[Compare Source](https://redirect.github.com/KaTeX/KaTeX/compare/v0.18.0...v0.18.1)

##### Features

- handle character metrics warnings via `strict` ([#&#8203;4243](https://redirect.github.com/KaTeX/KaTeX/issues/4243)) ([4237070](https://redirect.github.com/KaTeX/KaTeX/commit/423707055a37803acafef4c1533832273192ea0e))

### [`v0.18.0`](https://redirect.github.com/KaTeX/KaTeX/blob/HEAD/CHANGELOG.md#0180-2026-07-17)

[Compare Source](https://redirect.github.com/KaTeX/KaTeX/compare/v0.17.0...v0.18.0)

##### Features

- prefix css classes ([#&#8203;4229](https://redirect.github.com/KaTeX/KaTeX/issues/4229)) ([6f5c44f](https://redirect.github.com/KaTeX/KaTeX/commit/6f5c44f69bae0703877a3a8d934e20c47bbbbc32))

##### BREAKING CHANGES

- users who apply custom styles or have allowlists targeting KaTeX's internal classes must update their selectors.

### [`v0.17.0`](https://redirect.github.com/KaTeX/KaTeX/blob/HEAD/CHANGELOG.md#0170-2026-05-22)

[Compare Source](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.47...v0.17.0)

##### Performance Improvements

- simplify `defineFunction` to avoid destructuring, improve typing ([#&#8203;4222](https://redirect.github.com/KaTeX/KaTeX/issues/4222)) ([fb604e6](https://redirect.github.com/KaTeX/KaTeX/commit/fb604e6ba63e99809e242d37f9c8359209d55431))

##### BREAKING CHANGES

- The internal API for `__defineFunction` changed: you should no longer wrap properties in `props`.

#### [0.16.47](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.46...v0.16.47) (2026-05-16)

##### Bug Fixes

- correct size of `[` big delimiter ([#&#8203;4217](https://redirect.github.com/KaTeX/KaTeX/issues/4217)) ([7ba0027](https://redirect.github.com/KaTeX/KaTeX/commit/7ba0027d2f04abddd3b215362f867ab8260b09d7)), closes [#&#8203;4215](https://redirect.github.com/KaTeX/KaTeX/issues/4215)

#### [0.16.46](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.45...v0.16.46) (2026-05-13)

##### Bug Fixes

- preserve math font in some styling commands ([#&#8203;4214](https://redirect.github.com/KaTeX/KaTeX/issues/4214)) ([e9ee046](https://redirect.github.com/KaTeX/KaTeX/commit/e9ee0464ddb31da9bf9649eeb70e52236e7a974a)), closes [#&#8203;4213](https://redirect.github.com/KaTeX/KaTeX/issues/4213)

#### [0.16.45](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.44...v0.16.45) (2026-04-05)

##### Bug Fixes

- wrap vcenter mpadded in mrow for valid MathML ([#&#8203;4193](https://redirect.github.com/KaTeX/KaTeX/issues/4193)) ([ee66b78](https://redirect.github.com/KaTeX/KaTeX/commit/ee66b78d24340edbbd05b08a4a429ce9ed158b25)), closes [#&#8203;4078](https://redirect.github.com/KaTeX/KaTeX/issues/4078)

#### [0.16.44](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.43...v0.16.44) (2026-03-27)

##### Bug Fixes

- remove extra \jot space at bottom of align/gather/etc. ([#&#8203;4184](https://redirect.github.com/KaTeX/KaTeX/issues/4184)) ([3870ee9](https://redirect.github.com/KaTeX/KaTeX/commit/3870ee913e27fdde7bce244e4c6c5d63e2b28a62))

#### [0.16.43](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.42...v0.16.43) (2026-03-26)

##### Bug Fixes

- use makeEm() consistently to truncate long CSS decimals ([#&#8203;4181](https://redirect.github.com/KaTeX/KaTeX/issues/4181)) ([0967dcc](https://redirect.github.com/KaTeX/KaTeX/commit/0967dcc0278f20d4501a93f01c7343c70abb3fcd))

#### [0.16.42](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.41...v0.16.42) (2026-03-24)

##### Features

- \underbracket and \overbracket ([#&#8203;4147](https://redirect.github.com/KaTeX/KaTeX/issues/4147)) ([5be9abb](https://redirect.github.com/KaTeX/KaTeX/commit/5be9abb0b4d687a2a196b8adf9b5b9deeb60f7bc))

#### [0.16.41](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.40...v0.16.41) (2026-03-24)

##### Bug Fixes

- \sout in text mode ([#&#8203;4173](https://redirect.github.com/KaTeX/KaTeX/issues/4173)) ([e748578](https://redirect.github.com/KaTeX/KaTeX/commit/e748578b63e07ad30d5e404e60b04e5e794c0a5a))

#### [0.16.40](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.39...v0.16.40) (2026-03-20)

##### Bug Fixes

- **css:** specify position: relative for .katex ([#&#8203;4170](https://redirect.github.com/KaTeX/KaTeX/issues/4170)) ([020f0d8](https://redirect.github.com/KaTeX/KaTeX/commit/020f0d89567d59229bac5fc8d8f5832a9508a85f))

#### [0.16.39](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.38...v0.16.39) (2026-03-19)

##### Bug Fixes

- middle dot in text mode ([#&#8203;4169](https://redirect.github.com/KaTeX/KaTeX/issues/4169)) ([edb45b0](https://redirect.github.com/KaTeX/KaTeX/commit/edb45b0b17c7b33349ce5142fe39156da05cb4d8)), closes [#&#8203;3641](https://redirect.github.com/KaTeX/KaTeX/issues/3641)

#### [0.16.38](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.37...v0.16.38) (2026-03-08)

##### Bug Fixes

- accent skew mixed with font specifiers ([#&#8203;4159](https://redirect.github.com/KaTeX/KaTeX/issues/4159)) ([aea3375](https://redirect.github.com/KaTeX/KaTeX/commit/aea33758d6c98896017007d0244885301773856a)), closes [#&#8203;4121](https://redirect.github.com/KaTeX/KaTeX/issues/4121)

#### [0.16.37](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.36...v0.16.37) (2026-03-06)

##### Bug Fixes

- negative-width `\hphantom` and symmetric `\smash` ([#&#8203;4153](https://redirect.github.com/KaTeX/KaTeX/issues/4153)) ([d4799ca](https://redirect.github.com/KaTeX/KaTeX/commit/d4799cae585d909e2a4e3dedbebdc2f142998ca9))

#### [0.16.36](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.35...v0.16.36) (2026-03-06)

##### Bug Fixes

- contrib esm bloat ([#&#8203;4157](https://redirect.github.com/KaTeX/KaTeX/issues/4157)) ([2bde1ad](https://redirect.github.com/KaTeX/KaTeX/commit/2bde1adab2a23f61519145923329c915b04d4778))

#### [0.16.35](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.34...v0.16.35) (2026-03-05)

##### Bug Fixes

- version number regression ([#&#8203;4155](https://redirect.github.com/KaTeX/KaTeX/issues/4155)) ([db26b73](https://redirect.github.com/KaTeX/KaTeX/commit/db26b733805f2d0d71e82596475b313c8706557e))

#### [0.16.34](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.33...v0.16.34) (2026-03-05)

##### Bug Fixes

- emoji with variation selector ([#&#8203;4151](https://redirect.github.com/KaTeX/KaTeX/issues/4151)) ([c2606e5](https://redirect.github.com/KaTeX/KaTeX/commit/c2606e5db91ae199ee1ff0c8c2f7f9f70fcf589b))

#### [0.16.33](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.32...v0.16.33) (2026-02-23)

##### Bug Fixes

- **scss:** forward variables to fonts module ([#&#8203;4146](https://redirect.github.com/KaTeX/KaTeX/issues/4146)) ([9349a64](https://redirect.github.com/KaTeX/KaTeX/commit/9349a64a051ca408da713baf061e32ade80ed22a))

#### [0.16.32](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.31...v0.16.32) (2026-02-22)

##### Bug Fixes

- italic separation in \mathnormal ([#&#8203;4143](https://redirect.github.com/KaTeX/KaTeX/issues/4143)) ([71305a0](https://redirect.github.com/KaTeX/KaTeX/commit/71305a05140ca6203092bfdc14f689168b26ab8c))

#### [0.16.31](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.30...v0.16.31) (2026-02-22)

##### Bug Fixes

- `\*frac` sizing ([#&#8203;4137](https://redirect.github.com/KaTeX/KaTeX/issues/4137)) ([ef51f18](https://redirect.github.com/KaTeX/KaTeX/commit/ef51f18ded4ab9ba54ba750f2866241c4676c41c))

#### [0.16.30](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.29...v0.16.30) (2026-02-22)

##### Bug Fixes

- no line breaks after `\not` ([#&#8203;4140](https://redirect.github.com/KaTeX/KaTeX/issues/4140)) ([2d1ba86](https://redirect.github.com/KaTeX/KaTeX/commit/2d1ba86143bd45540d5a773cfa456081318f3f33))

#### [0.16.29](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.28...v0.16.29) (2026-02-22)

##### Bug Fixes

- `\imath` and other `\html@mathml` macros in arguments ([#&#8203;4139](https://redirect.github.com/KaTeX/KaTeX/issues/4139)) ([a850cce](https://redirect.github.com/KaTeX/KaTeX/commit/a850cce7ccbf95a0b187313d1e54d8d40dfc7273))

#### [0.16.28](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.27...v0.16.28) (2026-01-25)

##### Bug Fixes

- **type:** add missing types definition path to package.json ([#&#8203;4125](https://redirect.github.com/KaTeX/KaTeX/issues/4125)) ([0ef8921](https://redirect.github.com/KaTeX/KaTeX/commit/0ef8921d189346b0ff8f84a77f7f552349b76893))

#### [0.16.27](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.26...v0.16.27) (2025-12-07)

##### Features

- support equals sign and surrounding whitespace in \htmlData attribute values ([#&#8203;4112](https://redirect.github.com/KaTeX/KaTeX/issues/4112)) ([c77aaec](https://redirect.github.com/KaTeX/KaTeX/commit/c77aaec00c766f5bb02e332a1dc416b82a65fe8f))

#### [0.16.26](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.25...v0.16.26) (2025-12-07)

##### Bug Fixes

- \mathop followed by integral symbol ([6fbad18](https://redirect.github.com/KaTeX/KaTeX/commit/6fbad18857351e4d2a88ed3e3348bd76caad9be3))

#### [0.16.25](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.24...v0.16.25) (2025-10-13)

##### Features

- **css:** provide `katex-swap.css` that uses `font-display: swap` ([#&#8203;3940](https://redirect.github.com/KaTeX/KaTeX/issues/3940)) ([b3f9ce6](https://redirect.github.com/KaTeX/KaTeX/commit/b3f9ce691e89a52dea7ec8f10cc6ed4ddc8fc161)), closes [#&#8203;2242](https://redirect.github.com/KaTeX/KaTeX/issues/2242)

#### [0.16.24](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.23...v0.16.24) (2025-10-12)

##### Features

- support hex colors with alpha ([#&#8203;4090](https://redirect.github.com/KaTeX/KaTeX/issues/4090)) ([8c9b306](https://redirect.github.com/KaTeX/KaTeX/commit/8c9b3063965acc0d6e6a0b6df4d051169de9e1a9)), closes [#&#8203;4067](https://redirect.github.com/KaTeX/KaTeX/issues/4067) [#fA6](https://redirect.github.com/KaTeX/KaTeX/issues/fA6) [#fA6f1](https://redirect.github.com/KaTeX/KaTeX/issues/fA6f1)

#### [0.16.23](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.22...v0.16.23) (2025-10-03)

##### Bug Fixes

- Support `\def` with arguments via `macros` option ([#&#8203;4087](https://redirect.github.com/KaTeX/KaTeX/issues/4087)) ([80a8158](https://redirect.github.com/KaTeX/KaTeX/commit/80a815856a8c26d78b3669e9c05fff00efe82247))

#### [0.16.22](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.21...v0.16.22) (2025-04-09)

##### Bug Fixes

- \relax in base or exponent of super/subscript ([#&#8203;4045](https://redirect.github.com/KaTeX/KaTeX/issues/4045)) ([1f43c84](https://redirect.github.com/KaTeX/KaTeX/commit/1f43c84a175fb689f8c8d1d72b1e8b896a8b43d1))

#### [0.16.21](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.20...v0.16.21) (2025-01-17)

##### Bug Fixes

- escape \htmlData attribute name ([57914ad](https://redirect.github.com/KaTeX/KaTeX/commit/57914ad91eff401357f44bf364b136d37eba04f8))

#### [0.16.20](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.19...v0.16.20) (2025-01-12)

##### Bug Fixes

- \providecommand does not overwrite existing macro ([#&#8203;4000](https://redirect.github.com/KaTeX/KaTeX/issues/4000)) ([6d30fe4](https://redirect.github.com/KaTeX/KaTeX/commit/6d30fe47b06f9da9b836fe518d5cbbecf6a6a3a1)), closes [#&#8203;3928](https://redirect.github.com/KaTeX/KaTeX/issues/3928)

#### [0.16.19](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.18...v0.16.19) (2024-12-29)

##### Bug Fixes

- **types:** improve `strict` function type ([#&#8203;4009](https://redirect.github.com/KaTeX/KaTeX/issues/4009)) ([4228b4e](https://redirect.github.com/KaTeX/KaTeX/commit/4228b4eb529b8e35def66cc6e4fa467383b98c86))

#### [0.16.18](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.17...v0.16.18) (2024-12-18)

##### Bug Fixes

- Actually publish TypeScript type definitions ([#&#8203;4008](https://redirect.github.com/KaTeX/KaTeX/issues/4008)) ([629b873](https://redirect.github.com/KaTeX/KaTeX/commit/629b87354fdfc04a3769f09b69f6bbadebcb9ae8))

#### [0.16.17](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.16...v0.16.17) (2024-12-17)

##### Bug Fixes

- MathML combines multidigit numbers with sup/subscript, comma separators, and multicharacter text when outputting to DOM ([#&#8203;3999](https://redirect.github.com/KaTeX/KaTeX/issues/3999)) ([7d79e22](https://redirect.github.com/KaTeX/KaTeX/commit/7d79e220f465c42d4334dc95f1c41e333667e168)), closes [#&#8203;3995](https://redirect.github.com/KaTeX/KaTeX/issues/3995)

#### [0.16.16](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.15...v0.16.16) (2024-12-17)

##### Features

- ESM exports, TypeScript types ([#&#8203;3992](https://redirect.github.com/KaTeX/KaTeX/issues/3992)) ([ea9c173](https://redirect.github.com/KaTeX/KaTeX/commit/ea9c173a0de953b49b2ce5d131e88b785f5dffa1))

#### [0.16.15](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.14...v0.16.15) (2024-12-09)

##### Features

- italic sans-serif in math mode via `\mathsfit` command ([#&#8203;3998](https://redirect.github.com/KaTeX/KaTeX/issues/3998)) ([2218901](https://redirect.github.com/KaTeX/KaTeX/commit/22189018b63c9312ec4ad126804514a7390d60b5))

#### [0.16.14](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.13...v0.16.14) (2024-12-08)

##### Features

- \dddot and \ddddot support ([#&#8203;3834](https://redirect.github.com/KaTeX/KaTeX/issues/3834)) ([bda35cd](https://redirect.github.com/KaTeX/KaTeX/commit/bda35cdb0a6bbbc52dd27c79e4d984688be3b745)), closes [#&#8203;2744](https://redirect.github.com/KaTeX/KaTeX/issues/2744)

#### [0.16.13](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.12...v0.16.13) (2024-12-08)

##### Bug Fixes

- `\vdots` and `\rule` support in text mode ([#&#8203;3997](https://redirect.github.com/KaTeX/KaTeX/issues/3997)) ([0e08352](https://redirect.github.com/KaTeX/KaTeX/commit/0e0835262345d991df61a435800a16b069a4d5c7)), closes [#&#8203;3990](https://redirect.github.com/KaTeX/KaTeX/issues/3990)

#### [0.16.12](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.11...v0.16.12) (2024-12-08)

##### Features

- **css:** configurable margin for display math ([#&#8203;3638](https://redirect.github.com/KaTeX/KaTeX/issues/3638)) ([3405001](https://redirect.github.com/KaTeX/KaTeX/commit/3405001225b8ee0cf8b35b2e3a6c1fa2191e5fef))

#### [0.16.11](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.10...v0.16.11) (2024-07-02)

##### Features

- add \emph ([#&#8203;3963](https://redirect.github.com/KaTeX/KaTeX/issues/3963)) ([9f34da4](https://redirect.github.com/KaTeX/KaTeX/commit/9f34da4b3cf228a7af8134c394394d780a089f2b)), closes [#&#8203;3566](https://redirect.github.com/KaTeX/KaTeX/issues/3566)

#### [0.16.10](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.9...v0.16.10) (2024-03-24)

##### Bug Fixes

- \edef bypassing maxExpand via exponential blowup ([e88b4c3](https://redirect.github.com/KaTeX/KaTeX/commit/e88b4c357f978b1bca8edfe3297f0aa309bcbe34))
- escape \includegraphics src and alt ([c5897fc](https://redirect.github.com/KaTeX/KaTeX/commit/c5897fcd1f73da9612a53e6b5544f1d776e17770))
- force protocol to be lowercase for better protocol filtering ([fc5af64](https://redirect.github.com/KaTeX/KaTeX/commit/fc5af64183a3ceb9be9d1c23a275999a728593de)), closes [/datatracker.ietf.org/doc/html/rfc3986#section-3](https://redirect.github.com//datatracker.ietf.org/doc/html/rfc3986/issues/section-3)
- maxExpand limit with Unicode sub/superscripts ([085e21b](https://redirect.github.com/KaTeX/KaTeX/commit/085e21b5da05414efefa932570e7201a7c70e5b2))

#### [0.16.9](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.8...v0.16.9) (2023-10-02)

##### Features

- Support bold Fraktur ([#&#8203;3777](https://redirect.github.com/KaTeX/KaTeX/issues/3777)) ([240d5ae](https://redirect.github.com/KaTeX/KaTeX/commit/240d5aede915e0303929a9328745b1060e12004a))

#### [0.16.8](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.7...v0.16.8) (2023-06-24)

##### Features

- expose error length and raw error message on ParseError ([#&#8203;3820](https://redirect.github.com/KaTeX/KaTeX/issues/3820)) ([710774a](https://redirect.github.com/KaTeX/KaTeX/commit/710774aaebb38f43b1ec51c159fe9b9520c91424))

#### [0.16.7](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.6...v0.16.7) (2023-04-28)

##### Bug Fixes

- **docs/support_table.md:** delete redundant "varPsi" ([#&#8203;3814](https://redirect.github.com/KaTeX/KaTeX/issues/3814)) ([33a1b98](https://redirect.github.com/KaTeX/KaTeX/commit/33a1b98710c880d2d4a67aa0048f027a94b85702))

#### [0.16.6](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.5...v0.16.6) (2023-04-17)

##### Bug Fixes

- Support `\let` via `macros` option ([#&#8203;3738](https://redirect.github.com/KaTeX/KaTeX/issues/3738)) ([bdb0be2](https://redirect.github.com/KaTeX/KaTeX/commit/bdb0be201794d22adaee05438b07a2830efea9da)), closes [#&#8203;3737](https://redirect.github.com/KaTeX/KaTeX/issues/3737) [#&#8203;3737](https://redirect.github.com/KaTeX/KaTeX/issues/3737)

#### [0.16.5](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.4...v0.16.5) (2023-04-17)

##### Features

- \_\_defineFunction API exposing internal defineFunction ([#&#8203;3805](https://redirect.github.com/KaTeX/KaTeX/issues/3805)) ([c7b1f84](https://redirect.github.com/KaTeX/KaTeX/commit/c7b1f84b7801a29dffdfa3db0ff35de289db80c0)), closes [#&#8203;3756](https://redirect.github.com/KaTeX/KaTeX/issues/3756)

#### [0.16.4](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.3...v0.16.4) (2022-12-07)

##### Bug Fixes

- space should prevent optional argument to \ ([#&#8203;3746](https://redirect.github.com/KaTeX/KaTeX/issues/3746)) ([a0deb34](https://redirect.github.com/KaTeX/KaTeX/commit/a0deb3410fd92340556fc4c9edb8ab586077e5bf)), closes [#&#8203;3745](https://redirect.github.com/KaTeX/KaTeX/issues/3745)

#### [0.16.3](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.2...v0.16.3) (2022-10-22)

##### Bug Fixes

- \hline after \cr ([#&#8203;3735](https://redirect.github.com/KaTeX/KaTeX/issues/3735)) ([ebf6bf5](https://redirect.github.com/KaTeX/KaTeX/commit/ebf6bf5b50a98ac6c5aca1896c0a6ba985c1c91c)), closes [#&#8203;3734](https://redirect.github.com/KaTeX/KaTeX/issues/3734)

#### [0.16.2](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.1...v0.16.2) (2022-08-29)

##### Bug Fixes

- **auto-render:** concatenate content of successive text nodes ([#&#8203;3422](https://redirect.github.com/KaTeX/KaTeX/issues/3422)) ([4d3fdd8](https://redirect.github.com/KaTeX/KaTeX/commit/4d3fdd8647a1c320dc7bcb9c9ea2af81379f700d))
- Implement \pmb via CSS text-shadow ([#&#8203;3505](https://redirect.github.com/KaTeX/KaTeX/issues/3505)) ([176552a](https://redirect.github.com/KaTeX/KaTeX/commit/176552a69183d71425b491d4cc2fa1d462a1246a))

#### [0.16.1](https://redirect.github.com/KaTeX/KaTeX/compare/v0.16.0...v0.16.1) (2022-08-28)

##### Bug Fixes

- Use SVGs for some stacked delims ([#&#8203;3686](https://redirect.github.com/KaTeX/KaTeX/issues/3686)) ([8a65a2e](https://redirect.github.com/KaTeX/KaTeX/commit/8a65a2e1fd69ffeee2fac62229f9f05ebf6afd45))

</details>

---

### Configuration

📅 **Schedule**: (UTC)

- Branch creation
  - At any time (no schedule defined)
- Automerge
  - At any time (no schedule defined)

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

---

 - [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

---

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job log](https://developer.mend.io/github/mermaid-js/mermaid).
<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiI0NC4xMzQuMSIsInVwZGF0ZWRJblZlciI6IjQ0LjEzNC4xIiwidGFyZ2V0QnJhbmNoIjoiZGV2ZWxvcCIsImxhYmVscyI6W119-->

