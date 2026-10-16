# Automated deploys choose Production's region, and the dashboard opens that Production directly

## **User description**
<!-- claude-projects-attribution: {"github_login":"Phicks-debug"} -->
_Requested by **Phicks** · [project thread](https://claude.ai/code/project/chan_01HLRQQhPNaoSL4Le5CjrAKG?thread=cmsg_01HLRQQhPNaoSL4Le5CjrAKGPwniHAwvUShWBZKWjGLhWt)_

Before: a project that automation (the CLI, the SDK, CI or an AI agent) created and deployed to production could not choose Production's region, which matters for GDPR. Its Production stage had no region. The dashboard read "no region" as "Production not set up", so switching to Production always showed the first-time "Initialize Production / Deployment region" page.

After: `broods deploy --region <region>`, or `region` on the manifest passed to `BroodsSyncClient.putManifest`, chooses Production's region. The first deploy that syncs its manifest pins it. With no region named it pins `eu-west-1`, the only live region. A later deploy naming another region gets 409, so data does not move. A region that is not live yet, or an empty one, is refused. An unknown region is a 400. In the dashboard, an existing Production stage opens directly. The Initialize Production page appears only while the project has no Production stage, and it offers only live regions.

How:
- `packages/convex`
  - `cli/types.ts` holds the region lists: `DEPLOYMENT_REGIONS`, plus `LIVE_DEPLOYMENT_REGIONS`, which a deploy, Initialize Production and the dashboard picker all check.
  - `deploymentRegionToPin` in `model/cliSync.ts`: `ensureScopeBySecretHash` refuses a move or a region that is not live before any upload, and `syncManifestBySecretHash` writes the pin, so a deploy refused earlier pins nothing.
  - `ensureStage` returns the row as stored.
  - `initializeProduction` keeps a region a deploy already pinned.
  - Codegen committed.
- `packages/broods`
  - `deploy --region`, validated locally, including an empty value.
  - `CliManifest.region` and `DeploymentRegion` are exported for SDK users.
  - `init`/`dev` offer only live regions.
  - `BROODS_REGION` is deliberately not read, because `init` writes it as a default.
- `apps/dashboard`
  - `StageSelector` selects any stage on click.
  - The setup dialog closes for good if Production appears while it is open.
- Docs: `reference/cli.md` has a new "Production region" section, and `quickstart.md` covers the pin.

Tests:
- `packages/convex/tests/cliProductionRegion.test.ts` (10 cases):
  - the region is pinned, and defaults to `eu-west-1`
  - a deploy can't move it, and a region that is not live is refused
  - only Production takes a region
  - a refused deploy pins nothing
  - a legacy `production` stage stored as custom is fixed and pinned
  - the dashboard and a deploy each hold the other's region
  - Initialize Production refuses a region that is not live
- `packages/broods/tests/cli-deploy.test.ts`: `--region` rides the manifest and `BROODS_REGION` does not. An unknown or empty `--region` fails before any request.
- `scripts/local-verify/cases/production-region.ts`: end to end through the edge. It covers the pin, a 409 on a move, a 400 on an unknown region, and a later deploy keeping the pin.
- `apps/dashboard/e2e/app/automatedProduction.spec.ts`: a Production stage a deploy created opens without the setup dialog (fails on dev, passes here). A project without Production still gets the dialog, with only live regions enabled.

Checks on the final head: root `bun run check`, `format:check`, convex 812/812, broods 325/325, dashboard unit 257/257, `local:verify` and dashboard `app` 20/20 on the local stack, dashboard perf within budget, and `local:perf` Convex calls per turn equal to budget. Evidence (screenshots in light and dark, recordings, perf): https://claude.ai/artifact/DGGk1fW2CMDqJXCjuLidDZ

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_013pYzidbwEp1G9qWJMev57B


___

## **CodeAnt-AI Description**
**Pin Production's region on first deploy and open automated Production stages directly**

### What Changed
- `broods deploy --region` and SDK deploys can choose Production's region. The first deploy pins it, defaulting to `eu-west-1`; later deploys cannot move it, and unavailable regions are rejected.
- The dashboard opens an existing Production stage directly, including one created by an automated deploy. The setup dialog appears only when no Production stage exists and closes if a deploy creates one while it is open.

### Impact
`✅ Production stays in its chosen region`
`✅ Direct dashboard access to automated Production stages`
`✅ Invalid region choices rejected before deployment`
<details><summary><strong>💡 Usage Guide</strong></summary>

### Checking Your Pull Request
Every time you make a pull request, our system automatically looks through it. We check for security issues, mistakes in how you're setting up your infrastructure, and common code problems. We do this to make sure your changes are solid and won't cause any trouble later.

### Talking to CodeAnt AI
Got a question or need a hand with something in your pull request? You can easily get in touch with CodeAnt AI right here. Just type the following in a comment on your pull request, and replace "Your question here" with whatever you want to ask:
<pre>
<code>@codeant-ai ask: Your question here</code>
</pre>
This lets you have a chat with CodeAnt AI about your pull request, making it easier to understand and improve your code.

#### Example
<pre>
<code>@codeant-ai ask: Can you suggest a safer alternative to storing this secret?</code>
</pre>

### Preserve Org Learnings with CodeAnt
You can record team preferences so CodeAnt AI applies them in future reviews. Reply directly to the specific CodeAnt AI suggestion (in the same thread) and replace "Your feedback here" with your input:
<pre>
<code>@codeant-ai: Your feedback here</code>
</pre>
This helps CodeAnt AI learn and adapt to your team's coding style and standards.

#### Example
<pre>
<code>@codeant-ai: Do not flag unused imports.</code>
</pre>

### Retrigger review
Ask CodeAnt AI to review the PR again, by typing:
<pre>
<code>@codeant-ai: review</code>
</pre>

### Check Your Repository Health
To analyze the health of your code repository, visit our dashboard at [https://app.codeant.ai](https://app.codeant.ai). This tool helps you identify potential issues and areas for improvement in your codebase, ensuring your repository maintains high standards of code health.

</details>


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **New Features**
  * Production deployments now default to Europe (Ireland) when no region is specified. Use `--region` to select an available region on the first Production deploy; the region is then pinned and cannot be changed.
  * The dashboard enables only currently available regions during Production setup and opens an existing Production stage directly from the stage menu.
* **Bug Fixes**
  * Invalid regions and attempts to change a pinned Production region are rejected before deployment uploads begin.
* **Documentation**
  * Updated the quickstart and CLI reference with Production region selection and pinning details.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->
