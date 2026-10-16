# [style-value-parser] Fix invalid media-type conditions for mixed resp…

…onsive/print styles (#1860)
## What changed / motivation ?

Combining responsive values with an `@media print` value on the same property
made StyleX emit a media condition that never matches in browsers:

```css
@media (max-width: 900px) and (not (print)) { .x { margin-left: 168px } }


## Linked PR/Issues

Fixes # (issue)
https://github.com/facebook/stylex/issues/1860
## Additional Context

<!--- Screenshots, Tests, Breaking Change, Anything Else ? --->
<img width="1280" height="800" alt="image" src="https://github.com/user-attachments/assets/8433aa4a-6237-4819-bace-7b0f49d896fb" />

Screenshots, Tests, Anything Else
