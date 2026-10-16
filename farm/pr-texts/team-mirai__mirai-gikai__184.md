# 議案詳細ページにTwitterカード用メタデータを追加

# 議案詳細ページにTwitterカード用メタデータを追加

## Summary
議案詳細ページ（`/bills/[id]`）にTwitter/X専用のメタデータを追加しました。これにより、議案リンクをX（旧Twitter）でシェアした際に、適切なカードプレビューが表示されるようになります。

変更内容：
- `twitter` メタデータフィールドを `generateMetadata` 関数に追加
- `summary_large_image` カードタイプを使用
- 議案のサムネイルがある場合はそれを使用、ない場合はデフォルトのOGP画像にフォールバック

## Review & Testing Checklist for Human
リスク: 🟡 Yellow (1-2項目)

- [ ] **実際にXでシェアしてカードプレビューを確認** - 議案詳細ページのURLをX（旧Twitter）でシェアして、カードが正しく表示されることを確認してください
- [ ] サムネイル付きの議案とサムネイルなしの議案の両方で動作確認

### Test Plan
1. デプロイ後、サムネイル付きの議案URLをXの投稿ボックスに貼り付け
2. カードプレビューが表示され、画像・タイトル・説明文が正しく表示されることを確認
3. サムネイルなしの議案でも同様に確認（デフォルトOGP画像が使用されるはず）
4. （オプション）[Twitter Card Validator](https://cards-dev.twitter.com/validator) で確認

### Notes
- 変更は最小限で、既存のOpen Graph実装と同じパターンに従っています
- ルートレイアウトには既にTwitterカードサポートがあるため、この変更は議案詳細ページへの拡張です
- 型チェックとテストは全て通過しています

---
**Devin Session**: https://app.devin.ai/sessions/c49b7b0698e340b296ea32aef22df4fb  
**Requested by**: Shota Shimizu (tano.sukenyabu@gmail.com / @banbiossa)
