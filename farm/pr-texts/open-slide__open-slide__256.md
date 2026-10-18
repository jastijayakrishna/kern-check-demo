# feat: improve mobile presentation control bar

**Summary**
- Added a persistent mobile control bar and more menu for present mode, making prev/next, overview, blackout/whiteout, laser, fullscreen, and exit actions easier to reach on small screens.
- Adjusted the chrome display logic for desktop and mobile to avoid relying on bottom hot-zone swipe-in on mobile, and support toggling the mobile controls by tapping the center area.
- Added new copy and accessibility labels covering en, ja, zh-CN, and zh-TW.

**Testing**
- Not run (not requested)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **New Features**
  * Improved mobile presentation controls with easier single-tap playback, compact controls, and auto-hiding behavior.
  * Enhanced slide tap handling to support center-area actions and more detailed viewport click responses.
* **Bug Fixes**
  * Mobile controls now stay visible when required and don’t rely on desktop-style cursor hiding.
  * Mobile presentation now defaults to a mobile-friendly windowed view (instead of fullscreen).
  * Reduced accidental click-through by improving button click handling on mobile.
<!-- end of auto-generated comment: release notes by coderabbit.ai -->
