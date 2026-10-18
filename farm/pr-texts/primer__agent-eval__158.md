# feat: snapshot session UI in run artifacts

Capture the final UI at a 1440 × 900 laptop viewport and expose the snapshot in run details.

### Changes

- **Capture**
  - Start the scenario’s development server after the agent session.
  - Save `ui-snapshot.png` in the treatment workspace artifact.
  - Skip capture gracefully when no development server is available.

- **Output**
  - Add optional `screenshotPath` metadata.
  - Preserve compatibility with existing run output.

- **Run UI**
  - Load artifact screenshots securely.
  - Display snapshots alongside tests and transcripts.
  - Show an empty state for runs without snapshots.
