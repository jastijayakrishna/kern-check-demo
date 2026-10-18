# Resolve legacy Flamingo media by original name/size and normalize historic media URLs

### Motivation

- Ensure historical wall posts remain playable when an upload was retried and the UUID changed by matching legacy records using the original filename and byte size. 
- Route older absolute/legacy attachment URLs through the active API host so media published with previous hostnames continue to work after deployments.

### Description

- Extend storage APIs to accept `originalName` and `size` and update `findFlamingoDatabaseMedia` to search by `filename` or `metadata.originalName` and optionally match `length` when a safe size is provided. 
- Enhance `findFlamingoMedia` to, in addition to checking exact file UUIDs on disk, scan directories for files whose name encodes the original filename and whose file size matches the expected size to recover retried uploads. 
- Propagate `attachment.name` and `attachment.size` through the Flamingo routes, include them in download grants, and pass them to the updated storage lookup helpers. 
- Add `resolveWallMediaUrl` utility to normalize stored attachment URLs to the current `API_BASE_URL`, and use it from `MediaWall` and `Home` so relative, absolute legacy, and external sources are handled correctly. 
- Add and update unit tests: new `flamingoMediaUrl.test.js` for URL resolution and extend `flamingoStorage.test.js` with a case that verifies recovering a missing historical UUID from an identical retried upload.

### Testing

- Ran the project test suite (unit tests) which includes the added `flamingoMediaUrl.test.js` and the updated `flamingoStorage.test.js` and all tests passed. 
- Exercised the updated storage functions through the new unit case that simulates a retried upload and verified the alias recovery succeeds for matching size and fails when size differs. 
- Verified that the media URL normalization tests cover relative paths, legacy absolute API hosts, and external/blob URLs and they all passed.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a955b35e34883299e5667c16d2c68d6)
