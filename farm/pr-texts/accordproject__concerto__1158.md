# fix(concerto-core): fix logic error in skipValidationAndResolution guard

Due to operator precedence, `!options?.disableMetamodelValidation === false` negates the value before comparing, so passing `disableMetamodelValidation: true` with `skipValidationAndResolution: true` would incorrectly throw. The condition should mirror the adjacent `disableMetamodelResolution` check.

### Changes
- Fix `!options?.disableMetamodelValidation === false` → `options?.disableMetamodelValidation === false` in `decoratormanager.js`
- Add regression test: `skipValidationAndResolution: true` + `disableMetamodelValidation: true` must not throw
- Add test: `skipValidationAndResolution: true` + `disableMetamodelResolution: false` alone must throw
- Add test: `skipValidationAndResolution: true` + `disableMetamodelValidation: false` alone must throw
- Remove inadvertently included changes to `types/` files and `package-lock.json` that were unrelated to the fix

### Flags
- Pre-existing bug, not introduced by #1156 (surfaced during that review)

### Screenshots or Video
N/A

### Related Issues
- Issue #1157
- Pull Request #1156

### Author Checklist
- [x] Ensure you provide a [DCO sign-off](https://github.com/probot/dco#how-it-works) for your commits using the `--signoff` option of git commit.
- [x] Vital features and changes captured in unit and/or integration tests
- [x] Commits messages follow [AP format](https://github.com/accordproject/techdocs/blob/master/DEVELOPERS.md#commit-message-format)
- [ ] Extend the documentation, if necessary
- [x] Merging to `main` from `fork:branchname`

<!-- START COPILOT CODING AGENT TIPS -->
---

🔒 GitHub Advanced Security automatically protects Copilot coding agent pull requests. You can protect all pull requests by enabling Advanced Security for your repositories. [Learn more about Advanced Security.](https://gh.io/cca-advanced-security)
