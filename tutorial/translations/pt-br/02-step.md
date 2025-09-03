# Passo 2: Verificar seu ambiente

> **Resumo:**
> Neste passo, você verificará se o seu ambiente está configurado corretamente executando um script de teste. O script verifica a estrutura da sua aplicação, valida seu token do GitHub, testa a conectividade com o serviço de IA e confirma que todas as dependências estão instaladas.

O script `test_setup.py` é uma ferramenta de diagnóstico que realiza uma série de verificações para garantir que seu ambiente esteja configurado corretamente. Especificamente, ele:

* **Verifica a estrutura da aplicação**: Confirma que todos os arquivos necessários estão presentes (por exemplo, `app/main.py`, `app/services/github_client.py`).
* **Valida o token do GitHub**: Procura pela variável `GITHUB_TOKEN` no seu arquivo `.env` e garante que ela esteja configurada.
* **Testa a conectividade com o serviço de IA**: Envia uma solicitação de teste para o serviço de modelos de IA do GitHub usando seu token para verificar o acesso ao serviço e as permissões.
* **Confirma as dependências**: Verifica se todas as bibliotecas Python necessárias estão instaladas.

## ⌨️ Atividade: Teste Sua Configuração

1. Antes de executar o teste, você precisa implementar a função `check_dependencies` para verificar se todos os pacotes necessários estão instalados. Abra o arquivo `test_setup.py`, depois no painel **Copilot Chat** e selecione o modo **Edit**.

   <details>
      <summary>📸 Mostrar captura de tela</summary>
      <img src="../../images/2-edit-mode.png" alt="Captura de tela da aba Ports" />
   </details>

2. Peça ao Copilot para atualizar a função:

  > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social\&logo=github%20copilot)
  >
  > ```prompt
  > Atualize a função check_dependencies para ler os pacotes do requirements.txt e tentar importar cada um deles. Imprima "✅ Dependências importadas com sucesso" na lista de resultados final quando todas as dependências estiverem instaladas. Se alguma estiver faltando, liste os pacotes ausentes.
  > ```

3. Revise a implementação para garantir que ela verifica corretamente todas as dependências do arquivo requirements.txt.

4. Abra seu terminal e verifique sua configuração executando:

```bash
python test_setup.py
```

**Resultado esperado:**

```text
✅ Estrutura da aplicação verificada
✅ GITHUB_TOKEN encontrado
✅ Modelos do GitHub funcionando - Resposta: OK  
✅ Dependências importadas com sucesso
🎉 Configuração completa! Tudo pronto para executar a aplicação.
```

<details>
  <summary>🤷 Está com problemas?</summary>

1. **Problemas com o token do GitHub:**

   * Certifique-se de que ele foi copiado corretamente (sem espaços extras)
   * Confirme que o escopo `read:user` está habilitado
   * Use um token clássico, não de granulação fina

2. **Erros de dependência:**

```bash
# Atualize o pip
python -m pip install --upgrade pip

# Reinstale as dependências
pip install -r requirements.txt
```

3. **Python não encontrado localmente:**

   * Windows: Instale do [python.org](https://python.org)
   * Certifique-se de que a versão do Python é 3.9 ou superior

</details>

---

| [← Introdução ao Aplicativo StudyPlan e Configuração do Ambiente](01-step.md) | [Próximo: Backend e Integração com IA →](03-step.md) |
|:-----------------------------------|------------------------------------------:|
