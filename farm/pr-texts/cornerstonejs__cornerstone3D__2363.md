# Fix RectangleROI minimum value label display

<!-- Do Not Delete This! pr_template -->
<!-- Please read our Rules of Conduct: https://github.com/OHIF/Viewers/blob/master/CODE_OF_CONDUCT.md -->
<!-- :hand: Thank you for starting this amazing contribution! -->

### Context

Fixes a display bug in the RectangleROI annotation tool where the minimum value statistic was incorrectly labeled as "Max:" instead of "Min:" in the annotation text display.

**Linear ticket:** OHI-2230

**Issue:** Line 1082 in `RectangleROITool.ts` was showing two "Max:" labels instead of one "Max:" and one "Min:" label, creating confusion for users interpreting statistical measurements in their rectangular ROI annotations.

### Changes & Results

- **Changed:** Single line text label from `Max: ${csUtils.roundNumber(min)}` to `Min: ${csUtils.roundNumber(min)}` in the `defaultGetTextLines` function
- **Effect:** The RectangleROI tool now correctly displays "Min:" for minimum values, aligning its behavior with other ROI tools (EllipticalROI, CircleROI, PlanarFreehandROI)
- **Impact:** Users will now see accurate labeling when viewing rectangular ROI statistics

**Before:** Displayed two "Max:" labels (one for max value, one incorrectly for min value)  
**After:** Displays "Max:" for maximum value and "Min:" for minimum value

### Testing

To test this change:
1. Create a rectangular ROI annotation on a medical image
2. View the annotation statistics text display
3. Verify that both "Max:" and "Min:" labels are shown correctly
4. Compare with other ROI tool outputs to ensure consistency

### Human Review Checklist

⚠️ **Important items for reviewer:**
- Verify the annotation text display shows correct "Min:" and "Max:" labels
- Test that rectangular ROI statistics are calculated and displayed properly
- Confirm alignment with other ROI tools' labeling conventions
- Check that no other display functionality was affected

### Checklist

#### PR

- [x] My Pull Request title is descriptive, accurate and follows the semantic-release format and guidelines.

#### Code

- [x] My code has been well-documented (function documentation, inline comments, etc.)

#### Public Documentation Updates

- [x] The documentation page has been updated as necessary for any public API additions or removals. *(N/A - internal text label fix)*

#### Tested Environment

- [ ] "OS: Ubuntu Linux"
- [ ] "Node version: 20.x" 
- [ ] "Browser: Chrome/Firefox" *(Local testing blocked by environment setup issues)*

---

**Link to Devin run:** https://app.devin.ai/sessions/999649a9e11541d4b9ef8deffe23fd0e  
**Requested by:** @sedghi
