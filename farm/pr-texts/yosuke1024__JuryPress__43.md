# fix(validator): tier quality rules so one pass reports every defect

## なぜ

直近6回の生成が毎回「ちょうど1つ」のルールで落ち、直すと次が顔を出していた。保存済み7レコードで実測したところ、**各レコードの欠陥が1つだったからではない**ことが分かった。

`buildTrustedClaimReferences` は最初の違反で `throw` するため、**失敗レコードは何個欠陥を持っていても1個しか報告できない**。

| レコード | 報告されていた件数 | 実際の件数 |
|---|---|---|
| season-2-manual-29668300976 | 1 (`CLAIM_MIXED_FACT_CLASSES`) | **10** |
| season-2-request-36 | 1 (`CLAIM_STATEMENT_UNMATCHED`) | **5**(独立した2つの根本原因) |

つまり収束には違反の個数だけ本番生成が必要だった。「1つずつ後追い」は運用の問題ではなく、fail-fast の構造がそう強制していた。

## 変更

### 1. 全欠陥を1パスで報告(緩和ではない)

provenance ルールは既存の findings sink に **error** として記録し、走査を継続する。verdict は `failed` のままで fail-closed は不変。sink なし(公開ゲート / 生成時ビルダー)は従来どおり最初の1件で throw するので、**生成側と公開ゲートの対称性は保たれる**。

### 2. `CLAIM_MIXED_FACT_CLASSES` → 最弱クラスへ丸める

誘因が逆向きだった: README単独を引用した文は通り、**それを裏付けるマニフェストも併せて引用すると落ちた**。ルール自身の根拠「主張は最弱の出典と同じ強さ」は**丸める理由であって失格の理由ではない**。

- `SOURCE_FACT_CLASS_ORDER` は全順序なので最小値は **evidence_ids の順序に依存しない**(失格ルールが守ろうとしていた性質そのもの)
- `source_fact_classes` は全クラスを保持 → 読者への開示は減らない
- `attribution_required` は**全クラス集合**から計算されるので、`repository_observation` に丸まっても creator_claim を含む文は依然 attribution 必須

10件の違反すべてがこの形で、大半が `confirmed_fact + repository_observation`(APIメタデータをソースファイルが裏付ける = 最も自然な良い根拠付け)。

### 3. `Node.js` のセグメンテーション偽陽性

`Node.js` が `"…for Node."` + `"js."` に分割され、**どの annotation とも一致しない裸の `js.` 文**が生まれていた。URL basename ではないので attestation が届かず、リポジトリファイル名でもないので既存の閉じたリストにも無かった。

同じ**閉じたリスト**方式・同じ whole-token 境界判定で追加。汎用の `\w+\.js` パターンは従来どおり不採用(`the claim is false.js the tool is safe` で境界を隠せるため)。回帰テストで固定済み。

## 実測結果(保存済み7レコード)

**5 passed → 6 passed**

| レコード | before | after |
|---|---|---|
| season-2-manual-29626451493 (公開中) | passed | **passed** |
| season-2-manual-29633364803 (公開中) | passed | **passed** |
| season-2-2026-07-18-daily | passed | passed |
| season-2-manual-29664915161 | passed | passed |
| season-2-manual-29667424637 | passed | passed |
| season-2-manual-29668300976 | failed (10件) | **passed** |
| season-2-request-36 | failed (5件) | failed (2件・同一原因) |

**公開中2記事は passed のまま**(制約を毎回確認)。

残る `season-2-request-36` は**真陽性**。annotation が `not guaranteed`、本文が `not assured` とモデルが書き分けており、その文は本当に provenance 記録を持たない。近似一致で救う案は採らなかった — annotation は support_mode と evidence_ids を運ぶので、書いていない文へ証拠を後付けできてしまう。

## 維持したもの

- traceability 全般: evidence解決 / fact class導出 / `source_fact_classes`・`attribution_required` の永続化 / 全文注釈必須 — すべて fail-closed のまま
- `CLAIM_MIXED_SOURCE_VOICES`(creator と community の混在)は**引き続き致命的**。単一の attribution 値で記述できないため、強度の混在とは性質が違う
- 生成側と公開ゲートの対称性(`assertSourceAttribution` は共有のまま)

## 触っていないもの

- **Gemini prompt は変更なし**。prompt は今も「provenance ごとに分割せよ」と指示している(evaluator.ts:551,557,558)。validator だけ緩めるのは厳密に安全で、既存の挙動はそのまま通り、分割しない場合も通るようになるだけ。prompt 2.2.0 の revert(support_mode 崩壊)を踏まえ、prompt 変更は本番1本を回して評価できる別ステップとして分離した
- rubric / ペルソナ / スコア計算 / thinking level

`VALIDATOR_VERSION` 2.5.0 → 2.6.0、`CLAIM_RULE_VERSION` 3.0.0 → 3.1.0

## テスト

615 passed (56 files) / `tsc --noEmit` clean。挙動が変わったテストは削除せず**新しい不変条件を主張するよう書き換え**た(順序独立性は throw ではなく「両順序で同一の丸め結果」として、より強く検証している)。

🤖 Generated with [Claude Code](https://claude.com/claude-code)
