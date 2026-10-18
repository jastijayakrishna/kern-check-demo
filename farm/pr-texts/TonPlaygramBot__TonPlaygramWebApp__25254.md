# Fix protest video upload folder icon

### Motivation
- The developer upload control on the ProtestVideo gallery used an ambiguous upload icon and copy, making it unclear that the button should open the phone gallery/camera roll for selecting video clips.

### Description
- Replaced the upload icon with a folder-open icon and updated the helper copy in `webapp/src/pages/ProtestVideoGallery.jsx` so the button clearly indicates it opens the phone gallery.

### Testing
- Ran `npm --prefix webapp run build` which completed successfully and produced a production build.
- Ran `npm --prefix webapp run lint -- src/pages/ProtestVideoGallery.jsx` which completed successfully to validate the changed file.
- Note: an earlier lint invocation using the package-relative path failed due to an incorrect pattern, but the corrected lint run passed.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a5a632821988329aa92ab96b793f65e)
