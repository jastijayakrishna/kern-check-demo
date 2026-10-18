# feat: パスキーログインの土台（依存整理・プラグイン設定・マイグレーション）

## 変更内容

パスキーログインの**土台**を用意する PR です。画面の変更はまだありません（後続 PR で入れます）。

- **better-auth を 1.7.2 に統一** — `@better-auth/passkey@1.7.2` が `@better-auth/core@1.7.2` を直接依存に持つため、`better-auth@1.7.1` のままだと core が 2 バージョン同居していました。Workers のバンドルが太るうえ、エラーコードのレジストリも二重になります。catalog と CLI（`auth`）を 1.7.2 に揃えて 1 本化しました。
- **`passkey()` プラグインの設定** — 既定値のままだと困る 3 点を明示しました（下表）。
- **`passkeyClient()` の登録** — ブラウザから `authClient.signIn.passkey` と `authClient.passkey.addPasskey` が使えるようになります。
- **`passkey` テーブルのマイグレーション追加**（`0008_jazzy_bloodscream.sql`）。

### `passkey()` に設定した 3 点と、その理由

| 設定 | 既定値 | 変えた理由 |
| --- | --- | --- |
| `appName` → `rpName` | `"Better Auth"` | **OS やブラウザのパスキー保存ダイアログにそのまま表示される**文字列です。放置すると「"Better Auth" のパスキーを保存しますか？」と出てしまいます。 |
| `origin` | リクエストの `Origin` ヘッダー | 検証の期待値をクライアント任せにする理由がないため、`BETTER_AUTH_URL` に固定しました。 |
| `authenticatorSelection.residentKey` | `"preferred"` | `"required"` に変更。**discoverable credential でないと、後続 PR で入れるオートフィルと「メールアドレスを入力しないログイン」が動きません。** `"preferred"` のままだと認証器次第で保存されず、再現しにくい不具合になります。 |

`rpID` は `BETTER_AUTH_URL` のホスト名から自動で決まるため、あえて指定していません。ただしこの値は**登録済みのパスキー 1 つ 1 つに焼き付けられ、後から変えると既存のパスキーがすべて使えなくなります**。そのため `.dev.vars.example` とコード側のコメントに注意書きを残しました。

なお `toOrigin()` を防御的に書いているのは Better Auth CLI 対策です。CLI は `cloudflare:workers` を差し替えて `env` をダミーの Proxy にするため、素直に `new URL()` を呼ぶとスキーマ生成が `ERR_INVALID_URL` で落ちます（実際に踏みました）。

## 変更の検証方法

1. `pnpm install`
2. `pnpm why @better-auth/core` を実行し、`Found 1 version of @better-auth/core` になることを確認する
3. `pnpm db:migrate:local` を実行し、`0008_jazzy_bloodscream.sql` が適用されることを確認する
4. `npx wrangler d1 execute iclub-reserve-db --local --command "PRAGMA table_info(passkey);"` で 11 列あることを確認する
5. `pnpm lint` / `pnpm typecheck` / `pnpm test` が通ることを確認する

実施済みの結果:

| 項目 | 結果 |
| --- | --- |
| `pnpm lint` | exit 0 |
| `pnpm typecheck` | exit 0 |
| `pnpm test` | 8 ファイル / 73 テスト 通過 |
| 整形（CI と同じ LF の条件で判定） | 110 ファイルすべて通過 |
| マイグレーション連鎖 | 使い捨ての SQLite に 0000→0008 を順に適用し、9 テーブルと `passkey` の 11 列ができることを確認 |

## スクリーンショット/デモ

画面の変更はありません。

## レビュアーへの特記事項

- **パスキーの実機登録はまだ未検証です。** 登録用の UI が後続 PR のため、この PR の時点では画面から登録できません。workerd 上で `@simplewebauthn/server` が動くことの確認は、UI が入る PR で行います。
- **`pnpm db:generate` の後は drizzle-kit の出力に oxfmt をかける必要があります。** `meta/_journal.json` と `meta/000X_snapshot.json` は生成されたままだと oxfmt 準拠でなく、CI の Format ジョブが落ちます。この PR でも整形してからコミットしています。
- Windows のローカル環境では `pnpm format` が無関係のファイルで失敗して見えることがありますが、これは `core.autocrlf=true` による CRLF の見せかけです。CI は ubuntu で LF のままチェックアウトするので再現しません。根本的に消すならリポジトリに `.gitattributes`（`* text=auto eol=lf`）を入れるのが良さそうですが、この PR の範囲外としました。
- 後続の予定は次のとおりです。
  1. パスキー登録の導線（新規登録で名前を入れた直後 + メール OTP ユーザーへの定期的な推奨）
  2. ログイン画面（パスキーでのログイン / オートフィル / 前回使った方法を先頭に出す）
  3. パスキーの管理（マイページを作るときに追加）

## 関連する Issue

- Close #

## チェックリスト

- [ ] 関連する Issue へのリンクが記述されているか
- [x] コードがプロジェクトのコーディング規約に従っているか
- [ ] 新しいテストを追加したか (必要な場合)
- [x] ドキュメントを更新したか (必要な場合)
- [x] セルフレビューを行ったか

<!--
テストについて: この PR は依存の整理・プラグイン設定・マイグレーションのみで、
単体テストを書ける純粋なロジックを追加していないため未追加です。
判定ロジック（対応環境の判別など）は後続 PR で追加し、そこでテストを書きます。
-->

🤖 Generated with [Claude Code](https://claude.com/claude-code)


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **New Features**
  * Added passkey sign-in and registration using WebAuthn.
  * Passkeys support device metadata, recovery through user accounts, and secure credential management.
  * Passkey authentication is available alongside existing sign-in methods.
* **Documentation**
  * Clarified that passkeys are tied to the authentication URL’s hostname and become invalid if it changes.
* **Chores**
  * Updated authentication tooling and supporting packages.
<!-- end of auto-generated comment: release notes by coderabbit.ai -->
