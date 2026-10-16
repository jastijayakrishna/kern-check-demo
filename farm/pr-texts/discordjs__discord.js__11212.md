# fix(GuildMemberFlagsBitField): Remove duplicate "guild" word

Typo in JSDoc comment: "Numeric guild guild member flags" contained duplicate "guild" word.

## Changes
- Fixed line 14 in `GuildMemberFlagsBitField.js`: "Numeric guild guild member flags." → "Numeric guild member flags."

Now consistent with other BitField classes (ActivityFlagsBitField, ApplicationFlagsBitField, ChannelFlagsBitField, etc.).

> [!WARNING]
>
> <details>
> <summary>Firewall rules blocked me from connecting to one or more addresses (expand for details)</summary>
>
> #### I tried to connect to the following addresses, but was blocked by firewall rules:
>
> - `downloads.rclone.org`
>   - Triggering command: `node bin/rclone.js selfupdate` (dns block)
>
> If you need me to access, download, or install something from one of these locations, you can either:
>
> - Configure [Actions setup steps](https://gh.io/copilot/actions-setup-steps) to set up my environment, which run before the firewall is enabled
> - Add the appropriate URLs or hosts to the custom allowlist in this repository's [Copilot coding agent settings](https://github.com/discordjs/discord.js/settings/copilot/coding_agent) (admins only)
>
> </details>

<!-- START COPILOT CODING AGENT SUFFIX -->



<details>

<summary>Original prompt</summary>

> 
> ----
> 
> *This section details on the original issue you should resolve*
> 
> <issue_title>Duplicate "guild" word in guild member flags bit field documentation</issue_title>
> <issue_description>As seen here:
> 
> https://github.com/discordjs/discord.js/blob/56662ebad7b80ea3f474bf20562cc14fa87e6483/packages/discord.js/src/util/GuildMemberFlagsBitField.js#L14
> 
> There is a duplicate "guild" word. It should not be there!</issue_description>
> 
> ## Comments on the Issue (you are @copilot in this section)
> 
> <comments>
> </comments>
> 


</details>

- Fixes discordjs/discord.js#11211

<!-- START COPILOT CODING AGENT TIPS -->
---

💬 We'd love your input! Share your thoughts on Copilot coding agent in our [2 minute survey](https://gh.io/copilot-coding-agent-survey).
