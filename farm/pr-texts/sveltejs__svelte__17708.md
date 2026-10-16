# Warn on non-destructured `$props()` reads in runes mode

Non-destructured `$props()` access in runes mode silently skipped the `state_referenced_locally` warning, leading to missed guidance when users read `props` via identifiers or member expressions.

- **Analyzer behavior**
  - Include `rest_prop` bindings in `state_referenced_locally` detection so reads of `$props()` identifiers warn consistently with destructured props.

- **Validation coverage**
  - Add a validator fixture for `$props()` identifiers and update the `props-identifier` snapshot expectations to capture the new warnings.

Example:

```svelte
<script>
	const props = $props();
	const { model } = props;       // now warns
	const value = props.model.value; // now warns
</script>
```

<!-- START COPILOT ORIGINAL PROMPT -->



<details>

<summary>Original prompt</summary>

> 
> ----
> 
> *This section details on the original issue you should resolve*
> 
> <issue_title>False negative for `state_referenced_locally` warning on not destructured `$props` access?</issue_title>
> <issue_description>### Describe the bug
> 
> I was looking for a workaround for sveltejs/svelte#17669 and thought of not destructuring the `$props` directly; to my surprise there were no warnings at all.
> 
> 
> ### Reproduction
> 
> ```js
> const props = $props();
> const { model } = props; // missing warning
> 
> const value = props.model.value; // missing warning
> ```
> 
> [Playground](https://svelte.dev/playground/untitled?version=5.50.2#H4sIAAAAAAAACn2QT4vCQAzFv0oIe1CQ9l51YY97lj1tPYxtXAam6TAT_1H63U0HUax1j3nvJeT3OmTTEBb4w2LFUY0L3FtHEYvfDuXiB28QVL8lv7zP4pGcDNrORJrSq5aFWPQMrmIVrJfPkktROQp00LQ1OehhDR8-tD7O5ku174GjcQdSM8WyNC0hz4HOniqhGk4msOW_klf54zrPNkTwzVUbgsZuz8z1G6GzYCHhQP3iDdV47Zltwv2XMEGN6Cbgk5vIGhujAj3AXstI4WxcycvivZFn7q1OxrqT5RqLvXGR-itXywVk_AEAAA)
> 
> ### Logs
> 
> ```shell
> 
> ```
> 
> ### System Info
> 
> ```shell
> REPL - Svelte v.5.50.2
> ```
> 
> ### Severity
> 
> annoyance</issue_description>
> 
> ## Comments on the Issue (you are @copilot in this section)
> 
> <comments>
> </comments>
> 


</details>



<!-- START COPILOT CODING AGENT SUFFIX -->

- Fixes sveltejs/svelte#17685

<!-- START COPILOT CODING AGENT TIPS -->
---

💡 You can make Copilot smarter by setting up custom instructions, customizing its development environment and configuring Model Context Protocol (MCP) servers. Learn more [Copilot coding agent tips](https://gh.io/copilot-coding-agent-tips) in the docs.
