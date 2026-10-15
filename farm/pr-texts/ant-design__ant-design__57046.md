# fix(site): sync URL params and theme state with AI-generated algorithm

The AI theme generator response includes an `algorithm` field (e.g. `"algorithm": "light"`) which was being applied directly to the site's theme config, silently overriding the user's explicit dark/light preference set via URL param (`?theme=dark`) or local storage — while leaving the URL param stale and out of sync with the actual algorithm being used.

## Changes

- **`.dumi/theme/common/ThemeSwitch/index.tsx`**: When `onThemeChange` receives a `nextTheme` with an `algorithm` field, also update the site's `theme` state and local storage to match. This causes `updateSiteConfig` to propagate the change to the URL param (e.g. `?theme=dark` → `?theme=light`), keeping the URL consistent with the algorithm actually applied.

```diff
  onThemeChange={(nextTheme) => {
-   updateSiteConfig({
-     dynamicTheme: nextTheme,
-   });
+   const updates = { dynamicTheme: nextTheme };
+   // Sync the site theme (and URL param) with the AI-generated algorithm
+   if (nextTheme?.algorithm) {
+     const filteredTheme = theme.filter((t) => !['light', 'dark', 'auto'].includes(t));
+     updates.theme = [...filteredTheme, nextTheme.algorithm];
+     setTheme(nextTheme.algorithm);
+   }
+   updateSiteConfig(updates);
  }}
```

- **`.dumi/theme/layouts/GlobalLayout.tsx`**: The `algorithm` field from `dynamicTheme` is destructured but intentionally ignored (`_dynamicAlgorithm`) to prevent it from leaking into `rawComponentsClassNames`. The dark/light algorithm is always derived from the user's active `theme` state via `getAlgorithm(mergedTheme, systemTheme)`.

```diff
+   // Ignore `algorithm` from AI-generated theme to preserve user's dark/light preference
    const {
-     algorithm: dynamicAlgorithm,
+     algorithm: _dynamicAlgorithm,
      token: dynamicToken,
      ...rawComponentsClassNames
    } = dynamicTheme || {};
-
-   if (dynamicAlgorithm) {
-     mergedTheme = mergedTheme.filter((c) => c !== 'dark' && c !== 'light');
-     mergedTheme.push(dynamicAlgorithm);
-   }
```

<!-- START COPILOT ORIGINAL PROMPT -->



<details>

<summary>Original prompt</summary>

> 
> ----
> 
> *This section details on the original issue you should resolve*
> 
> <issue_title>官网在dark模式下AI对话完毕后会强制light</issue_title>
> <issue_description><img width="3234" height="1920" alt="Image" src="https://github.com/user-attachments/assets/29e41d95-69e1-48b1-b5d0-7efbd5a283fb" />
> 
> <img width="3378" height="1912" alt="Image" src="https://github.com/user-attachments/assets/7f71007f-0b04-43c4-bdc2-1ca9c2c91882" />
> 
> <img width="3358" height="1896" alt="Image" src="https://github.com/user-attachments/assets/66668ecb-63fd-4485-8636-4d646eada388" />
> </issue_description>
> 
> ## Comments on the Issue (you are @copilot in this section)
> 
> <comments>
> <comment_new><author>@zombieJ</author><body>
> 预期行为。如果说需要暗色主题，它也会替换默认算法为暗色算法。不过看起来和 param 有点冲突？</body></comment_new>
> </comments>
> 


</details>



<!-- START COPILOT CODING AGENT SUFFIX -->

- Fixes ant-design/ant-design#56746

<!-- START COPILOT CODING AGENT TIPS -->
---

💡 You can make Copilot smarter by setting up custom instructions, customizing its development environment and configuring Model Context Protocol (MCP) servers. Learn more [Copilot coding agent tips](https://gh.io/copilot-coding-agent-tips) in the docs.
