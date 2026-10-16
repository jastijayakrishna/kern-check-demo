# refactor: address react doctor findings

Run React Doctor on the React app and address actionable findings across security, accessibility, and state handling.

- **Security:** Remove the dynamic syntax probe and prevent the registry proxy from automatically following upstream redirects:
  ```js
  fetch(url, { ...options, redirect: 'manual' });
  ```
- **Accessibility:** Make interactive controls keyboard-operable and expose graph nodes as focusable buttons.
- **Correctness and maintainability:** Guard async updates against stale requests, revoke download object URLs, handle missing map entries safely, and reuse duplicated help markup.

<!-- START COPILOT CODING AGENT SUFFIX -->
