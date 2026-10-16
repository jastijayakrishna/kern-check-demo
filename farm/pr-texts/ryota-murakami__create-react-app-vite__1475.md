# Enable MSW in production builds

# Enable MSW in production builds

Resolves #1473

## Changes
- Modified `src/main.tsx` to enable MSW in both development and production environments
- Removed the conditional logic that previously only enabled MSW in development
- Simplified the code by using a single import and initialization flow

## Testing
- Verified all tests pass with the changes
- Ran linting and type checking to ensure code quality

This change allows the app to work with mock API responses in production builds, making it easier to prototype and deploy applications with fetch logic to services like Vercel.

Link to Devin run: https://app.devin.ai/sessions/0e6e2c2a51884ff69ff5084335019240
Requested by: Ryota Murakami
