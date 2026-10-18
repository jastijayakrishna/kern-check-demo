# fix: make Rake Owner Address read-only on table creation form

The "Rake Owner Address" field on the table creation form was editable, allowing users to set an arbitrary rake recipient. It should always be locked to the current user's wallet address.

## Changes

- **`src/pages/TableAdminPage.tsx`**: Removed `onChange` handler from the Rake Owner Address input, added `readOnly`, and applied `cursor-not-allowed opacity-70` styling to visually signal the field is non-editable.

```diff
- onChange={e => setRakeOwner(e.target.value)}
+ readOnly
  className="... cursor-not-allowed opacity-70"
```

The field continues to display the connected wallet address as its value, sourced from `cosmosWallet.address`.

<!-- START COPILOT CODING AGENT SUFFIX -->

- Fixes #579
