# Passo 7: Criando Modos de Chat Personalizados para Testes de Acessibilidade

> **Resumo:**
> Neste passo, você aprenderá como criar modos de chat especializados do GitHub Copilot para testes de acessibilidade. Você implementará um assistente personalizado que identifica problemas de acessibilidade em aplicações web, sugere melhorias baseadas nos padrões WCAG e ajuda a integrar verificações de acessibilidade em seu fluxo de desenvolvimento. [Explore opções avançadas de personalização para o chat do GitHub Copilot](https://code.visualstudio.com/docs/copilot/customization/overview).

## Entendendo Modos de Chat Personalizados

Os modos de chat personalizados no GitHub Copilot permitem adaptar o assistente para tarefas de desenvolvimento especializadas. Ao criar um modo dedicado a testes de acessibilidade, você garante que o Copilot se concentre exclusivamente em identificar e resolver problemas de acessibilidade em seu código.

Para construir este modo, usaremos o repositório **Awesome GitHub Copilot Customizations**—uma coleção curada de prompts, instruções e modos de chat que estendem o Copilot através de linguagens, domínios e fluxos de trabalho.

Este repositório fornece três recursos principais que você pode usar ao definir seu modo de chat personalizado:

* **[![Awesome Prompts](https://img.shields.io/badge/Awesome-Prompts-blue?logo=githubcopilot)](https://github.com/github/awesome-copilot/blob/main/README.prompts.md)** – Prompts específicos para tarefas de geração de código, documentação ou resolução de problemas específicos.
* **[![Awesome Instructions](https://img.shields.io/badge/Awesome-Instructions-blue?logo=githubcopilot)](https://github.com/github/awesome-copilot/blob/main/README.instructions.md)** – Padrões de codificação e melhores práticas para projetos inteiros ou arquivos específicos.
* **[![Awesome Chat Modes](https://img.shields.io/badge/Awesome-Chat_Modes-blue?logo=githubcopilot)](https://github.com/github/awesome-copilot/blob/main/README.chatmodes.md)** – Personas e modos de conversação prontos para uso adaptados para diferentes funções de desenvolvedor e contextos.

## ⌨️ Atividade: Criar um Modo de Chat de Acessibilidade Personalizado

Implementaremos o modo assistente de acessibilidade usando o [modo de Acessibilidade](https://github.com/github/awesome-copilot/blob/main/chatmodes/accesibility.chatmode.md) do repositório GitHub.

1. **Abra o Copilot Chat** clicando no ícone do Copilot na barra lateral do VS Code.

2. No painel Copilot Chat, selecione **⚙️ Configure Chat** > **Modes** > **Create new custom chat mode file**. Por padrão, os arquivos de modo de chat estão localizados na pasta `.github/chatmodes`.

   <details>
      <summary>📸 Mostrar captura de tela</summary>
       <img src="../../images/6-configure-chat-instructions.png" alt="Captura de tela mostrando a visualização de Chat e o menu Configure Chat, destacando o botão Configure Chat" />
   </details>

3. Nomeie o modo de chat como `accessibility`. Ele aparecerá na lista suspensa de modos de chat.
   
4. Uma vez que o arquivo `accessibility.chatmode.md` seja criado, copie seu conteúdo do [repositório do modo de Acessibilidade](https://github.com/github/awesome-copilot/blob/main/chatmodes/accesibility.chatmode.md) usando a opção "Copy raw file".

   <details>
      <summary>📸 Mostrar captura de tela</summary>
       <img src="../../images/6-copy-raw.png" alt="Captura de tela mostrando como copiar o conteúdo do arquivo bruto" />
   </details>

5. Abra o painel Copilot Chat e selecione `accessibility` na lista suspensa de modos de chat.

   <details>
      <summary>📸 Mostrar captura de tela</summary>
       <img src="../../images/6-chat-mode-dropdown.png" alt="Captura de tela mostrando a visualização de Chat, destacando a lista suspensa de modos de chat" />
   </details>

6. Peça ao Copilot para verificar seu arquivo `index.html`.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social\&logo=github%20copilot)
   >
   > ```prompt
   > Verifique a acessibilidade em index.html
   > ```

7. Revise as sugestões do assistente de chat de Acessibilidade. Use o **modo Agent** para atualizar seu arquivo `index.html` e corrigir quaisquer problemas de acessibilidade identificados.

---

| [← Adicionando Validação de Formulário](06-step.md) | [Próximo: Commit e Revisão de Código com GitHub Copilot →](08-step.md) |
|:-----------------------------------|------------------------------------------:|
