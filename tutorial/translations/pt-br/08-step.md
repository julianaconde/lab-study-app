# Passo 8: Commit e Revisão de Código com GitHub Copilot

> **Resumo:**
> Neste passo, você aprenderá como usar o GitHub Copilot para gerar automaticamente mensagens de commit significativas com base em suas alterações de código e para realizar revisões de código antes de fazer commit. Esses recursos ajudam a melhorar seu fluxo de trabalho Git e manter alta qualidade de código.

## ⌨️ Atividade: Gerando uma Mensagem de Commit

Vamos usar o GitHub Copilot para gerar uma mensagem de commit para as melhorias de acessibilidade que você fez:

1. **Abra a visualização de Controle de Código Fonte** no VS Code clicando no ícone Git ou pressionando `Ctrl+Shift+G` (`Cmd+Shift+G` no macOS).

2. Prepare suas alterações clicando no ícone `+` ao lado dos arquivos modificados ou usando a opção "Stage All Changes" (Preparar Todas as Alterações).

   <details>
      <summary>📸 Mostrar captura de tela</summary>
       <img src="../../images/7-stage-changes.png" alt="Captura de tela mostrando todas as alterações preparadas" />
   </details>
   
3. **Clique no ícone do GitHub Copilot** na área de entrada da mensagem de commit (parece um ícone de brilho ou IA).

   <details>
      <summary>📸 Mostrar captura de tela</summary>
       <img src="../../images/7-generate-commit-message.png" alt="Captura de tela da interface de commit com botão do Copilot" />
   </details>

4. **Aguarde o Copilot analisar suas alterações** e gerar uma mensagem de commit automaticamente. A mensagem aparecerá no campo de entrada do commit.

5. **Revise e edite** a mensagem gerada, se necessário. Mesmo com assistência de IA, é uma boa prática verificar se a mensagem reflete com precisão suas alterações.

6. **Complete o commit** clicando no ícone de marca de seleção ou pressionando `Ctrl+Enter` (`Cmd+Enter` no macOS).

<details>
  <summary>Exemplo de uma mensagem de commit gerada</summary>

```
Melhorar acessibilidade no painel StudyPlan AI

- Adicionar marcos semânticos HTML5 (header, nav, main, footer)
- Tornar todos os elementos interativos acessíveis por teclado
- Adicionar atributos ARIA adequados a ícones e componentes de UI
- Melhorar a rotulagem e associações de campos de formulário
- Adicionar anúncios de mensagens de status para leitores de tela

Essas alterações garantem conformidade com WCAG 2.1 AA e melhoram a experiência para usuários com deficiências.
```

</details>

## ⌨️ Atividade: Realizando Revisões de Código com Copilot

Antes de finalizar seu commit, use o GitHub Copilot para revisar suas alterações de código:

1. **Abra a Paleta de Comandos** com `Ctrl+Shift+P` (`Cmd+Shift+P` no macOS).

2. **Pesquise por "GitHub Copilot: Review Changes"** (Revisar Alterações) e selecione-o.

3. **Aguarde o Copilot analisar suas alterações** e fornecer feedback sobre possíveis problemas ou melhorias.

   <details>
      <summary>📸 Mostrar captura de tela</summary>
       <img src="../../images/7-code-review.png" alt="Captura de tela do recurso de revisão de código" />
   </details>

4. Revise as sugestões fornecidas pelo Copilot, que podem incluir possíveis bugs ou erros de lógica, problemas de acessibilidade, otimizações de desempenho, vulnerabilidades de segurança e melhorias no estilo de código.

5. Aborde quaisquer sugestões relevantes antes de prosseguir com seu commit.

6. Gere uma nova mensagem de commit que reflita quaisquer melhorias adicionais que você tenha feito.


## 💡 Melhores Práticas para Usar Esses Recursos

1. **Sempre revise as mensagens de commit geradas** antes de fazer o commit para garantir a precisão.

2. **Adicione contexto quando necessário** - A IA pode não entender o "porquê" por trás de certas mudanças.

3. **Considere a revisão de código do Copilot como uma ferramenta complementar** - ela não substitui a revisão de código humana.

4. **Combine com verificações de acessibilidade** do passo anterior para garantia de qualidade abrangente.

5. **Use esses recursos consistentemente** para construir bons hábitos de desenvolvimento.

---

| [← Criando Modos de Chat Personalizados para Testes de Acessibilidade](07-step.md) | [Próximo: Revisão e próximos passos →](09-step.md) |
|:-----------------------------------|------------------------------------------:|
