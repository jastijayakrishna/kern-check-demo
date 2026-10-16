# feat: Display browser event count in in-browser toolbar when recording

<!--- Provide a general summary of your changes in the Title above -->

## Description

This PR adds a counter showing the number of browser events to the in-browser toolbar while recording. This improves the experience because it lets the user know that something is actually happening as they navigate the page.

## How to Test

1. Start a recording
2. Do a bunch of stuff

The counter on the toggle sidepanel button should match the number of browser events generated.

## Checklist

- [ ] I have performed a self-review of my code.
- [ ] I have added tests for my changes.
- [ ] I have commented on my code, particularly in hard-to-understand areas.
<!-- - [ ] Any other relevant item -->

## Related PR(s)/Issue(s)

Resolves https://github.com/grafana/k6-studio/issues/657

<!-- CURSOR_SUMMARY -->
---

> [!NOTE]
> **Low Risk**
> Low risk UI-only change that mostly refactors existing event-list state into a shared hook and surfaces a counter; minimal impact beyond in-browser controls rendering.
> 
> **Overview**
> Displays a live recorded-event counter on the in-browser toolbar’s event-list toggle button.
> 
> Refactors recorded event state/loading logic into a new `useRecordedEvents` hook, wires it through `InBrowserControls`, and updates `EventDrawer` to receive `events` via props while `ToolBox` shows the count badge alongside the drawer icon.
> 
> <sup>Written by [Cursor Bugbot](https://cursor.com/dashboard?tab=bugbot) for commit 2d6173541aa01462389f0692a2652407c11f02f4. This will update automatically on new commits. Configure [here](https://cursor.com/dashboard?tab=bugbot).</sup>
<!-- /CURSOR_SUMMARY -->

BEGIN_COMMIT_OVERRIDE
feat(browser): Display browser event count in in-browser toolbar when recording
END_COMMIT_OVERRIDE
