# 1144: Implement Levenshtein distance matching in search()

Changed `tokenMatches` in `search.ts` to use a word-length-based Levenshtein threshold (2 edits for haystack words >5 chars, 1 for shorter) instead of a fixed MAX_EDIT_DIST=2. Added four acceptance-criteria tests covering 'goretex rain jckt', 'shell jckt', 'fleese', and the false-positive guard ('x' must not match shell products).
