import pytest
from playwright.sync_api import sync_playwright, Page

@pytest.fixture(scope="function")
def page():
    """
    Fixture para inicializar e fechar o navegador Playwright para cada teste.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True) # Mude para False para ver o navegador
        page = browser.new_page()
        yield page
        browser.close()

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """
    Configuração opcional para o contexto do navegador, como viewport.
    """
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
    }
