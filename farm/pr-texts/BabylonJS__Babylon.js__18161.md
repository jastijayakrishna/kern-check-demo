# Fix delayLoadState assignment order in EquiRectangularCubeTexture.delayLoad

`delayLoadState` was being set to `DELAYLOADSTATE_LOADED` *after* the `_loadImage` call, meaning any code inspecting the state during the async load would see the wrong value. The assignment must happen before the `if` block to match the original behavior.

```typescript
// Before: state set after async call starts
if (!this._texture) {
    this._loadImage(() => { this._loadTexture(); }, this._onError);
}
this.delayLoadState = Constants.DELAYLOADSTATE_LOADED; // ❌ too late

// After: state set synchronously before async call
this.delayLoadState = Constants.DELAYLOADSTATE_LOADED; // ✅
if (!this._texture) {
    this._loadImage(() => { this._loadTexture(); }, this._onError);
}
```

<!-- START COPILOT CODING AGENT TIPS -->
---

📍 Connect Copilot coding agent with [Jira](https://gh.io/cca-jira-docs), [Azure Boards](https://gh.io/cca-azure-boards-docs) or [Linear](https://gh.io/cca-linear-docs) to delegate work to Copilot in one click without leaving your project management tool.
