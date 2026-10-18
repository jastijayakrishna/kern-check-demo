# Remove community notice from Home page

### Motivation
- The temporary Albanian community pause banner and its static content were removed from the Home page to follow the request to stop showing the "Njoftim për komunitetin" notice.

### Description
- Deleted the `ALBANIA_PAUSE_NOTICE` constant and removed the banner/notice markup from `webapp/src/pages/Home.jsx` so the home page now begins directly with the profile/account section.

### Testing
- Ran `npm run lint -- src/pages/Home.jsx` and it completed successfully.
- Ran the production build with `npm run build` and the build succeeded.
- Verified in a 390×844 portrait browser viewport that the notice text ("Njoftim për komunitetin") is no longer present.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a70774dc5c4832982e038a428710051)
