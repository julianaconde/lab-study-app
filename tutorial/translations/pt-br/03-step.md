# Passo 3: Backend e Integração com IA

> **Resumo:**
> Neste passo, você implementará a funcionalidade principal do StudyPlan AI conectando o backend aos modelos de IA do GitHub e criando o endpoint de API que alimenta a aplicação.

## Visão Geral do Aplicativo StudyPlan

O StudyPlan AI segue um fluxo de processamento claro, começando com a entrada do usuário e terminando com um plano de estudo personalizado:

1. **Entrada do Usuário:** O usuário preenche um formulário na interface web com suas informações de perfil (área de interesse, nível de habilidade atual, tempo de estudo disponível).

2. **Camada de API (`app/api/api.py`):** Recebe a solicitação, valida os dados e os mapeia para os objetos de modelo apropriados.

3. **Serviço de Prompts (`app/services/prompts.py`):** Formata as informações do usuário em instruções estruturadas para o modelo de IA, projetadas para produzir resultados ótimos.

4. **Cliente GitHub (`app/services/github_client.py`):** Envia as instruções formatadas para os Modelos do GitHub e aguarda a resposta da IA.

5. **Tratamento de Resposta:** A resposta gerada pela IA é processada, formatada e retornada ao usuário através da interface web como um plano de estudo estruturado e personalizado.

## ⌨️ Atividade: Implementar o Cliente de Modelos do GitHub

O cliente de Modelos do GitHub é essencial para a comunicação com os serviços de IA. Ele lida com autenticação, formatação de requisições e processamento de respostas, permitindo que o StudyPlan AI gere conteúdo personalizado. Nesta atividade, implementaremos o cliente que se comunica com as capacidades de IA do GitHub.

1. Abra `app/services/github_client.py`. Você verá a classe `GitHubModelsClient` com alguma estrutura pré-definida, incluindo métodos de inicialização e configuração.

2. Na classe `GitHubModelsClient`, clique com o botão direito no nome da classe e selecione **Explain this** no menu de contexto do GitHub Copilot para entender sua estrutura e comportamento pretendido.

3. Abra o painel **Copilot Chat**, mude para o modo **Agent** e peça ao Copilot para implementar o cliente usando a biblioteca Azure AI Inference com o seguinte prompt:

    > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social\&logo=github%20copilot)
    >
    > ```prompt
    > Implemente o cliente de Modelos do GitHub usando a biblioteca Azure AI Inference:
    >
    > - Primeiro instale o pacote necessário: pip install azure-ai-inference
    > - Use ChatCompletionsClient da azure.ai.inference
    > - Use SystemMessage e UserMessage de azure.ai.inference.models
    > - Conecte-se ao endpoint https://models.github.ai/inference
    > - Use o modelo openai/gpt-4o-mini
    > - Implemente uma resposta simulada de fallback para testes
    > - Trate erros e forneça mensagens de erro detalhadas
    > ```

> [!IMPORTANTE]
> Quando você enviar este prompt, o Copilot Chat pode solicitar permissão para instalar o pacote Azure AI Inference.
> - Clique em **Continue** na janela de chat para autorizar a instalação
>
> - Clique em **Keep** quando solicitado a salvar as alterações no arquivo de requisitos
>
> Este pacote é essencial para estabelecer comunicação com a API de Modelos do GitHub e habilitar a geração de planos de estudo com IA.

<details>
  <summary>🤔 Como funciona?</summary><br/>

A implementação do **GitHubModelsClient** integra-se aos modelos de IA do GitHub para gerar planos de estudo personalizados. Ela usa a **biblioteca Azure AI Inference** para estabelecer conexões seguras com o endpoint da API de Modelos do GitHub, lida com autenticação por meio de **tokens do GitHub** e converte mensagens do usuário no formato apropriado para processamento de IA. 

O cliente inclui um **mecanismo de fallback** que automaticamente muda para respostas simuladas quando a API está indisponível, garantindo que a aplicação permaneça funcional durante o desenvolvimento e testes.

</details>

---

| [← Verificar seu ambiente](02-step.md) | [Próximo: Modelos de Dados e Endpoint da API →](04-step.md) |
|:-----------------------------------|------------------------------------------:|
