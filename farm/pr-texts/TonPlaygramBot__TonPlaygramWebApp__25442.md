# Support browser account messaging + notifications; fix send/receive flow

### Motivation
- Make the Social Hub work for users who sign in via browser/Google (not only Telegram) so conversations and friend flows are accessible. 
- Prevent the UI from becoming unresponsive/black after sending a message and give clear feedback on failures. 
- Provide timely user-facing notifications for new messages and friend requests (in-app and browser notifications). 

### Description
- Persist and route mixed identity types by allowing string account IDs or numeric Telegram IDs in the models: `Message.from/to` and `FriendRequest.from/to` are now `mongoose.Schema.Types.Mixed` and `User.friends` accepts mixed ids. 
- Resolve identities server-side with `findSocialUser` + `userIdentity`/`userIdentityFilter` helpers and update social endpoints to accept either Telegram ids or account ids, emit `privateMessage` via Socket.IO to recipient sockets, and send Telegram pushes only when a Telegram id exists. 
- Update the web client `Messages.jsx` to use a `socialId` (Telegram id or browser `accountId`), load conversations for that identity, handle incoming `privateMessage` correctly across string/number ids, and add guarded send flow with `isSending`, optimistic update protection, and visible error messages. 
- Add client-side notification UX in `Layout.jsx` for incoming private messages and friend requests using the Notification API and an in-app tappable banner, and register the socket identity on the client when available. 
- Minor styling update in `messages.css` for error/toast states. 

### Testing
- Checked server-side files with `node --check` for modified modules and they passed (no syntax errors). 
- Built the webapp with `npm --prefix webapp run build` and the production build completed successfully. 
- Ran lint on changed client files (`eslint`), which completed without blocking errors. 
- Ran the existing unit test `test/socialSearchFilterSelf.test.js` with `jest` and it passed. 
- Started dev server (`npm --prefix webapp run dev`) and exercised messaging flows during build/dev; attempted a Playwright portrait screenshot to validate mobile UI but Chromium failed to start in this environment due to missing native libraries (`libatk-1.0.so.0`), unrelated to the feature changes.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a918438fccc832980a45cf124083d5b)
