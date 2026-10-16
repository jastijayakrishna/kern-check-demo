# fix(kno-11370): prevent iconSize prop from spreading onto DOM element

## Summary

Fixes:
<img width="774" height="351" alt="Screenshot 2026-01-26 at 5 13 27 PM" src="https://github.com/user-attachments/assets/a581fd29-8e39-47bd-853b-208fe4746e04" />


Fixes a React warning where `iconSize` prop was being spread onto a DOM element in the Toggle Switch component.

The `TOGGLE_SIZE_MAP` contains `{ w, h, iconSize }` for each size. Previously, the entire `sizeConfig` object was spread onto `Button.Root` (line 168), which passed the invalid `iconSize` prop through to the DOM, causing the warning:
> Warning: React does not recognize the `iconSize` prop on a DOM element

The fix destructures `iconSize` separately before spreading the remaining props (`w`, `h`) onto `Button.Root`, while using `iconSize` directly for the `Icon` component.

## Review & Testing Checklist for Human

- [ ] Verify the Toggle component renders correctly at both size "1" and size "2"
- [ ] Confirm the React warning no longer appears in the console when using the Toggle component

### Notes

Requested by: @MikeCarbone

Link to Devin run: https://app.devin.ai/sessions/80ce2ee5fdbc4e28b6595e5eb7bf0caf
