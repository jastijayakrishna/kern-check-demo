# Support CSS asset names with fragment/query suffixes in minifier

### Motivation

- Ensure CSS assets whose filenames include fragment or query suffixes (for example `fragment.css#dark`) are recognized and minified by the built-in CSS minimizer.
- The previous filter only allowed query suffixes and therefore skipped fragment-suffixed asset names.

### Description

- Relax `cssMinify.filter` to use the regex `/.css(?:[?#].*)?$/i` so assets with either `?` or `#` suffixes are claimed for minification.
- Update the test harness to simulate a legacy plugin emitting an asset named `fragment.css#dark` and add an expectation that `fragment.css` is minified.
- Add a changeset file `.changeset/008-css-minify-fragment-suffix.md` documenting the patch.

### Testing

- Ran the updated test case `test/configCases/css/minimize-experiments-true` and its assertions succeeded for the added `fragment.css` expectation.
- Existing assertions in the same test case (for `bundle0.css`, `copied.css`, and `already.css`) continued to pass.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6ab448b4f95c832594948c50ea343c6f)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **Bug Fixes**
  * JavaScript, CSS, and HTML assets with fragment suffixes are now correctly recognized for minification, including filenames generated with both query and fragment components.
  * Asset names with `?` or `#` before the file extension are no longer incorrectly treated as matching that asset type.
<!-- end of auto-generated comment: release notes by coderabbit.ai -->
