# Relatório de Execução de Testes - [Nome do Projeto/Ciclo]

**Data de Execução:** [26/05/2026]
**Versão da Aplicação Testada:** [Versão 0.0]
**Ambiente de Teste:** [Homologação]
**Responsável pela Execução:** [Divino Cecim da Silva]

## 1. Resumo Geral

Este relatório apresenta os resultados da execução dos testes funcionais para Desafio Sea Tecnologia. O objetivo principal foi validar as funcionalidades de Cadastro e Visualização de Empregados, e verificar a conformidade com o protótipo.

### 1.1. Estatísticas Gerais

* **Total de Casos de Teste Executados:** [Substituir pelo valor de `27`]
* **Testes que Passaram:** [Substituir pelo valor de `9`] (`33.333%`)
* **Testes que Falharam:** [Substituir pelo valor de `18`] (`66.667%`)
* **Testes Bloqueados:** [Substituir pelo valor de `0`] (`0%`)


### 1.2. Gráfico de Resultados

![Foram executados 27 testes manuais](testes manuais/Estatistica.png)


## 2. Resultados Detalhados por Funcionalidade

| Funcionalidade                                          | Passou | Falhou | Bloqueado | Total por Funcionalidade |
| :------------------------------------------------------ | :----: | :----: | :-------: | :----------------------: |
| **Testes de Compatibilidade com Navegadores**           |  [3]   |  [1]   |    [0]    |           [4]            |
| **Testes de Navegação**                                 |  [1]   |  [2]   |    [0]    |           [3]            |
| **Testes de Edição e Exclusão de Registros**            |  [0]   |  [4]   |    [0]    |           [4]            |
| **Testes de Adição de EPI e Atividades**                |  [0]   |  [4]   |    [0]    |           [4]            |
| **Testes de Validação de Formulário**                   |  [4]   |  [3]   |    [0]    |           [7]            |
| **Testes de Conformidade com o Protótipo**              |  [0]   |  [4]   |    [0]    |           [7]            |
| **Testes de Persistência e Recuperação de Dadoss**      |  [1]   |  [0]   |    [0]    |           [1]            |
| **TOTAL GERAL**                                         |**[9]** |**[18]**|  **[0]**  |         **[27]**         |



## 3. Análise dos Resultados e Pontos Críticos

### 3.1. Testes que Falharam

| ID  | Funcionalidade        | Caso de Teste                                  | bservações                                                          |
| :-: | :-------------------- | :--------------------------------------------- | :------------------------------------------------------------------- |
| [2] | [Login]               | [Login com credenciais inválidas (usuário)]   | [Mensagem de erro não clara]                                         |
| [3] | [Login]               | [Login com credenciais inválidas (senha)]     | [Permite múltiplas tentativas sem bloqueio]                         |
| [6] | [Cadastro Empregado]  | [Incluir empregado sem nome]                   | [Campo nome obrigatório não validado]                                |
| [13]| [Persistência Dados]  | [Verificar se novo empregado aparece na lista imediatamente] | [Registro não visível sem refresh]                             |
| [14]| [Persistência Dados]  | [Verificar se novo empregado aparece na lista após refresh] | [Registro não visível mesmo após refresh e scroll (falta paginação/scroll)] |

*(Copie e cole a saída "Casos de Teste que Falharam" do script Python aqui, formatando como uma tabela).*

**Análise das Falhas:**
* [Descreva os principais motivos das falhas. Por exemplo: A funcionalidade X apresenta inconsistência na validação de campos obrigatórios. O fluxo Y não exibe mensagens de erro claras para o usuário.]
* [Destaque os defeitos críticos que impedem o uso de funcionalidades chave.]
* **Defeito Crítico Identificado: Problema de Visualização de Registros Recém-Incluídos.**
    * **Observação:** Conforme identificado nos testes exploratórios e confirmado pelos testes automatizados (IDs 13 e 14), os registros recém-incluídos não são exibidos na lista de funcionários imediatamente após a inclusão, nem após um refresh da página. Mesmo com a tentativa de rolagem da tela, a ausência de paginação ou de um mecanismo de scroll eficaz impede a visualização do novo registro. Isso é considerado um defeito crítico, pois impede a validação da persistência dos dados e a interação subsequente com o registro (como alteração ou exclusão).
    * **Evidências:** Screenshots `NAO_VISIVEL_SEM_REFRESH_...png` e `NAO_VISIVEL_APOS_REFRESH_...png` (geradas pelo seu script de teste de cadastro).

