# feat: 開発用の DB シードを追加する

## 変更内容

- 空の DB では画面を確認できないため、`pnpm run db:seed` でローカルの D1 に開発用の初期データ（ユーザー 3 / 団体 3 / 所属 3 / 施設 3 / 予約 5 件）を投入できるようにしました。README に「追って整備します」とあったシード手順を埋めるものです。
- 投入するデータは `app/db/seed.ts` に手書きしています。
  - ID はすべて `seed_` で始まる固定値です。実行のたびに `seed_` の行だけを消してから入れ直すので**何度実行してもよく**、手で追加したデータは消えません。
  - INSERT は **D1 のプレースホルダ上限（1 クエリ 100 個）** に収まるよう分割しています。ローカルの D1 は素の SQLite なので気づけませんが、Cloudflare 上では必要です。
  - 予約は「今」からの相対日時（日本時間のきりのよい時刻）で作るので、しばらく経ってから流し直しても全部が過去の予約になりません。申請中・承認済み・却下・取消を一通り揃えています。
  - ユーザーは `@osaka-u.ac.jp` のアドレスなので、そのまま認証コードでログインできます。
- 実行用の `scripts/seed.ts` は Wrangler の `getPlatformProxy()` を使い、SQLite ファイルを直接開くのではなく**アプリと同じ D1 の API**を通します。「D1 では通らない書き方」をここで見逃さないためです。対象は `pnpm run db:migrate:local` と同じローカルの DB で、Cloudflare 上の DB は書き換えません。
- TS のスクリプトを実行するため `tsx` を、テスト用に `@types/better-sqlite3` を devDependency に追加しました（`better-sqlite3` 本体は既存）。あわせて `scripts/**/*.ts` を型検査の対象に含めています。

### drizzle-seed を使わなかった理由

[drizzle-seed](https://orm.drizzle.team/docs/seed-overview) は SQLite に対応しており、型の上では D1 にもそのまま渡せます（`DrizzleD1Database` は `BaseSQLiteDatabase` の一種）。ただし実際には次の問題があり、採用を見送りました。

1. **D1 のプレースホルダ上限を超える** — `floor(32766 ÷ 列数)` 行をまとめて INSERT するため、1 テーブル 10 行あまりで [D1 の上限（1 クエリ 100 個）](https://developers.cloudflare.com/d1/platform/limits/)に当たります。
2. **`reset()` が D1 で正しく動かない** — `PRAGMA foreign_keys = OFF` を単独実行していますが、[D1 の PRAGMA はトランザクション内でしか効かない](https://developers.cloudflare.com/d1/sql-api/sql-statements/)ため無効化されず、外部キーの張られたテーブルの削除に失敗します。
3. **生成されるのがランダムなデータ** — `status` の enum や「開始 < 終了」といったこのアプリの決まりごとを満たさず、結局ほぼ全列を `refine()` で書くことになります。

大量データで表示や性能を試したくなったときに、改めて検討すればよいと考えています。この経緯は `app/db/seed.ts` の冒頭にも残してあります。

## 変更の検証方法

1. `pnpm install`
2. `pnpm run db:migrate:local` でマイグレーションを適用する
3. `pnpm run db:seed` を実行し、各テーブルの件数が表示されることを確認する
4. **もう一度** `pnpm run db:seed` を実行し、件数が増えない（重複しない）ことを確認する
   - `pnpm exec wrangler d1 execute iclub-reserve-preview-db --local --command "select count(*) from reservation"` などでも確認できます
5. `pnpm run dev` で起動し、ログイン後に `/group/seed_group_robot` を開くと「ロボット研究会」が表示される
6. `pnpm test` / `pnpm run typecheck` / `pnpm run lint` が通ること

手元での確認結果:

- `pnpm run db:seed` … ローカル D1 に投入成功。2 回連続実行しても件数は 3/3/3/3/5 のまま
- `pnpm test` … 292 件すべて通過（シードのテスト 15 件を追加）
- `pnpm run typecheck` / `pnpm run lint` … 指摘なし
- `pnpm run build` … 成功。シードのコードが本番ビルドに混入しないことを grep で確認

## スクリーンショット/デモ

```console
$ pnpm run db:seed
ローカルの D1 にシードしました:
  users: 3 件
  groups: 3 件
  memberships: 3 件
  facilities: 3 件
  reservations: 5 件
```

## レビュアーへの特記事項

- `app/db/seed.test.ts` では、実際のマイグレーションを当てたメモリ上の SQLite（外部キー検査 ON）にシードを流し込んで検証しています。列名の取り違えや、削除・挿入の順番による外部キー違反は実行してみないと分からないためです。
- シードの対象はローカルの DB だけです。プレビュー環境の D1 に入れる手段は用意していません。必要になったら別途ご相談ください。
- 投入するデータの中身（団体名・施設名など）は仮のものです。実態に合わせたいものがあればお知らせください。

## 関連する Issue

<!-- 例えば `- Close #10` と入力すると、自動で #10 の Issue にリンクされます -->

- Close #

## チェックリスト

- [ ] 関連する Issue へのリンクが記述されているか
- [x] コードがプロジェクトのコーディング規約に従っているか
- [x] 新しいテストを追加したか (必要な場合)
- [x] ドキュメントを更新したか (必要な場合)
- [x] セルフレビューを行ったか

🤖 Generated with [Claude Code](https://claude.com/claude-code)

