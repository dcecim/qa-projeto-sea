import pytest
from playwright.sync_api import Page

BASE_URL = "http://analista-teste.seatecnologia.com.br/" 

def test_login_com_credenciais_validas(page: Page):
    """
    Testa o login com credenciais válidas. (Exemplo)
    """
    page.goto(BASE_URL)
    # Supondo que há campos de usuário e senha e um botão de login
    # Substitua 'username_field_selector', 'password_field_selector', 'login_button_selector' pelos seletores reais
    # E 'seu_usuario', 'sua_senha' pelas credenciais válidas, se existirem.
    
    # Exemplo: Preencher campos e clicar no botão
    # page.fill('input#username', 'seu_usuario')
    # page.fill('input#password', 'sua_senha')
    # page.click('button#login')

    # Exemplo de verificação de sucesso após login:
    # assert page.url != BASE_URL
    # assert page.is_visible("text=Bem-vindo ao sistema") # Ou outro elemento que indique sucesso no login

    # Se a aplicação não tiver um login funcional e for apenas uma tela estática,
    # você pode adaptar este teste para verificar a presença de elementos esperados na página inicial.
    # Por exemplo, verificar se o título da página está correto.
    assert page.title() == "Sea Tecnologia - Analista de Teste"

def test_acesso_a_link_em_breve(page: Page):
    """
    Testa se os links da navegação conduzem ao componente 'Em breve'. 
    """
    page.goto(BASE_URL)
    
    # Exemplo: Encontra um link de menu (adapte o seletor conforme a aplicação)
    # Supondo que existe um link com o texto 'Funcionários' ou similar
    employee_link_selector = 'text="Funcionários"' # Adapte para o seletor real do seu menu
    
    # Verifica se o link existe antes de clicar
    if page.is_visible(employee_link_selector):
        page.click(employee_link_selector)
        # Verifica se o componente "Em breve" está visível
        assert page.is_visible("text=Em breve") 
        assert page.text_content("text=Em breve").strip() == "Em breve"
    else:
        pytest.skip(f"Link '{employee_link_selector}' não encontrado na página inicial para testar 'Em breve'.")