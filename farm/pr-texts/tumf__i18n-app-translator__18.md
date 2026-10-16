# Add integration tests with chroma and openrouter

# Add integration tests with chroma and openrouter

This PR adds integration tests using chroma (local file db) and openrouter. The tests are configured to be skipped in CI environments and can be run locally using dotenvx with the .env.devin file.

## Changes
- Added integration test file using chroma and openrouter
- Added integration script to package.json
- Updated CI workflow to skip integration tests
- Added chroma-db directory to .gitignore

## Testing
Integration tests can be run locally using:
```bash
dotenvx run -f .env.devin -- npm run integration
```

Link to Devin run: https://app.devin.ai/sessions/ef49dbd8b2b4432e9dbaa2786dab7125
Requested by: tumf (y.takahara@gmail.com)
