# SCRUM-72: reaplicar o cadastro da régua de parcelas

## Por que esta PR existe

A SCRUM-72 foi mergeada e revertida na sequência, depois de um `npm ci` que abortou com `EPERM` e deixou o `node_modules` sem `tsx` nem `next`. A causa não estava no código: um `next dev` esquecido em segundo plano (iniciado por mim durante o smoke test das rotas) mantinha o `next-swc.win32-x64-msvc.node` aberto, e o `npm ci` apaga o `node_modules` antes de reinstalar — apagou parte, bateu no arquivo travado e parou. Os erros seguintes (`'tsx' não é reconhecido`, `'next' não é reconhecido`) são consequência disso.

Esta PR desfaz os quatro reverts, em um único commit, restaurando exatamente o que estava na `main` antes deles: `git diff` contra o último commit da SCRUM-72 (`0974c3e`) não acusa diferença nenhuma.

## O que voltou

- `/admin/installment-rules` para cadastrar uma vigência da régua e listar as existentes por administradora e produto, marcando `Vigente`, `Futura` ou `Encerrada`;
- conversão do percentual digitado (`0,75; 0,50; 0,25`) para pontos-base inteiros no domínio;
- recusa de administradora inexistente ou inativa, com a linha da administradora bloqueada antes da gravação;
- `POST /api/admin/administrator-installment-rules` restrito a administradores;
- o primitivo `Textarea` do Design System e o item de menu.

## Ambiente

Antes de validar, os processos resíduos foram encerrados e o `node_modules` foi reinstalado do zero. Vale registrar para a próxima vez: o projeto vive dentro do OneDrive, onde `EPERM` e `ENOTEMPTY` no `node_modules` são recorrentes. A sequência confiável no Windows é parar servidores de dev, `rm -rf node_modules` e então `npm ci`; `npm install` também evita o problema, porque não apaga a pasta inteira.

## Validação

Com o ambiente reinstalado, nesta branch: `npm run format:check`, `npm run typecheck`, `npm run lint`, `npm test` (329 testes), `npm run db:check` e `npm run build` passaram, e `npm run db:migrate` aplicou as migrações no banco local sem erro.

## Como testar localmente

```bash
git switch main
git pull --ff-only
git fetch origin
git switch --track origin/fix/SCRUM-72-reapply
npm install
npm run db:up
npm run db:migrate
npm run dev
```

1. Entre como administrador e abra **Réguas de parcelas** no menu.
2. Cadastre administradora ativa, produto `Auto Leve`, vigência `2026-01-01`, distribuição `0,75; 0,50; 0,25`: a linha aparece com 3 parcelas, total `1,50%` e badge `Vigente`.
3. Repita a mesma data com o produto `AUTO leve`: a mensagem de sobreposição aparece no campo da vigência.
4. Informe `0,755`: o erro aparece sob o campo da distribuição.
5. Cadastre uma vigência futura e uma anterior para o mesmo produto: a mais recente até hoje fica `Vigente`, as outras `Futura` e `Encerrada`.
6. Inative a administradora e confirme que ela sai do select; forçando o `POST` pela API, a resposta aponta o campo da administradora.

Se aparecer `EPERM` de novo, encerre o `next dev` antes (`Get-Process node`) em vez de reinstalar com o servidor rodando.

## Jira

SCRUM-72

---

🤖 Generated with [Claude Code](https://claude.com/claude-code)

