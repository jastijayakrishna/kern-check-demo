# [Fleet] Fix agent policy filter: use policy_base_id for versioned policy lookup

## Summary

Closes #281093

Follow-up to #279716 (now merged).

The agent policy dropdown filter on the agents list page used an exact KQL match on `policy_id`:

```
fleet-agents.policy_id : ("fleet-server-policy")
```

When Fleet assigns agents to version-specific policies (e.g. `fleet-server-policy#9.4`), those agents have a versioned `policy_id` and do not match the exact filter — resulting in 0 agents shown.

**Fix:** use `buildPolicyBaseIdsWithFallbackKuery` so the generated KQL queries the denormalized `policy_base_id` field (term query, no prefix) for migrated agents, with an exact `policy_id` fallback for agents enrolled before the backfill ran:

```
(fleet-agents.policy_base_id:(fleet-server-policy) or (fleet-agents.policy_id:(fleet-server-policy) and not fleet-agents.policy_base_id:*))
```

This is compatible with `search.allow_expensive_queries: false` (no prefix/wildcard). Also adds `policy_base_id` to `AGENT_MAPPINGS` so the KQL route validator accepts the field.

Also adds `buildPolicyBaseIdsWithFallbackKuery` (multi-id KQL variant, counterpart of the already-merged `buildPolicyBaseIdsWithFallbackEsFilter`).

## Test plan

**Pre-requisites**
- Local Kibana + Elasticsearch + Fleet Server running with at least one enrolled agent
- Enable the version-specific policy assignment feature in `kibana.yml`:
  ```yaml
  xpack.fleet.enableExperimental:
    - versionSpecificAgentPolicies
  ```

**Setup: put an agent onto a versioned policy_id**

Either wait for the `fleet:version-specific-policy-assignment-task` to run after agent check-in, or manually update one agent doc in Elasticsearch:

```
POST .fleet-agents/_update/<agent-id>
{
  "doc": {
    "policy_id": "fleet-server-policy#9.4",
    "policy_base_id": "fleet-server-policy"
  }
}
```

**Reproduce the bug (on `main` before fix)**
1. Go to **Fleet → Agents**
2. Open the **Agent policy** dropdown filter
3. Select the policy the agent is enrolled in (e.g. `fleet-server-policy`)
4. Agent count shows 0 — the agent on `fleet-server-policy#9.4` is missed

**Verify the fix (on PR branch)**
1. Same steps — agent with `policy_id: fleet-server-policy#9.4` now appears in the filtered list
2. In browser DevTools → Network, find the `/api/fleet/agents` request and confirm the `kuery` param contains `fleet-agents.policy_base_id:(fleet-server-policy)`
3. Deselect filter → all agents visible again
4. Select a different policy → only agents on that policy are shown
5. Test with an agent that has only `policy_id` set (no `policy_base_id`) — agent still appears via the fallback branch

**Unit tests**
- [x] `get_kuery.test.ts` passes: `selectedAgentPolicies` filter now asserts `policy_base_id` fallback kuery

🤖 Generated with [Claude Code](https://claude.ai/claude-code)

<img width="1585" height="482" alt="image" src="https://github.com/user-attachments/assets/e96c89de-0245-46aa-ba94-182e42b451f1" />
<img width="1589" height="544" alt="image" src="https://github.com/user-attachments/assets/9ac2e418-a984-416a-b931-bfa94498e80a" />

Verified again after the `policy_base_id` changes:
<img width="1784" height="557" alt="image" src="https://github.com/user-attachments/assets/1eca16ba-22a3-41cf-82c4-6217f74b4320" />



<!--ONMERGE {"backportTargets":["9.4","9.5"]} ONMERGE-->
