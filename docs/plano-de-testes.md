
---

### `docs/plano-de-testes.md`

Este plano de testes segue as boas práticas e diretrizes da ISO/IEC/IEEE 29119 e ISTQB. [cite: 5]


# Plano de Testes - Aplicação SEA Tecnologia

## 1. Introdução

Este documento detalha o plano de testes para a aplicação web da SEA Tecnologia, acessível em `http://analista-teste.seatecnologia.com.br/`. [cite: 8] O objetivo é garantir a qualidade da aplicação, sua conformidade com os requisitos e o protótipo funcional (`https://tinyurl.com/yl58hs4m`). [cite: 9, 10]

## 2. Escopo dos Testes

O escopo dos testes abrange as seguintes áreas:

* **Validação de Formulários**: Verificação das validações de CPF, data, nome, adição de EPI e atividades. [cite: 3, 4, 14]
* **Persistência e Recuperação de Dados**: Garantir que as informações dos funcionários sejam salvas e recuperadas corretamente. [cite: 15, 16]
* **Edição e Exclusão de Registros**: Teste da funcionalidade de edição e exclusão de funcionários. [cite: 17]
* **Navegação**: Verificação dos links e menus da aplicação. [cite: 18, 19]
* **Conformidade Visual (Design)**: Avaliação da fonte, cores e presença de elementos conforme o protótipo. [cite: 11, 12, 13]
* **Compatibilidade com Navegadores**: Testes em diferentes navegadores web. [cite: 20]
* **Segurança (Injeção)**: Verificação de validações de entrada para prevenir injeção de código. [cite: 3, 4]

## 3. Estratégia de Testes

Será utilizada uma abordagem de testes automatizados E2E (End-to-End) com foco em testes funcionais, não-funcionais e de segurança. [cite: 6, 8]

* **Ferramentas**: Playwright com Python será a principal ferramenta de automação. [cite: 6, 21] `pytest` será o framework de testes e `allure-pytest` ou `pytest-html` para relatórios. [cite: 6]
* **Metodologia**: Serão criados casos de teste detalhados e scripts de automação baseados neles. Testes exploratórios também serão conduzidos para descobrir comportamentos não documentados. [cite: 8]

## 4. Tipos de Testes

Conforme o desafio, os seguintes tipos de testes serão incluídos: [cite: 8]

* **Testes Funcionais**:
    * Login [cite: 8]
    * Cadastro de empregado [cite: 8]
    * Validações de campos (nome, CPF, data, EPI, atividades) [cite: 4, 14]
    * Navegação entre páginas [cite: 8]
    * Persistência, recuperação, edição e exclusão de dados [cite: 15, 16, 17]
* **Testes Não-Funcionais**:
    * Compatibilidade com navegadores (Chrome, Firefox, Edge) [cite: 20]
    * Responsividade (diferentes resoluções de tela) [cite: 8]
* **Testes de Segurança**:
    * Validação de entrada para prevenir injeção (ex: SQL Injection através do campo nome). [cite: 3, 4, 8]
* **Testes Exploratórios**:
    * Identificação de falhas e comportamentos inesperados não cobertos pelos testes automatizados. [cite: 2, 8]

## 5. Ambientes de Teste

* **Ambiente de Aplicação**: `http://analista-teste.seatecnologia.com.br/` [cite: 8]
* **Ambiente de Desenvolvimento/Execução dos Testes**: Máquina local com Python e Playwright configurados.

## 6. Critérios de Sucesso e Falha

* **Sucesso**:
    * Todos os testes automatizados são executados com sucesso (passam).
    * A aplicação está em conformidade com os requisitos funcionais e não-funcionais.
    * A aplicação reflete o design e a estrutura propostos no protótipo. [cite: 10]
* **Falha**:
    * Qualquer teste automatizado falha.
    * Desvio significativo dos requisitos ou do protótipo.
    * Defeitos críticos encontrados durante testes exploratórios.

## 7. Entregas

* Plano de Testes (este documento). [cite: 5]
* Casos de Teste detalhados. [cite: 5]
* Estrutura de automação com scripts Playwright/Pytest. [cite: 5]
* Evidências de testes (relatórios e screenshots). [cite: 5]
* Documentação do projeto no GitHub. [cite: 5]

## 8. Cronograma (Exemplo)

| Fase            | Duração (Estimada) | Atividades                                     |
| :-------------- | :----------------- | :--------------------------------------------- |
| Análise         | 1 dia              | Entendimento dos requisitos e protótipo.       |
| Planejamento    | 1 dia              | Criação deste plano de testes.                 |
| Desenvolvimento | 3 dias             | Criação da estrutura e scripts de testes.      |
| Execução        | Conforme demanda   | Execução contínua dos testes automatizados.    |
| Relatório       | Conforme demanda   | Análise de resultados e geração de relatórios. |

