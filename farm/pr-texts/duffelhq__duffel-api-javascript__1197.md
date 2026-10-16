# TSP-1694: add Order content type

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary
- add the missing `content` attribute to the `Order` interface
- model its documented values as `managed | self_managed`
- update typed Order fixtures to cover both values

## Testing
- `corepack yarn test src/booking/Orders/Orders.spec.ts`
- `corepack yarn build:test`
- `corepack yarn eslint src/booking/Orders/OrdersTypes.ts src/booking/Orders/mockOrders.ts`
<!-- CURSOR_AGENT_PR_BODY_END -->

[Slack Thread](https://duffel.slack.com/archives/C05GANU3TB6/p1785421286484479?thread_ts=1785421286.484479&cid=C05GANU3TB6)

<div><a href="https://cursor.com/agents/bc-f72f8808-f1f8-51a9-aaa0-5453cd79e1a9?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-f72f8808-f1f8-51a9-aaa0-5453cd79e1a9&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
