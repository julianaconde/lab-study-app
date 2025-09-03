# Passo 4: Modelos de Dados e Endpoint da API

> **Resumo:**
> Neste passo, você criará os modelos de dados para estruturar requisições e respostas, e implementará o endpoint da API que conecta a interface do usuário com a integração de IA.

## Modelos de Dados e API REST

Para completar nossa aplicação StudyPlan AI, precisamos criar:

1. **Modelos de Dados**: Classes que definem a estrutura de requisições e respostas, garantindo consistência e facilitando a validação.

2. **Endpoint da API**: Uma rota Flask que recebe requisições do usuário, processa os dados, interage com o cliente de Modelos do GitHub e retorna o plano de estudo gerado.

Este passo é crucial para conectar a interface do usuário com a inteligência artificial, completando o fluxo da aplicação.

## ⌨️ Atividade: Criar Modelos de Dados

Antes de implementar o endpoint da API, precisamos criar os modelos de dados que estruturarão nossas requisições e respostas. Esses modelos garantirão formatos de dados consistentes e facilitarão a validação.

1. Crie um novo arquivo `app/models/study_plan.py` para definir nossos modelos de dados.

2. Use o seguinte prompt com o Copilot para implementar os modelos:

    > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social\&logo=github%20copilot)
    >
    > ```prompt
    > Crie dois modelos de dados para nossa aplicação de plano de estudos:
    > 
    > 1. StudyPlanRequest com:
    >    - Campos para area, level, weekly_hours, duration_months, specific_objectives
    >
    > 2. StudyPlanResponse com:
    >    - Campos para structured_plan, success, metadata, error
    > ```

## ⌨️ Atividade: Implementar o Endpoint da API

Com nosso cliente de Modelos do GitHub e modelos de dados prontos, é hora de criar o endpoint da API que alimenta nossa aplicação. Este endpoint serve como ponte entre o frontend e a IA, tratando requisições e retornando planos de estudo personalizados.

O endpoint recebe e valida solicitações de planos de estudo do frontend, processa as preferências do usuário, incluindo área, nível e compromisso de tempo, comunica-se com o serviço de IA de Modelos do GitHub e retorna conteúdo educacional estruturado. Ao implementar este endpoint, completamos a infraestrutura de backend para nosso gerador inteligente de planos de estudo.

1. **Navegue até o arquivo da API** abrindo `app/api/api.py` no painel Explorer. Este arquivo contém as rotas Flask que definem todos os nossos endpoints de API.

2. **Atualize as importações** para usar os modelos:

```python
from app.models.study_plan import StudyPlanRequest, StudyPlanResponse
```

3. **Abra o painel Copilot Chat** e selecione o modo **Edit** para ajudar a implementar a funcionalidade ausente. Use o seguinte prompt:

    > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
    >
    > ```prompt
    > Atualize a função `generate_study_plan` na API Flask para usar o cliente de Modelos do GitHub:
    > 
    > - Adicione validação para verificar se github_client.token está configurado
    > - Adicione uma estrutura try/except para tratamento detalhado de erros
    > - Use `build_study_plan_prompt()` com os parâmetros corretos do StudyPlanRequest
    > - Chame `github_client.chat_completion()` assincronamente com as mensagens
    > - Para caso de sucesso: retorne StudyPlanResponse com o plano gerado pela IA
    > - Para caso de erro: retorne resposta com success=False e mensagem de erro detalhada
    > ```

> [!DICA]
> O parâmetro de temperatura (definido como 0.7 no exemplo) controla a aleatoriedade da resposta da IA. Valores mais baixos (próximos a 0) tornam as respostas mais determinísticas e focadas, enquanto valores mais altos (próximos a 1) as tornam mais criativas e variadas. Você pode experimentar com este valor para encontrar o equilíbrio certo para conteúdo educacional.

---

| [← Backend e Integração com IA](03-step.md) | [Próximo: Elaboração de Prompts para IA →](05-step.md) |
|:-----------------------------------|------------------------------------------:|
