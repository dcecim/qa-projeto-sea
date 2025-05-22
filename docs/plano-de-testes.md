# Plano de Testes

## 1. Introdução

### 1.1 Objetivo
Este plano de testes define a estratégia, recursos, cronograma e escopo dos testes a serem realizados na aplicação web disponível em `http://analista-teste.seatecnologia.com.br/`. O documento segue as diretrizes da ISO/IEC/IEEE 29119 e as boas práticas do ISTQB.

### 1.2 Escopo
O escopo deste plano inclui testes manuais para todas as funcionalidades da aplicação e testes automatizados para validação de nome/CPF e conformidade com o protótipo.

### 1.3 Referências
- Protótipo da aplicação: `https://tinyurl.com/yl58hs4m`
- Aplicação a ser testada: `http://analista-teste.seatecnologia.com.br/`
- ISO/IEC/IEEE 29119 (Padrão internacional para testes de software)
- ISTQB (International Software Testing Qualifications Board)

## 2. Estratégia de Teste

### 2.1 Níveis de Teste
- **Testes de Componente**: Validação de campos individuais (nome, CPF, data)
- **Testes de Integração**: Interação entre componentes (formulário e persistência)
- **Testes de Sistema**: Funcionalidades completas (CRUD, navegação)
- **Testes de Aceitação**: Conformidade com o protótipo e requisitos

### 2.2 Tipos de Teste
- **Testes Funcionais**: Verificação de funcionalidades específicas
- **Testes de Interface**: Conformidade com o protótipo (cores, fontes, elementos)
- **Testes de Usabilidade**: Facilidade de uso e navegação
- **Testes de Compatibilidade**: Funcionamento em diferentes navegadores

### 2.3 Abordagem de Teste
- **Testes Manuais**: Execução manual de casos de teste documentados
- **Testes Automatizados**: Scripts para validação de nome/CPF e conformidade com o protótipo
- **Testes Exploratórios**: Identificação de problemas não cobertos pelos casos de teste

## 3. Ambiente de Teste

### 3.1 Hardware
- Computadores com configuração padrão para desenvolvimento web

### 3.2 Software
- Navegadores: Chrome, Firefox, Edge (últimas versões)
- Sistema Operacional: Windows 10/11, macOS, Linux
- Ferramentas: Playwright, Python, pytest

### 3.3 Dados de Teste
- Dados válidos e inválidos para campos de formulário
- Conjunto de CPFs válidos e inválidos
- Nomes com diferentes formatos e caracteres

## 4. Critérios de Entrada e Saída

### 4.1 Critérios de Entrada
- Ambiente de teste configurado e acessível
- Casos de teste documentados e revisados
- Scripts de automação implementados e funcionais

### 4.2 Critérios de Suspensão e Retomada
- **Suspensão**: Falhas críticas que impedem a continuidade dos testes
- **Retomada**: Correção das falhas críticas e verificação do ambiente

### 4.3 Critérios de Saída
- Todos os casos de teste executados
- Defeitos críticos e de alta prioridade corrigidos
- Relatórios de teste gerados e aprovados

## 5. Entregáveis de Teste

### 5.1 Documentação
- Plano de Testes (este documento)
- Casos de Teste detalhados (`docs/casos-de-teste.md`)
- Relatórios de Execução de Teste

### 5.2 Código
- Scripts de automação para validação de nome/CPF
- Scripts de automação para conformidade com o protótipo
- Utilitários e helpers para suporte aos testes

## 6. Tarefas de Teste

### 6.1 Planejamento e Controle
- Elaboração do plano de testes
- Definição de cronograma e recursos
- Monitoramento da execução dos testes

### 6.2 Análise e Design
- Análise dos requisitos e protótipo
- Elaboração de casos de teste
- Design dos scripts de automação

### 6.3 Implementação e Execução
- Configuração do ambiente de teste
- Implementação dos scripts de automação
- Execução dos casos de teste manuais e automatizados

### 6.4 Avaliação e Relatório
- Análise dos resultados dos testes
- Registro e classificação de defeitos
- Elaboração de relatórios de teste

## 6.5 Cronograma (Exemplo)

| Fase            | Duração (Estimada) | Atividades                                     |
| :-------------- | :----------------- | :--------------------------------------------- |
| Análise         | 1 dia              | Entendimento dos requisitos e protótipo.       |
| Planejamento    | 1 dia              | Criação deste plano de testes.                 |
| Desenvolvimento | 3 dias             | Criação da estrutura e scripts de testes.      |
| Execução        | Conforme demanda   | Execução contínua dos testes automatizados.    |
| Relatório       | Conforme demanda   | Análise de resultados e geração de relatórios. |

## 7. Riscos e Contingências

### 7.1 Riscos de Projeto
- Alterações nos requisitos durante o ciclo de testes
- Indisponibilidade do ambiente de teste
- Restrições de tempo para execução completa dos testes

### 7.2 Riscos de Produto
- Incompatibilidade com navegadores específicos
- Problemas de desempenho em condições específicas
- Falhas de segurança em validações de entrada

### 7.3 Contingências
- Priorização de testes críticos em caso de restrição de tempo
- Plano de comunicação para reportar defeitos críticos
- Estratégias de mitigação para cada risco identificado

## 8. Aprovações

| Nome             | Cargo                   | Data           | Assinatura |
|------------------|-------------------------|----------------|------------|
|Divino Cecim      | Analista de Teste       | 22/05/2025     |            |
|                  |                         |                |            |
|                  |                         |                |            |
|                  |                         |                |            |
