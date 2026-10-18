# feat: 家族の安否画面を memberStatus API に繋ぐ (FE-16)

## 何を直したか

家族の安否画面（`/family`）が実際のバックエンド API を呼んでいなかったので、`memberStatus` ルーターに接続した。

- `apps/frontend/src/components/family/family-status-board.tsx`（新規）
  - `api.memberStatus.listForHousehold.useQuery()` で世帯の家族一覧と現在の安否を取得して表示する。
  - `api.memberStatus.set.useMutation()` で安否を登録し、成功後に一覧を `invalidate` して再取得する。
  - 状態は 6 つ（自宅で無事／避難の準備中／避難中／避難済み／支援が必要／別の場所で無事）から選ぶ。
  - 「支援が必要」は状態とは別のトグルにした（現在の状態を保ったまま `needsHelp` だけ反転させる）。
  - 読み込み中・エラー・空（家族が 0 人）の 3 状態をすべて描画する。API が落ちても画面は白くならず、`role="alert"` のメッセージが出る。
- `apps/frontend/src/app/(app)/family/page.tsx`
  - ハードコードしていた「母／父」と「サンプル表示です」を削除し、上記コンポーネントを描画するだけにした。
- テストを追加・更新（`family-status-board.test.tsx`、`page.test.tsx`）。
- `apps/frontend/vitest.config.mts` のカバレッジ対象に `src/components/family/**` を追加した。

## なぜそうしたか

- **ページはサーバーコンポーネントのまま、安否まわりだけをクライアントコンポーネントに切り出した。**
  `export const metadata` は Server Component でしか使えない（`node_modules/next/dist/docs/01-app/01-getting-started/14-metadata-and-og-images.md`）ため、`page.tsx` に `"use client"` を付けると既存のメタデータが壊れる。安否は取得のたびに変わるので、その部分だけを境界の内側に置いた。
- **編集できる行を「自分」と「アカウントを持たない家族」に限った。**
  バックエンドの代理登録は `can_update_member_status`（DB 側）でアカウントを持たない構成員だけに許されている。画面側でも同じ条件（`isSelf || !hasAccount`）にして、押しても必ず失敗するボタンを出さないようにした。
- **「支援が必要」を状態と分けた。**
  `member-status.ts` のコメントどおり「避難済みでも支援が要ることがある」ため、`status` と `needsHelp` を別々に送れるようにした。
- **エラーはコード別に文言を出し分けた。**
  世帯未登録（`NOT_FOUND`）と未ログイン（`UNAUTHORIZED`）は利用者側で対処できるので、汎用の失敗文言とは分けた。判定のしかたは既存の `posts/page.tsx` の `getSubmitErrorMessage` に揃えた。
- **想定外の `status` 値が来ても「未確認」へ寄せる。**
  DB の enum が増えたときに画面が落ちないようにするため。
- デザイントークン（`bg-passable` `bg-caution` `bg-impassable` `bg-neutral-soft` `text-ink` `text-muted` `border-outline` `border-brand`）だけを使い、色は直書きしていない。タップ領域は状態バッジが `min-h-14`、選択肢と支援トグルが `min-h-11`。バッジのボタンには「〇〇の安否は△△。変更する」という `aria-label`、開閉には `aria-expanded` / `aria-controls`、エラーには `role="alert"` を付けた。

## 動作確認の方法

1. `pnpm db:start` でローカル Supabase を起動し、`pnpm demo:seed` でデモデータを入れる。
2. `pnpm dev` で起動し、ログイン後（またはローカルの `DEV_AUTH_BYPASS=true`）に `/family` を開く。
3. 世帯の家族が API から取得した名前・状態で並ぶこと、自分の行（と、アカウントを持たない家族の行）のバッジを押すと状態の選択肢が開くことを確認する。
4. 「避難済み」などを選ぶと一覧が更新されること、「支援が必要と伝える」で状態を変えずに支援フラグだけ立つことを確認する。
5. Supabase を止めた状態で `/family` を開き、画面が白くならずエラー文言と「設定」への導線が残ることを確認する。

自動テスト:

- `mise exec -- pnpm lint` … 通過（biome + 全ワークスペースの typecheck）
- `mise exec -- pnpm --filter @michinavi/frontend test` … 25 ファイル / 136 件すべて通過
- `mise exec -- pnpm --filter @michinavi/frontend test:coverage` … 閾値 80% を満たす（新規コンポーネントは stmts 92.3% / branch 87.7%）
- `mise exec -- pnpm --filter @michinavi/frontend build` … 成功

## 残した課題（このPRでは直していない）

家族まわりの外で気づいた点。スコープを広げないため手を付けていない。

- **`memberStatus.setShareScope`（共有範囲 E5）が画面から呼ばれていない。** 「安否を誰に見せるか」を切り替える UI が無く、`/family/settings` の項目はすべて「準備中」のまま。
- **`memberStatus.history`（安否の履歴）も未使用。** 家族の状態がいつどう変わったかを追えない。
- **`message`（安否メッセージ）は表示のみで、画面から入力できない。** バックエンドの `set` は 200 文字までの `message` を受け付ける。
- **家族の連携（`/family/connect`）が実装されていない。** QR コードはプレースホルダのままで、招待の仕組み（A2）がバックエンドにも無い。バックエンドのテストも service role で構成員行を直接足して代用している。
- **`fieldReport` / `health` 以外の 14 ルーターのうち、このPRで繋いだのは `memberStatus` だけ。** `evacuation` `shelter` `route` `roadStatus` `household` などは引き続き画面から呼ばれていない。
- **`apps/backend/src/demo/__tests__/seed-demo-data.test.ts` が `main` の時点で落ちる。** 「架空の家族と投稿が入り、地図が空にならない」が `expected 0 to be 12`。このPRの変更（フロントエンドのみ）を stash した状態でも同じように失敗することを確認済み。BE-26 側の別課題。
- **`posts/page.tsx` が存在しないユーティリティクラス `bg-disabled` を使っている。** `globals.css` に `--color-disabled` が無いため、無効時の背景色が効いていない。

## 補足

- 実行環境に `mise` が入っていなかったため、実際には `corepack pnpm@10.12.2 …` で同じスクリプトを実行した。
- `pnpm tasks:check` は Node 24 でないと動かない（`scripts/google-tasks.ts` を Node が直接読めない）ため実行できていない。Google Sheet への書き戻しは行っていない。

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_018deLGsjikeqCm399GTTWd5

