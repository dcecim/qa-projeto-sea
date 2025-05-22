# Casos de Teste - Aplicação SEA Tecnologia

Este documento detalha os casos de teste para a aplicação da SEA Tecnologia, com foco nas funcionalidades e validações.

## Módulo: Cadastro de Empregado

### CT-001: Validação de Campo "Nome do Empregado" - Cenário Positivo

* **ID**: CT-001
* **Módulo**: Cadastro de Empregado
* **Funcionalidade**: Validação de Nome
* **Pré-condições**:
    * Usuário está na tela de cadastro de empregado.
* **Passos**:
    1.  Preencher o campo "Nome do Empregado" com um nome válido (ex: "João da Silva"."Li Nan Ci", "Otávio Oliveira Santos","John Bitarmill Sênior). [cite: 4]
    2.  Preencher os demais campos obrigatórios com dados válidos (CPF, Data, etc.). [cite: 14]
    3.  Clicar no botão "Salvar".
* **Resultado Esperado**:
    * A aplicação **não** deve exibir mensagem de erro para o campo "Nome do Empregado".
    * O cadastro **deve ser realizado com sucesso** ou, se houver outras validações pendentes, a **mensagem de erro deve ser referente a elas e não ao nome**.
    * O nome deve estar em conformidade com as regras: Mínimo 2 caracteres, máximo 120 caracteres, apenas letras (acentos permitidos), traços e espaços opcionais, sem dígitos, caracteres especiais ou palavras reservadas de PL/SQL. [cite: 4]

### CT-002: Validação de Campos - Cenário Negativo

* **ID**: CT-002
* **Módulo**: Cadastro de Empregado
* **Funcionalidade**: Validação de Campos 
* **Pré-condições**:
    * Usuário está na tela de cadastro de empregado.
* **Passos**:
    1.  Não preencher nenhum campo.
    3.  Clicar no botão "Salvar".
* **Resultado Esperado**:
    * A aplicação **deve exibir mensagem de erro para o campo "Nome do Empregado"**.
    * O cadastro **não deve ser realizado com sucesso**.
    * O nome deve estar em conformidade com as regras: Mínimo 2 caracteres, máximo 120 caracteres, apenas letras (acentos permitidos), traços e espaços opcionais, sem dígitos, caracteres especiais ou palavras reservadas de PL/SQL. [cite: 4]


### CT-003: Validação de Campo "Nome do Empregado" - Nome Curto (Negativo)

* **ID**: CT-003
* **Módulo**: Cadastro de Empregado
* **Funcionalidade**: Validação de Nome
* **Pré-condições**:
    * Usuário está na tela de cadastro de empregado.
* **Passos**:
    1.  Preencher o campo "Nome do Empregado" com um nome com menos de 2 caracteres (ex: "J"). [cite: 4]
    2.  Preencher os demais campos obrigatórios com dados válidos.
    3.  Clicar no botão "Salvar".
* **Resultado Esperado**:
    * A aplicação deve exibir uma mensagem de erro indicando que o nome é muito curto.

### CT-004: Validação de Campo "Nome do Empregado" - Nome Longo (Negativo)

* **ID**: CT-004
* **Módulo**: Cadastro de Empregado
* **Funcionalidade**: Validação de Nome
* **Pré-condições**:
    * Usuário está na tela de cadastro de empregado.
* **Passos**:
    1.  Preencher o campo "Nome do Empregado" com um nome com mais de 120 caracteres. [cite: 4]
    2.  Preencher os demais campos obrigatórios com dados válidos.
    3.  Clicar no botão "Salvar".
* **Resultado Esperado**:
    * A aplicação deve exibir uma mensagem de erro indicando que o nome é muito longo.

### CT-005: Validação de Campo "Nome do Empregado" - Com Dígitos (Negativo)

* **ID**: CT-005
* **Módulo**: Cadastro de Empregado
* **Funcionalidade**: Validação de Nome
* **Pré-condições**:
    * Usuário está na tela de cadastro de empregado.
* **Passos**:
    1.  Preencher o campo "Nome do Empregado" com um nome contendo dígitos (ex: "João123"). [cite: 4]
    2.  Preencher os demais campos obrigatórios com dados válidos.
    3.  Clicar no botão "Salvar".
* **Resultado Esperado**:
    * A aplicação deve exibir uma mensagem de erro indicando que o nome não pode conter dígitos.

### CT-006: Validação de Campo "Nome do Empregado" - Com Caracteres Especiais (Negativo)

* **ID**: CT-006
* **Módulo**: Cadastro de Empregado
* **Funcionalidade**: Validação de Nome
* **Pré-condições**:
    * Usuário está na tela de cadastro de empregado.
* **Passos**:
    1.  Preencher o campo "Nome do Empregado" com um nome contendo caracteres especiais (ex: "João!@#"). [cite: 4]
    2.  Preencher os demais campos obrigatórios com dados válidos.
    3.  Clicar no botão "Salvar".
* **Resultado Esperado**:
    * A aplicação deve exibir uma mensagem de erro indicando que o nome não pode conter caracteres especiais.

### CT-007: Validação de Campo "Nome do Empregado" - Com Palavra Reservada PL/SQL (Negativo)

* **ID**: CT-007
* **Módulo**: Cadastro de Empregado
* **Funcionalidade**: Validação de Nome
* **Pré-condições**:
    * Usuário está na tela de cadastro de empregado.
* **Passos**:
    1.  Preencher o campo "Nome do Empregado" com uma palavra reservada de PL/SQL (ex: "SELECT * FROM"). [cite: 4]
    2.  Preencher os demais campos obrigatórios com dados válidos.
    3.  Clicar no botão "Salvar".
* **Resultado Esperado**:
    * A aplicação deve exibir uma mensagem de erro ou impedir o envio, indicando que o nome contém termos Negativos.

## Módulo: Login

### CT-008: Login com Credenciais Válidas (Não será implementado, pois a aplicação ainda não possui modulo de Login)

* **ID**: CT-008
* **Módulo**: Login
* **Funcionalidade**: Acesso ao sistema
* **Pré-condições**:
    * Usuário está na tela de login.
    * Credenciais válidas conhecidas (usuário e senha).
* **Passos**:
    1.  Preencher o campo de usuário com credenciais válidas.
    2.  Preencher o campo de senha com credenciais válidas.
    3.  Clicar no botão "Entrar".
* **Resultado Esperado**:
    * Usuário é redirecionado para a página inicial ou dashboard da aplicação.

### CT-009: Login com Credenciais Inválidas (Não será implementado, pois a aplicação ainda não possui modulo de Login)

* **ID**: CT-009
* **Módulo**: Login
* **Funcionalidade**: Acesso ao sistema
* **Pré-condições**:
    * Usuário está na tela de login.
* **Passos**:
    1.  Preencher o campo de usuário com credenciais inválidas.
    2.  Preencher o campo de senha com credenciais inválidas.
    3.  Clicar no botão "Entrar".
* **Resultado Esperado**:
    * A aplicação exibe uma mensagem de erro clara indicando que as credenciais são inválidas.
    * O usuário permanece na tela de login.