# Fix: Accept keyboard apostrophe (U+0027) in arithmetic parser for apostrophe-dot format

Transaction amounts like `12'345.67` were truncated to `12.00` when using apostrophe-dot format (`1'000.33`). The arithmetic parser's regex only matched U+2019 (RIGHT SINGLE QUOTATION MARK) from `Intl.NumberFormat` output, not U+0027 (APOSTROPHE) from keyboard input.

### Changes

- **`packages/loot-core/src/shared/arithmetic.ts`**: Added U+0027 to the number character regex
  ```diff
  - while (char(state) && char(state).match(/[0-9,.'\u00A0\u202F ]|\p{Sc}/u)) {
  + while (char(state) && char(state).match(/[0-9,.'\u2019\u00A0\u202F ]|\p{Sc}/u)) {
  ```

- **`packages/loot-core/src/shared/util.test.ts`**: Added test cases with explicit character code verification using escape sequences (`\u0027` and `\u2019`) to prevent copy-paste regressions

- **`packages/loot-core/src/shared/arithmetic.test.ts`**: Added comprehensive test cases for the arithmetic parser:
  - Tests keyboard apostrophe (U+0027) with character code verification
  - Tests typographic apostrophe (U+2019) with character code verification
  - Tests arithmetic operations (addition, subtraction, multiplication, division) with both apostrophe types

The parser now accepts both the typographic apostrophe that the formatter outputs and the keyboard apostrophe that users type.

<!-- START COPILOT ORIGINAL PROMPT -->



<details>

<summary>Original prompt</summary>

> 
> ----
> 
> *This section details on the original issue you should resolve*
> 
> <issue_title>[Bug]: Thousands separator breaks the transaction amount</issue_title>
> <issue_description>### Verified issue does not already exist?
> 
> - [x] I have searched and found no existing issue
> 
> ### What happened?
> 
> When formatting is configured to use `1'000.33` when entering a transaction amount exactly like this, it is being truncated to a only the part before the separator.
> 
> E.g. `12'345.67` gets truncated to `12.00`; `1'234.56` gets truncated to `1.00`
> 
> This is a regression introduced in v26.1.0 for a feature that was working correctly in v25.12.0
> 
> It may be a premature theory but PR https://github.com/actualbudget/actual/pull/6274 was touching the code responsible for the formatting so it's potentially the one introducing this regression.
> 
> ### How can we reproduce the issue?
> 
> 1) In the settings, configure formatting to use `1'000.33`
> 2) Enter transaction with amount `1'234.56`
> 3) "Add" the transaction
> 4) Resulting transaction has amount `1.00`
> 
> ### Where are you hosting Actual?
> 
> Docker
> 
> ### What browsers are you seeing the problem on?
> 
> Firefox
> 
> ### Operating System
> 
> Linux</issue_description>
> 
> ## Comments on the Issue (you are @copilot in this section)
> 
> <comments>
> </comments>
> 


</details>



<!-- START COPILOT CODING AGENT SUFFIX -->

- Fixes actualbudget/actual#6794

<!-- START COPILOT CODING AGENT TIPS -->
---

💬 We'd love your input! Share your thoughts on Copilot coding agent in our [2 minute survey](https://gh.io/copilot-coding-agent-survey).

<!--- actual-bot-sections --->
<hr />

<!--- bundlestats-action-comment key:combined start --->
### Bundle Stats

Bundle | Files count | Total bundle size | % Changed
------ | ----------- | ----------------- | ---------
desktop-client | 28 | 14.47 MB → 14.47 MB (+4 B) | +0.00%
loot-core | 1 | 5.84 MB | 0%
api | 1 | 4.38 MB | 0%

<details>
<summary>View detailed bundle stats</summary>

#### desktop-client

**Total**
Files count | Total bundle size | % Changed
----------- | ----------------- | ---------
28 | 14.47 MB → 14.47 MB (+4 B) | +0.00%

<details>
<summary>Changeset</summary>

File | Δ | Size
---- | - | ----
`home/runner/work/actual/actual/packages/loot-core/src/shared/arithmetic.ts` | 📈 +4 B (+0.16%) | 2.39 kB → 2.39 kB
</details>

<details>
<summary>View detailed bundle breakdown</summary>
<div>

**Added**
No assets were added

**Removed**
No assets were removed

**Bigger**
Asset | File Size | % Changed
----- | --------- | ---------
static/js/index.js | 9.24 MB → 9.24 MB (+4 B) | +0.00%

**Smaller**
No assets were smaller

**Unchanged**
Asset | File Size | % Changed
----- | --------- | ---------
static/js/indexeddb-main-thread-worker-e59fee74.js | 12.94 kB | 0%
static/js/workbox-window.prod.es5.js | 5.64 kB | 0%
static/js/da.js | 106.62 kB | 0%
static/js/de.js | 175.93 kB | 0%
static/js/en-GB.js | 7.18 kB | 0%
static/js/en.js | 162.2 kB | 0%
static/js/es.js | 171.21 kB | 0%
static/js/fr.js | 179.72 kB | 0%
static/js/it.js | 171.54 kB | 0%
static/js/nb-NO.js | 157.23 kB | 0%
static/js/nl.js | 103.35 kB | 0%
static/js/pl.js | 88.64 kB | 0%
static/js/pt-BR.js | 146.35 kB | 0%
static/js/ru.js | 106.97 kB | 0%
static/js/sv.js | 78.2 kB | 0%
static/js/th.js | 182.35 kB | 0%
static/js/uk.js | 215.11 kB | 0%
static/js/resize-observer.js | 18.37 kB | 0%
static/js/BackgroundImage.js | 120.54 kB | 0%
static/js/ReportRouter.js | 1.11 MB | 0%
static/js/narrow.js | 641.19 kB | 0%
static/js/TransactionList.js | 105.97 kB | 0%
static/js/wide.js | 159.97 kB | 0%
static/js/AppliedFilters.js | 9.71 kB | 0%
static/js/usePayeeRuleCounts.js | 11.79 kB | 0%
static/js/useTransactionBatchActions.js | 13.23 kB | 0%
static/js/FormulaEditor.js | 1.04 MB | 0%
</div>
</details>

---

#### loot-core

**Total**
Files count | Total bundle size | % Changed
----------- | ----------------- | ---------
1 | 5.84 MB | 0%

<details>
<summary>View detailed bundle breakdown</summary>
<div>

**Added**
No assets were added

**Removed**
No assets were removed

**Bigger**
No assets were bigger

**Smaller**
No assets were smaller

**Unchanged**
Asset | File Size | % Changed
----- | --------- | ---------
kcab.worker.BP2M0O6Y.js | 5.84 MB | 0%
</div>
</details>

---

#### api

**Total**
Files count | Total bundle size | % Changed
----------- | ----------------- | ---------
1 | 4.38 MB | 0%

<details>
<summary>View detailed bundle breakdown</summary>
<div>

**Added**
No assets were added

**Removed**
No assets were removed

**Bigger**
No assets were bigger

**Smaller**
No assets were smaller

**Unchanged**
Asset | File Size | % Changed
----- | --------- | ---------
bundle.api.js | 4.38 MB | 0%
</div>
</details>
</details>

<!--- bundlestats-action-comment key:combined end --->
