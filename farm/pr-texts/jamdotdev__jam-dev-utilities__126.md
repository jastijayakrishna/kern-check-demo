# feat: enhance regex tester with interactive playground features

# feat: enhance regex tester with interactive playground features

## Summary

Transforms the basic regex tester into an interactive playground inspired by regexer. The enhancement adds several features to make regex more accessible to junior developers:

**Core Features:**
- Toggleable pattern flags (g, i, m, s, u, y) with hover card explanations
- Preset regex patterns (email, URL, phone, date, IP, hex color, HTML tag, credit card) for quick demos
- Real-time pattern explanation with color-coded components (hover for details)
- Capture group visualization in CSS box model style with nested indentation (collapsible section)
- Match statistics dashboard showing total/unique matches, average length, and execution time
- Collapsible regex cheat sheet with click-to-insert functionality
- Enhanced match highlighting with hover cards showing position and length

**Technical Changes:**
- Added 6 new React components in `components/regex/`
- Extended `regex-tester.utils.ts` with pattern parsing, explanation, and stats functions
- Added `@radix-ui/react-hover-card` and `@radix-ui/react-tooltip` dependencies via shadcn
- Updated main page to use tabs for Pattern Explanation and Statistics

**Layout & UX Improvements:**
- Widened layout from `max-w-2xl` to `max-w-4xl` for more breathing room
- Moved capture groups to a collapsible section in the main card for easier access
- Replaced Radix Tooltip with HoverCard (fixes content not updating when moving mouse quickly)
- All hover cards use sans-serif fonts consistently with `bg-muted` background highlighting for code values
- Email preset includes `gm` flags for multi-line matching
- Clear button resets all fields

## Review & Testing Checklist for Human

- [ ] **Test capture groups collapsible section**: Enter a pattern with groups like `/(a)(b)/g` with test string `ab ab`, expand the "Capture Groups" section, verify visualization displays correctly
- [ ] **Test preset patterns**: Click through presets (especially Email), verify they load correctly with proper flags and show matches
- [ ] **Verify font consistency**: Hover over flags, pattern components, capture groups, and match highlights - all should use sans-serif fonts with background highlighting for code values
- [ ] **Test clear button**: Fill in pattern and test string, click Clear, verify all fields reset including flags

**Recommended test plan:**
1. Load page fresh, select Email preset - verify it matches emails in the test string
2. Enter a pattern with capture groups, expand the collapsible section, verify groups display
3. Hover over various elements (flags, pattern components, matches) and verify consistent styling
4. Click Clear and verify everything resets
5. Check the wider layout looks good on different screen sizes

### Notes

- Capture groups are now in a collapsible section in the main card rather than a separate tab
- The tabs section contains only Pattern Explanation and Statistics

**Link to Devin run:** https://app.devin.ai/sessions/93dfd4f1aa4649e7917bfc1f71f62694
**Requested by:** @peckz
