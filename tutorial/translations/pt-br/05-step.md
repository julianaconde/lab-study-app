# Passo 5: Elaboração de Prompts para IA

> **Resumo:**
> Neste passo, você aprenderá como elaborar prompts para geração de conteúdo por IA via requisições de API. Você implementará um sistema de prompts estruturado para o StudyPlan AI, testará em diferentes cenários e o refinará iterativamente para produzir planos de estudo de alta qualidade.

A qualidade dos planos de estudo gerados por IA depende muito de como os prompts são escritos. Prompts claros e bem estruturados ajudam a IA a entender o contexto, incluir todos os componentes necessários e retornar respostas no formato certo. Um sistema de prompts robusto geralmente inclui duas partes:

* **Prompt do Sistema** – Define o papel, tom e diretrizes comportamentais da IA. Por exemplo, você pode instruir a IA a agir como um mentor educacional ou a sempre fornecer respostas concisas e estruturadas.
* **Prompt do Usuário** – Contém a solicitação específica e dados de entrada, geralmente formatados com um template para guiar a saída da IA.

## ⌨️ Atividade: Implementar a Função de Construção de Prompt para Plano de Estudos

A função `build_study_plan_prompt` cria prompts personalizados que orientam a IA na geração de planos de estudo relevantes. Vamos implementá-la com o GitHub Copilot.

1. **Abra o arquivo de prompts** em `app/services/prompts.py`. Você encontrará exemplos de prompts e um espaço reservado para a função.

2. Vamos completar a função `build_study_plan_prompt` usando o modo Agent. Abra o painel **Copilot Chat**, mude para o modo **Agent** e forneça as seguintes instruções:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social\&logo=github%20copilot)
   >
   > ```prompt
   > Complete a função `build_study_plan_prompt` para que ela retorne uma lista de mensagens:
   >
   > **O prompt do sistema deve incluir:**
   > - Você é um especialista em educação com mais de 10 anos de experiência
   > - Sempre responda no idioma preferido do usuário
   > - Crie planos práticos, estruturados e realistas
   > - Inclua projetos práticos e recursos específicos
   >
   > **O prompt do usuário deve incluir:**
   > - Template com variáveis: área, nível, tempo, duração, objetivos
   > - Solicitação para cronograma semanal detalhado
   > - Solicitação para recursos específicos (cursos, livros, ferramentas)
   > - Solicitação para projetos práticos progressivos
   > - Solicitação para marcos de avaliação mensais
   > ```

3. Salve as alterações e teste com entradas de exemplo. Por exemplo:

   | Área          | Nível        | Tempo Semanal | Duração | Objetivo Específico                                |
   | ------------- | ------------ | ------------- | ------- | -------------------------------------------------- |
   | backend       | iniciante    | 10            | 3       | "Quero construir APIs REST com Node.js"            |
   | frontend      | intermediário| 15            | 4       | "Preciso dominar React e aprender Next.js"         |
   | data\_science | avançado     | 20            | 6       | "Quero implementar modelos de ML em produção"      |
   | fullstack     | iniciante    | 12            | 6       | "Quero criar uma aplicação web completa"           |
   | ai\_ml        | intermediário| 18            | 5       | "Preciso entender deep learning para NLP"          |

Esses exemplos testam diferentes áreas, níveis de habilidade e objetivos, dando a você uma imagem clara de como seu sistema de prompts se adapta a vários cenários.

---

| [← Modelos de Dados e Endpoint da API](04-step.md) | [Próximo: Adicionando Validação de Formulário →](06-step.md) |
|:-----------------------------------|------------------------------------------:|
