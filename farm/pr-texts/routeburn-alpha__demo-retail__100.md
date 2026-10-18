# 1137: Implement token expansion with alias map in search

Added ALIAS_MAP and exportable expandTokens() to search.ts; modified search() to expand tokens before filtering (using some instead of every). Added a 'rain jacket' product to catalog.json to exercise the new alias expansion in tests.
