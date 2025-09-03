# Passo 6: Adicionando Validação de Formulário

> **Resumo:**
> Neste passo, você usará o modo Agent do GitHub Copilot para implementar a validação do formulário de Parâmetros do Plano, garantindo que os usuários preencham todos os campos necessários antes do envio.

A validação de formulários é essencial para aplicações web que coletam dados do usuário. Ela garante que os usuários forneçam as informações necessárias no formato correto, dá feedback imediato sobre erros e impede que o backend receba dados inválidos ou incompletos. 

Atualmente, nosso formulário de plano de estudos permite que os usuários enviem sem preencher todos os campos, o que pode causar erros ou planos incompletos.

## ⌨️ Atividade: Implementar Validação de Formulário com o Agente Copilot

Vamos usar o modo Agent do GitHub Copilot para adicionar validação ao nosso formulário:

1. Abra o painel **Copilot Chat** e mude para o modo **Agent**.

2. Forneça as seguintes instruções para o agente:

    > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social\&logo=github%20copilot)
    >
    > ```prompt
    > Modifique o código JavaScript no arquivo index.html para adicionar validação ao formulário de Parâmetros do Plano.
    > 
    > Implemente validação JavaScript para o formulário de Parâmetros do Plano em index.html com estes requisitos:
    > - Marque visualmente os campos obrigatórios para orientar o usuário
    > - Impeça o envio do formulário se qualquer campo obrigatório (área, nível, tempo semanal, duração e objetivos específicos) estiver vazio
    > - Mostre mensagens de erro específicas para campos ausentes
    > - Destaque campos inválidos com uma borda vermelha
    > - Remova o destaque quando um campo for corrigido
    > ```

### 🧪 Teste a Validação do Formulário

Após implementar a validação, teste-a para garantir que funcione como esperado:

1. Execute a aplicação se ela ainda não estiver em execução
2. Tente clicar no botão "Gerar Plano de Estudos" sem preencher nenhum campo
3. Verifique se aparecem mensagens de erro para todos os campos obrigatórios
4. Preencha alguns campos e tente novamente para verificar se as mensagens de erro persistem apenas nos campos vazios
5. Preencha todos os campos obrigatórios e verifique se o formulário é enviado corretamente

### 📝 Considerações de Implementação

Ao usar o Agente GitHub Copilot para esta tarefa, observe como ele:

1. Analisa a estrutura HTML e JavaScript existente
2. Mantém consistência com o código existente
3. Implementa uma solução que se integra perfeitamente ao fluxo existente
4. Adiciona feedback visual para melhorar a experiência do usuário

A validação de formulários é uma excelente oportunidade para usar o modo Agent do GitHub Copilot, pois envolve entender a estrutura de código existente, adicionar lógica de validação e melhorar a experiência do usuário—tarefas que o Agente Copilot pode realizar eficientemente com uma única instrução clara.

---

| [← Elaboração de Prompts para IA](05-step.md) | [Próximo: Criando Modos de Chat Personalizados para Testes de Acessibilidade →](07-step.md) |
|:-----------------------------------|------------------------------------------:|
