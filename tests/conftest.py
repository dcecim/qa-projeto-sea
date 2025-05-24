import pytest
from playwright.sync_api import sync_playwright, Page, Browser, BrowserContext
import os
import datetime # Para timestamps nas screenshots de falha do conftest

# URL da aplicação - DEFINIDA AQUI
APP_URL = "http://analista-teste.seatecnologia.com.br/"

# Variável global para armazenar dados de empregados criados para limpeza.
pytest.global_data_for_cleanup = []

# --- Fixtures do Playwright (sem alteração) ---
@pytest.fixture(scope="class")
def browser_class(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="class")
def context_class(browser_class: Browser):
    context = browser_class.new_context()
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context_class: BrowserContext) -> Page:
    page = context_class.new_page()
    yield page
    page.close()

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
    }

# --- FUNÇÃO DE LIMPEZA (já movida para conftest.py) ---
def limpar_cadastro_conftest_impl(page_cleanup: Page, dados_empregado: dict):
    nome_empregado = dados_empregado["nome"]
    cpf_empregado = dados_empregado["cpf"]

    print(f"INFO: [LIMPEZA NO CONFTEST] Tentando limpar o cadastro de '{nome_empregado}' (CPF: {cpf_empregado})...")
    try:
        page_cleanup.goto(APP_URL) # Usa o APP_URL definido no conftest
        page_cleanup.wait_for_load_state("networkidle")
        
        empregado_locator_unico = page_cleanup.locator(
            f'div.c-bXqUbA:has-text("{nome_empregado}"):has(div.c-iYbcAK:has-text("{cpf_empregado}"))'
        ).first
        
        dots_locator_limpeza = empregado_locator_unico.locator('div.c-jyZWAy')
        
        dots_locator_limpeza.wait_for(state="visible", timeout=7000)
        dots_locator_limpeza.click()
        
        page_cleanup.locator('button:has-text("Excluir")').wait_for(state="visible", timeout=5000)
        page_cleanup.locator('button:has-text("Excluir")').click()
        
        page_cleanup.locator('button:has-text("Confirmar")').wait_for(state="visible", timeout=5000)
        page_cleanup.locator('button:has-text("Confirmar")').click()
        
        empregado_locator_unico.wait_for(state="detached", timeout=10000)
        print(f"✅ [LIMPEZA NO CONFTEST] Cadastro '{nome_empregado}' (CPF: {cpf_empregado}) excluído com sucesso.")
    except Exception as e:
        print(f"AVISO: [LIMPEZA NO CONFTEST] Falha ao excluir o cadastro '{nome_empregado}' (CPF: {cpf_empregado}): {e}.")
        # Opcional: tirar screenshot da falha de limpeza
        # base_screenshots_dir_cleanup = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tests", "screenshots") # Assume conftest está na raiz
        # if not os.path.exists(base_screenshots_dir_cleanup):
        #     os.makedirs(base_screenshots_dir_cleanup)
        # timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        # page_cleanup.screenshot(path=os.path.join(base_screenshots_dir_cleanup, f"FALHA_LIMPEZA_{nome_empregado.replace(' ', '_')}_{timestamp}.png"))


# --- FIXTURE DE LIMPEZA PÓS-SESSÃO ---
@pytest.fixture(scope="session", autouse=True)
def cleanup_after_all_tests(request): # request não é necessário aqui se não for usado
    yield 
    print("\n--- Iniciando limpeza de dados de teste (conftest.py) ---")
    if hasattr(pytest, 'global_data_for_cleanup') and pytest.global_data_for_cleanup:
        with sync_playwright() as p:
            browser_cleanup = p.chromium.launch(headless=True) 
            page_cleanup = browser_cleanup.new_page()
            
            for dados_empregado in pytest.global_data_for_cleanup:
                limpar_cadastro_conftest_impl(page_cleanup, dados_empregado)
            
            browser_cleanup.close()
    else:
        print("Nenhum empregado para limpar (conftest.py).")
    print("--- Limpeza de dados de teste concluída (conftest.py) ---")

