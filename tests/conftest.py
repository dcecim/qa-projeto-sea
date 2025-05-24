import pytest
from playwright.sync_api import sync_playwright, Page, Browser, BrowserContext
import os

# Variável global para armazenar dados de empregados criados para limpeza.
# Isso permite que a fixture de teardown acesse os dados gerados durante os testes.
pytest.global_data_for_cleanup = []

# Define uma fixture 'browser' com escopo de classe
@pytest.fixture(scope="class")
def browser_class(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) # Mantenha headless=False para ver o browser
        yield browser
        browser.close()

# Define uma fixture 'context_class' com escopo de classe
@pytest.fixture(scope="class")
def context_class(browser_class: Browser):
    context = browser_class.new_context()
    yield context
    context.close()

# Redefine a fixture 'page' para usar o 'context_class' e ter escopo de função
@pytest.fixture(scope="function")
def page(context_class: BrowserContext) -> Page:
    page = context_class.new_page()
    yield page
    page.close()

# Opcional: Configuração para argumentos do contexto do navegador
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
    }

# --- NOVA FIXTURE PARA LIMPEZA PÓS-SESSÃO (com autouse=True para executar sempre) ---
@pytest.fixture(scope="session", autouse=True)
def cleanup_after_all_tests(request):
    """
    Fixture para executar limpeza após todos os testes da sessão.
    Isso ajuda a remover registros de testes que falharam na exclusão, por exemplo.
    """
    # O código antes do 'yield' é o setup da fixture
    yield # Onde os testes são executados

    # O código após o 'yield' é o teardown (executado após todos os testes, mesmo em caso de falha)
    print("\n--- Iniciando limpeza de dados de teste ---")
    if pytest.global_data_for_cleanup:
        # Re-inicia o Playwright para a limpeza, se o navegador original já fechou
        with sync_playwright() as p:
            browser_cleanup = p.chromium.launch(headless=True) # Limpeza pode ser headless
            page_cleanup = browser_cleanup.new_page()
            
            # Importa a função de limpeza do arquivo de teste
            # Isso é necessário porque a fixture está em conftest e a função está no test_file
            from tests.test_cadastro_empregado import limpar_cadastro_final_conftest

            for dados_empregado in pytest.global_data_for_cleanup:
                try:
                    limpar_cadastro_final_conftest(page_cleanup, dados_empregado)
                except Exception as e:
                    print(f"ERRO CRÍTICO NA LIMPEZA: Falha ao tentar limpar o empregado {dados_empregado['nome']} (CPF: {dados_empregado['cpf']}): {e}")
            
            browser_cleanup.close()
    else:
        print("Nenhum empregado para limpar.")
    print("--- Limpeza de dados de teste concluída ---")

# --- Funções de configuração de pytest_html e screenshots (para informações de relatório) ---
def pytest_configure(config):
    # Cria diretório para screenshots se não existir, relativo ao rootdir do pytest
    screenshots_dir = os.path.join(config.rootdir, "tests", "screenshots") 
    os.makedirs(screenshots_dir, exist_ok=True)
    
    print("\nIniciando testes automatizados para o projeto SEA Tecnologia")
    print("URL da aplicação: https://analista-teste.seatecnologia.com.br/")
    print("URL do protótipo: https://tinyurl.com/yl58hs4m")

def pytest_sessionfinish(session, exitstatus):
    print("\n===== Resumo da Execução de Testes =====")
    print(f"Total de testes executados: {session.testscollected}")
    print(f"Testes com sucesso: {session.testscollected - session.testsfailed}")
    print(f"Testes com falha: {session.testsfailed}")
    
    if session.testsfailed == 0:
        print("\n✅ Todos os testes foram executados com sucesso!")
    else:
        print(f"\n⚠️ {session.testsfailed} teste(s) falharam. Verifique os logs para mais detalhes.")
    
    print(f"\nEvidências de teste disponíveis em: {os.path.join(session.rootdir, 'tests', 'screenshots')}")
    print("=======================================\n")
    