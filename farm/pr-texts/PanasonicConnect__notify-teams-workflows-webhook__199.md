# 変更ファイル一覧をフェンス付きコードブロック形式で表示する

## Summary

Teams の Adaptive Card に表示される変更ファイル一覧（`{CHANGED_FILES}`）を、ファイルごとのインラインコード（`` `file` ``）から、全体を囲むフェンス付きコードブロック形式に変更しました。

- `generateChangedFilesString`（src/contents.js）を修正し、非リンクのファイルをバッククートなしのプレーンテキストで `\n` 連結し、全体を ```` ``` ```` フェンスで囲む形式に変更
  - 例: `['file1', 'file2']` → ```` ```\nfile1\nfile2\n``` ````
  - `max` 超過時の `'...'` はコードブロック内の最終行として出力
- mkdocs リンクが生成されるファイルが表示対象に1件でもある場合は、リンクを機能させるため従来のインラインコード/リンク形式（`[`file`](url)`、`` `file` `` を `separator` 連結、フェンスなし）にフォールバック
- 呼び出し側 `replaceBodyParameters` の separator `'\n\n'` はそのままに、コードブロック内の区切りは改行1つとするよう関数内で調整（`makeIssueBody` への影響なし）
- `__tests__/contents.test.js` / `__tests__/main.test.js` を新形式に更新し、「mkdocs 設定があるがリンク対象ファイルがない場合はコードブロックになる」ケースを追加
- `README.md` / `README-en.md` の `{CHANGED_FILES}` 説明にコードブロック形式である旨を反映

Link to Devin session: https://app.devin.ai/sessions/7dda088b88db478889744e4622ff5bd7
Open in Devin Desktop: https://app.devin.ai/desktop/session/7dda088b88db478889744e4622ff5bd7?variant=devin
Requested by: @dev-mochizuki-kohei
