# Enhance Raspberry Pi support in Docker setup and API (Codex)

Updated docker-compose.yml to include environment variables for Node.js heap size and PostgreSQL connection pool size, optimizing performance on Raspberry Pi Zero 2 W. Added documentation in README.md to clarify the resource constraints for small Raspberry Pi boards. Improved API pairing process by introducing a claimId for retrying claims, allowing clients to recover from timeouts without invalidating the pairing code. Updated relevant code in the PairingService to handle claimId and ensure consistent responses.
