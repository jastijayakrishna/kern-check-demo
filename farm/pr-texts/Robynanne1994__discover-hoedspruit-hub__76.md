# Refactor category display from chips to dot-separated line

## Summary
Refactored the category display in the listing detail page from floating pill-shaped chips to a simple dot-separated text line positioned directly under the listing title.

## Key Changes
- **Removed chip-based category display**: Deleted two separate category chip implementations:
  - Absolute-positioned chips overlaid on the hero image
  - Conditional chips displayed above the title when no hero image exists
  
- **Implemented new category line format**: Added a single, unified category display that:
  - Appears directly under the listing title
  - Uses dot separators (·) between category items
  - Applies consistent brown text styling (using `C.primary` color)
  - Works uniformly regardless of hero image presence

- **Updated styling**: Replaced `categoryChipStyle` with `categoryLineStyle` featuring:
  - Smaller font size (14px vs 10.5px)
  - Lighter font weight (600 vs 700)
  - Reduced letter spacing (0.005em vs 0.13em)
  - Removed uppercase transformation and pill-shaped styling
  - Added line-height for better readability

## Implementation Details
The new category line uses a simple inline layout with conditional dot separators rendered between items, providing a cleaner, more integrated appearance with the listing title rather than competing for visual attention as floating elements.

https://claude.ai/code/session_01S6moJMVvABqkzEkVkq7xaa
