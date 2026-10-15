import { execSync } from 'node:child_process';

// The shop's version for its footer, from the newest git tag.
export function version() {
  try {
    return execSync('git describe --tags --always').toString().trim();
  } catch {
    return 'dev';
  }
}
