# feat: support Node.js 26

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
<!--
PRs prefixed with `chore:` will skip creating a changelog entry and release.
PRs prefixed with `fix:` will do a patch release.
PRs prefixed with `feat:` will do a minor release.
-->

## Summary
- Add Node.js 26 to the CI test matrix
- Update npm package manager metadata and Node typings
- Bump Node 26-sensitive integration dependencies and refresh affected fixtures
- Skip Node 26-incompatible Datadog/PhantomJS fixtures via `skipOnNode26AndAbove`
- Keep `phantomjs-prebuilt` as a real devDependency and fixture for Node 20/22/24 coverage
- Use a Node script in CI to remove `phantomjs-prebuilt` from the Node 26 install manifest, since the PhantomJS fixture is skipped on Node 26 and its unsupported installer blocks Windows/macOS installs

## Coverage comparison
- With `phantomjs-prebuilt`: lines 91.03%, functions 96.36%, branches 88.31%
- After removing `phantomjs-prebuilt`: tests pass, but functions drop to 95.75%
- Kept the fixture because it covers a unique source path

## Testing
- `npx npm@11.14.1 install`
- `npx npm@11.14.1 run build`
- `npx npm@11.14.1 run prettier-check`
- `npx jest --verbose test/unit.test.js -t "phantomjs-prebuilt|datadog-pprof-node-gyp"`
- `npx -y -p node@20 -c 'node -v && node node_modules/typescript/bin/tsc --sourceMap && node node_modules/jest/bin/jest.js --verbose test/unit.test.js -t "phantomjs-prebuilt|module-sync-condition-es-node20|module-sync-condition-cjs-node20"'`
- `npx npm@11.14.1 run test-verbose`
- `npx -y -p node@26 -c 'node node_modules/typescript/bin/tsc --sourceMap && node node_modules/jest/bin/jest.js --verbose --coverage --globals "{\"coverage\":true}"'`
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-6803f787-e3d6-467b-921c-f205be885409"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-6803f787-e3d6-467b-921c-f205be885409"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
