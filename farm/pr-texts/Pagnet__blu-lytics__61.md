# feat(statsig): session replay do Statsig por opção, com máscara total

# Description

Adiciona ao provider Statsig a opção `statsigOptions.sessionReplay` (desligada por padrão), para gravar sessões no Statsig e assistir aos replays junto com gates, eventos e Pulse no mesmo console.

- Com a opção ligada, o client usa o `runStatsigTriggeredSessionReplay` (`@statsig/session-replay@3.33.5`, mesma versão do `@statsig/js-client`) com `autoStartRecording` e `keepRollingWindow`. Quem decide quando gravar são a amostragem e os gatilhos configurados no console (Project Settings > Analytics & Session Replay).
- Todo texto e todo input são mascarados no próprio client (`maskAllInputs: true`, `maskTextSelector: '*'`), independentemente da configuração de privacidade do console.
- Com a opção ligada, o usuário é identificado já na criação do client, a partir do `client_uuid` salvo em `_bl_props`. Assim o gate de targeting do replay consegue avaliá-lo.
- Se o replay falhar ao iniciar, o erro é só logado e o envio de eventos continua.
- Sem a opção, nada muda: o client nasce anônimo e não grava sessões.

## Type of change

- [ ] Bug fix _(non-breaking change which fixes an issue)_
- [x] New feature _(non-breaking change which adds functionality)_
- [ ] **Breaking change** _(fix or feature that would cause existing functionality to not work as before)_

# Checklist

- [x] Perform a code self-review
- [x] Comment the code, particularly in hard-to-understand areas
- [x] Add documentation
- [x] Cover changes with tests
- [x] Ensure the test suite passes (`yarn test`)
- [ ] Make sure code lints (`yarn lint`). Fix it with `yarn lint:fix` in case of failure.
- [x] Make sure types are fine (`yarn lint:types`).

Link to Devin session: https://app.devin.ai/sessions/2f94e7cf008b4b17af9718396162845a
Open in Devin Desktop: https://app.devin.ai/desktop/session/2f94e7cf008b4b17af9718396162845a?variant=devin
