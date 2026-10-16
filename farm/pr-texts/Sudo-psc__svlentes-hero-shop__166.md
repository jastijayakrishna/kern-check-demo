# Add Firebase token verification API

## Summary
- export a reusable Firebase Admin initialization flag for server handlers that guard authentication logic
- add a dedicated /api/auth/verify-firebase-token route that validates ID tokens, syncs Prisma user records, and returns structured responses
- create Jest coverage for the new endpoint and fix Firebase analytics logging to use the shared error helper

## Testing
- npm test -- src/__tests__/api/auth-verify-firebase-token.test.ts *(fails: jest executable missing in environment)*

------
[Codex Task](https://chatgpt.com/codex/tasks/task_e_691217b2e12883289e7ba2ad14dac3b8)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

## Notas de Versão

* **Novas Funcionalidades**
  * Autenticação aprimorada com verificação segura de tokens e sincronização automática de perfil de usuário.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

---

<!-- kody-pr-summary:start -->
Este pull request introduz um novo endpoint de API (`/api/auth/verify-firebase-token`) para a verificação de tokens de ID do Firebase e a sincronização de perfis de usuário com o banco de dados local.

As principais mudanças incluem:

*   **Novo Endpoint de API (`/api/auth/verify-firebase-token`):**
    *   Permite que os clientes enviem um token de ID do Firebase para validação.
    *   Verifica a validade do token usando o SDK Admin do Firebase.
    *   Após a validação bem-sucedida, sincroniza o perfil do usuário (cria ou atualiza) no banco de dados local (Prisma), utilizando `firebaseUid` ou `email` para identificar o usuário.
    *   Retorna informações detalhadas do usuário e o status da sincronização do perfil.
    *   Inclui tratamento de erros para tokens inválidos, payloads JSON malformados, serviço Firebase Admin indisponível e falhas na sincronização do banco de dados.
    *   Suporta CORS para acesso de diferentes origens.
*   **Flag de Inicialização do Firebase Admin:** Adiciona `isFirebaseAdminInitialized` em `src/lib/firebase-admin.ts` para verificar de forma explícita se o SDK Admin do Firebase foi inicializado, permitindo um tratamento de erro mais robusto.
*   **Testes Abrangentes:** Inclui um novo arquivo de teste (`src/__tests__/api/auth-verify-firebase-token.test.ts`) para garantir a funcionalidade e a resiliência do novo endpoint.
*   **Pequena Refatoração:** Ajusta a forma como os erros do Firebase Analytics são registrados no lado do cliente para maior clareza.

Esta funcionalidade é essencial para garantir que os dados do usuário estejam atualizados em nosso sistema após a autenticação via Firebase, melhorando a segurança e a consistência dos dados.
<!-- kody-pr-summary:end -->
