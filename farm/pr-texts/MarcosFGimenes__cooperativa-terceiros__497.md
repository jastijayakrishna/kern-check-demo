# Auditoria Firestore: status canônico, índice, backfills e melhorias de tokens/pesquisa

### Motivation

- Reduzir leituras Firestore eliminando N+1 em serviços disponíveis e estabilizar o cálculo/armazenamento de metadados relevantes (status exibido, tokens, search tokens, assignment canônico). 
- Fornecer compatibilidade com documentos legados enquanto se adiciona um índice composto e backfills manuais para normalizar o estado.
- Tornar operações de escrita em massa seguras contra limites do Firestore e introduzir estratégia determinística para atualizações de progresso.

### Description

- Adiciona novo índice composto em `firestore.indexes.json` para `services(displayStatus, packageId, folderId, createdAt desc)` e cria documentação da auditoria em `FIRESTORE_READS_AUDIT.md`.
- Introduz canonicalização de status (`src/lib/serviceStatus.ts`), tokens canônicos e roteiros de reparo/garantia (`src/lib/repo/accessTokens.ts`, `scripts/backfill-*`), e um endpoint para invalidar caches de dashboard (`src/app/api/management/services/cache/route.ts`).
- Remove varreduras N+1 em serviços disponíveis substituindo pela query canônica por `displayStatus/packageId/folderId/createdAt`, implementa tokens apontados, reconciliação de assignment e search tokens, e adiciona backfills e scripts utilitários (`scripts/run-ts.cjs`, `scripts/backfill-*.ts`, `scripts/backfill-common.ts`).
- Diversas mudanças operacionais e de segurança: escrita segura por chunk/planejamento (`src/lib/firestoreWriteLimits.ts`), estratégia de atualização de progresso (`src/lib/progressUpdateStrategy.ts`), construção de tokens de busca trigram controlados (`src/lib/serviceSearch.ts`), campos de assignment canônico (`src/lib/serviceAssignment.ts`), atualizações em revalidações de cache e criação/atualização de serviços/pacotes, e pequenas alterações UI (debounce de busca para 400ms) e invalidação de cache no cliente.

### Testing

- Adicionados testes unitários com `vitest` para `accessTokenState`, `firestoreWriteLimits`, `progressUpdateStrategy`, `serviceAssignment`, `serviceSearch` e `serviceStatus` em `tests/unit/*.test.ts`.
- Executado `npm test` (invoca `vitest run`) sobre a suíte de unidades adicionada e todos os testes unitários passaram com sucesso.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a871109ff1883299ee3cdf68c52cffb)
