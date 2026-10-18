# Protect wall videos from temporary storage and restore missing originals

The September 7 “Dita e 99” post is still present, but a range request for its original `23117.mp4` returns HTTP 404. The live health response reported roughly 415 GB of filesystem capacity while the Blueprint declares a 10 GB persistent disk. That suggests a different filesystem is in use; the live Render mount has not been verified. The earlier August 30 cleanup does not target this post.

This change:

- Defaults Render uploads to the persistent mount and verifies the canonical upload directory against Linux mount information. New media is refused with `WALL_STORAGE_NOT_DURABLE` when a persistent disk cannot be verified and GridFS backup is disabled. Health exposes the same condition. Text articles remain available.
- Stops automatically deleting existing GridFS backups when publishing disk-only uploads. HTTP uploads and Telegram imports use the same guarded destination.
- Adds a media-status response and an author-only **Restore video / Restore original** flow. It resumes original-file uploads and updates the existing attachment while retaining the post ID, caption, date, author and engagement keys. It rejects other owners and different file sizes.
- Retries incomplete restoration after a database failure without duplicating the post or treating a staged filename alias as a completed backup. Existing ownership tokens remain required.
- Redacts credential-bearing Telegram avatar URLs from public wall responses and strips ownership hashes from publication responses. Previously exposed credentials still need rotation; this does not revoke them or repair other profile services.

Validation: 63 tests passed across 13 media/upload suites, including real HTTP streams, byte ranges, resume, ownership, interrupted restoration and router restart with persisted files. The post database is mocked in those route tests. Focused TypeScript checking and the isolated preview build passed. The Cloud Browser blocked local preview URLs, so visual verification could not be completed.

Production follow-through is required before calling the incident resolved: verify the actual Render persistent disk/environment, deploy, recover the original from an existing server backup or use Restore video with the original file, and confirm playback/seek after an API restart. This PR cannot reconstruct missing video bytes or provision an existing Render service's disk. It is a draft pending those deployment checks. See `docs/social-wall-storage-recovery.md` for the exact settings and recovery steps.
