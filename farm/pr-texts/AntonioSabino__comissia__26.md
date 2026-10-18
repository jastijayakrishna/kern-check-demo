# SCRUM-71: modelar régua de parcelas da administradora

## O que mudou

- modela a régua de parcelas da administradora: uma versão por produto ou plano e por data de vigência;
- guarda a distribuição como lista ordenada de percentuais inteiros em pontos-base, da primeira à última parcela;
- aceita de 1 a 120 parcelas, cada percentual entre 1 e 10.000 pontos-base, e define o percentual total da regra como a soma da lista;
- recusa ponto flutuante em vez de arredondar;
- cria `administrator_installment_rules`, apenas de inclusão, com índice único por administradora, `lower(product)` e vigência;
- recusa administradora inexistente pela chave estrangeira, devolvida como `AdministratorNotFoundError`;
- encontra de forma determinística a régua vigente em uma data com `findAdministratorInstallmentRuleOn`, e recusa a data sem regra;
- promove a busca da vigência válida para `src/shared`, agora usada pelos vendedores e pelas administradoras.

## Modelo de dados

A distribuição fica em uma única coluna `integer[]`, e não em uma tabela filha. A ordem das parcelas é a própria ordem do array, então não existe numeração para ficar com lacuna nem linha órfã de uma régua, e a versão inteira é lida e gravada em uma operação. O banco valida o conteúdo do array: quantidade de parcelas, faixa de cada percentual, ausência de elementos nulos e recusa de array aninhado.

Como cada vigência é aberta e termina quando a próxima começa, sobreposição só poderia acontecer com o mesmo início repetido — o que o índice único impede, inclusive em cadastros simultâneos e inclusive quando o produto é digitado em outra caixa.

A tabela segue a decisão já usada no histórico de percentuais dos vendedores: o gatilho `administrator_installment_rules_append_only` recusa `UPDATE` e `DELETE`, então uma nova vigência nunca altera as versões históricas nem as vendas que as usaram. Corrigir uma régua errada é criar a vigência seguinte.

O percentual total não recebeu limite superior próprio: o aceite o define apenas como a soma da distribuição. Quem compõe a régua com o percentual do vendedor é o módulo de comissões, que já recusa distribuição cuja soma não seja exatamente o percentual usado no cálculo.

## Verificação no PostgreSQL

As duas migrações foram aplicadas em um banco descartável (`comissia_scrum71_check`, criado e removido no container local), e cada garantia foi exercitada:

| Caso | Resultado |
| --- | --- |
| régua válida, nova vigência do mesmo produto, mesma vigência em outro produto | aceitos |
| 120 parcelas de 10.000 pontos-base | aceito |
| vigência repetida, inclusive com o produto em outra caixa | `23505` |
| distribuição vazia, com zero, negativa, acima de 10.000, com elemento nulo, com 121 parcelas ou aninhada | `23514` |
| administradora inexistente | `23503` |
| `UPDATE` ou `DELETE` de uma versão | `P0001 administrator_installment_rules is append-only` |
| excluir administradora que já tem régua | `23503` |
| consulta da vigente em 15/03 e em 10/09 | devolve a régua de 01/01 e a de 01/06, respectivamente |

## Commits atômicos

- `9ce1aa7` — `refactor(shared)`: busca da vigência válida em `src/shared`, reusada pelos dois módulos;
- `ccd697f` — `feat(sales)`: domínio da régua e validação da distribuição;
- `ba4bcee` — `feat(sales)`: casos de uso de criação e de busca por data;
- `d9a5ac3` — `feat(sales)`: tabela, migrações e repositório;
- `1304376` — `docs(sales)`: documentação do módulo e da arquitetura.

## Fora deste incremento

Conforme o aceite: nenhuma tela de cadastro da régua, nenhuma seleção automática ao cadastrar a venda, nenhum snapshot da régua na venda e nenhuma persistência das parcelas geradas.

Também não há teste de integração automatizado do repositório: o CI ainda não sobe PostgreSQL. Por isso as garantias do banco foram exercitadas manualmente, como está na tabela acima, e ficaram cobertas por testes do schema Drizzle e do SQL das migrações.

## Como testar localmente

```bash
git switch main
git pull --ff-only
git fetch origin
git switch --track origin/feat/SCRUM-71-administrato
