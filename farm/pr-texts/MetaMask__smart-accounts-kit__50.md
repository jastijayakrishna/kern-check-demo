# Improve api for Caveat Enforcer actions and Client

## 📝 Description

This PR refactors the caveat enforcer actions and client within the `@metamask/delegation-toolkit` package to simplify their API and improve developer experience.

Note: This PR was authored with Cursor Agent.

## 🔄 What Changed?

-   **Simplified Action Parameters**: All caveat enforcer actions (e.g., `getMultiTokenPeriodEnforcerAvailableAmount`) now exclusively accept a single parameter: `{ delegation: Delegation }`.
-   **Removed Explicit Address Parameters**: `delegationManager` and `enforcerAddress` are no longer accepted as explicit parameters; they are always derived from the `environment` object. This simplifies the interface, and allows for this functionality to be added in the future.
- **Moved client factory to main export**: `createCaveatEnforcerClient` and `CaveatEnforcerClient` are now exported to the main API export at `@metamask/delegation-toolkit` while the individual actions and the actions factory are exported at `@metamask/delegation-toolkit/actions`

## 🚀 Why?

-   **Improved Developer Experience**: Callers no longer need to manually hash delegations, extract caveat terms/args, or resolve enforcer/delegation manager addresses. The API is significantly more ergonomic, requiring only the `Delegation` object.
-   **Simplified API**: A single, consistent parameter type across all caveat enforcer actions reduces cognitive load and improves predictability.
-   **Centralized Client Access**: Moving the `CaveatEnforcerClient` to the main package export makes it more discoverable and directly accessible.
-   **Standard Practices**: Adopting standard `Error` objects aligns with common JavaScript error handling patterns.

## 🧪 How to Test?

-   [ ] Manual testing steps:
    1.  Import `createCaveatEnforcerClient` from `@metamask/delegation-toolkit` and verify it can be instantiated.
    2.  Call any caveat enforcer action (e.g., `client.getMultiTokenPeriodEnforcerAvailableAmount`) passing only a `{ delegation: Delegation }` object and confirm correct results.
    3.  Test scenarios where a delegation contains no matching caveat or multiple matching caveats for a specific enforcer, ensuring a standard `Error` with a descriptive message is thrown.
-   [ ] Automated tests added/updated
-   [ ] All existing tests pass

## ⚠️ Breaking Changes

-   [x] Breaking changes (describe below):
    -   The API for all caveat enforcer actions has changed. Callers must now pass a `{ delegation: Delegation }` object. The previous parameters (`delegationHash`, `terms`, `args`, `delegationManager`, `enforcerAddress`) are no longer accepted.

This is only a breaking change in development, as these interfaces have not been released.

## 📋 Checklist

-   [x] Code follows the project's coding standards
-   [x] Self-review completed
-   [ ] Documentation updated (if needed)
-   [x] Tests added/updated
-   [ ] Changelog updated (if needed)
-   [ ] All CI checks pass

## 🔗 Related Issues

Closes #
Related to #

## 📚 Additional Notes

This PR is the result of several iterations to refine the API based on feedback, leading to a much cleaner and more intuitive interface for interacting with caveat enforcer contracts.

---
<a href="https://cursor.com/background-agent?bcId=bc-729d14e5-89eb-4a92-b88a-e83eeb1b2c07">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/open-in-cursor-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://cursor.com/open-in-cursor-light.svg">
    <img alt="Open in Cursor" src="https://cursor.com/open-in-cursor.svg">
  </picture>
</a>
<a href="https://cursor.com/agents?id=bc-729d14e5-89eb-4a92-b88a-e83eeb1b2c07">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/open-in-web-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://cursor.com/open-in-web-light.svg">
    <img alt="Open in Web" src="https://cursor.com/open-in-web.svg">
  </picture>
</a>
