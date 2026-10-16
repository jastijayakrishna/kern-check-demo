# feat: Support wildcard search for Prüfidentifikator descriptions

Enable `*` searches in the Prüfidentifikator/Beschreibung input, including patterns such as `Änderung*TR` for descriptions beginning with `Änderung` and containing `TR` later.

- **Search behavior**
  - Adds case-insensitive wildcard matching to autocomplete suggestions.
  - Aligns REST/API and MCP search behavior with the same prefix-and-segment semantics.
  - Escapes SQL-LIKE backslashes, `%`, and `_` safely.

- **API and MCP**
  - Documents wildcard semantics in OpenAPI, generated API types, MCP tool schemas, and README.
  - Updates the input placeholder with a wildcard example.

- **Coverage**
  - Adds regression coverage for UI suggestions, MCP schema documentation, SQL wildcard handling, and backslash escaping.

```text
Änderung*TR
# matches: Änderung der Stammdaten TR Hinweis
# excludes: Keine Änderung der TR-Stammdaten
```

<!-- START COPILOT CODING AGENT SUFFIX -->

- Fixes #931
