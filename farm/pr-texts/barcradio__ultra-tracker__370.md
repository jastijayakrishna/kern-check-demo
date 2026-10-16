# Reduce Stats DataGrid horizontal waste by making trailing utility column optional

On smaller high-DPI displays, the Stats panel consumed horizontal space with an effectively unused trailing column, causing values to clip out of view and triggering horizontal scroll earlier than expected. This change removes that dead width in Stats while preserving existing DataGrid behavior elsewhere.

- **Targeted layout fix (Stats only)**
  - `RunnerEntry/Stats` now opts out of the trailing utility/reset spacer column:
  ```tsx
  <DataGrid
    data={stats}
    columns={Columns}
    classNames={{ header: "text-primary", table: "table-auto" }}
    showTrailingUtilityColumn={false}
  />
  ```

- **DataGrid API extension**
  - Added optional `showTrailingUtilityColumn?: boolean` to `DataGrid` (default: shown).
  - Prop is threaded into both header and body rendering paths so column counts stay aligned.

- **Conditional trailing column render**
  - `Headers` only renders the trailing reset-column `<th>` when enabled.
  - `TableContent` only renders the trailing spacer `<td>` when enabled and no row action column is present.

- **Behavioral impact**
  - Stats grid uses less horizontal width, reducing premature overflow.
  - Other DataGrid consumers retain current layout/controls by default.

<!-- START COPILOT CODING AGENT SUFFIX -->

- Fixes #369
