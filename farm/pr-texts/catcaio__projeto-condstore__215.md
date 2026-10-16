# feat(site): add MVP supervised flow section (WhatsApp → Cotação → Aprovação → Pedido → Logística → Cockpit)

### Motivation

- Tornar explícito o fluxo operacional central do MVP (WhatsApp → Cotação → Aprovação → Pedido → Logística → Cockpit) com ênfase em auditabilidade e controle humano (gate de aprovação obrigatório).
- Entregar apenas uma seção principal reestruturada com componentes visuais e copy, mantendo escopo fechado e sem tocar backend ou superfícies frozen.

### Description

- Adiciona o componente visual `MvpCoreFlowSection` em `src/ui/site/mvp-core-flow-section.tsx` que materializa as etapas do fluxo (entrada, simulação, aprovação obrigatória, bloqueio sem aceite, pedido, logística, cockpit) com badges e linguagem operacional.
- Substitui o bloco anterior na home por `MvpCoreFlowSection` em `src/app/(public)/page.tsx` e atualiza a copy editorial para explicitar o gate de aprovação e o bloqueio de conversão.
- Exporta o novo componente no barrel `src/ui/site/index.ts` para manter a arquitetura de UI consistente.
- Visual e responsividade: layout baseado em lista vertical/card que prioriza legibilidade e sensação de controle sem animações pesadas.

### Testing

- `npm run scope:pr-tests -- --files 'src/app/(public)/page.tsx' src/ui/site/index.ts src/ui/site/mvp-core-flow-section.tsx` — executed and returned suggested gates (OK).
- `npm run guardrail:mvp-freeze` — initial run failed in the ephemeral environment due to missing `origin/main`, then validated with `MVP_FREEZE_BASE=HEAD` which reported no hard-frozen surface violations (OK with documented workaround).
- `npm run routes:sync` (runs `routes:inventory` + `routes:verify`) — succeeded and route registry remained consistent (OK).
- `npm run lint` — passed (OK).
- `npm run typecheck` — passed (OK).

Files changed: `src/app/(public)/page.tsx`, `src/ui/site/mvp-core-flow-section.tsx`, `src/ui/site/index.ts`.

------
[Codex Task](https://chatgpt.com/codex/tasks/task_e_69cb11f279b08331b53b9ed90ef4aead)
