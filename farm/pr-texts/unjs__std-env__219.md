# refactor: normalize gitHub copilot cloud agent alias

`AI_AGENT=github_copilot_cloud_agent` was returned as an unrecognized agent name instead of `copilot`. Normalize it alongside the existing VS Code alias.

- **Detection:** Map the cloud-agent alias to `copilot`.
- **Coverage and docs:** Add a regression test and document the alias.

```js
// AI_AGENT=github_copilot_cloud_agent
detectAgent(); // { name: "copilot" }
```
