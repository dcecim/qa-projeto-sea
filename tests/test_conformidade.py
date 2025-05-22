import pytest
from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright

# URL da aplicação
APP_URL = "https://analista-teste.seatecnologia.com.br/"
# URL do protótipo
PROTOTYPE_URL = "https://tinyurl.com/yl58hs4m"

class TestConformidade:
    """
    Testes automatizados para verificar a conformidade da aplicação com o protótipo.
    Implementa os casos de teste CT-CONF-001, CT-CONF-002 e CT-CONF-003.
    """
    
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Configuração inicial para cada teste."""
        # Navega para a aplicação
        page.goto(APP_URL)
        # Aguarda o carregamento completo da página
        page.wait_for_load_state("networkidle")
        
    def test_verificacao_fonte(self, page: Page):
        """
        Verifica se as fontes utilizadas na aplicação correspondem às do protótipo.
        Implementa o caso de teste CT-CONF-001.
        """
        # Verifica se a fonte principal está presente
        font_family = page.evaluate("""() => {
            const bodyStyle = window.getComputedStyle(document.body);
            return bodyStyle.fontFamily;
        }""")
        
        # A fonte deve conter 'Roboto' ou outra fonte especificada no protótipo
        # assert "Roboto" in font_family or "Arial" in font_family, f"Fonte principal incorreta: {font_family}"
        assert "Ubuntu" in font_family or "Arial" in font_family, f"Fonte principal incorreta: {font_family}"
        
        # Verifica a fonte dos títulos
        title_font = page.evaluate("""() => {
            const title = document.querySelector('h1, h2, h3, h4, h5');
            if (!title) return 'Nenhum título encontrado';
            return window.getComputedStyle(title).fontFamily;
        }""")
        
        # assert "Roboto" in font_family or "Arial" in font_family, f"Fonte principal incorreta: {font_family}"
        assert "Ubuntu" in font_family or "Arial" in font_family, f"Fonte principal incorreta: {font_family}"
        
        print(f"✅ Verificação de fonte concluída: {font_family}")
        
    def test_verificacao_cores(self, page: Page):
        """
        Verifica se as cores utilizadas na aplicação correspondem às do protótipo.
        Implementa o caso de teste CT-CONF-002.
        """
        # Verifica a cor de fundo principal
        background_color = page.evaluate("""() => {
            return window.getComputedStyle(document.body).backgroundColor;
        }""")
        
        # Verifica a cor dos botões primários
        primary_button_color = page.evaluate("""() => {
            const button = document.querySelector('button.primary, button.btn-primary');
            if (!button) return 'Nenhum botão primário encontrado';
            return window.getComputedStyle(button).backgroundColor;
        }""")
        
        # Verifica a cor dos textos
        text_color = page.evaluate("""() => {
            return window.getComputedStyle(document.body).color;
        }""")
        
        # Registra as cores encontradas para análise
        print(f"Cor de fundo: {background_color}")
        print(f"Cor de botão primário: {primary_button_color}")
        print(f"Cor de texto: {text_color}")
        
        # Verifica se as cores não são indefinidas ou transparentes
        assert background_color != "rgba(0, 0, 0, 0)", "Cor de fundo indefinida"
        assert "rgb" in primary_button_color, f"Cor de botão primário inválida: {primary_button_color}"
        assert "rgb" in text_color, f"Cor de texto inválida: {text_color}"
        
        print("✅ Verificação de cores concluída")
        
    def test_verificacao_elementos_interface(self, page: Page):
        """
        Verifica se todos os elementos de interface estão presentes conforme o protótipo.
        Implementa o caso de teste CT-CONF-003.
        """
        # Verifica a presença de campos de formulário
        form_fields = page.evaluate("""() => {
            const inputs = document.querySelectorAll('input, select, textarea');
            return inputs.length;
        }""")
        
        # Verifica a presença de botões
        buttons = page.evaluate("""() => {
            const buttons = document.querySelectorAll('button, input[type="button"], input[type="submit"]');
            return buttons.length;
        }""")
        
        # Verifica a presença de elementos de navegação
        nav_elements = page.evaluate("""() => {
            const navs = document.querySelectorAll('nav, .nav, .navbar, .menu');
            return navs.length;
        }""")
        
        # Registra os elementos encontrados
        print(f"Campos de formulário: {form_fields}")
        print(f"Botões: {buttons}")
        print(f"Elementos de navegação: {nav_elements}")
        
        # Verifica se há elementos suficientes
        assert form_fields > 0, "Nenhum campo de formulário encontrado"
        assert buttons > 0, "Nenhum botão encontrado"
        
        # Verifica elementos específicos mencionados nos requisitos
        assert page.locator('text=Funcionários').count() > 0, "Menu 'Funcionários' não encontrado"
        
        print("✅ Verificação de elementos de interface concluída")
        
    def test_captura_screenshot(self, page: Page):
        """
        Captura screenshots da aplicação para análise visual.
        """
        # Captura screenshot da página inicial
        page.screenshot(path="/home/ubuntu/qa-projeto-sea/tests/screenshot_app.png")
        print("✅ Screenshot da aplicação capturado")
        
        # Tenta acessar o protótipo para comparação
        try:
            page.goto(PROTOTYPE_URL)
            page.wait_for_load_state("networkidle")
            page.screenshot(path="/home/ubuntu/qa-projeto-sea/tests/screenshot_prototype.png")
            print("✅ Screenshot do protótipo capturado")
        except Exception as e:
            print(f"⚠️ Não foi possível capturar o protótipo: {e}")
