# chore: Make npm scripts cross-platform compatible

## Summary
- Replace Unix-specific shell commands with Node.js scripts for Windows compatibility
- Created `scripts/clean.js` to replace `rm -rf` with `fs.rmSync()`
- Created `scripts/write-cjs-package.js` to replace `echo` redirect with `fs.writeFileSync()`
- Created `scripts/update-version.js` to replace macOS-specific `sed` command with Node.js file operations

## Changes
**prebuild script:**
- Before: `rm -rf dist lib types`
- After: `node scripts/clean.js`

**postbuild script:**
- Before: `echo '{"type": "commonjs"}' > lib/cjs/package.json`
- After: `node scripts/write-cjs-package.js`

**version script:**
- Before: `sed -i '' "s/VERSION = .*/VERSION = \"$npm_package_version\"/" src/amqp-base-client.ts && ...`
- After: `node scripts/update-version.js && ...`

## Benefits
- ✅ Works identically on Windows, macOS, and Linux
- ✅ No additional dependencies (uses Node.js built-in APIs)
- ✅ More maintainable and readable than shell one-liners
- ✅ Already requires Node.js ≥16, so `fs.rmSync()` is guaranteed to be available

## Test plan
- [ ] Verify `npm run prebuild` successfully removes dist/lib/types directories
- [ ] Verify `npm run build` completes successfully
- [ ] Verify `lib/cjs/package.json` is created correctly with `{"type": "commonjs"}`
- [ ] Test on Windows environment to ensure all scripts work

🤖 Generated with [Claude Code](https://claude.com/claude-code)
