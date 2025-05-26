# Projeto de QA Automatizado - SEA Tecnologia

Este repositório contém um projeto estruturado de testes para a aplicação disponível em http://analista-teste.seatecnologia.com.br/, seguindo as diretrizes da ISO/IEC/IEEE 29119 e as boas práticas do ISTQB.

## Estrutura do Projeto

```
/qa-projeto-sea/
├── docs/
│   ├── plano-de-testes.md
│   └── casos-de-teste.md
├── tests/
|   ├── results/
|   ├── screenshots/
│   ├── test_conformidade.py
│   └── test_validacao.py
├── utils/
│   └── helpers.py
├── requirements.txt
└── README.md
```

## Sobre o Projeto

Este projeto foi desenvolvido como parte de um desafio de teste para avaliar a aplicação web da SEA Tecnologia. O objetivo é verificar a conformidade com o protótipo, validar as funcionalidades do formulário e garantir a qualidade geral da aplicação.

### Escopo do Teste

- **Testes Manuais**: Documentação detalhada de casos de teste para todas as funcionalidades
- **Testes Automatizados**: Scripts para validação de nome/CPF e conformidade com o protótipo

### Requisitos da Aplicação

A aplicação deve ser testada considerando:

1. **Conformidade com o Protótipo**: Verificação de design, cores, fontes e elementos conforme o protótipo disponível em https://tinyurl.com/yl58hs4m
2. **Validação de Formulários**: Verificação de campos como nome, CPF e data
3. **Funcionalidades CRUD**: Persistência, recuperação, edição e exclusão de registros
4. **Navegação**: Verificação de links e fluxos de navegação
5. **Compatibilidade**: Funcionamento em diferentes navegadores

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

## Execução dos Testes Automatizados

```bash
pytest tests/
```

Para gerar relatório HTML:
```bash
pytest tests/ --html=tests/results/report.html --css=assets/custom_style.css  # ou
pytest tests/ --headed --html=tests/results/report.html --self-contained-html
```

## Documentação

- [Plano de Testes](docs/plano-de-testes.md): Estratégia, escopo e abordagem de testes
- [Casos de Teste](docs/casos-de-teste.md): Casos de teste detalhados para execução manual
- [Relatório de Teste](docs/relatorio_testes_gerado.md): Relatório detalhados sobre execução de teste com analise da situaçã

## Tecnologias Utilizadas

- **Playwright**: Framework para automação de testes em navegadores
- **pytest**: Framework de testes para Python
- **Python**: Linguagem de programação principal

## Autor

[`Divino Cecim da Silva`]