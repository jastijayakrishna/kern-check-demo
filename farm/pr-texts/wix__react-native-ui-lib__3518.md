# feat(checkbox/radioButton): ensure minimum 48x48 hit target for better accessibility

## Description
This PR improves the accessibility of the Checkbox and RadioButton components by ensuring a minimum hit target size of 48x48 pixels, following WCAG guidelines. The changes maintain the visual appearance while making the components more accessible for touch interactions.

## Changelog
- Checkbox & RadioButton: Added hitSlop to ensure minimum 48x48 touch target

## Additional info
Ticket: MADS-4591
