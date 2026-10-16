# Exclude instance from "start all" function

This PR implements the feature requested in [#451](https://github.com/clusterio/clusterio/issues/451), allowing users to exclude specific instances from being started by the "Start all" button in the web interface. Previously, the "Start all" button would attempt to start all stopped instances. This change introduces a new configuration field `instance.exclude_from_start_all` which, when set to `true`, will cause the "Start all" operation to skip that instance. The field is exposed in the instance configuration UI and documented.

```
## Changelog
### Features
- Added ability to exclude instances from the 'Start all' web UI button. [#451](https://github.com/clusterio/clusterio/issues/451)
```

---

**Open Background Agent:** 
[Web](https://www.cursor.com/agents?id=bc-bc30acf1-4c3e-4bd2-928a-efc910587faa) · [Cursor](https://cursor.com/background-agent?bcId=bc-bc30acf1-4c3e-4bd2-928a-efc910587faa)

Learn more about [Background Agents](https://docs.cursor.com/background-agent/web-and-mobile)
