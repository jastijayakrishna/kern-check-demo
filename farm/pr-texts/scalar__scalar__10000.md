# chore(fastapi): update dependency idna to v3.15 [security]

This PR contains the following updates:

| Package | Change | [Age](https://docs.renovatebot.com/merge-confidence/) | [Confidence](https://docs.renovatebot.com/merge-confidence/) |
|---|---|---|---|
| [idna](https://redirect.github.com/kjd/idna) ([changelog](https://redirect.github.com/kjd/idna/blob/master/HISTORY.md)) | `==3.11` → `==3.15` | ![age](https://developer.mend.io/api/mc/badges/age/pypi/idna/3.15?slim=true) | ![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/idna/3.11/3.15?slim=true) |

---

> [!WARNING]
> Some dependencies could not be looked up. Check the [Dependency Dashboard](../issues/6153) for more information.

---

### Internationalized Domain Names in Applications (IDNA): Specially crafted inputs to idna.encode() can bypass CVE-2024-3651 fix
[CVE-2026-45409](https://nvd.nist.gov/vuln/detail/CVE-2026-45409) / [GHSA-65pc-fj4g-8rjx](https://redirect.github.com/advisories/GHSA-65pc-fj4g-8rjx)

<details>
<summary>More information</summary>

#### Details
This is the same issue as CVE-2024-3651, however the original remediation in 2024 was not a complete fix. Payloads such as `"\u0660" * N` or `"\u30fb" * N + "\u6f22"` utilize the `valid_contexto` function prior to length rejection, and for high values of `N` will take a long time to process.

##### Impact
A specially crafted argument to the `idna.encode()` function could consume significant resources. This may lead to a denial-of-service.

##### Patches
Starting in version 3.14, the function rejects long inputs as soon as practicable prior to any further processing to minimize resource consumption. In version 3.15, this approach was extended to lesser used alternate functions (i.e. per-label conversions and codec support).

##### Workarounds
Domain names cannot exceed 253 characters in length, if this length limit is enforced prior to passing the domain to the `idna.encode()` function it should no longer consume significant resources. This is triggered by arbitrarily large inputs that would not occur in normal usage, but may be passed to the library assuming there is no preliminary input validation by the higher-level application.

#### Severity
- CVSS Score: 6.9 / 10 (Medium)
- Vector String: `CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:N/VI:N/VA:L/SC:N/SI:N/SA:N`

#### References
- [https://github.com/kjd/idna/security/advisories/GHSA-65pc-fj4g-8rjx](https://redirect.github.com/kjd/idna/security/advisories/GHSA-65pc-fj4g-8rjx)
- [https://nvd.nist.gov/vuln/detail/CVE-2026-45409](https://nvd.nist.gov/vuln/detail/CVE-2026-45409)
- [https://github.com/pypa/advisory-database/tree/main/vulns/idna/PYSEC-2026-215.yaml](https://redirect.github.com/pypa/advisory-database/tree/main/vulns/idna/PYSEC-2026-215.yaml)
- [https://github.com/advisories/GHSA-65pc-fj4g-8rjx](https://redirect.github.com/advisories/GHSA-65pc-fj4g-8rjx)

This data is provided by the [GitHub Advisory Database](https://redirect.github.com/advisories/GHSA-65pc-fj4g-8rjx) ([CC-BY 4.0](https://redirect.github.com/github/advisory-database/blob/main/LICENSE.md)).
</details>

---

### Release Notes

<details>
<summary>kjd/idna (idna)</summary>

### [`v3.15`](https://redirect.github.com/kjd/idna/blob/HEAD/HISTORY.md#315-2026-05-12)

[Compare Source](https://redirect.github.com/kjd/idna/compare/v3.14...v3.15)

- Enforce DNS-length cap on individual labels early in `check_label`,
  short-circuiting contextual-rule processing for oversized input
  while staying compatible with UTS 46 usage.
- Tidy core helpers: hoist bidi category sets to module-level
  frozensets (avoiding per-codepoint list construction), simplify
  length checks, and reuse the shared `_unicode_dots_re` from
  `idna.core` in the codec module.
- Use `raise ... from err` for proper exception chaining and
  switch internal string formatting to f-strings.
- Allow `flit_core` 4.x in the build backend.
- Expand the ruff lint set (flake8-bugbear, flake8-simplify,
  pyupgrade, perflint) and apply the surfaced fixes; pin lint CI
  to Python 3.14.
- Add Dependabot configuration for GitHub Actions.
- Convert README and HISTORY from reStructuredText to Markdown.
- Reference CVE-2026-45409 for the 3.14 advisory in place of the
  initial GHSA identifier.

Thanks to Felix Yan, Stan Ulbrych, and metsw24-max for
contributions to this release.

### [`v3.14`](https://redirect.github.com/kjd/idna/blob/HEAD/HISTORY.md#314-2026-05-10)

[Compare Source](https://redirect.github.com/kjd/idna/compare/v3.13...v3.14)

- Removed opportunity to process long inputs into quadratic
  time by rejecting oversize inputs up-front. Closes a bypass
  of the CVE-2024-3651 mitigation. \[CVE-2026-45409]

Thanks to Stan Ulbrych for reporting the issue.

### [`v3.13`](https://redirect.github.com/kjd/idna/compare/v3.12...v3.13)

[Compare Source](https://redirect.github.com/kjd/idna/compare/v3.12...v3.13)

### [`v3.12`](https://redirect.github.com/kjd/idna/compare/v3.11...v3.12)

[Compare Source](https://redirect.github.com/kjd/idna/compare/v3.11...v3.12)

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

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job log](https://developer.mend.io/github/scalar/scalar).
<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiI0NC40Ni4wIiwidXBkYXRlZEluVmVyIjoiNDQuNDYuMCIsInRhcmdldEJyYW5jaCI6Im1haW4iLCJsYWJlbHMiOlsiZGVwZW5kZW5jaWVzIl19-->

