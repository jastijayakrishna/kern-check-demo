# feat(dashboard): add csv download from ui and loading state

## Summary
- add a dropdown download menu for customizable dashboard charts
- show download button on chart hover

## Testing
- `pnpm run lint`

------
https://chatgpt.com/codex/tasks/task_e_6851784c6a8883299cfbb6d88e3c8996
<!-- ELLIPSIS_HIDDEN -->


----

> [!IMPORTANT]
> Add CSV download feature and loading state to dashboard charts, refactor `BigNumber` for dynamic data handling.
> 
>   - **Features**:
>     - Add `DownloadButton` component for CSV download in `DownloadButton.tsx`.
>     - Show download button on chart hover in `DashboardWidget.tsx`.
>     - Add loading indicator for chart data in `DashboardWidget.tsx`.
>   - **Components**:
>     - Refactor `BigNumber` in `BigNumber.tsx` to calculate metrics from data and handle loading state.
>     - Update `Chart` in `Chart.tsx` to use `BigNumber` with data prop.
>   - **Misc**:
>     - Add `Loader2` icon for loading state in `DashboardWidget.tsx`.
> 
> <sup>This description was created by </sup>[<img alt="Ellipsis" src="https://img.shields.io/badge/Ellipsis-blue?color=175173">](https://www.ellipsis.dev?ref=langfuse%2Flangfuse&utm_source=github&utm_medium=referral)<sup> for 4718034064d6503f8c596701e378df872ea242bf. You can [customize](https://app.ellipsis.dev/langfuse/settings/summaries) this summary. It will automatically update as commits are pushed.</sup>


<!-- ELLIPSIS_HIDDEN -->
