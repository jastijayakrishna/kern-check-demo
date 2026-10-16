# UI: Respect reduced motion and pause,stop,hide in Card animations

## What I did

<img width="333" height="295" alt="image" src="https://github.com/user-attachments/assets/d9ceb6c3-992f-4e3d-b186-0f6123a13889" />
<img width="320" height="256" alt="image" src="https://github.com/user-attachments/assets/a634ea34-c328-4f90-8153-8e9063e5edf1" />



Fixed two categories of a11y violations with our animated borders in the onboarding widget and TestProvider: [SC 2.2.2 Pause, Stop, Hide](https://www.w3.org/WAI/WCAG21/Understanding/pause-stop-hide.html) and [SC 2.3.3 Animation from interactions](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html).

The problems were:
* TestProvider did not respect reduced motion, as it used a rotating colours animation, violating SC 2.3.3
* Onboarding widget ran automatically and forever, violating SC 2.2.2
* Onboarding widget respected reduced motion but looked exceptionally ugly, violating my sanity

To fix this, I added a new type of pulsating animation that does not trigger vestibular disorder and can be used safely. It replaces the ugly static rainbow of the onboarding widget, and the rotating animation of the test provider.

I also limited the duration of the onboarding widget animation to 5 seconds. I didn't limit duration for the test widget because we provide a stop control that stops the process and associated animation.

## LLM slop details

**Onboarding checklist (`outlineAnimation="rainbow"`)**

- The animation now ends after 5 seconds in both motion modes, to meet WCAG 2.2.2 (Pause, Stop, Hide). Previously the colours slid indefinitely and faded in and out every 60 seconds.
- The border is now a still diagonal gradient, orange at the bottom left to green at the top right, using the orange and green from the previous rainbow.
- Full motion: the gradient stays in place while its colours cycle once through the spectrum (`hue-rotate` from 0° to 360°, 5 s, ease-in-out), then it rests on orange and green. Nothing slides, so the card growing while the widget loads no longer affects the animation. The border no longer fades back to grey.
- Reduced motion: the previous static rainbow is replaced by the same gradient. Its opacity dims from 1 to 0.5 and back twice over 5 seconds, then stays at 1.
- `ChecklistWidget` only enables the animation once the widget is shown. The widget is mounted collapsed until the checklist has loaded and has items, and the animation used to start at mount, so part or all of the 5 seconds could pass while it was hidden.

**Testing widget (`outlineAnimation="spin"`)**

- Reduced motion was not respected. With reduced motion, the rotating arc is replaced by a static diagonal gradient of the same two colours (blue and seafoam, or orange and gold while running with errors), whose opacity pulses for as long as tests run. It does not stop after 5 seconds, because the user starts it and the widget has a stop control.
- Full motion is unchanged: one rotation every 5 seconds, repeating while tests run.
- The Review widget also uses this outline, so with reduced motion it now pulses instead of rotating. Its animation still never ends; its dismiss button is the mechanism that hides it.

The spin colour selection moved into a `getSpinColors()` helper so the rotating and reduced-motion gradients share the same colours.

## Checklist for Contributors

### Testing

#### The changes in this PR are covered in the following automated tests:

- [x] stories
- [ ] unit tests
- [ ] integration tests
- [ ] end-to-end tests

The `Rainbow` Card story has a `play` function that fails if any outline animation lasts longer than 5 seconds.

The new `RainbowReducedMotion` and `SpinningReducedMotion` stories are snapshotted by Chromatic with `prefersReducedMotion: 'reduce'`.

The `Rainbow` snapshot is now taken at the end of the animation. Chromatic snapshots for the Card, ChecklistWidget and TestingWidget stories are expected to change.

#### Manual testing

1. Run `cd code && yarn storybook:ui` and open Storybook.
2. Open **manager/components/sidebar/ChecklistWidget › Default**. The border is an orange (bottom left) to green (top right) gradient whose colours cycle once through the spectrum over about 5 seconds without moving, then stay orange and green.
3. Open **manager/Sidebar/TestingWidget › Running** and **Running With Errors**. The coloured arc keeps rotating (blue and seafoam; orange and gold with errors).
4. Turn on reduced motion, either in the operating system (macOS: System Settings › Accessibility › Display › Reduce motion; Windows: Settings › Accessibility › Visual effects › Animation effects off) or in Chrome DevTools (Rendering › Emulate CSS media feature `prefers-reduced-motion: reduce`), then reload the story.
5. **ChecklistWidget › Default**: the same gradient stays still and dims and brightens twice over 5 seconds, then stays at full brightness.
6. **TestingWidget › Running** and **Running With Errors**: the border is a static two-colour diagonal gradient that keeps dimming and brightening and does not rotate.
7. In the Storybook UI itself, reload the page and watch the onboarding checklist at the top of the sidebar. The animation starts when the widget appears, not before.
8. Optionally, check the **components/Card** stories `Rainbow`, `Rainbow Reduced Motion`, `Spinning` and `Spinning Reduced Motion` in both modes.

### Documentation

ø
