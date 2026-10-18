# Fix cropped and empty reference gallery rows

## Summary
- group project photos by before, after, and in-progress status
- show portrait photos in full over a soft blurred backdrop instead of cropping them
- make odd single photos span the full gallery row so no empty black half remains
- keep the full-screen photo viewer working

## Validation
- npm run typecheck
- npm run lint
- npm test -- --run (29 passed)
- manually checked the gallery and full-screen viewer in the browser
