# feat: グループの認可基盤を追加する

## 変更内容

グループ（団体）に対する**認可の基盤**を追加し、Better Auth の Organization プラグインを導入しました。

> [!WARNING]
> **マイグレーション 0010 は破壊的です。**
> `DELETE FROM reservation` → `DROP TABLE group` / `DROP TABLE membership` を行うため、**既存の団体・所属・予約データはすべて失われます。**
> 旧 `group` テーブルには `slug` / `status` などの列が無く、`membership.role` も値の体系が違うため、移行ではなく作り直しを選んでいます。理由はマイグレーション内のコメントに記載しています。適用前に各環境のデータが失われて問題ないか確認してください。

### 認可の基盤 (`app/domain/authz`)

- 「役割 → 許可される操作」の表 (`PermissionTable`) の**形と読み方だけ**を定義しました。
- 中身（誰が何をできるか）は資源側のドメインが持ちます。表をここに集めると、機能を足すたびに全機能が共有するファイルを書き換えることになるためです。
- `Record` で縛っているので、役割を増やしたときに直し忘れた表がコンパイル時に分かります。

### Membership ドメイン (`app/domain/membership`)

- 所属を表すモデルと、認可判定の入口となる `canPerform` を追加しました。
- `canPerform` は `Membership | null` を受け取り、`null` なら必ず `false` を返します。「所属していないグループでは何もできない」を、各ドメインで `!== null` を書き忘れようのない形にするためです。
- `MembershipRepository.findByGroupAndUser` は「所属していない」を `ok(null)` で返します。`err(NOT_FOUND)` にすると呼び出し側での畳み直しを誤ったときに DB エラーまで「所属していない」に潰れ、障害が 404 として表示されて気づけなくなるためです。

### Group ドメイン (`app/domain/group`)

- `isActive` (boolean) を `GroupStatus` (`enabled` / `pending` / `disabled`) に置き換えました。
- グループに対する操作 (`GroupAction`) と権限表 (`groupPermissions`) を定義しました。**グループの権限はこの表が唯一の定義元**です。
- グループの削除は意図的に含めていません。予約が紐づくグループの物理削除は外部キー違反になるため、無効化 (`Disabled`) で運用します。

### Better Auth Organization の導入 (`app/lib/auth/permission.ts`)

- Better Auth のロール (`admin` / `member`) を、**ドメインの権限表から導出**しています。手で二重に書くと片方だけ直したときにずれ、「画面には編集ボタンが出ないのに API では通る」という食い違いが起きるためです。

### 所属していないグループの秘匿 (`app/usecases/group/get-group.ts`)

- グループを取得できるのは自分が所属しているものだけになりました。
- 所属していない場合は「権限がありません」ではなく**存在しないときと完全に同じエラー**を返します。グループ ID を総当たりされても存在を気取られないようにするためです。
- 所属判定を先に行い、閲覧できないと分かった時点で打ち切ります。本体を取りに行ってから判定すると、存在するグループのときだけ問い合わせが 1 回増え、応答時間の差から存在を推測できてしまうためです。

### 組織エンドポイントの遮断 (`app/lib/auth/organization-guard.ts`)

`app/routes/api.auth.$.ts` は catch-all のため、Organization プラグインが生やすエンドポイントはすべて外から叩けます。以下を塞ぎました。

- `allowUserToCreateOrganization: false` — 既定は `true` で、**ログイン済みなら誰でも自分を admin とする団体を作れてしまう**状態でした。団体は運営が承認して作るものなので塞いでいます。
- `get-organization` / `get-full-organization` / `check-slug` — 「存在するが所属していない」(403) と「存在しない」(400) を別のエラーで返すため、`get-group.ts` で隠している存在情報がこの経路から漏れます。
- `organization/delete` — 権限表では既に不許可ですが、表の書き換えひとつで開いてしまう状態にしたくないため経路ごと閉じています。
- `invite-member` / `update-member-role` の `role` を `MembershipRole` のみに制限。Better Auth は配列でもカンマ区切り文字列でも役割を受け取るため、同じ分解の仕方で検証しないと `"admin,owner"` のような値がすり抜けます。

## 変更の検証方法

1. `pnpm install`
2. `pnpm test` — 327 件すべて成功することを確認
3. `pnpm typecheck` — エラーが出ないことを確認
4. `pnpm lint` / `pnpm format` — 指摘が出ないことを確認
5. `pnpm db:migrate:local` — 0000 から 0010 までが最後まで適用できることを確認
6. `pnpm db:seed` — シードが投入できることを確認
7. `pnpm dev` で `usr_student_01` としてログインし、`/group/grp_robotics` が表示されること
8. 同じユーザーで `/group/grp_disabled_group`（所属していない団体）を開き、**「グループが見つかりません」**になること（「権限がありません」ではない）
9. ログイン済みの状態で `POST /api/auth/organization/create` を叩き、`FORBIDDEN` が返ること
10. `POST /api/auth/organization/get-organization` を叩き、`404` が返ること

## スクリーンショット/デモ

<!-- 変更内容がわかるスクリーンショット等を貼り付けてください -->

## レビュアーへの特記事項

- **マイグレーションの破壊性**（冒頭の警告）を最初に確認してください。適用のタイミングは相談させてください。
- 権限のルールを変えたいときは `app/domain/group/index.ts` の `groupPermissions` **だけ**を直してください。Better Auth のロールはそこから導出されます。
- 認可の判定は権限表を直接読まず、必ず `canPerform` を通してください。直接読むと「所属しているか」の判定が抜け落ちます。
- `beforeUpdateMemberRole` フックは意図的に定義していません。このフックにだけは**更新前の既存行**が渡ってくるため、`{ ...member, updatedAt }` と展開すると古い `role` が混ざり、Better Auth 側の `response.data.role || newRole` が古い値を採用して「役割変更が 200 を返しながら何も起きない」という壊れ方をします。理由は `auth.server.ts` のコメントに残しています。
- 旧 `membership.role` の `owner` は廃止し `admin` に統一しました。`toMembershipRoles` は知らない役割を捨て、1 つも残らなければ最小権限の `member` として扱います。

## 関連する Issue

- Related to #35

## チェックリスト

- [x] 関連する Issue へのリンクが記述されているか
- [x] コードがプロジェクトのコーディング規約に従っているか
- [x] 新しいテストを追加したか (必要な場合)
- [x] ドキュメントを更新したか (必要な場合)
- [x] セルフレビューを行ったか

🤖 Generated with [Claude Code](https://claude.com/claude-code)

