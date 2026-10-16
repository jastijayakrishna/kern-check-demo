# Upgrade Paper Old Arch Gallery to React Native 0.80.0 and rename to "React Native Gallery (Legacy)" (Windows only)

Upgrades the Paper (Old Architecture) Gallery app from React Native 0.79.2 to 0.80.0 and renames it to "React Native Gallery (Legacy)" on Windows platform only to distinguish it from the New Architecture version.

## Dependency Updates
- React Native: `0.79.2` → `0.80.0`
- React: `19.0.0` → `19.1.0`
- react-native-windows: `0.79.2` → `0.80.0`
- All `@react-native/*` packages: `0.79.2` → `0.80.0`
- Supporting packages updated to align versions (react-test-renderer, @types/react)

## Display Name Changes
Updated app name to "React Native Gallery (Legacy)" on Windows only:
- **app.json**: `displayName` updated to "React Native Gallery (Legacy)"
- **Windows**: `Package.appxmanifest` DisplayName and Description updated to "React Native Gallery (Legacy)"
- **Android**: `strings.xml` app_name - **no change** (remains "rngallery")
- **iOS**: `Info.plist` CFBundleDisplayName - **no change** (remains "rngallery")

## Notes
- yarn.lock updated with new dependency resolutions
- Pre-existing `@react-native/metro-config` duplication in dependencies/devDependencies maintained (now both at 0.80.0)
- iOS and Android platforms retain the original "rngallery" name per project requirements

<issue_title>Upgrade Paper Old Arch Gallery app to React Native 0.80.0 and rename it to "React Native Gallery (Legacy)"</issue_title>
&gt;<issue_description>Upgrade Paper Old Arch Gallery app to React Native 0.80.0 and rename it to "React Native Gallery (Legacy)"</issue_description>
&gt; 
&gt; ## Comments on the Issue (you are @copilot in this section)
&gt; 
&gt;<comments>
&gt;</comments>
&gt;

- Fixes microsoft/react-native-gallery#749

<!-- START COPILOT CODING AGENT SUFFIX -->



<details>

<summary>Original prompt</summary>

> 
> ----
> 
> *This section details on the original issue you should resolve*
> 
> <issue_title>Upgrade Paper Old Arch Gallery app to React Native 0.80.0 and rename it to "React Native Gallery (Legacy)"</issue_title>
> <issue_description>Upgrade Paper Old Arch Gallery app to React Native 0.80.0 and rename it to "React Native Gallery (Legacy)"</issue_description>
> 
> ## Comments on the Issue (you are @copilot in this section)
> 
> <comments>
> </comments>
> 


</details>

- Fixes microsoft/react-native-gallery#749

<!-- START COPILOT CODING AGENT TIPS -->
---

💬 We'd love your input! Share your thoughts on Copilot coding agent in our [2 minute survey](https://gh.io/copilot-coding-agent-survey).

 ###### Microsoft Reviewers: [Open in CodeFlow](https://microsoft.github.io/open-pr/?codeflow=https://github.com/microsoft/react-native-gallery/pull/750)
