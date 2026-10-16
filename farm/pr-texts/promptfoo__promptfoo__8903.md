# fix: trailing slashes on internal routes, Docusaurus Link for internal hrefs, and test hygiene

The site is built with `trailingSlash: true`, but several internal routes were missing trailing slashes, causing unnecessary 308 redirects. Additionally, an internal link was using MUI's `Link` (no route normalization) instead of Docusaurus's `Link`.

## Route fixes (`docusaurus.config.ts`)
- Added trailing `/` to nav item targets: `/docs/red-team/`, `/validator/`
- Added trailing `/` to redirect destinations: `/docs/intro/`, `/docs/guides/` (×2)

## Internal link hygiene (`contact.tsx`)
- Swapped MUI `Link` → Docusaurus `Link` with `to=` for the `/docs/enterprise/` link so it benefits from Docusaurus route normalization
- External links (GitHub, Discord) retain MUI `MuiLink` with `href=`
- Added `text-decoration: none` to `.resourceLink` CSS class to maintain visual parity (previously handled by MUI's `underline="none"` prop)

## Test improvements
- **`trailingSlash.test.ts`**: Removed dead condition `entry.name !== '.'` (always true; `readdir` never yields `.` as an entry name)
- **`envars.test.ts`**: Added explicit test for `'yeppers'` as a truthy value; removed redundant uppercase variant test (implementation calls `toLowerCase()` before comparison, already covered)
- **`redteamTestCaseGenerationService.test.ts`**: Replaced hardcoded `REMOTE_GENERATION_URL` with a dynamic import of `getRemoteGenerationUrl()` from source; renamed `REQUEST_TIMEOUT_MS` → `TEST_REQUEST_TIMEOUT_MS`; made `expectTaskRequest` async accordingly

<!-- START COPILOT CODING AGENT SUFFIX -->



<!-- START COPILOT ORIGINAL PROMPT -->



<details>

<summary>Original prompt</summary>


    Please apply the following diffs and create a pull request.
    Once the PR is ready, give it a title based on the messages of the fixes being applied.

    [{"message":"Missing trailing slash on internal route. The site is configured with `trailingSlash: true` (line 34), so this should be `/docs/red-team/` to avoid a 308 redirect.","fixFiles":[{"filePath":"site/docusaurus.config.ts","diff":"diff --git a/site/docusaurus.config.ts b/site/docusaurus.config.ts\n--- a/site/docusaurus.config.ts\n+++ b/site/docusaurus.config.ts\n@@ -300,7 +300,7 @@\n             },\n             {\n               label: 'LLM Red Teaming',\n-              to: '/docs/red-team',\n+              to: '/docs/red-team/',\n             },\n             {\n               label: 'Foundation Model Reports',\n"}]},{"message":"Missing trailing slash on internal route. The site is configured with `trailingSlash: true` (line 34), so this should be `/validator/` to avoid a 308 redirect.","fixFiles":[{"filePath":"site/docusaurus.config.ts","diff":"diff --git a/site/docusaurus.config.ts b/site/docusaurus.config.ts\n--- a/site/docusaurus.config.ts\n+++ b/site/docusaurus.config.ts\n@@ -328,7 +328,7 @@\n             },\n             {\n               label: 'Config Validator',\n-              to: '/validator',\n+              to: '/validator/',\n             },\n           ],\n         },\n"}]},{"message":"Missing trailing slash on internal route. The site is configured with `trailingSlash: true` (line 34), so this should be `/docs/intro/` to avoid a 308 redirect.","fixFiles":[{"filePath":"site/docusaurus.config.ts","diff":"diff --git a/site/docusaurus.config.ts b/site/docusaurus.config.ts\n--- a/site/docusaurus.config.ts\n+++ b/site/docusaurus.config.ts\n@@ -459,7 +459,7 @@\n           },\n           {\n             from: '/docs',\n-            to: '/docs/intro',\n+            to: '/docs/intro/',\n           },\n           {\n             from: '/vegas-contact',\n"}]},{"message":"Missing trailing slash on internal route. The site is configured with `trailingSlash: true` (line 34), so this should be `/docs/guides/` to avoid a 308 redirect.","fixFiles":[{"filePath":"site/docusaurus.config.ts","diff":"diff --git a/site/docusaurus.config.ts b/site/docusaurus.config.ts\n--- a/site/docusaurus.config.ts\n+++ b/site/docusaurus.config.ts\n@@ -471,7 +471,7 @@\n           },\n           {\n             from: '/docs/category/guides',\n-            to: '/docs/guides',\n+            to: '/docs/guides/',\n           },\n           {\n             from: '/docs/guides/gpt-5-vs-gpt-5-mini-mmlu',\n"}]},{"message":"Missing trailing slash on internal route. The site is configured with `trailingSlash: true` (line 34), so this should be `/docs/guides/` to avoid a 308 redirect.","fixFiles":[{"filePath":"site/docusaurus.config.ts","diff":"diff --git a/site/docusaurus.config.ts b/site/docusaurus.config.ts\n--- a/site/docusaurus.config.ts\n+++ b/site/docusaurus.config.ts\n@@ -545,7 +545,7 @@\n           // Deleted guides redirected to guides index\n           {\n             from: '/docs/guides/cohere-command-r-benchmark',\n-            to: '/docs/guides',\n+            to: '/docs/guides/',\n           },\n           {\n             from: '/docs/guides/dbrx-benchmark',\n"}]},{"message":"This MUI Link component uses `href=\"/docs/enterprise/\"` which bypasses Docusaurus's route normalization. Since the site is configured with `trailingSlash: true`, this will work correctly. However, the test in `trailingSlash.test.ts` is designed to catch exactly this pattern to ensure consistency. While the URL already has a trailing slash, using MUI's Link instead of Docusaurus's Link component means it won't benefit from automatic normalization if the path is ever changed incorrectly.","fixFiles":[{"filePath":"site/src/pages/contact.tsx","diff":"diff --git a/site/src/pages/contact.tsx b/site/src/pages/contact.tsx\n--- a/site/src/pages/contact.tsx\n+++ b/site/src/pages/contact.tsx\n@@ -10,7 +10,8 @@\n import Container from '@mui/material/Container';\n import FormControl from '@mui/material/FormControl';\n import InputLabel from '@mui/material/InputLabel';\n-import Link from '@mui/material/Link';\n+import Link as MuiLink from '@mui/material/Link';\n+import Link from '@docusaurus/Link';\n import MenuItem from '@mui/material/MenuItem';\n import Paper from '@mui/material/Paper';\n import Select from '@mui/material/Select';\n@@ -289,7 +290,7 @@\n                   Resources\n                 </Typography>\n                 <Box className={styles.resourceLinks}>\n-                  <Link\n+                  <MuiLink\n                     href=\"https://github.com/promptfoo/promptfoo\"\n                     target=\"_blank\"\n                     rel=\"noreferrer\"\n@@ -298,8 +299,8 @@\n                   >\n                     GitHub\n                     <ArrowForwardIcon className={styles.resourceLinkIcon} />\n-                  </Link>\n-                  <Link\n+                  </Mu...

</details>
