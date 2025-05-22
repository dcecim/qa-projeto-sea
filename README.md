# Projeto de Testes Automatizados - SEA Tecnologia

Este projeto contém testes automatizados para a aplicação web da SEA Tecnologia, focando na qualidade e conformidade com os requisitos e protótipos fornecidos. [       Requisitos mínimos e protótipo funcional
📄 A URL da aplicação é:  http://analista-teste.seatecnologia.com.br/;  
Os requisitos disponibilizados pela organização são apenas esses:
Referências de Design e Funcionalidades:
- Conformidade com o Protótipo: Verifique a aplicação em comparação com o protótipo disponível em https://tinyurl.com/yl58hs4m. É crucial que a aplicação reflita o design e a estrutura propostos no protótipo.
Elementos de Design a Serem Avaliados:
-  Fonte: Verifique se a fonte usada na aplicação corresponde à especificada no protótipo.
-  Cores: As cores da aplicação devem ser idênticas às do protótipo.
-  Itens: Todos os itens (botões, campos de formulário, menus, etc.) devem estar presentes conforme o design proposto.
Funcionalidades e Comportamentos a Serem Testados:
- Formulário: Avalie as validações implementadas no formulário, incluindo a verificação do CPF e da data, bem como as funcionalidades para adicionar EPI (Equipamento de Proteção Individual) e atividades.
- Persistência de Dados: Certifique-se de que as informações dos funcionários sejam corretamente salvas (persistidas) no sistema.
- Recuperação de Dados: Teste se as informações de um funcionário podem ser recuperadas sem erros.
- Edição e Exclusão: Verifique a funcionalidade que permite editar e excluir registros de funcionários, geralmente acessível através de um menu de opções (indicado por elipses (...)).
- Navegação: Teste os links para assegurar que eles conduzam às etapas e itens de menu corretos. Todos os links devem levar ao componente "Em breve", indicando funcionalidades que serão implementadas no futuro.
- Compatibilidade com Navegadores: A aplicação deve funcionar corretamente nos principais navegadores web, garantindo a acessibilidade para uma ampla gama de usuários.
]

## Visão Geral

O objetivo principal é garantir a validação de dados de entrada, a funcionalidade do sistema e a conformidade visual, utilizando Python com Playwright para automação de testes E2E. [cite: 1, 6, 10, 14]

## Estrutura do Projeto

* `docs/`: Contém a documentação do projeto, incluindo o plano de testes e os casos de teste. [cite: 7]
* `tests/`: Armazena os scripts de testes automatizados. [cite: 7]
* `utils/`: Funções auxiliares e helpers. [cite: 7]
* `.github/workflows/`: (Opcional) Configurações para Integração Contínua (CI/CD) com GitHub Actions. [cite: 7]
* `requirements.txt`: Lista de dependências do projeto. [cite: 7]
* `README.md`: Este arquivo. [cite: 7]

## Configuração do Ambiente

1.  **Pré-requisitos**:
    * Python 3.8+ instalado.
    * Navegadores instalados (Chromium, Firefox, WebKit serão baixados automaticamente pelo Playwright).

2.  **Clone o repositório**:
    ```bash
    git clone [https://github.com/seu-usuario/qa-projeto-sea.git](https://github.com/seu-usuario/qa-projeto-sea.git)
    cd qa-projeto-sea
    ```

3.  **Crie e ative um ambiente virtual (recomendado)**:
    ```bash
    python -m venv venv
    # No Windows
    .\venv\Scripts\activate
    # No macOS/Linux
    source venv/bin/activate
    ```

4.  **Instale as dependências**:
    ```bash
    pip install -r requirements.txt
    playwright install
    ```

## Executando os Testes

Para executar todos os testes:

```bash
pytest