# Expand About page with detailed sections and add Recruit page

## Summary

Restructured and expanded the About page with comprehensive sections covering the organization's approach, process, and values. Added a new Recruit page for recruitment information. Updated the home page to use a new AboutIntro component.

## Key Changes

- **About page restructuring**: Replaced single Mission component with modular sections:
  - `Intro`: Main mission statement and overview
  - `Values`: Three core principles (内因性, 重要性, 解決性)
  - `Process`: Six-step activity workflow with numbered steps
  - `Stance`: Political neutrality and public policy focus
  - `NextActions`: Link cards to Achievement, Members, and Recruit pages

- **New Recruit page** (`/recruit/`): Placeholder page for recruitment information with contact link

- **Home page update**: Replaced `Mission` component with `AboutIntro` component (similar content, optimized for home context)

- **Metadata improvements**: Added description meta tags to About and Recruit pages; updated root meta title to reflect "公共政策コミュニティ" positioning

- **Route registration**: Added `/recruit/` route to route tree

## Implementation Details

- All new components follow existing patterns: use `PageContainer`, `SectionHeader`, and consistent color scheme (#1c2b33, #e60012)
- Process section uses a 2-column grid with numbered steps
- Values section highlights three key questions the organization asks
- NextActions provides navigation to related pages with hover animations
- Recruit page uses placeholder content with contact CTA, ready for future updates

https://claude.ai/code/session_016tPtGKKw7heitLcnV8RnJy
