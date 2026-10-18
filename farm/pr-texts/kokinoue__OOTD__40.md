# feat: タワー — 出勤服を積む物理パズル（どうぶつタワーバトル風）

## 概要

出勤服のくり抜き（`public/cutouts/*.webp`）を積み上げる物理パズル「タワー」を追加します。どうぶつタワーバトル風の1人スコアアタックです。

- ドラッグで横位置、**タップで90°回転**、はなすと落下（キーボード: ←→ 移動 / R↑ 回転 / Space↓ 落下）
- 積めたら +1 体。どれか1体でも台から落ちたらゲームオーバー
- タワーが伸びるとカメラが上にパン。ベストスコアは localStorage (`tower.best`)
- 各ピースに `#no 日付` のキャプション、次のピースのプレビュー付き

## 技術選定

| 選択 | 理由 |
|---|---|
| 物理: **planck.js** (Box2D 移植, 1.5.0) | タワー積みは resting contact の解の質が命。matter.js はスタッキングが不安定な上 2024年6月から更新停止のため不採用 |
| 描画: **素の Canvas 2D** | DuelGameView / PlatformGameView と同じ流儀。pixi.js は本用途にオーバーキル |
| 衝突形状: **アルファの実行時スキャン** | くり抜きのアルファを水平16バンドの不透明区間→矩形群として抽出し compound body に。脚の間の隙間や腕の凹みが物理に反映され「シルエットで積む」面白さが出る。1ターン1体なので実行時抽出で十分（ビルド時JSONだと656体分で数百KB増えるため不採用） |

## バンドルへの影響

planck を `manualChunks` で vendor から分離したため、**初期バンドルは据え置き**（vendor 142.79kB のまま）。planck チャンク (gzip 46kB) と TowerGameView (gzip 3.3kB) はタワーを開いた時だけロードされます。

## テスト

- `tower.test.ts` — アルファ→矩形抽出の純粋ロジック 7件（二本脚の分離・くびれ・ノイズ除去・AA連結など）
- `tower.physics.test.ts` — planck 統合スモーク 3件（台上で静止 / 台外は落下し続ける / 2体スタック）

`pnpm test` 198件全パス、`pnpm build`（tsc + vite）通過。

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01UWnhB2fFBW1KTZU8FGZsQ3

## スクリーンショット
<img width="3042" height="2134" alt="CleanShot 2026-07-07 at 22 20 16@2x" src="https://github.com/user-attachments/assets/238157e4-7abb-42be-8b11-991293b72619" />

