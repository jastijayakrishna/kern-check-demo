# feat:ミッション完了モーダルのSNS共有ボタンをアイコンにする

# MissionCompleteDialog UI Redesign
スマホ(Before / After)

<img width="250" alt="スクリーンショット 2025-06-26 14 23 40" src="https://github.com/user-attachments/assets/4ec7fb0a-c33a-4092-85e0-57dfec81d23a" />
<img width="250" alt="スクリーンショット 2025-06-26 14 22 58" src="https://github.com/user-attachments/assets/df7e126f-2649-45d7-9763-713660e84d82" />
  
  
PC(Before / After)

<img width="300" alt="スクリーンショット 2025-06-26 14 24 04" src="https://github.com/user-attachments/assets/ddd9b131-45ab-4a97-8c7c-71313cddf48a" />
<img width="300" alt="スクリーンショット 2025-06-26 14 29 45" src="https://github.com/user-attachments/assets/8499108e-ea93-40cf-922f-4cca91a0a9eb" />

## 変更内容

### デザイン変更
- **シェアボタン**: テキストベースから60x60pxアイコンに変更し、横並び配置
- **閉じるボタン**: 右上に24x24pxのXアイコンを追加
- **シェアブロック**: 上部に「シェアして応援の輪を広げよう」文言を追加
- **ボタンテキスト**: 下部の閉じるボタンを「OK」から「このまま閉じる」に変更

## ファイル変更
- `app/missions/[id]/_components/MissionCompleteDialog.tsx`: メインコンポーネント更新
- `public/img/icon-*.png`: 5つのシェアアイコン画像を追加

---

Link to Devin run: https://app.devin.ai/sessions/cc37a30b2e674faaa094c2ea9e55e2cb  
Requested by: sumaitahtondy@gmail.com

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/team-mirai/action-board/blob/develop/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました
