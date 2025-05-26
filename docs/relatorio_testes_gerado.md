
# Relatório de Execução de Testes

**Data da Execução:** N/A

## 1. Resumo Geral
- **Total de Casos de Teste Executados:** 27
- **Passaram:** 9 (33.33%)
- **Falharam:** 18 (66.67%)
- **Bloqueados:** 0 (0.00%)

## 2. Visão Geral dos Resultados (Gráfico)
![Visão Geral dos Resultados dos Testes](reports_graphs\test_results_pie_chart.png)

## 3. Casos de Teste por Cenário
![Casos de Teste por Cenário](reports_graphs\tests_per_scenario_bar_chart.png)

### Detalhes por Cenário:
- **Testes de Validação de Formulário:** 7 caso(s) de teste
- **Testes de Edição e Exclusão de Registros:** 4 caso(s) de teste
- **Testes de Compatibilidade com Navegadores:** 4 caso(s) de teste
- **Testes de Conformidade com o Protótipo:** 4 caso(s) de teste
- **Testes de Adição de EPI e Atividades:** 4 caso(s) de teste
- **Testes de Navegação:** 3 caso(s) de teste
- **Testes de Persistˆncia e Recuperação de Dados:** 1 caso(s) de teste

## 4. Detalhes dos Testes que Falharam
<table class="dataframe table table-striped table-sm">
  <thead>
    <tr style="text-align: left;">
      <th>Cenário</th>
      <th>Caso de Teste</th>
      <th>Resultado</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Testes de Compatibilidade com Navegadores</td>
      <td>CT-COMP-004: Compatibilidade com Dispositivos Móveis</td>
      <td>Falhou</td>
    </tr>
    <tr>
      <td>Testes de Navegação</td>
      <td>CT-NAV-001: Navegação entre Páginas</td>
      <td>Falhou</td>
    </tr>
    <tr>
      <td>Testes de Navegação</td>
      <td>CT-NAV-002: Navegação para Componente "Em Breve"</td>
      <td>Falhou</td>
    </tr>
    <tr>
      <td>Testes de Edição e Exclusão de Registros</td>
      <td>CT-EXCL-001: Exclusão de Funcionário</td>
      <td>Falhou</td>
    </tr>
    <tr>
      <td>Testes de Edição e Exclusão de Registros</td>
      <td>CT-EXCL-002: Cancelamento de Exclusão</td>
      <td>Falhou</td>
    </tr>
    <tr>
      <td>Testes de Edição e Exclusão de Registros</td>
      <td>CT-EDIT-001: Edição de Dados do Funcionário</td>
      <td>Falhou</td>
    </tr>
    <tr>
      <td>Testes de Edição e Exclusão de Registros</td>
      <td>CT-EDIT-002: Edição de EPIs e Atividades</td>
      <td>Falhou</td>
    </tr>
    <tr>
      <td>Testes de Adição de EPI e Atividades</td>
      <td>CT-ATIV-001: Adição de Atividades</td>
      <td>Falhou</td>
    </tr>
    <tr>
      <td>Testes de Adição de EPI e Atividades</td>
      <td>CT-ATIV-002: Remoção de Atividades</td>
      <td>Falhou</td>
    </tr>
    <tr>
      <td>Testes de Adição de EPI e Atividades</td>
      <td>CT-EPI-001: Adição de EPI</td>
      <td>Falhou</td>
    </tr>
    <tr>
      <td>Testes de Adição de EPI e Atividades</td>
      <td>CT-EPI-002: Remoção de EPI</td>
      <td>Falhou</td>
    </tr>
    <tr>
      <td>Testes de Validação de Formulário</td>
      <td>CT-FORM-002: Validação de Nome - Cenários Inválidos</td>
      <td>Falhou</td>
    </tr>
    <tr>
      <td>Testes de Validação de Formulário</td>
      <td>CT-FORM-004: Validação de CPF - Cenários Inválidos</td>
      <td>Falhou</td>
    </tr>
    <tr>
      <td>Testes de Validação de Formulário</td>
      <td>CT-FORM-007: Validação de Data - Cenários Inválidos</td>
      <td>Falhou</td>
    </tr>
    <tr>
      <td>Testes de Conformidade com o Protótipo</td>
      <td>CT-CONF-001: Verificação de Fonte</td>
      <td>Falhou</td>
    </tr>
    <tr>
      <td>Testes de Conformidade com o Protótipo</td>
      <td>CT-CONF-002: Verificação de Cores</td>
      <td>Falhou</td>
    </tr>
    <tr>
      <td>Testes de Conformidade com o Protótipo</td>
      <td>CT-CONF-003: Verificação de Elementos de Interface</td>
      <td>Falhou</td>
    </tr>
    <tr>
      <td>Testes de Conformidade com o Protótipo</td>
      <td>CT-CONF-004: Verificação de Layout Responsivo</td>
      <td>Falhou</td>
    </tr>
  </tbody>
</table>

## 5. Detalhes dos Testes Bloqueados
<p>Nenhum teste foi bloqueado.</p>

## 6. Graficos gerados
 [Resultado dos testes](reports_graphs/test_results_pie_chart.png) 
 [Resultado por cenário](reports_graphs/tests_per_scenario_bar_chart.png.png) 
 
## 6. Conclusão e Recomendações
# Considerações Finais e Recomendações

A presente rodada de testes focou em avaliar a funcionalidade e a conformidade da aplicação com o protótipo fornecido. Durante o processo, foram identificados tanto aspectos funcionais implementados quanto oportunidades significativas de melhoria e correção de defeitos.

## Testes de Conformidade com o Protótipo

A análise de conformidade visual da aplicação com o protótipo foi realizada por meio de inspeção visual. Devido a restrições de acesso que impediram a extração direta de parâmetros de CSS do protótipo, a automatização destes testes de conformidade não pôde ser executada com o nível de precisão desejado. Os scripts para estes testes foram desenvolvidos e encontram-se comentados na pasta `tests/` do projeto, aguardando a disponibilização de parâmetros técnicos para sua efetivação.

## Escopo dos Testes Automatizados

Os esforços de automação concentraram-se nas funcionalidades de CRUD (Create, Read, Update, Delete) para o cadastro de empregados. Especificamente, foram automatizados os fluxos de inclusão e consulta, além das tentativas de alteração e exclusão de registros, que se mostraram não implementadas.

## Principais Observações e Defeitos Identificados

1.  **Validação de Campos Críticos (Nome e CPF):**
    * **Nome do Empregado:** Verificou-se a ausência de validações robustas para o campo "Nome do Empregado"[cite: 16]. Recomenda-se fortemente a implementação de validações utilizando **expressões regulares** para garantir a integridade dos dados e prevenir a inserção de caracteres especiais, números ou códigos maliciosos (como tentativas de SQL Injection)[cite: 16]. Uma abordagem eficaz considera as variações comuns em nomes, como acentos, hífens e múltiplos sobrenomes, respeitando um limite mínimo e máximo de caracteres[cite: 17].
        * **Exemplo de Expressão Regular para Nome Completo (considerando as regras fornecidas [cite: 17]):**
            ```regex
            ^(?=.{2,120}$)[A-Za-zÀ-ÖØ-öø-ÿ]+(?:[-' ][A-Za-zÀ-ÖØ-öø-ÿ]+)*$
            ```
            * **Explicação da Regex:**
                * `^(?=.{2,120}$)`: Garante que o nome completo tenha entre 2 e 120 caracteres (lookahead positivo)[cite: 17].
                * `[A-Za-zÀ-ÖØ-öø-ÿ]+`: Permite uma ou mais letras (maiúsculas, minúsculas, com acentos)[cite: 17].
                * `(?:[-' ][A-Za-zÀ-ÖØ-öø-ÿ]+)*`: Permite, opcionalmente (zero ou mais ocorrências), um hífen, apóstrofo ou espaço, seguido por mais uma ou mais letras[cite: 17]. Isso cobre nomes compostos e sobrenomes[cite: 17].
            * *Nota: Para uma validação ainda mais completa, seria necessário um tratamento em código para verificar a lista de palavras reservadas de PL/SQL (como SELECT, DROP, INSERT, etc.), pois expressões regulares sozinhas podem se tornar excessivamente complexas para essa tarefa específica.* [cite: 17]
    * **CPF:** Constatou-se que o campo CPF atualmente não possui validação adequada[cite: 15], aceitando inclusive caracteres alfabéticos, o que compromete a integridade e a unicidade deste dado fundamental. É crucial implementar a validação do formato numérico (XXX.XXX.XXX-XX) e, idealmente, a validação do dígito verificador.

2.  **Visualização e Paginação de Registros:** Um defeito crítico identificado refere-se à visualização de registros de empregados após a inclusão. Atualmente, não há um mecanismo de paginação ou rolagem (scroll) eficiente na lista de empregados. Isso impede a visualização de novos registros quando a base de dados ultrapassa um número reduzido de entradas (aproximadamente seis empregados). Este comportamento compromete a capacidade do usuário de confirmar inclusões e acessar registros para edição ou exclusão.
    * **Sugestão de Melhoria Crítica:** Implementar paginação ou scroll infinito na lista de empregados para garantir a acessibilidade de todos os registros.

3.  **Funcionalidades de Edição e Exclusão:** Conforme testes exploratórios e tentativas de automação, as funcionalidades de alteração e exclusão de registros, que deveriam ser acessadas através do menu de opções ("...") ao lado de cada empregado (conforme protótipo), não se encontram implementadas na versão atual da aplicação. O clique no referido ícone não resulta na exibição do menu esperado.

## Outras Sugestões de Melhoria

* **Detalhamento de EPIs e Atividades:** Recomenda-se a inclusão de uma funcionalidade que permita visualizar uma lista clara das atividades e dos Equipamentos de Proteção Individual (EPIs) associados a cada empregado. Atualmente, essa informação não é facilmente acessível ou detalhada.
* **Usabilidade do Componente de Calendário:** O componente de calendário utilizado para o campo "Data de Nascimento" apresenta uma usabilidade confusa, especialmente para a seleção de datas anteriores ao ano de 2025. Sugere-se uma revisão deste componente para facilitar a navegação e seleção de datas mais antigas.
* **Conteúdo Placeholder ("Lorem Ipsum"):** O texto "Lorem Ipsum" presente em seções da aplicação deve ser substituído pelo conteúdo final e relevante antes da entrada em produção. Este item é considerado um placeholder de desenvolvimento e não um defeito funcional nesta fase.

## Conclusão Geral

A aplicação, em seu estado atual, reflete parcialmente as especificações e funcionalidades delineadas no protótipo. As observações e defeitos listados, em particular os relacionados à validação de dados, visualização de registros e à ausência de funcionalidades CRUD essenciais (alteração e exclusão via menu), indicam que a versão testada provavelmente se encontra em um estágio preliminar de desenvolvimento. Recomenda-se a priorização na correção dos defeitos críticos e na implementação das funcionalidades ausentes para alinhar a aplicação com os requisitos e garantir uma experiência de usuário satisfatória e segura.

---
