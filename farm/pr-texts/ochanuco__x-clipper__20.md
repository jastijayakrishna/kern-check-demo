# Add typecheck stubs and CI workflow

## Summary
- add local module declarations to satisfy vitest and jsdom during type checking
- adjust TypeScript configuration to include the declarations
- add a GitHub Actions workflow to run pnpm typecheck on pull requests

## Testing
- pnpm run typecheck

------
[Codex Task](https://chatgpt.com/codex/tasks/task_e_6925c1c7a3b08328875c53e1770d7008)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

## リリースノート

* **Tests**
  * 自動型チェックの検証ワークフローを追加しました。
  * テスト環境の設定を改善し、より堅牢なテストハーネスに対応しました。

* **Chores**
  * TypeScript型定義ファイルを追加し、テストフレームワークと外部ライブラリの型サポートを強化しました。
  * コンパイラ設定を最適化しました。

<sub>✏️ Tip: You can customize this high-level summary in your review settings.</sub>

<!-- end of auto-generated comment: release notes by coderabbit.ai -->
