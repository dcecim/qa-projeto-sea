import pytest
from playwright.sync_api import sync_playwright, Page, Browser, BrowserContext
import os
import datetime 
from py.xml import html
from py._xmlgen import raw
import pytest_html.extras


# URL da aplicação - DEFINIDA AQUI
APP_URL = "http://analista-teste.seatecnologia.com.br/"

# Variável global para armazenar dados de empregados criados para limpeza.
pytest.global_data_for_cleanup = []

# --- Fixtures do Playwright ---
# (Suas fixtures do Playwright existentes permanecem inalteradas)
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

# --- FUNÇÃO DE LIMPEZA (MOVIDA PARA CONFTEST.PY) ---
# (Sua função limpar_cadastro_conftest_impl existente permanece inalterada)
def limpar_cadastro_conftest_impl(page_cleanup: Page, dados_empregado: dict):
    nome_empregado = dados_empregado["nome"]
    cpf_empregado = dados_empregado["cpf"]

    print(f"INFO: [LIMPEZA NO CONFTEST] Tentando limpar o cadastro de '{nome_empregado}' (CPF: {cpf_empregado})...")
    try:
        page_cleanup.goto(APP_URL)
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


# --- FIXTURE DE LIMPEZA PÓS-SESSÃO ---
# (Sua fixture cleanup_after_all_tests existente permanece inalterada)
@pytest.fixture(scope="session", autouse=True)
def cleanup_after_all_tests(request):
    yield
    print("\n--- Iniciando limpeza de dados de teste (conftest.py) ---")
    if hasattr(pytest, 'global_data_for_cleanup') and pytest.global_data_for_cleanup:
        with sync_playwright() as p:
            browser_cleanup = p.chromium.launch(headless=True)
            page_cleanup = browser_cleanup.new_page()

            for dados_empregado in pytest.global_data_for_cleanup:
                limpar_cadastro_conftest_impl(page_cleanup, dados_empregado) # Chama a função local

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

    if rep.when == "call" and rep.failed:
        try:
            page = item.funcargs.get("page")
            # Alteração na condição:
            # Se 'page' existir e 'pytest_html.extras' foi importado com sucesso, podemos prosseguir.
            if page and pytest_html.extras:
                base_screenshots_dir = os.path.join(str(item.fspath.dirpath()), "screenshots")
                if not os.path.exists(base_screenshots_dir):
                    os.makedirs(base_screenshots_dir)

                test_name_cleaned = "".join(c if c.isalnum() else "_" for c in item.name)
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                screenshot_filename = f"FALHA_{test_name_cleaned}_{timestamp}.png"
                screenshot_path_abs = os.path.join(base_screenshots_dir, screenshot_filename)
                page.screenshot(path=screenshot_path_abs)
                print(f"📸 Screenshot AUTOMÁTICA em falha salva: {screenshot_path_abs}")

                # Adiciona ao html report.
                # A verificação hasattr(item, 'extras') é importante.
                if hasattr(item, 'extras'):
                    item.extras.append(pytest_html.extras.image(screenshot_path_abs, name="Screenshot Automático em Falha"))
        except Exception as e:
            print(f"AVISO: Não foi possível capturar screenshot automática em falha para {item.name}: {e}")

def pytest_configure(config):
    screenshots_dir = os.path.join(str(config.rootpath), "tests", "screenshots")
    os.makedirs(screenshots_dir, exist_ok=True)
    # Inicialize o stash para estatísticas personalizadas, se não estiver presente
    if not hasattr(config, 'stash'):
        config.stash = {} # Versões mais antigas do pytest podem precisar disso
    config.stash['my_report_stats'] = {}


    print("\nIniciando testes automatizados para o projeto SEA Tecnologia")
    print(f"URL da aplicação: {APP_URL}")
    print("URL do protótipo: https://tinyurl.com/yl58hs4m")

def pytest_html_report_title(report):
    report.title = "Relatório de Testes Automatizados - SEA Tecnologia (Customizado)"

