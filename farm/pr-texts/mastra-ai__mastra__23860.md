# feat(playground-ui): add gradient focus-visible styles

## Description

Shared controls now use native `:focus-visible` with indicators adapted to each component. Buttons and menu items get a growing 1px gradient line, compact controls get orbit points, slider thumbs get an opening notch, tabs get curved contours, and table selections get paired 1px lines. Gradients fade to transparent at both ends, with animated entry and exit.

Text inputs and textareas keep their border focus treatment, with a stronger background on filled variants. Grouped fields and popup search inputs apply that treatment to their surrounding field. Click and keyboard focus use the same native behavior on text fields; error borders remain visible while focused or hovered. There are no custom keyboard or pointer listeners.

Validated with 264 tests, package typecheck/build, and browser checks for pointer and keyboard focus, error states, grouped fields, popup searches, and command activation. Field styles were inspected in both themes. Targeted lint has no errors and 9 existing class-order warnings. Reduced-motion and forced-colors fallbacks are included but were not browser-emulated.

## Related issue(s)

Design-system follow-up; no linked issue.

## Type of change

- [ ] Bug fix (non-breaking change that fixes an issue)
- [x] New feature (non-breaking change that adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to change)
- [ ] Documentation update
- [ ] Code refactoring
- [ ] Performance improvement
- [x] Test update

## Checklist

- [ ] I have linked the related issue(s) in the description above
- [ ] I have made corresponding changes to the documentation (if applicable)
- [x] I have added tests that prove my fix is effective or that my feature works
- [ ] I have addressed all Coderabbit comments on this PR


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## ELI5

This PR gives shared Playground controls clearer focus indicators when users navigate with a keyboard. Each control uses an indicator that matches its shape, while text fields keep their border-based focus style.

## Changes

- Added shared `:focus-visible` styles for buttons, menus, compact controls, sliders, tabs, table rows, checkboxes, radio groups, switches, and command inputs.
- Added component-specific indicators:
  - Gradient lines for controls and menu items.
  - Orbit indicators for compact controls.
  - Notches for slider thumbs.
  - Contours for tabs.
  - Paired lines for table rows.
- Kept border-based focus styles for inputs and textareas.
- Strengthened filled input backgrounds during focus.
- Preserved error borders during focus and hover.
- Applied focus styles to grouped fields and popup search inputs.
- Added reduced-motion and forced-colors fallbacks.
- Added slider accessibility regression tests and updated related test coverage.
- Added a patch changeset for `@mastra/playground-ui`.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->
