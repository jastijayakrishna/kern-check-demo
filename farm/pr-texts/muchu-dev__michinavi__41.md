# feat: ログイン処理の見直しとパスワード再設定を追加 (BE-08)

BE-08「認証の実装」のうち、**ログイン処理の見直し**と**パスワード再設定**を実装しました。
認証のサーバー処理は Server Action と Route Handler に集約しています（セッションCookieを書き戻せるのが Next.js 側だけのため）。`apps/backend` は変更していません。

## ログイン処理の見直し

| 変更 | 内容 |
| --- | --- |
| 戻り先の保持 | 未ログインで弾いた画面を `?next=` で持ち回り、ログイン後にそこへ戻す（従来はクエリを捨てて常に `/onboarding`） |
| オープンリダイレクト対策 | `lib/auth/redirect-target.ts` で自サイト内のパスだけを許可。`//host`、絶対URL、制御文字、認証画面自身は既定値へ落とす |
| エラー分類 | 回数制限（429）とメール未確認を、資格情報の誤りとは別の文言に。従来はすべて「メールアドレスまたはパスワードが正しくありません」で、レート制限時に手が止まった |
| 既ログイン時 | `/login` を開いたらアプリ側へ送り返す。`/forgot-password` と `/reset-password` は、リンク期限切れの案内が出るため対象外 |

## パスワード再設定

`/forgot-password` は「準備中」の静的ページでしたが、通しで動くようにしました。

- `app/forgot-password/actions.ts` — `resetPasswordForEmail`。宛先が登録済みかどうかは応答に出しません（この画面が「誰が使っているか」を確かめる道具にならないように）。回数制限だけは別文言
- `app/auth/confirm/route.ts` — メールのリンクを検証してセッションCookieを発行。`token_hash`（`recovery` のみ）と PKCE の `code` の両方に対応。失敗は `/forgot-password?error=link_expired` へ
- `app/reset-password/` — 8文字以上・確認一致を検証して `updateUser`。回復セッション切れは「メールを送り直す」動線へ戻す
- `lib/auth/site-url.ts` + 新 env `SITE_URL` — メールのリンク先は設定値を最優先。Host ヘッダーを差し替えたリクエストでリンク先を書き換えられないようにするため。未設定ならリクエストから組み立て
- `packages/db/supabase/{config.toml,templates/recovery.html}` — ローカルの Recovery メールを `/auth/confirm?token_hash=…` 形式に

## 途中で見つけた不具合の修正（`87c320e`）

`"use server"` のファイルは async 関数しか export できないため、`initialLoginState` の const export で Server Action の呼び出しが `A "use server" file can only export async functions, found object.` で落ちていました。**origin/main の時点から入っていたもの**で、ビルドもユニットテストも通ってしまい、ログインを実行したときだけ再現します。初期値と型を `state.ts` へ分離しました。

## 確認したこと

- ユニットテスト 22ファイル / 107テスト、カバレッジ statements 96.6% / branches 93.2%（閾値80%）
- `pnpm lint`（Biome + `tsgo --noEmit`）、`pnpm build`（`/auth/confirm`、`/reset-password` を認識）
- ローカル実機（`pnpm db:start` + `pnpm demo:seed`）でブラウザから通し確認
  - `demo-sato@michinavi.example` でログイン → トップ到達
  - `/forgot-password` 送信 → 送信済みの表示
  - `/auth/confirm?token_hash=…&type=recovery` → `/reset-password` へ遷移
  - `/reset-password` で `same_password` の文言変換

記録は `docs/testing/auth-password-reset.tdd.md` にあります。

## 未確認・申し送り

- パスワード変更の**成功**経路は実機未確認（デモ資格情報を壊さないよう、同じパスワードを送る形で止めたため）。ユニットテストでは網羅
- 実際のメール受信は未確認（ローカルの inbucket が停止していたため、管理APIで回復リンクを発行して代用）
- **BE-08 の残り（新規登録・ログアウト）は未着手**です。完了の定義「登録・ログイン・ログアウトが動く」に対する部分的な PR です
- `/login` と `/forgot-password` は `searchParams` を読むため、静的生成からリクエスト時レンダリングに変わりました

## マージ後に必要な設定

- Vercel に `SITE_URL` を追加
- Supabase の Redirect URLs に同じオリジンを登録
- Supabase ダッシュボードの Recovery テンプレートを `packages/db/supabase/templates/recovery.html` と同内容に

なお、このブランチには `.agents/` のリネームと `.gitignore` の更新（作者の既存コミット2件）も含まれています。

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_019rf4aQ5q8t32ivemmraBvW
