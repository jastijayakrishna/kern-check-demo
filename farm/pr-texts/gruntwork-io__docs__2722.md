# Add Patcher self-hosting documentation

# Add Patcher self-hosting documentation

## Summary
This PR adds comprehensive documentation for self-hosting Patcher binaries to address DEV-1044. The changes include:

- **New self-hosting guide** at `docs/2.0/docs/patcher/guides/self-hosting.md` (163 lines) explaining how customers can self-host Patcher and Terrapatch binaries rather than downloading directly from github.com/gruntwork-io
- **Updated installation documentation** to include a link to the new self-hosting guide in the appropriate section
- **Updated sidebar navigation** to include the new guide in the Patcher guides section

The documentation covers the requested structure: introduction to self-hosting, self-hosting options (repo-copier, forking, alternatives), GitHub Actions parameters and current limitations, code examples for GitHub Enterprise and GitLab CI, and unsupported methods.

## Review & Testing Checklist for Human
- [ ] **Verify technical accuracy of patcher-action limitations**: The documentation claims the action hardcodes GitHub organizations - confirm this is accurate by reviewing the patcher-action source code
- [ ] **Test internal documentation links**: Verify the link to `/2.0/docs/library/guides/self-hosting` works correctly in the docs site
- [ ] **Check sidebar navigation**: Ensure the new "Self-hosting Patcher" guide appears correctly in the Patcher guides section and the navigation works
- [ ] **Validate YAML syntax**: Review the GitHub Actions workflow examples for correct syntax and best practices
- [ ] **Verify content completeness**: Confirm all requested sections from DEV-1044 are covered (intro, self-hosting options, GitHub Actions parameters, code examples, unsupported methods)

### Test Plan
1. Build the docs site locally and navigate to the new self-hosting guide
2. Verify all internal links work correctly
3. Check that the sidebar navigation includes the new guide in the correct location
4. Review the GitHub Actions YAML examples for syntax correctness

### Notes
- The documentation is based on analysis of the patcher-action source code (lines 184-197 in src/action.ts) which shows hardcoded GitHub organizations
- GitLab CI support is mentioned as newer/experimental per the requirements, directing users to contact support
- Artifactory is explicitly noted as unsupported per requirements
- Link to Devin run: https://app.devin.ai/sessions/124b574c4e504fa485d99dc085e021b6
- Requested by: Josh Padnick (@josh-padnick)