# Armazena resultados agregados em pytest_sessionfinish
def pytest_sessionfinish(session, exitstatus):
    print("\n===== Resumo da Execução de Testes =====")
    num_collected = session.testscollected
    num_failed = 0
    num_passed = 0
    for item in session.items:
        if hasattr(item, 'rep_call') and item.rep_call.when == 'call':
            if item.rep_call.failed:
                num_failed += 1
            elif item.rep_call.passed:
                num_passed += 1

    print(f"Total de testes executados: {num_collected}")
    print(f"Testes com sucesso: {num_passed}")
    print(f"Testes com falha: {num_failed}")

    stats_for_report = {
        'total': num_collected,
        'passed': num_passed,
        'failed': num_failed,
        'skipped': num_collected - (num_passed + num_failed)
    }
    # Armazena no stash da configuração (bom para plugins internos)
    session.config.stash['my_report_stats'] = stats_for_report
    # <<NOVA LINHA>> Armazena também no módulo pytest para acesso simplificado no hook
    pytest.my_report_stats_for_html = stats_for_report


    if num_failed == 0 and num_collected > 0 :
        print("\n✅ Todos os testes foram executados com sucesso!")
    elif num_collected == 0:
        print("\nℹ️ Nenhum teste foi coletado.")
    else:
        print(f"\n⚠️ {num_failed} teste(s) falharam. Verifique os logs e o relatório HTML para mais detalhes.")

    screenshots_dir_path = os.path.join(str(session.config.rootpath), "tests", "screenshots")
    print(f"\nEvidências de teste (screenshots) disponíveis em: {screenshots_dir_path}")
    print("=======================================")


# Ajuste em pytest_html_results_summary:
@pytest.hookimpl(optionalhook=True)
def pytest_html_results_summary(prefix, summary, postfix):
    # 1. Adicione o CDN do Chart.js - como um nó de script HTML
    prefix.append(html.script(src="https://cdn.jsdelivr.net/npm/chart.js"))

    # 2. Adicione um contêiner e um canvas para o gráfico - construindo os elementos
    chart_container_div = html.div(class_="chart-container")
    chart_container_div.append(html.h3("Visão Geral dos Testes"))
    chart_container_div.append(html.canvas(id="testSummaryChart"))
    prefix.append(chart_container_div)

    # 3. Recupere as estatísticas (esta parte está correta)
    stats = getattr(pytest, 'my_report_stats_for_html', {})
    total = stats.get('total', 0)
    passed = stats.get('passed', 0)
    failed = stats.get('failed', 0)
    skipped = stats.get('skipped', 0)

    # 4. Adicione JavaScript para renderizar o gráfico
    # O conteúdo JS em si, sem as tags <script></script> externas
    script_content_js_puro = f"""
            document.addEventListener('DOMContentLoaded', function() {{
                const ctx = document.getElementById('testSummaryChart');
                if (ctx && typeof Chart !== 'undefined') {{
                    new Chart(ctx.getContext('2d'), {{
                        type: 'pie',
                        data: {{
                            labels: ['Passou', 'Falhou', 'Outros/Não Executado'],
                            datasets: [{{
                                label: 'Resultados dos Testes',
                                data: [{passed}, {failed}, {skipped}],
                                backgroundColor: [
                                    'rgba(75, 192, 192, 0.7)',
                                    'rgba(255, 99, 132, 0.7)',
                                    'rgba(201, 203, 207, 0.7)'
                                ],
                                borderColor: [
                                    'rgba(75, 192, 192, 1)',
                                    'rgba(255, 99, 132, 1)',
                                    'rgba(201, 203, 207, 1)'
                                ],
                                borderWidth: 1
                            }}]
                        }},
                        options: {{
                            responsive: true,
                            maintainAspectRatio: true,
                            plugins: {{
                                legend: {{
                                    position: 'top',
                                }},
                                title: {{
                                    display: false,
                                }}
                            }}
                        }}
                    }});
                }} else {{
                    if (!ctx) console.error('Elemento canvas para o gráfico não encontrado.');
                    if (typeof Chart === 'undefined') console.error('Chart.js não carregado.');
                }}
            }});
    """
    # Crie um nó de script HTML e adicione o conteúdo JS bruto dentro dele
    chart_script_tag = html.script(type="text/javascript")
    chart_script_tag.append(raw(script_content_js_puro)) # Use raw() para o conteúdo do script
    postfix.append(chart_script_tag)

    # Adicionando as estatísticas personalizadas - construindo os elementos
    stats_container_div = html.div(class_="stats-container")

    total_div = html.div(class_="stat-item")
    total_div.append(html.h3("Total"))
    total_div.append(html.p(str(total))) # Conteúdo de <p> é string
    stats_container_div.append(total_div)

    passed_div = html.div(class_="stat-item")
    passed_div.append(html.h3("Sucesso"))
    passed_p = html.p(str(passed))
    passed_p.attr.style = "color: green;" # Adicionando estilo ao <p>
    passed_div.append(passed_p)
    stats_container_div.append(passed_div)

    failed_div = html.div(class_="stat-item")
    failed_div.append(html.h3("Falha"))
    failed_p = html.p(str(failed))
    failed_p.attr.style = "color: red;" # Adicionando estilo ao <p>
    failed_div.append(failed_p)
    stats_container_div.append(failed_div)

    skipped_div = html.div(class_="stat-item")
    skipped_div.append(html.h3("Outros"))
    skipped_div.append(html.p(str(skipped)))
    stats_container_div.append(skipped_div)

    prefix.append(stats_container_div)


