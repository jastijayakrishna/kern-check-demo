# SCRUM-72: cadastrar a régua de parcelas da administradora

## O que mudou

- `/admin/installment-rules` cadastra uma vigência da régua de parcelas e lista as existentes por administradora e produto, da mais recente para a mais antiga;
- a listagem mostra quantidade de parcelas, percentual total e qual vigência vale hoje (`Vigente`, `Futura` ou `Encerrada`);
- a distribuição é digitada em percentual (`0,75; 0,50; 0,25`) e convertida para pontos-base inteiros, sem ponto flutuante em nenhuma etapa;
- o repositório confirma a administradora com a linha bloqueada antes de gravar: inexistente volta como `AdministratorNotFoundError`, inativa como erro no campo da administradora;
- sobreposição de vigência continua recusada pelo índice único e chega ao formulário no campo da data;
- `POST /api/admin/administrator-installment-rules` exige perfil de administrador e devolve os erros no campo responsável;
- o Design System recebe o primitivo `Textarea`, usado pela distribuição.

## Decisões

**Tela própria, não aba da administradora.** A régua é consultada por administradora *e* produto, e uma administradora tem várias. Uma tela dedicada com a lista completa evita criar agora uma página de detalhe da administradora, que nenhuma história pediu.

**Percentual digitado, pontos-base gravados.** A entrada aceita `;`, espaço ou quebra de linha entre as parcelas e vírgula ou ponto como decimal. A conversão vive no domínio (`parseInstallmentPercentages`), e a entrada em pontos-base continua válida entre camadas — por isso o erro é reportado no campo que foi informado, `installmentPercentages` na tela e `installmentRatesBasisPoints` entre camadas.

**Régua longa não estoura a tabela.** Acima de nove parcelas a célula mostra as oito primeiras e quantas faltam. A régua completa continua inteira no banco e na API.

**Sem edição, por decisão anterior.** A tabela é apenas de inclusão desde a SCRUM-71, então a tela não oferece editar nem excluir e diz explicitamente que corrigir é cadastrar a vigência seguinte.

## Verificação

Controle de acesso, com o servidor de desenvolvimento em pé:

| Requisição sem sessão | Resultado |
| --- | --- |
| `GET /admin/installment-rules` | `307` para `/login` |
| `POST /api/admin/administrator-installment-rules` | `401 Faça login para continuar` |

Caso de uso e repositório contra PostgreSQL, em banco descartável criado e removido no container local:

| Caso | Resultado |
| --- | --- |
| régua digitada `0,75; 0,50; 0,25`, produto com espaços sobrando | gravada como `[75, 50, 25]`, produto normalizado, total 150 |
| mesma vigência com o produto em outra caixa | `DuplicateAdministratorInstallmentRuleError` |
| administradora inativa | erro no campo `administratorId` |
| administradora inexistente | `AdministratorNotFoundError` |
| percentual com três casas (`0,755`) | erro no campo `installmentPercentages` |
| nova vigência do mesmo produto | gravada, sem alterar a anterior |
| listagem em 12/09/2026 | a vigência de 01/06 marcada como vigente e a de 01/01 como encerrada |
| filtro por administradora sem régua | lista vazia |

## Commits atômicos

- `ef0286b` — `feat(sales)`: conversão de percentual digitado para pontos-base (domínio);
- `1171d79` — `feat(sales)`: listagem com nome da administradora, recusa de inativa e marcação da vigência atual (aplicação e infraestrutura);
- `aef35f0` — `feat(sales)`: endpoint, tela, item de menu e primitivo `Textarea` (exposição);
- `0d282f2` — `docs(sales)`: documentação do módulo.

## Fora deste incremento

Conforme o aceite: a venda não seleciona a régua automaticamente, nada de snapshot na venda nem de parcelas persistidas (isso é a SCRUM-73), nenhuma importação de arquivo e nenhuma edição ou encerramento de vigência.

## Como testar localmente

```bash
git switch main
git pull --ff-only
git fetch origin
git switch --track origin/feat/SCRUM-72-installment-rule-registration
npm ci
npm run db:up
npm run db:migrate
npm run dev
```

1. Entre como administrador e abra **Réguas de parcelas** no menu.
2. Cadastre uma régua: administradora ativa,