### 3.2. Testes Bloqueados

| ID  | Funcionalidade       | Caso de Teste                                    | Observações                                                              |
| :-: | :------------------- | :----------------------------------------------- | :----------------------------------------------------------------------- |
| [11]| [Edição Empregado]   | [Alterar dados de empregado (se menu funcionasse)]| [Teste bloqueado pela não implementação do menu de Alterar/Excluir] |
| [12]| [Exclusão Empregado] | [Tentar excluir empregado (se menu funcionasse)] | [Teste bloqueado pela não implementação do menu de Alterar/Excluir] |

*(Copie e cole a saída "Casos de Teste Bloqueados" do script Python aqui, formatando como uma tabela).*

**Análise dos Bloqueios:**
* [Descreva os motivos dos bloqueios. Por exemplo: Os testes para a funcionalidade X foram bloqueados devido à não implementação da funcionalidade Y, que é um pré-requisito.]
* **Defeito Crítico Identificado: Menu de Ações "Alterar/Excluir" Não Implementado.**
    * **Observação:** Conforme o protótipo, ao clicar nos "..." ao lado de um registro de empregado, um menu com as opções "Alterar" e "Excluir" deveria ser exibido. Este menu não está funcional na versão atual da aplicação (conforme evidenciado pelo teste de ID 10). Isso impede a execução dos testes de alteração e exclusão.
    * **Evidências:** Screenshot `NAO_IMPLEMENTADO_Menu_Alterar_Excluir_...png` (gerada pelo seu script de teste de cadastro quando ele tenta interagir com este menu).

### 3.3. Pontos de Atenção e Melhorias Sugeridas (Opcional)

* [Liste sugestões de melhorias para a aplicação com base nos resultados dos testes, ex: melhorar as mensagens de erro, implementar validações faltantes, revisar o fluxo de atualização da lista de empregados.]
* [Sugira melhorias para o processo de teste, se aplicável.]

## 4. Conformidade com o Protótipo

* **Fonte:** [Resultado do seu teste de fonte - Ex: "Em conformidade" ou "Divergência: Fonte X utilizada em vez de Y"]
* **Cores:** [Resultado do seu teste de cores - Ex: "Em conformidade" ou "Divergência: Cor do botão X está Z em vez de W"]
* **Presença de Itens:** [Resultado do seu teste de itens - Ex: "Em conformidade" ou "Divergência: Botão Y não encontrado"]
* **Funcionalidade do Menu "..." (Alterar/Excluir):** Não implementado conforme o protótipo.
* **Visualização de Novos Registros:** Não implementado conforme o esperado (requer refresh e não há paginação/scroll adequado).

## 5. Conclusão e Recomendações

Com base nos resultados dos testes, [Faça uma conclusão geral sobre a qualidade da aplicação ou da funcionalidade testada].

**Recomendações:**
1.  **Correção Urgente dos Defeitos Críticos:**
    * Priorizar a correção do problema de visualização/atualização da lista de empregados após a inclusão.
    * Implementar a funcionalidade do menu "..." (Alterar/Excluir) conforme especificado no protótipo.
2.  **Revisão das Validações:** [Ex: Revisar as validações de campos obrigatórios no formulário de cadastro e as mensagens de erro.]
3.  **[Outras recomendações específicas]**

## 6. Anexos (Evidências)

* Gráfico de Resultados: `relatorio_testes_grafico.png`
* Screenshots das falhas e etapas críticas (salvas na pasta `screenshots/` e referenciadas no relatório).
* [Link para o arquivo CSV de resultados, se aplicável]
* [Link para o log de execução completo do Pytest, se aplicável]

