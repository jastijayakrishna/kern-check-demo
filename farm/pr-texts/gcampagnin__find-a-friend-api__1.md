# Ensure pet listing pagination returns newest records first

## Summary
- sort in-memory pet listings by creation date to mirror Prisma order and ensure newest pets come first
- add regression test validating newest-first ordering during pagination

## Testing
- npm test


------
[Codex Task](https://chatgpt.com/codex/tasks/task_e_69231aac0cf48320aa796aa358e47482)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

## Notas da Versão

* **Novas Funcionalidades**
  * Pets agora são ordenados por data de criação (mais recentes primeiro) ao buscar por cidade com paginação, garantindo que os anúncios mais recentes apareçam primeiro nas listas paginadas.

* **Testes**
  * Adicionado teste automatizado para validar a ordenação correta de pets durante a paginação, aumentando a confiabilidade do comportamento.

<sub>✏️ Tip: You can customize this high-level summary in your review settings.</sub>
<!-- end of auto-generated comment: release notes by coderabbit.ai -->
