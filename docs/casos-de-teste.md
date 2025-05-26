# Casos de Teste

Este documento contém os casos de teste manuais detalhados para a aplicação disponível em http://analista-teste.seatecnologia.com.br/, organizados por funcionalidade e seguindo as diretrizes da ISO/IEC/IEEE 29119 e as boas práticas do ISTQB.

## Índice

1. [Testes de Conformidade com o Protótipo](#1-testes-de-conformidade-com-o-protótipo)
2. [Testes de Validação de Formulário](#2-testes-de-validação-de-formulário)
3. [Testes de Adição de EPI e Atividades](#3-testes-de-adição-de-epi-e-atividades)
4. [Testes de Persistência e Recuperação de Dados](#4-testes-de-persistência-e-recuperação-de-dados)
5. [Testes de Edição e Exclusão de Registros](#5-testes-de-edição-e-exclusão-de-registros)
6. [Testes de Navegação](#6-testes-de-navegação)
7. [Testes de Compatibilidade com Navegadores](#7-testes-de-compatibilidade-com-navegadores)

## 1. Testes de Conformidade com o Protótipo

### CT-CONF-001: Verificação de Fonte

**Objetivo:** Verificar se a fonte utilizada na aplicação corresponde à especificada no protótipo.

**Pré-condições:**
- Acesso à aplicação em http://analista-teste.seatecnologia.com.br/
- Acesso ao protótipo em https://tinyurl.com/yl58hs4m

**Passos:**
1. Acessar a aplicação
2. Comparar a fonte dos títulos com o protótipo
3. Comparar a fonte dos textos com o protótipo
4. Comparar a fonte dos botões com o protótipo
5. Comparar a fonte dos campos de formulário com o protótipo

**Resultado Esperado:**
- As fontes utilizadas na aplicação devem ser idênticas às especificadas no protótipo

**Critérios de Aceitação:**
- Família de fonte correta
- Tamanho de fonte proporcional
- Estilo de fonte (negrito, itálico) correspondente

**Prioridade:** Alta

### CT-CONF-002: Verificação de Cores

**Objetivo:** Verificar se as cores utilizadas na aplicação correspondem às especificadas no protótipo.

**Pré-condições:**
- Acesso à aplicação em http://analista-teste.seatecnologia.com.br/
- Acesso ao protótipo em https://tinyurl.com/yl58hs4m

**Passos:**
1. Acessar a aplicação
2. Verificar a cor de fundo principal
3. Verificar a cor dos botões primários
4. Verificar a cor dos botões secundários
5. Verificar a cor dos textos
6. Verificar a cor dos elementos de destaque
7. Verificar a cor dos campos de formulário

**Resultado Esperado:**
- As cores utilizadas na aplicação devem ser idênticas às especificadas no protótipo

**Critérios de Aceitação:**
- Cores exatas (valores hexadecimais correspondentes)
- Consistência de cores em toda a aplicação
- Contraste adequado entre texto e fundo

**Prioridade:** Alta

### CT-CONF-003: Verificação de Elementos de Interface

**Objetivo:** Verificar se todos os elementos de interface estão presentes conforme o protótipo.

**Pré-condições:**
- Acesso à aplicação em http://analista-teste.seatecnologia.com.br/
- Acesso ao protótipo em https://tinyurl.com/yl58hs4m

**Passos:**
1. Acessar a aplicação
2. Verificar a presença de todos os campos de formulário
3. Verificar a presença de todos os botões
4. Verificar a presença de todos os elementos de navegação
5. Verificar a presença de todos os ícones
6. Verificar a presença de todos os elementos de feedback (mensagens, alertas)

**Resultado Esperado:**
- Todos os elementos presentes no protótipo devem estar presentes na aplicação

**Critérios de Aceitação:**
- Quantidade correta de elementos
- Posicionamento similar ao protótipo
- Tamanho proporcional ao protótipo

**Prioridade:** Alta

### CT-CONF-004: Verificação de Layout Responsivo

**Objetivo:** Verificar se o layout da aplicação se adapta a diferentes tamanhos de tela conforme o protótipo.

**Pré-condições:**
- Acesso à aplicação em http://analista-teste.seatecnologia.com.br/
- Acesso ao protótipo em https://tinyurl.com/yl58hs4m

**Passos:**
1. Acessar a aplicação em um dispositivo desktop
2. Redimensionar a janela para diferentes larguras
3. Verificar a adaptação dos elementos em cada tamanho
4. Acessar a aplicação em um dispositivo móvel (ou emulador)
5. Verificar a adaptação dos elementos em orientação retrato
6. Verificar a adaptação dos elementos em orientação paisagem

**Resultado Esperado:**
- O layout deve se adaptar de forma similar ao protótipo em diferentes tamanhos de tela

**Critérios de Aceitação:**
- Elementos reposicionados adequadamente
- Textos legíveis em todos os tamanhos
- Funcionalidades acessíveis em todos os tamanhos

**Prioridade:** Média

## 2. Testes de Validação de Formulário

### CT-FORM-001: Validação de Nome - Cenários Válidos

**Objetivo:** Verificar se o campo de nome aceita entradas válidas conforme as regras definidas.

**Pré-condições:**
- Acesso à aplicação em http://analista-teste.seatecnologia.com.br/

**Passos:**
1. Acessar o formulário de cadastro de funcionário
2. Inserir nome com 2 caracteres (ex: "Jo")
3. Verificar aceitação
4. Inserir nome com 30 caracteres (ex: "Joãooooooooooooooooooooooooo")
5. Verificar aceitação
6. Inserir nome com espaço (ex: "João Silva")
7. Verificar aceitação
8. Inserir nome com hífen (ex: "Maria-Clara")
9. Verificar aceitação
10. Inserir nome com acentos (ex: "José Antônio")
11. Verificar aceitação

**Resultado Esperado:**
- Todos os formatos válidos de nome devem ser aceitos sem mensagens de erro

**Critérios de Aceitação:**
- Nenhuma mensagem de erro exibida
- Campo mantém o valor inserido
- Possibilidade de prosseguir com o formulário

**Prioridade:** Alta

### CT-FORM-002: Validação de Nome - Cenários Inválidos

**Objetivo:** Verificar se o campo de nome rejeita entradas inválidas conforme as regras definidas.

**Pré-condições:**
- Acesso à aplicação em http://analista-teste.seatecnologia.com.br/

**Passos:**
1. Acessar o formulário de cadastro de funcionário
2. Inserir nome com 1 caractere (ex: "J")
3. Verificar rejeição
4. Inserir nome com mais de 120 caracteres
5. Verificar rejeição
6. Inserir nome com números (ex: "João123")
7. Verificar rejeição
8. Inserir nome com caracteres especiais (ex: "João@Silva")
9. Verificar rejeição
10. Inserir palavras reservadas de PL/SQL (ex: "SELECT FROM")
11. Verificar rejeição
12. Deixar o campo em branco
13. Verificar rejeição

**Resultado Esperado:**
- Todos os formatos inválidos de nome devem ser rejeitados com mensagens de erro apropriadas

**Critérios de Aceitação:**
- Mensagem de erro clara e específica
- Impossibilidade de prosseguir com o formulário até correção
- Foco mantido no campo com erro

**Prioridade:** Alta

### CT-FORM-003: Validação de CPF - Cenários Válidos

**Objetivo:** Verificar se o campo de CPF aceita entradas válidas.

**Pré-condições:**
- Acesso à aplicação em http://analista-teste.seatecnologia.com.br/

**Passos:**
1. Acessar o formulário de cadastro de funcionário
2. Inserir CPF válido sem formatação (ex: "12345678909")
3. Verificar aceitação
4. Inserir CPF válido com formatação (ex: "123.456.789-09")
5. Verificar aceitação
6. Inserir diferentes CPFs válidos
7. Verificar aceitação

**Resultado Esperado:**
- Todos os CPFs válidos devem ser aceitos sem mensagens de erro

**Critérios de Aceitação:**
- Nenhuma mensagem de erro exibida
- Campo mantém o valor inserido (possivelmente formatado)
- Possibilidade de prosseguir com o formulário

**Prioridade:** Alta

### CT-FORM-004: Validação de CPF - Cenários Inválidos

**Objetivo:** Verificar se o campo de CPF rejeita entradas inválidas.

**Pré-condições:**
- Acesso à aplicação em http://analista-teste.seatecnologia.com.br/

**Passos:**
1. Acessar o formulário de cadastro de funcionário
2. Inserir CPF com menos de 11 dígitos (ex: "1234567890")
3. Verificar rejeição
4. Inserir CPF com mais de 11 dígitos (ex: "123456789012")
5. Verificar rejeição
6. Inserir CPF com dígitos verificadores inválidos (ex: "12345678900")
7. Verificar rejeição
8. Inserir CPF com caracteres não numéricos (ex: "123.456.78A-09")
9. Verificar rejeição
10. Inserir CPF com dígitos repetidos (ex: "11111111111")
11. Verificar rejeição
12. Deixar o campo em branco
13. Verificar rejeição

**Resultado Esperado:**
- Todos os CPFs inválidos devem ser rejeitados com mensagens de erro apropriadas

**Critérios de Aceitação:**
- Mensagem de erro clara e específica
- Impossibilidade de prosseguir com o formulário até correção
- Foco mantido no campo com erro

**Prioridade:** Alta

### CT-FORM-005: Validação de Data - Cenários Válidos

**Objetivo:** Verificar se o campo de data aceita entradas válidas.

**Pré-condições:**
- Acesso à aplicação em http://analista-teste.seatecnologia.com.br/

**Passos:**
1. Acessar o formulário de cadastro de funcionário
2. Inserir data atual
3. Verificar aceitação
4. Inserir data passada
5. Verificar aceitação
6. Inserir data futura (se aplicável ao contexto)
7. Verificar aceitação
8. Inserir data em diferentes formatos aceitos
9. Verificar aceitação

**Resultado Esperado:**
- Todas as datas válidas devem ser aceitas sem mensagens de erro

**Critérios de Aceitação:**
- Nenhuma mensagem de erro exibida
- Campo mantém o valor inserido (possivelmente formatado)
- Possibilidade de prosseguir com o formulário

**Prioridade:** Média

### CT-FORM-006: Validação de Data - Cenários Inválidos

**Objetivo:** Verificar se o campo de data rejeita entradas inválidas.

**Pré-condições:**
- Acesso à aplicação em http://analista-teste.seatecnologia.com.br/

**Passos:**
1. Acessar o formulário de cadastro de funcionário
2. Inserir data inexistente (ex: 30/02/2023)
3. Verificar rejeição
4. Inserir data em formato inválido
5. Verificar rejeição
6. Inserir caracteres não numéricos
7. Verificar rejeição
8. Deixar o campo em branco
9. Verificar rejeição

**Resultado Esperado:**
- Todas as datas inválidas devem ser rejeitadas com mensagens de erro apropriadas

**Critérios de Aceitação:**
- Mensagem de erro clara e específica
- Impossibilidade de prosseguir com o formulário até correção
- Foco mantido no campo com erro

**Prioridade:** Média

### CT-FORM-007: Validação de Data - Cenários Inválidos

**Objetivo:** Verificar se o campo de data rejeita entradas inválidas.

**Pré-condições:**
- Acesso à aplicação em http://analista-teste.seatecnologia.com.br/

**Passos:**
1. Acessar o formulário de cadastro de funcionário
2. Inserir data futura (ex: 30/12/2030)
3. Verificar rejeição
4. Inserir data em formato inválido
5. Verificar rejeição
6. Inserir caracteres não numéricos
7. Verificar rejeição
8. Deixar o campo em branco
9. Verificar rejeição

**Resultado Esperado:**
- Todas as datas inválidas devem ser rejeitadas com mensagens de erro apropriadas

**Critérios de Aceitação:**
- Mensagem de erro clara e específica
- Impossibilidade de prosseguir com o formulário até correção
- Foco mantido no campo com erro

**Prioridade:** Média

## 3. Testes de Adição de EPI e Atividades

### CT-EPI-001: Adição de EPI

**Objetivo:** Verificar se é possível adicionar equipamentos de proteção individual (EPI) ao cadastro de funcionário.

**Pré-condições:**
- Acesso à aplicação em http://analista-teste.seatecnologia.com.br/

**Passos:**
1. Acessar o formulário de cadastro de funcionário
2. Preencher os campos obrigatórios
3. Localizar a seção de adição de EPI
4. Adicionar um EPI
5. Verificar se o EPI foi adicionado à lista
6. Adicionar múltiplos EPIs
7. Verificar se todos os EPIs foram adicionados à lista

**Resultado Esperado:**
- Deve ser possível adicionar um ou mais EPIs ao cadastro de funcionário

**Critérios de Aceitação:**
- EPIs adicionados aparecem na lista
- Contagem de EPIs é atualizada corretamente
- Informações dos EPIs são exibidas corretamente

**Prioridade:** Alta

### CT-EPI-002: Remoção de EPI

**Objetivo:** Verificar se é possível remover equipamentos de proteção individual (EPI) do cadastro de funcionário.

**Pré-condições:**
- Acesso à aplicação em http://analista-teste.seatecnologia.com.br/
- Pelo menos um EPI adicionado ao cadastro

**Passos:**
1. Acessar o formulário de cadastro de funcionário
2. Adicionar um ou mais EPIs
3. Localizar a opção de remoção de EPI
4. Remover um EPI
5. Verificar se o EPI foi removido da lista
6. Remover todos os EPIs
7. Verificar se a lista está vazia

**Resultado Esperado:**
- Deve ser possível remover EPIs do cadastro de funcionário

**Critérios de Aceitação:**
- EPIs removidos não aparecem mais na lista
- Contagem de EPIs é atualizada corretamente
- Feedback visual da remoção é apresentado

**Prioridade:** Alta

### CT-ATIV-001: Adição de Atividades

**Objetivo:** Verificar se é possível adicionar atividades ao cadastro de funcionário.

**Pré-condições:**
- Acesso à aplicação em http://analista-teste.seatecnologia.com.br/

**Passos:**
1. Acessar o formulário de cadastro de funcionário
2. Preencher os campos obrigatórios
3. Localizar a seção de adição de atividades
4. Adicionar uma atividade
5. Verificar se a atividade foi adicionada à lista
6. Adicionar múltiplas atividades
7. Verificar se todas as atividades foram adicionadas à lista

**Resultado Esperado:**
- Deve ser possível adicionar uma ou mais atividades ao cadastro de funcionário

**Critérios de Aceitação:**
- Atividades adicionadas aparecem na lista
- Contagem de atividades é atualizada corretamente
- Informações das atividades são exibidas corretamente

**Prioridade:** Alta

### CT-ATIV-002: Remoção de Atividades

**Objetivo:** Verificar se é possível remover atividades do cadastro de funcionário.

**Pré-condições:**
- Acesso à aplicação em http://analista-teste.seatecnologia.com.br/
- Pelo menos uma atividade adicionada ao cadastro

**Passos:**
1. Acessar o formulário de cadastro de funcionário
2. Adicionar uma ou mais atividades
3. Localizar a opção de remoção de atividade
4. Remover uma atividade
5. Verificar se a atividade foi removida da lista
6. Remover todas as atividades
7. Verificar se a lista está vazia

**Resultado Esperado:**
- Deve ser possível remover atividades do cadastro de funcionário

**Critérios de Aceitação:**
- Atividades removidas não aparecem mais na lista
- Contagem de atividades é atualizada corretamente
- Feedback visual da remoção é apresentado

**Prioridade:** Alta

## 4. Testes de Persistência e Recuperação de Dados

### CT-PERS-001: Persistência de Dados do Funcionário

**Objetivo:** Verificar se os dados do funcionário são corretamente salvos no sistema.

**Pré-condições:**
- Acesso à aplicação em http://analista-teste.seatecnologia.com.br/

**Passos:**
1. Acessar o formulário de cadastro de funcionário
2. Preencher todos os campos obrigatórios com dados válidos
3. Adicionar EPIs (se aplicável)
4. Adicionar atividades (se aplicável)
5. Salvar o cadastro
6. Verificar se uma mensagem de sucesso é exibida
7. Navegar para a lista de funcionários
8. Verificar se o funcionário cadastrado aparece na lista

**Resultado Esperado:**
- Os dados do funcionário devem ser corretamente salvos e o registro deve aparecer na lista

**Critérios de Aceitação:**
- Mensagem de sucesso ao salvar
- Funcionário visível na lista após o cadastro
- Todos os dados inseridos foram salvos corretamente

**Prioridade:** Alta

### CT-PERS-002: Persistência de Dados com Campos Opcionais

**Objetivo:** Verificar se os dados do funcionário são corretamente salvos quando apenas os campos obrigatórios são preenchidos.

**Pré-condições:**
- Acesso à aplicação em http://analista-teste.seatecnologia.com.br/

**Passos:**
1. Acessar o formulário de cadastro de funcionário
2. Preencher apenas os campos obrigatórios com dados válidos
3. Deixar os campos opcionais em branco
4. Salvar o cadastro
5. Verificar se uma mensagem de sucesso é exibida
6. Navegar para a lista de funcionários
7. Verificar se o funcionário cadastrado aparece na lista

**Resultado Esperado:**
- Os dados do funcionário devem ser corretamente salvos mesmo sem os campos opcionais

**Critérios de Aceitação:**
- Mensagem de sucesso ao salvar
- Funcionário visível na lista após o cadastro
- Campos obrigatórios salvos corretamente
- Ausência de erros relacionados aos campos opcionais

**Prioridade:** Média

### CT-RECUP-001: Recuperação de Dados do Funcionário

**Objetivo:** Verificar se os dados do funcionário são corretamente recuperados ao visualizar um registro existente.

**Pré-condições:**
- Acesso à aplicação em http://analista-teste.seatecnologia.com.br/
- Pelo menos um funcionário cadastrado no sistema

**Passos:**
1. Acessar a lista de funcionários
2. Localizar um funcionário cadastrado
3. Acessar os detalhes do funcionário
4. Verificar se todos os dados são exibidos corretamente
5. Verificar se os EPIs são exibidos corretamente (se aplicável)
6. Verificar se as atividades são exibidas corretamente (se aplicável)

**Resultado Esperado:**
- Todos os dados do funcionário devem ser corretamente recuperados e exibidos

**Critérios de Aceitação:**
- Todos os campos preenchidos são exibidos com os valores corretos
- EPIs e atividades são listados corretamente
- Não há dados faltando ou incorretos

**Prioridade:** Alta

## 5. Testes de Edição e Exclusão de Registros

### CT-EDIT-001: Edição de Dados do Funcionário

**Objetivo:** Verificar se é possível editar os dados de um funcionário existente.

**Pré-condições:**
- Acesso à aplicação em http://analista-teste.seatecnologia.com.br/
- Pelo menos um funcionário cadastrado no sistema

**Passos:**
1. Acessar a lista de funcionários
2. Localizar um funcionário cadastrado
3. Acessar a opção de edição (geralmente através do menu de elipses (...))
4. Modificar alguns campos do cadastro
5. Salvar as alterações
6. Verificar se uma mensagem de sucesso é exibida
7. Acessar novamente os detalhes do funcionário
8. Verificar se as alterações foram aplicadas corretamente

**Resultado Esperado:**
- Deve ser possível editar os dados de um funcionário e as alterações devem ser salvas corretamente

**Critérios de Aceitação:**
- Mensagem de sucesso ao salvar as alterações
- Alterações visíveis ao acessar novamente os detalhes
- Todos os campos editados foram atualizados corretamente

**Prioridade:** Alta

### CT-EDIT-002: Edição de EPIs e Atividades

**Objetivo:** Verificar se é possível editar EPIs e atividades de um funcionário existente.

**Pré-condições:**
- Acesso à aplicação em http://analista-teste.seatecnologia.com.br/
- Pelo menos um funcionário cadastrado com EPIs e atividades

**Passos:**
1. Acessar a lista de funcionários
2. Localizar um funcionário com EPIs e atividades
3. Acessar a opção de edição
4. Adicionar novos EPIs
5. Remover EPIs existentes
6. Adicionar novas atividades
7. Remover atividades existentes
8. Salvar as alterações
9. Verificar se uma mensagem de sucesso é exibida
10. Acessar novamente os detalhes do funcionário
11. Verificar se as alterações em EPIs e atividades foram aplicadas corretamente

**Resultado Esperado:**
- Deve ser possível editar EPIs e atividades de um funcionário e as alterações devem ser salvas corretamente

**Critérios de Aceitação:**
- Mensagem de sucesso ao salvar as alterações
- Novos EPIs e atividades visíveis nos detalhes
- EPIs e atividades removidos não aparecem mais
- Contagens atualizadas corretamente

**Prioridade:** Alta

### CT-EXCL-001: Exclusão de Funcionário

**Objetivo:** Verificar se é possível excluir um funcionário do sistema.

**Pré-condições:**
- Acesso à aplicação em http://analista-teste.seatecnologia.com.br/
- Pelo menos um funcionário cadastrado no sistema

**Passos:**
1. Acessar a lista de funcionários
2. Localizar um funcionário cadastrado
3. Acessar a opção de exclusão (geralmente através do menu de elipses (...))
4. Confirmar a exclusão (se solicitado)
5. Verificar se uma mensagem de sucesso é exibida
6. Verificar se o funcionário não aparece mais na lista

**Resultado Esperado:**
- Deve ser possível excluir um funcionário e o registro deve ser removido do sistema

**Critérios de Aceitação:**
- Mensagem de sucesso ao excluir
- Funcionário não aparece mais na lista
- Não é possível acessar os detalhes do funcionário excluído

**Prioridade:** Alta

### CT-EXCL-002: Cancelamento de Exclusão

**Objetivo:** Verificar se é possível cancelar a exclusão de um funcionário.

**Pré-condições:**
- Acesso à aplicação em http://analista-teste.seatecnologia.com.br/
- Pelo menos um funcionário cadastrado no sistema

**Passos:**
1. Acessar a lista de funcionários
2. Localizar um funcionário cadastrado
3. Acessar a opção de exclusão
4. Cancelar a exclusão (se houver opção)
5. Verificar se o funcionário ainda aparece na lista

**Resultado Esperado:**
- Deve ser possível cancelar a exclusão de um funcionário e o registro deve permanecer no sistema

**Critérios de Aceitação:**
- Funcionário ainda aparece na lista após cancelamento
- Não há alterações nos dados do funcionário
- Não há mensagens de erro

**Prioridade:** Média

## 6. Testes de Navegação

### CT-NAV-001: Navegação entre Páginas

**Objetivo:** Verificar se a navegação entre as diferentes páginas da aplicação funciona corretamente.

**Pré-condições:**
- Acesso à aplicação em http://analista-teste.seatecnologia.com.br/

**Passos:**
1. Acessar a página inicial
2. Navegar para a página de cadastro de funcionário
3. Verificar se a página carrega corretamente
4. Navegar para a lista de funcionários
5. Verificar se a página carrega corretamente
6. Navegar para outras páginas disponíveis
7. Verificar se todas as páginas carregam corretamente

**Resultado Esperado:**
- Deve ser possível navegar entre todas as páginas da aplicação sem erros

**Critérios de Aceitação:**
- Todas as páginas carregam sem erros
- Elementos de navegação funcionam corretamente
- Não há links quebrados

**Prioridade:** Alta

### CT-NAV-002: Navegação para Componente "Em Breve"

**Objetivo:** Verificar se os links para funcionalidades futuras direcionam para o componente "Em Breve".

**Pré-condições:**
- Acesso à aplicação em http://analista-teste.seatecnologia.com.br/

**Passos:**
1. Acessar a página inicial
2. Identificar links para funcionalidades futuras
3. Clicar em cada um desses links
4. Verificar se todos direcionam para o componente "Em Breve"

**Resultado Esperado:**
- Todos os links para funcionalidades futuras devem direcionar para o componente "Em Breve"

**Critérios de Aceitação:**
- Componente "Em Breve" é exibido corretamente
- Mensagem informativa sobre funcionalidade futura é apresentada
- Possibilidade de retornar à navegação anterior

**Prioridade:** Média

### CT-NAV-003: Navegação com Histórico do Navegador

**Objetivo:** Verificar se a navegação utilizando os botões de voltar e avançar do navegador funciona corretamente.

**Pré-condições:**
- Acesso à aplicação em http://analista-teste.seatecnologia.com.br/

**Passos:**
1. Acessar a página inicial
2. Navegar para a página de cadastro de funcionário
3. Navegar para a lista de funcionários
4. Utilizar o botão "Voltar" do navegador
5. Verificar se retorna para a página de cadastro
6. Utilizar o botão "Voltar" novamente
7. Verificar se retorna para a página inicial
8. Utilizar o botão "Avançar" do navegador
9. Verificar se avança para a página de cadastro

**Resultado Esperado:**
- A navegação utilizando os botões de voltar e avançar do navegador deve funcionar corretamente

**Critérios de Aceitação:**
- Páginas corretas são exibidas ao utilizar os botões de navegação
- Estado das páginas é mantido (formulários preenchidos, seleções, etc.)
- Não há erros ou comportamentos inesperados

**Prioridade:** Média

## 7. Testes de Compatibilidade com Navegadores

### CT-COMP-001: Compatibilidade com Google Chrome

**Objetivo:** Verificar se a aplicação funciona corretamente no navegador Google Chrome.

**Pré-condições:**
- Acesso à aplicação em http://analista-teste.seatecnologia.com.br/
- Navegador Google Chrome instalado (versão mais recente)

**Passos:**
1. Acessar a aplicação no Google Chrome
2. Verificar a renderização de todos os elementos visuais
3. Testar o cadastro de um funcionário
4. Testar a edição de um funcionário
5. Testar a exclusão de um funcionário
6. Testar a navegação entre páginas

**Resultado Esperado:**
- A aplicação deve funcionar corretamente no Google Chrome sem erros visuais ou funcionais

**Critérios de Aceitação:**
- Todos os elementos são renderizados corretamente
- Todas as funcionalidades operam sem erros
- Desempenho adequado

**Prioridade:** Alta

### CT-COMP-002: Compatibilidade com Mozilla Firefox

**Objetivo:** Verificar se a aplicação funciona corretamente no navegador Mozilla Firefox.

**Pré-condições:**
- Acesso à aplicação em http://analista-teste.seatecnologia.com.br/
- Navegador Mozilla Firefox instalado (versão mais recente)

**Passos:**
1. Acessar a aplicação no Mozilla Firefox
2. Verificar a renderização de todos os elementos visuais
3. Testar o cadastro de um funcionário
4. Testar a edição de um funcionário
5. Testar a exclusão de um funcionário
6. Testar a navegação entre páginas

**Resultado Esperado:**
- A aplicação deve funcionar corretamente no Mozilla Firefox sem erros visuais ou funcionais

**Critérios de Aceitação:**
- Todos os elementos são renderizados corretamente
- Todas as funcionalidades operam sem erros
- Desempenho adequado

**Prioridade:** Alta

### CT-COMP-003: Compatibilidade com Microsoft Edge

**Objetivo:** Verificar se a aplicação funciona corretamente no navegador Microsoft Edge.

**Pré-condições:**
- Acesso à aplicação em http://analista-teste.seatecnologia.com.br/
- Navegador Microsoft Edge instalado (versão mais recente)

**Passos:**
1. Acessar a aplicação no Microsoft Edge
2. Verificar a renderização de todos os elementos visuais
3. Testar o cadastro de um funcionário
4. Testar a edição de um funcionário
5. Testar a exclusão de um funcionário
6. Testar a navegação entre páginas

**Resultado Esperado:**
- A aplicação deve funcionar corretamente no Microsoft Edge sem erros visuais ou funcionais

**Critérios de Aceitação:**
- Todos os elementos são renderizados corretamente
- Todas as funcionalidades operam sem erros
- Desempenho adequado

**Prioridade:** Alta

### CT-COMP-004: Compatibilidade com Dispositivos Móveis

**Objetivo:** Verificar se a aplicação funciona corretamente em navegadores de dispositivos móveis.

**Pré-condições:**
- Acesso à aplicação em http://analista-teste.seatecnologia.com.br/
- Dispositivo móvel ou emulador com navegador instalado

**Passos:**
1. Acessar a aplicação em um dispositivo móvel
2. Verificar a renderização de todos os elementos visuais
3. Testar o cadastro de um funcionário
4. Testar a edição de um funcionário
5. Testar a exclusão de um funcionário
6. Testar a navegação entre páginas
7. Testar a usabilidade em tela sensível ao toque

**Resultado Esperado:**
- A aplicação deve funcionar corretamente em dispositivos móveis sem erros visuais ou funcionais

**Critérios de Aceitação:**
- Todos os elementos são renderizados corretamente
- Todas as funcionalidades operam sem erros
- Interface adaptada para tela sensível ao toque
- Desempenho adequado

**Prioridade:** Média