# --- HOOKS PARA pytest-html E SCREENSHOTS ---
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    
    # Adiciona screenshot ao extra do HTML report em caso de falha na fase 'call'
    # E também para screenshots de etapas tiradas com a função take_screenshot
    if rep.when == "call": # Processar apenas para a fase de 'call' do teste
        # Screenshots tiradas explicitamente com take_screenshot e retornadas
        # geralmente são adicionadas ao 'item' pelo próprio teste.
        # Aqui, focamos em adicionar uma screenshot *automática* na falha.
        if rep.failed:
            try:
                page = item.funcargs.get("page") 
                if page:
                    # Caminho base para os screenshots DENTRO de tests/screenshots
                    # item.fspath é um objeto Path do Pytest
                    # O diretório do arquivo de teste é item.fspath.dirpath()
                    # Ou os.path.dirname(str(item.fspath))
                    screenshots_dir = os.path.join(str(item.fspath.dirpath()), "screenshots")
                    if not os.path.exists(screenshots_dir):
                        os.makedirs(screenshots_dir)
                    
                    test_name_cleaned = "".join(c if c.isalnum() else "_" for c in item.name)
                    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                    screenshot_filename = f"FALHA_{test_name_cleaned}_{timestamp}.png"
                    screenshot_path_abs = os.path.join(screenshots_dir, screenshot_filename)
                    page.screenshot(path=screenshot_path_abs)
                    print(f"📸 Screenshot AUTOMÁTICA em falha salvo: {screenshot_path_abs}")
                    
                    # Adiciona ao html report
                    if hasattr(item, 'extras'):
                        # Para --self-contained-html, o ideal é embutir como base64
                        # Mas pytest_html.extras.image(path) tenta linkar.
                        # Para embutir, o conteúdo da imagem precisa ser passado.
                        # pytest_html.extras.image(pytest_html.extras.image_base64(screenshot_path_abs))
                        # Ou simplesmente linkar, e garantir que o caminho é acessível pelo report.
                        item.extras.append(pytest_html.extras.image(screenshot_path_abs, name="Screenshot Automático em Falha"))
            except Exception as e:
                print(f"AVISO: Não foi possível capturar screenshot automática em falha para {item.name}: {e}")

def pytest_configure(config):
    # Caminho para a pasta screenshots dentro de tests, relativo à raiz do projeto
    screenshots_dir = os.path.join(str(config.rootpath), "tests", "screenshots") 
    os.makedirs(screenshots_dir, exist_ok=True)
    config.addinivalue_line("markers", "screenshots_on_failure: mark test to take screenshots on failure")
    
    print("\nIniciando testes automatizados para o projeto SEA Tecnologia")
    print(f"URL da aplicação: {APP_URL}") # Agora APP_URL está definido neste arquivo
    print("URL do protótipo: https://tinyurl.com/yl58hs4m")

def pytest_html_report_title(report):
    report.title = "Relatório de Testes Automatizados - SEA Tecnologia"

def pytest_sessionfinish(session, exitstatus):
    print("\n===== Resumo da Execução de Testes =====")
    num_collected = session.testscollected
    num_failed = 0
    num_passed = 0
    
    for item in session.items:
        if hasattr(item, 'rep_call') and item.rep_call.when == 'call': # Considerar apenas a fase de 'call'
            if item.rep_call.failed:
                num_failed += 1
            elif item.rep_call.passed:
                num_passed += 1
    
    print(f"Total de testes executados: {num_collected}")
    print(f"Testes com sucesso: {num_passed}")
    print(f"Testes com falha: {num_failed}")
    
    if num_failed == 0 and num_collected > 0 :
        print("\n✅ Todos os testes foram executados com sucesso!")
    elif num_collected == 0:
        print("\nℹ️ Nenhum teste foi coletado.")
    else:
        print(f"\n⚠️ {num_failed} teste(s) falharam. Verifique os logs e o relatório HTML para mais detalhes.")
    
    screenshots_dir_path = os.path.join(str(session.config.rootpath), "tests", "screenshots")
    print(f"\nEvidências de teste (screenshots) disponíveis em: {screenshots_dir_path}")
    print("=======================================")

try:
    import pytest_html.extras
except ImportError:
    pytest_html = None # Define como None se não puder ser importado
    