# build: migrate styled-components from Babel plugin to Next SWC compiler

## Summary
Replace the \`.babelrc\` + \`babel-plugin-styled-components\` setup with Next's built-in SWC compiler support for styled-components.

**Why:** while \`.babelrc\` exists, Next 13 disables SWC site-wide and routes every file through Babel. Removing it lets the entire app compile via SWC — the recommended path since Next 12.

The \`.babelrc\` has been present since the project's first feature commit (Annie Chi, Feb 2023) and never modified. Just legacy default from when SWC support for styled-components was still maturing.

## Changes
- Delete \`.babelrc\`
- \`next.config.js\`: add \`compiler.styledComponents: true\`
- \`package.json\`: drop the now-unused \`babel-plugin-styled-components\` devDep

## Behavior parity
- The SWC compiler enables \`displayName\` and \`ssr\` (stable class identifiers across SSR/CSR) **by default**, matching the previous Babel plugin's \`{ ssr: true }\` option.
- \`pages/_document.tsx\`'s manual \`ServerStyleSheet\` style collection is still needed and untouched.

## Expected wins
- Faster builds (no Babel pass over the whole app)
- Slightly smaller client bundle
- Build output no longer prints \`Disabled SWC as replacement for Babel because of custom Babel configuration ".babelrc"\`

## Test plan
- [x] \`npm run lint\` clean
- [x] \`npm run test\` (5 tests pass)
- [x] \`npm run build\` succeeds locally; no "Disabled SWC" warning
- [ ] Netlify deploy preview renders home, agenda, visainfo correctly — this is the real check. A class-name mismatch between SSR and CSR would produce a hydration warning in DevTools.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
