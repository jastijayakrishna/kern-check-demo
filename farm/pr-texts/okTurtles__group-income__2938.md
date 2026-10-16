# Render Global News & Updates dynamically from JSON feed

# Render Global News & Updates dynamically from JSON feed

## Summary
Implements issue #2934 to fetch news dynamically from https://groupincome.org/news.json instead of using hardcoded data. The implementation tracks the last seen news date in user preferences (identity KV store) and displays badge indicators on both the Global Dashboard logo and News & Updates menu item when new news is available.

Key changes:
- **NewsAndUpdates.vue**: Fetches news dynamically with loading/error states, marks news as seen when page is visited
- **Navigation.vue & GroupsList.vue**: Display badge when new news exists, fetch latest news date on component creation
- **misc.js**: Added `fetchNews()` utility function to avoid code duplication
- **Error handling**: Uses `errorMessage: null` instead of separate error boolean flag

## Review & Testing Checklist for Human

- [ ] **Badge behavior**: Verify badge appears on both the Global Dashboard logo (left sidebar) and News & Updates menu item when there's unread news. Badge should disappear after visiting the news page and not reappear until new news is published.
- [ ] **Edge cases**: Test first-time visit (no lastSeenNewsDate stored), empty news feed, and error states (can simulate by blocking https://groupincome.org/news.json in DevTools Network tab).
- [ ] **Multi-tab behavior**: Open multiple tabs and verify KV store conflict resolution works correctly when visiting news page in different tabs simultaneously.
- [ ] **Date comparison**: Verify the badge logic correctly compares ISO date strings - badge should only show when latest news createdAt is newer than stored lastSeenNewsDate.

### Test Plan
1. Start the app and log in
2. Check if badges appear on Global Dashboard logo and/or News menu item (depends on whether you've seen latest news)
3. Navigate to Global Dashboard → News & Updates
4. Verify badges disappear immediately on both locations
5. Refresh and confirm badges don't reappear
6. Simulate error by blocking news.json URL in DevTools → verify error message displays with actual error text
7. Open 2-3 tabs, visit news page in one tab, verify badge disappears in all tabs

### Notes
- CORS issue on groupincome.org/news.json was resolved by @taoeffect
- The `hasNewNews` computed property is duplicated in Navigation.vue and GroupsList.vue by design (per user feedback, backend caching solution will come in separate PR)
- Session: https://app.devin.ai/sessions/b9121f419c0c4b30972fff3051fb7554
- Requested by: Greg Slepak (@taoeffect)
