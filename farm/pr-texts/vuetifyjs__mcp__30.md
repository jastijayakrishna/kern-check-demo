# feat(migrations): add version-upgrade migration engine with MigrationReceipt contract

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary

Implements a Vuetify version-upgrade migration engine with MCP tools that provide machine-actionable migration rules, plus a **MigrationReceipt schema/contract** for structured findings.

### Key Insight: Server Returns Rules, Client Scans

The hosted MCP (`mcp.vuetifyjs.com`) **cannot read user files**. This design separates concerns:
- **Server** returns migration rules with `detect.grep` patterns
- **Client agent** scans user codebase and emits structured receipts
- Agents can **batch safe changes** (`disposition: 'auto'`) and **surface weird ones** (`disposition: 'review'`) for humans

## New Tools

### `get_upgrade_plan({ from, to })`
Returns a structured upgrade plan that:
- Resolves multi-hop migrations (e.g., `v2.6 → v4` becomes `v2→v3→v4`)
- Provides tooling recommendations per hop (`eslint-plugin-vuetify`, `vuetify-codemods`)
- Includes effort estimates (`low`, `medium`, `high`, `very-high`)
- Returns a rule index with IDs, titles, severity, and codemod availability

**This is the first call agents should make when planning a migration.**

### `get_upgrade_rules({ from, to, ids?, category?, component? })`
Returns full machine-actionable migration rules with:
- `detect.grep`: Patterns for scanning user code
- `detect.files`: File patterns to search
- `replace`: From/to mappings with notes
- `codemod`: Plugin name when `vuetify-codemods` supports it
- `revert`: Snippets for incremental migration paths
- `docs`: Link to upgrade guide section

### `get_migration_receipt_schema()` (NEW)
Returns the **MigrationReceipt** schema that agents MUST use when reporting findings:

```typescript
interface MigrationReceipt {
  appVersion: string           // Detected Vuetify version in user's app
  component: string | null     // Component/API affected
  breakingRule: string         // Rule ID (e.g., 'v4/typography-classes')
  breakingRuleTitle?: string   // Human-readable title
  filePath: string             // Path in user project
  line?: number | { start, end }
  proposedPatch: string | { from, to, note? }
  confidence: 'high' | 'medium' | 'low'
  docsLink: string             // Upgrade guide URL
  disposition: 'auto' | 'review'
  codemod?: string
  hop?: { from, to }
  matchedText?: string
}
```

**Confidence Guidance:**
| Confidence | When to Use | Disposition |
|------------|-------------|-------------|
| `high` | Exact match + codemod + single unambiguous match | `auto` |
| `medium` | Replace mapping but multiple matches or no codemod | `review` |
| `low` | Detect hit but no clean replace | `review` |

**Batch Envelope:**
```typescript
interface MigrationReceiptReport {
  from: string
  to: string  
  appVersion: string
  generatedAt: string
  findings: MigrationReceipt[]
  summary: { auto: number, review: number, total: number, byConfidence: {...} }
}
```

## Schema Design

The migration data schema (`src/data/migrations/schema.ts`) is designed so a future generated `migrations.json` from the Vuetify docs build can replace the hardcoded data without rewriting tool implementations.

## Data Coverage

**v3 → v4** (25+ rules):
- Typography class renames (MD2 → MD3) with codemod support
- CSS layers (mandatory in v4)
- Elevation levels (0-24 → 0-5)
- Grid system overhaul
- Component changes: VSnackbar, VSelect/VAutocomplete/VCombobox item slot, VForm slot props, VBtn, VTextField, etc.

**v2 → v3** (10 rules):
- Vue 3 migration prerequisite
- Composition API adoption
- createVuetify() plugin changes
- Removed components

**v1 → v2** (4 rules):
- Grid system rewrite (v-layout/v-flex → v-row/v-col)
- Component naming changes

## Deprecation

`get_v4_breaking_changes` is marked as deprecated in its description but preserved for backward compatibility.

## Files Changed

```
src/data/migrations/
├── schema.ts       # Type definitions + MigrationReceipt schema
├── index.ts        # Loader boundary + version normalization
├── v1-to-v2.ts     # v1→v2 rules
├── v2-to-v3.ts     # v2→v3 rules
└── v3-to-v4.ts     # v3→v4 rules

src/services/migrations.ts  # Migration service + getMigrationReceiptSchema
src/tools/documentation.ts  # Updated to register new tools
test/migrations.test.ts     # Unit tests including receipt schema tests
```

## Test Plan

Unit tests cover:
- Version normalization (aliases like `2.7`, `latest`, `next`)
- Hop resolution (single and multi-hop)
- Rule filtering by IDs, category, and component
- Honest catalog mappings (docs host, typography, no invented APIs)
- Error handling for invalid versions
- **MigrationReceipt schema validation**
- **MigrationReceiptReport fixture validation**
- **Confidence to disposition mapping guidance**
- **get_migration_receipt_schema output structure**

Run tests with: `npx tsx test/migrations.test.ts`

## Receipt Feedback

This PR directly addresses feedback from John (2026-09-06):
> "Vuetify MCP should return a migration receipt, not just a scan: app version, component, breaking rule, file path, proposed patch, confidence, and docs link. Agents can batch the safe changes and leave the weird ones for a human."

The MigrationReceipt schema captures all requested fields plus extras (`disposition`, `line`, `codemod`, `hop`) for comprehensive migration tracking.
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-01602e29-236b-4e60-ac81-4736e16b63c0?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-01602e29-236b-4e60-ac81-4736e16b63c0&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
