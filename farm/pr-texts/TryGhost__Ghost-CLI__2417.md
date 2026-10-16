# 🐛 Skipped Ghost's in-development tables in SQLite migration exports

Follow-up to #2397, which stopped new installs from creating Ghost's in-development tables. Sites set up with an older CLI still have them in their SQLite database, so their `mysql-data` bundle fails to import:

```
Table 'ghost.app_installation_manifests' doesn't exist
```

### Changes

- `inDevelopmentTables()` reads `IN_DEVELOPMENT_TABLES` from the installed Ghost (`current/core/server/data/schema/in-development.js`) for Ghost 6.69.0+.
  - The mechanism shipped in 6.66.0, but the list was empty until 6.69.0.
  - The require runs in a child process from the install dir. Requiring it loads Ghost's nconf config, which reads the CLI's cwd and argv in-process.
- `dumpSqliteData()` takes a `skipTables` list, and the SQLite conversion step passes the lookup result to it.

MySQL sources are unchanged. mysqldump includes the schema, so extra tables load fine.

### Testing

- `pnpm test` passes. New specs cover skipping tables, the list lookup, the version cutoff and the lookup failure.
- Tested end to end against a real Ghost 6.70.0 local install with `createInDevelopmentTables` removed from config. After a boot, both tables exist in SQLite. `migrate-export` leaves them out of `database.sql`.
- Not tested: importing the bundle into ghost-docker.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
