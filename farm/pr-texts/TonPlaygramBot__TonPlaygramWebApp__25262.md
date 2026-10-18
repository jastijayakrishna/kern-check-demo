# Fix Render deployment port timeout

### Motivation

- Render deployments were failing with a port timeout because `bot/server.js` performed a synchronous `npm install` / Vite build of the `webapp` during startup and blocked before binding to the assigned port. 
- Production services must rely on the platform's install/build phase to produce `webapp/dist` so `npm start` can open the port quickly. 
- Keep on-demand client build behavior for local development but avoid blocking builds in production.

### Description

- Add a root-level `postinstall` script in `package.json` to install and build the `webapp` during repository install and add a `build:webapp` helper script. 
- Remove the blocking `prestart` build and stop running the webapp install/build from the server in production by having `ensureWebappBuilt()` return `false` (and log an error) when `NODE_ENV === 'production'`. 
- Stop invoking `ensureWebappBuilt()` synchronously during startup so the server can bind to the port even if `webapp/dist` is missing and can return a `503` for missing builds instead of blocking. 
- Preserve the existing on-demand build fallback for non-production environments so local development still auto-builds the client when needed.

### Testing

- Successfully ran `npm run build` and `npm run build:webapp` to produce the frontend `dist`. 
- Executed `npm test -- --runInBand test/apiGoogleHeaderFallback.test.js` and the test passed. 
- Performed a production-mode smoke test with `NODE_ENV=production` and `webapp/dist` temporarily absent and confirmed the server bound to the assigned port and returned `503` rather than blocking startup. 
- Verified with `curl` that the server responds quickly with `Webapp build not available` when the client build is absent, confirming the Render timeout is avoided.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a706a1de0448329920b957307af5d25)
