# fix(fleet): move add_integration_to_policy route from Fleet to Integrations app

## Summary

Fixes #279108. The `CreatePackagePolicyPage` ("Add integration" form) was routed through the Fleet app even when the user arrived from the Integrations app. This caused two visible bugs with a [TODO comment dating back to 2021 (#101828)](https://github.com/elastic/kibana/pull/101828).

**Before:** Clicking "Add integration" from `/app/integrations/...` triggered `navigateToApp('fleet', ...)`, loading the Fleet app shell and producing a layout flash. URL was `/app/fleet/integrations/:pkgkey/add-integration`. Left sidebar highlighted Fleet.

**After:** URL is `/app/integrations/detail/:pkgkey/add-integration`. No app switch, no flash, sidebar highlights Integrations.

## Changes

- Add `add_integration_to_policy` to `INTEGRATIONS_ROUTING_PATHS` (`/detail/:pkgkey/add-integration/:integration?`)
- Register the route in `EPMApp` (`integrations/sections/epm/index.tsx`) before the `integration_details` catch-all
- Remove the route (and TODO comment) from `fleet/app.tsx`
- Update `pagePathGetters.add_integration_to_policy` to use `INTEGRATIONS_BASE_PATH` and the new path
- Fix `getInstallPkgRouteOptions` to return `INTEGRATIONS_PLUGIN_ID` instead of `PLUGIN_ID`
- Update affected unit tests
- Add scout tests verifying URL stays in `/app/integrations/` after clicking "Add integration"

## Manual verification steps

**1. No layout flash**
1. Go to `/app/integrations`
2. Open any integration detail page (e.g. nginx)
3. Click "Add nginx" — watch for Fleet shell flashing before the form renders. Should be gone.

**2. URL stays in Integrations app**
1. Same flow as above
2. URL after clicking "Add nginx" should be `/app/integrations/detail/nginx-<version>/add-integration`
3. Old (broken) URL was `/app/fleet/integrations/nginx-<version>/add-integration`

**3. Left nav highlights Integrations, not Fleet**
1. On the add integration form, check the left sidebar
2. "Integrations" item should be highlighted/active, not "Fleet"

**4. Breadcrumb**
1. On the add integration form, breadcrumb should read `Integrations > nginx > Add integration`
2. Verify no breadcrumb flicker from Fleet context

**5. Cancel returns to Integrations**
1. Open the add integration form
2. Click Cancel — should return to the integration detail overview within `/app/integrations/...`

**6. Save (no agentPolicyId) navigates to Integrations policies tab**
1. Fill out the form, save
2. Should navigate to `/app/integrations/detail/<pkgkey>/policies`

**7. Save (with agentPolicyId) navigates to Fleet policy details**
1. Navigate to an agent policy, click "Add integration"
2. Fill out the form, save
3. Should navigate to `/app/fleet/policies/<id>` — this redirect to Fleet is intentional

**8. Old Fleet route no longer serves the form**
1. Navigate directly to `/app/fleet/integrations/nginx-1.3.0/add-integration`
2. Should redirect to the Fleet default page (agents/policies), not show the form

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<img width="1584" height="1327" alt="image" src="https://github.com/user-attachments/assets/d6e05faa-1f70-44d4-8afd-e1cf83d556cf" />
<img width="1585" height="1335" alt="image" src="https://github.com/user-attachments/assets/1120a5e7-f006-47a5-8dd9-2978c5c9e597" />

https://github.com/user-attachments/assets/aa5011a7-40e7-4edc-895e-3f95b84bbb46

https://github.com/user-attachments/assets/268e4146-e925-48d4-b0cf-68f2b3f42425



<!--ONMERGE {"backportTargets":["9.5"]} ONMERGE-->
