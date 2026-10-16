# Add Memory Soundtrack blog post

# Add Memory Soundtrack blog post

## Summary
Added a new blog post titled "Ultimate Guide to the Memory Soundtrack (2025 Edition)" to the eveokee web app. The post includes comprehensive content about the Memory Soundtrack film score, covering composer background, track-by-track analysis, thematic analysis, listening recommendations, and FAQs.

**Changes:**
- Created new markdown file at `apps/web/src/content/blog/memory-soundtrack.md` with full blog content
- Updated `apps/web/src/lib/blog-service.ts` to import and include the new blog post in the posts array
- Blog post configured with slug `memory-soundtrack`, 15 min read time, and appropriate tags (music, soundtrack, film, memory, guide)
- Fixed CI type-check failures by reverting pnpm-lock.yaml changes (the lockfile version mismatch was causing unrelated type errors in mobile package)

## Review & Testing Checklist for Human
- [ ] **Navigate to `/blog/memory-soundtrack` and verify the blog post renders correctly** - This is the most critical check. Ensure all sections display properly, markdown formatting is correct, images load, and there are no rendering issues.
- [ ] **Verify the blog post appears in the blog listing** - Go to `/blog` and confirm the Memory Soundtrack post shows up as the first/newest post with correct metadata (title, excerpt, tags, read time, author, date).
- [ ] **Test embedded content and external links** - Check that the YouTube video embed works and all external links (Roger Ebert review, Film Music Reporter, Rupert Parkes website, Spotify, etc.) are functional.

### Test Plan
1. Visit the preview deployment: https://eveokee-monorepo-web-git-devin-17-737efd-sams-projects-5004ee76.vercel.app/blog
2. Verify the Memory Soundtrack post appears at the top of the list
3. Click through to the full post at `/blog/memory-soundtrack`
4. Scroll through the entire post checking formatting, images, and links
5. Test the YouTube embed plays correctly
6. Click a few external links to verify they work
7. Check mobile responsiveness

### Notes
- The blog post content was provided by the user and formatted according to the existing blog post structure
- The post is dated 2025-11-12 and will appear as the most recent post
- All images are hosted on Supabase storage (user-provided URLs)
- The meta description requested by the user is set as the "excerpt" field - please verify this is what's used for SEO tags in the BlogPost component
- CI initially failed due to pnpm-lock.yaml version mismatch causing unrelated type errors in the mobile package; this was fixed by reverting the lockfile to match main

**Link to Devin run:** https://app.devin.ai/sessions/c0c38bd3143d46ef87c486b08a74e7a7  
**Requested by:** Sam He (@NanHeSam, sam@eveoky.com)
