# Actually write the coordinator's path, and stop claiming Zigbee works…

… when it doesn't

A Zero 2 W with a SONOFF dongle installed cleanly, identified the stick, handed it the board, turned Matter off, started Zigbee2MQTT — and sat at `zigbee.connected: false`. The hub could talk to nothing but MQTT. The whole install left one line of evidence:

    chmod: cannot access '/etc/gethome/zigbee.env': No such file or directory

zigbee-detect.sh wrote the override as

    { … ; [[ -n "$PINNED" ]] && echo "GETHOME_ZIGBEE_PINNED=$PINNED" ; } \
      > "$ENV_FILE.tmp" && mv "$ENV_FILE.tmp" "$ENV_FILE"

A group's exit status is its last command's. With nothing pinned — every install that doesn't pass --zigbee, i.e. the normal one — that test is false, the group returns 1, and the `mv` never runs. A perfect config sat in zigbee.env.tmp; the real file was never created. Z2M's `EnvironmentFile=-` is optional by design, so it started happily with no serial port and never reached the radio.

Write the pinned line with `if`, and treat a failed write as a failure: say so and exit non-zero instead of leaving a chmod error to be noticed.

The test suite could not have caught this. It staged a coordinator by pinning one, and pinning is the single path the broken code got right. So the scan root is now overridable (GETHOME_ZIGBEE_SCAN_DIR) and the tests stage a device the way one actually arrives; four new cases cover the write, including that no temp file is left behind. Reverting the fix fails them. It also makes the suite hermetic — it no longer reads the host's /dev/serial/by-id.

Two more things the same install log showed:

- `@@CAPABILITIES:Zigbee, …@@` was emitted because the *detector* succeeded, which only means a device node was found and a unit started. The installer now polls the hub's own `zigbee.connected` for a minute and warns, dropping Zigbee from the list, if it never comes up. The board-level narrative keeps reading ZIGBEE_CONFIGURED, so a hub whose radio isn't talking yet is not told it has no stick.

- systemd printed "Unknown key 'StartLimitIntervalSec' in section [Service], ignoring" eight times: those keys moved to [Unit] in v230, so the hub's restart rate limit was never in force. Moved in both units and pinned by a test.

The final status line now re-reads GET /hub instead of reprinting the copy taken at the health check, which predated the radio decision and ended the install claiming "matter":true directly under a line saying Matter is off.


Claude-Session: https://claude.ai/code/session_016cwgr3qEHcB6uWg19nTmc8
