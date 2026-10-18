# 通勤ランナー（群衆増殖エンドレスラン）を追加

## 概要

出勤服アーカイブのゲームハブに、5つ目のミニゲーム **通勤ランナー**（Count Masters 型の群衆増殖ラン）を追加します。kokiの「群れ」を増やしながら通勤路を走る横スクロールのエンドレスランです。

OGP:

![og-runner](https://kokinoue.github.io/OOTD/og-runner.png)

## 遊び方

- 開始時は群れ1人。上下2レーンを **タップ / 上下スワイプ / ↑↓キー・スペース** で切り替えて走る（スペースはレーン切替トグル、R でやり直し）。
- 一定間隔で上下レーンに **ゲート対** が出現。効果は `+n`（n=3〜20）/ `×2` / `−n` / `÷2`。通過したレーンのゲートが群れの人数に適用される（下限0・上限9999）。
- **障害物**: 満員電車のドア（接触で30%減）・水たまり（10%減）。ゲートと重ならない位置に配置。
- スクロール速度は距離とともに緩やかに加速。群れが **0人になったら終了**、到達距離(m)がスコア。ベストは `localStorage`（`runner.best`）に保存。
- 群れは開始時にランダムに選んだ出勤服の切り抜きを人数分ワラワラ描画（最大60体、超過分は `×N` 表示）。

## 実装構成

- **`src/lib/runner.ts`（純粋ロジック・テスト対象）**
  - `applyGate` / `applyObstacle`（floor・0〜9999 clamp）
  - `generateSegment(seed, index)` … シード付き擬似乱数（`mulberry32` を自前実装）でコースを決定的に生成
  - 難易度曲線 `lossChance(index)` / `trainChance(index)`（index が進むほどマイナスゲート・満員電車の比率が上がる単調非減少関数）
  - `simulateGreedyBot` … Canvas 不要のロジックシミュレーション
  - 即死回避の保証: 各ゲート対には必ず「1人以上残せる選択肢」が存在する（両方マイナスの対は必ず片方を `÷2` にし、序盤 index<3 はマイナスを出さない）
- **`src/components/RunnerGameView.tsx`** … 描画（Canvas 2D 横スクロール・rAF 固定タイムステップ）・入力・UI。ロジックは持たず `runner.ts` を呼ぶ。街並みシルエットは白黒基調のシルエット、ゲートは緑（増）/赤（減）で色分け。
- **ゲーム登録**: `App.tsx`（View 型・lazy import・Suspense 分岐・`isPlayingGame`・タブ active 判定）、`lib/router.ts`（`#/runner`）、`GameHubView.tsx`（`CROWD RUNNER` カード）、`GameShareButton.tsx`（`runner` 追加）
- **スタイル**: `styles.css` 末尾に `g-runner-*` を追記（SP 375px ファースト・和文 line-height 1.6+）
- **OGP**: `scripts/make-game-og.mjs` に `runner()` を追加（既存4関数と同じく cutouts のみ・ネットワーク不要）＋ `public/game/runner/index.html`（`#/runner` へリダイレクトするクローラー向けページ）

## テスト結果

- `pnpm test`: **240 passed**（既存 + 新規 `runner.test.ts`）
  - applyGate 各効果と clamp 境界 / applyObstacle
  - `generateSegment` の決定性（同 seed・同 index → 同結果）
  - ゲート対に即死しない選択肢が常に存在（群れ2人以上・index 全域）
  - 難易度曲線の単調非減少
  - **プレイアビリティ**: 「常に期待値の高い方のゲートを選ぶ bot」がシード10種で2000m 生存
- `pnpm build`（`tsc --noEmit` 込み）: 成功。`RunnerGameView` は遅延読み込みで分割（gzip 約5KB）
- `pnpm og:games`: `public/og-runner.png` を生成（他の og-*.png は再生成分を `git checkout --` で戻し、本 PR には含めていません）

## 設計上の妥協点

- **「両方マイナス」ゲート対の解釈**: 仕様の3種混在（両方プラス / プラスとマイナス / 両方マイナス）は満たしつつ、貪欲bot の生存と「即死しない選択肢が常に存在」を厳密に保証するため、両方マイナスの対では必ず片方を `÷2`（＝2人以上なら1人以上残る）にしています。−n 同士で瞬間全滅するパターンは意図的に生成しません。
- **ライブ動作の目視確認**: プレビュー用ブラウザタブが `document.hidden === true` で動作するため `requestAnimationFrame` が停止し、Canvas アニメーションの実走行は目視確認できませんでした（コードの不具合ではなく環境制約）。代わりに、ビルド/型チェック通過・全240テスト通過（ロジックとプレイアビリティのシミュレーション）・コンソールエラーなし・スタート画面描画とプレイ遷移・Canvas 初期化を確認済みです。rAF + 固定タイムステップのループは既存の稼働中 `TowerGameView` / `PlatformGameView` と同一パターンです。

🤖 Generated with [Claude Code](https://claude.com/claude-code)
