# fix: add support for double slash SQL comments

Closes: #12920 

This PR adds support for '//' single-line comments in SQL queries.

Changes:
- Added regex pattern to handle '//' comments in queryBuilder.removeComments
- Added test cases to verify '//' comment handling with:
  - Mixed comment styles (// and --)
  - Comments containing division operations
  - Complex scenarios with multiple comment types
- Improved whitespace handling in comment removal

Testing:
 All unit tests pass (284 tests)
 Manual verification of comment removal functionality
 Linting and formatting checks pass

Note: Current CI failures are infrastructure-related:
1. Missing 'lz4' module in Databricks SQL client (unrelated to comment handling)
2. Render environment not ready (infrastructure issue)

Link to Devin run: https://app.devin.ai/sessions/5a0fd4dc1a8b4dd3b47cdb6e65f335fe

test-frontend
