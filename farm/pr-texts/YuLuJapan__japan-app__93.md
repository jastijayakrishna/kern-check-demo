# Redesign the trip screen and day plan (options 1e/1f/1g)

Implements the Onward redesign's trip overview and day-by-day planning screens, replacing the carousel-based flight card with a collapsible countdown widget and redesigning the activity timeline.

## Summary

This change brings three major UI redesigns to life:
- **Trip screen hero** (1e/1f): Replaces the sushi animation with a photo of the destination, adds a collapsible countdown card that opens to show flight details, and introduces a new map view showing all stops in space.
- **Day plan timeline** (1g): Redesigns activities from a card list to a left-aligned timeline with dots, fixed-width time column, and category tags pulled from linked places.
- **Supporting components**: Updates the day strip (date picker) to use rings instead of filled tiles, simplifies the journey slider to show only city names and numbers, and adds a reusable `PhotoHero` component for both trip and city screens.

## Key Changes

**CountdownWidget** (`src/components/CountdownWidget.tsx`)
- Removed two-pane carousel (swipe/chevron navigation) in favor of a collapsible disclosure
- Card now opens/closes with a single tap, showing both outbound and return flights stacked
- Redesigned numerals and labels with new color palette (sand background, graphite text)
- Removed touch handling; simplified state from `pane` index to boolean `open` flag
- Removed `ChevronIcon` component (no longer needed)

**PhotoHero** (`src/components/PhotoHero.tsx`, new)
- Reusable full-bleed photo header with dual-layer scrim (top 28% for app chrome, bottom 45% ramping to 68% black)
- Supports eyebrow pill, title, meta line, back button, and action slot
- Used by both trip overview and city screens with configurable height and overlap

**Journey page** (`src/pages/Journey.tsx`)
- Replaced `HeroTitle` with `PhotoHero` showing destination photo
- Added `journey-sushi-hero` flag (defaults off) to gate the animation; photo is now the default
- Added `trip-map` flag (defaults on) to gate the new map view
- Simplified hero logic: no longer gates flight card on Japan trip

**TripMap** (`src/pages/TripMap.tsx`, new)
- Displays all trip stops as clusters on a hatched field (tiles to be added later)
- `projectStops()` function projects real coordinates linearly, with fallback to even spacing for ungeocode stops
- Clusters sized by saved-place count, colored cyclically, each linking to its city
- Includes comprehensive tests for projection logic and link generation

**DayPlan** (`src/components/DayPlan.tsx`)
- Redesigned from card list to left-aligned timeline with hairline border and dots
- First activity of day gets coral dot and coral time; rest are muted
- Time moved to fixed-width column so titles align
- Added category tag and file list under each activity (pulled from linked place)
- Removed padding/spacing in favor of timeline structure

**DayStrip** (`src/components/DayStrip.tsx`)
- Changed from filled tiles to ring circles (46px on trip, 42px on city)
- Added plane icon above dashed ring for days when city changes
- Selected day gets thicker coral ring with blush fill; today gets coral dot when not selected
- Increased gap between chips from 2 to 2.5

**JourneyStepsSlider** (`src/components/JourneyStepsSlider.tsx`)
- Simplified to show only city number, name, and photo
- Removed dates and nights (now on city screen only)
- Reduced gap from 3.5 to 3

**Zone page** (`src/pages/Zone.tsx`)
- Replaced `Breadcrumbs` + `ZoneImage` with `PhotoHero`
- Computes eyebrow from trip stops in this city (date range + night count)
- Adds back button linking to trip

**API & server changes**
- `ItineraryItemView` interface adds `place_category` and `place_files` fields (derived per request,

https://claude.ai/code/session_01KfCDCtWnrcMzxTk127NG75
