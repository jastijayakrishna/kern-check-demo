# fix(mandala): decouple embeddings from card serving — no more 0-card on embed fail (P0)

**CP512 P0 (PR-1).** 만다라 생성 → 카드 0장. 근본 = 임베딩이 카드 서빙의 하드 선행조건으로 **3곳** 커플링. admin Search-Trace: 임베딩 있으면 60장 placed되나 Mac Mini 임베딩 타임아웃(30s, 5.6s/셀×8)이 step1 실패 → 하위 전부 사망. 임베딩은 셀배정·정렬용, 카드 발굴은 search.list. 원칙 = "덜 정렬된 카드 > 카드 0장"(감독).

**게이트 3종 제거:**
- **executor.ts:175** — `if(cnt<8) return ok:false` 제거. sub_goal 텍스트를 `user_mandala_levels`(depth=0 subjects, 원본)에서 로드 → 임베딩 0개여도 subGoals 존재; 임베딩은 있으면 per-index 부착(semantic 경로 사용, lexical은 무임베딩 동작).
- **pipeline-runner.ts:173** — step1 실패/타임아웃이 step2/3 skip 안 함. degraded(lexical) 진행, 임베딩은 다음 ensure에서 백필.
- **ensure-mandala-embeddings.ts:182** — all-or-nothing 제거. 8셀 중 일부 실패 시 성공분만 INSERT(루프가 이미 null skip), 실패분은 다음 idempotent 호출서 백필. **한 셀 실패가 만다라를 죽이지 않음.**

**flag ** (default on; 'false'=3종 정확 롤백). **무회귀**: 임베딩 존재 시 semantic 경로·결과 불변.
**베타 후 보류(감독)**: pool-first, reuse-loop, 후보소진, maxResults, 카드상한, cosine하한.

**검증**: Ollama 중단 상태서 만다라 생성해도 카드 나옴(Tier2 lexical) / 임베딩 정상 시 결과 불변.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
