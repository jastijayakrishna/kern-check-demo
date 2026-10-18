# feat: 性格診断ゲーム「あなたのkokiはこれ！」

## 概要

MBTI風の性格診断ミニゲームを追加。8問の質問に答えると、性格タイプ（8種の「◯◯koki」）と、660着の実データから選ばれた「あなたのkoki（ぴったりの出勤服1着）」が表示される。

## 仕組み

- 各選択肢が5軸スコア（モノトーン↔カラフル / カジュアル↔きれいめ / 定番派↔冒険派 / 身軽↔マシマシ / 寒がり↔暑がり）を持ち、合計を集計
- タイプ判定は colorful / formal / adventurous の正負 2^3 = 8通り
- 服のマッチングは、各outfitの特徴量（colors.jsonの色味・カテゴリ/ブランドからのフォーマル度・着用回数の逆数=冒険度・小物数・投稿月の季節感）とのコサイン類似度で決定。乱数なしで、同じ回答なら常に同じ結果（シェア向き）

## 変更内容

- `src/lib/quiz.ts` — 質問・タイプ・マッチングの純粋ロジック
- `src/lib/__tests__/quiz.test.ts` — 決定性 / 8タイプ全到達可能 / 結果の多様性（16回答パターンで4種類以上）/ 実データで有効なoutfitが返ることを保証
- `src/components/QuizGameView.tsx` — intro / asking（進捗バー・前の質問に戻れる）/ result（タイプ・5軸バー・服カード・noteリンク）
- 登録: `App.tsx`（lazy import）、`router.ts`（`#/quiz`）、`GameHubView.tsx`
- OGP: `make-game-og.mjs` に quiz() を追加し `og-quiz.png` 生成、`public/game/quiz/index.html`（クローラー用エントリ）。共有URLは https://kokinoue.github.io/OOTD/game/quiz/
- 既存バグ修正: ゲームタブのアクティブ判定に `tower` が抜けていたのを追加

## 確認

- `pnpm test` 205/205 pass、`pnpm build` 成功
- devサーバーで intro → 8問回答 → 結果表示 → もう一度診断、を実際に操作して確認（コンソールエラーなし）

🤖 Generated with [Claude Code](https://claude.com/claude-code)
