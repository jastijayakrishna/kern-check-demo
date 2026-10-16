# Fix subquery collection ranges and aggregate function parsing

Subquery collection ranges omitted the opening parenthesis, and `ALL`, `FIRST`, or `LAST` calls with regular arguments could be routed into subquery parsing.

- **Collection ranges:** Start the range at the consumed `(`.
- **Function parsing:** Select the aggregate-subquery branch only when the argument starts with `SELECT`; otherwise parse a normal function call.

```sql
SELECT FIRST(c.field) FROM c
SELECT * FROM (SELECT * FROM c)
```

<!-- START COPILOT CODING AGENT SUFFIX -->



<!-- START COPILOT ORIGINAL PROMPT -->



<details>

<summary>Original prompt</summary>

> 
>     Please apply the following diffs and create a pull request.
>     Once the PR is ready, give it a title based on the messages of the fixes being applied.
> 
>     [{"message":"The `SubqueryCollection` range starts at the nested query's `SELECT` token rather than the opening parenthesis consumed on line 327. This produces a range that excludes part of the collection syntax, unlike other parenthesized expressions. Retain the opening-paren token and use its position as the range start.","fixFiles":[{"filePath":"packages/nosql-language-service/src/parser/SqlParser.ts","diff":"diff --git a/packages/nosql-language-service/src/parser/SqlParser.ts b/packages/nosql-language-service/src/parser/SqlParser.ts\n--- a/packages/nosql-language-service/src/parser/SqlParser.ts\n+++ b/packages/nosql-language-service/src/parser/SqlParser.ts\n@@ -324,13 +324,13 @@\n             },\n             {\n                 ALT: () => {\n-                    this.CONSUME(T.LParen);\n+                    const lp = this.CONSUME(T.LParen);\n                     const query = this.SUBRULE(this.sqlQuery);\n                     const rp = this.CONSUME(T.RParen);\n                     return {\n                         kind: 'SubqueryCollection' as const,\n                         query,\n-                        range: query.range ? { start: query.range.start, end: posEnd(rp) } : undefined,\n+                        range: query.range ? { start: pos(lp), end: posEnd(rp) } : undefined,\n                     };\n                 },\n             },\n"}]},{"message":"Chevrotain's `OR` does not backtrack after selecting an alternative. For `ALL`, `FIRST`, or `LAST`, this gate selects the subquery alternative solely from the function name, so calls whose argument is not a `SELECT` (for example, `FIRST(c.value)`) fail while parsing `sqlQuery` instead of falling through to the normal function-call alternative. Include `LA(1) === T.Select` in the gate, or choose the aggregate branch only when the first argument begins a subquery.","fixFiles":[{"filePath":"packages/nosql-language-service/src/parser/SqlParser.ts","diff":"diff --git a/packages/nosql-language-service/src/parser/SqlParser.ts b/packages/nosql-language-service/src/parser/SqlParser.ts\n--- a/packages/nosql-language-service/src/parser/SqlParser.ts\n+++ b/packages/nosql-language-service/src/parser/SqlParser.ts\n@@ -1137,7 +1137,10 @@\n                         {\n                             GATE: () => {\n                                 const nameUpper = name?.value?.toUpperCase() ?? '';\n-                                return nameUpper === 'ALL' || nameUpper === 'FIRST' || nameUpper === 'LAST';\n+                                return (\n+                                    (nameUpper === 'ALL' || nameUpper === 'FIRST' || nameUpper === 'LAST') &&\n+                                    this.LA(1).tokenType === T.Select\n+                                );\n                             },\n                             ALT: () => {\n                                 const query = this.SUBRULE3(this.sqlQuery);\n"}]}]
>   


</details>
