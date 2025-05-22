import pytest
from playwright.sync_api import Page
from utils.helpers import is_valid_name, PLSQL_RESERVED_WORDS 

BASE_URL = "http://analista-teste.seatecnologia.com.br/" 

@pytest.fixture(autouse=True)
def navigate_to_employee_registration(page: Page):
    """
    Navega para a tela de cadastro de empregado antes de cada teste.
    Adapte esta função para a navegação real se não for a página inicial.
    """
    page.goto(BASE_URL)
    # Supondo que a tela de cadastro de empregado é a página inicial ou há um link para ela.
    # Se houver um link, adicione: page.click('seletor_do_link_cadastro')
    # Exemplo: page.click('text="Cadastrar Empregado"') # Se houver um botão ou link para o cadastro

def test_validacao_nome_valido(page: Page):
    """
    Testa o preenchimento de um nome válido no campo "Nome do Empregado". 
    """
    nome_valido = "Ana da Silva" 
    assert is_valid_name(nome_valido) # Validação com a função helper 

    # Supondo o seletor do campo de nome
    page.fill('input#nomeEmpregado', nome_valido)
    # Simular saída do campo para acionar validação (se houver)
    page.press('input#nomeEmpregado', 'Tab')

    # Verifica se não há mensagem de erro (adapte o seletor da mensagem de erro)
    # assert not page.is_visible('div#erroNomeEmpregado')
    # Ou verifica se a mensagem de erro esperada não aparece
    # assert "Nome inválido" not in page.text_content('body')

def test_validacao_nome_curto(page: Page):
    """
    Testa o preenchimento de um nome muito curto (inválido). 
    """
    nome_curto = "A" 
    assert not is_valid_name(nome_curto) 

    page.fill('input#nomeEmpregado', nome_curto)
    page.press('input#nomeEmpregado', 'Tab')

    # Verifica se a mensagem de erro para nome curto aparece
    # assert page.is_visible('div#erroNomeEmpregado')
    # assert "Nome muito curto" in page.text_content('div#erroNomeEmpregado')

def test_validacao_nome_longo(page: Page):
    """
    Testa o preenchimento de um nome muito longo (inválido). 
    """
    nome_longo = "A" * 121 # Mais de 120 caracteres 
    assert not is_valid_name(nome_longo) 

    page.fill('input#nomeEmpregado', nome_longo)
    page.press('input#nomeEmpregado', 'Tab')

    # Verifica se a mensagem de erro para nome longo aparece
    # assert page.is_visible('div#erroNomeEmpregado')
    # assert "Nome muito longo" in page.text_content('div#erroNomeEmpregado')

def test_validacao_nome_com_digitos(page: Page):
    """
    Testa o preenchimento de um nome contendo dígitos (inválido). 
    """
    nome_com_digitos = "Joao123" 
    assert not is_valid_name(nome_com_digitos) 

    page.fill('input#nomeEmpregado', nome_com_digitos)
    page.press('input#nomeEmpregado', 'Tab')

    # Verifica se a mensagem de erro para dígitos aparece
    # assert page.is_visible('div#erroNomeEmpregado')
    # assert "Nome não pode conter dígitos" in page.text_content('div#erroNomeEmpregado')

def test_validacao_nome_com_caracteres_especiais(page: Page):
    """
    Testa o preenchimento de um nome contendo caracteres especiais (inválido). 
    """
    nome_com_especiais = "João!@" 
    assert not is_valid_name(nome_com_especiais) 

    page.fill('input#nomeEmpregado', nome_com_especiais)
    page.press('input#nomeEmpregado', 'Tab')

    # Verifica se a mensagem de erro para caracteres especiais aparece
    # assert page.is_visible('div#erroNomeEmpregado')
    # assert "Nome não pode conter caracteres especiais" in page.text_content('div#erroNomeEmpregado')

@pytest.mark.parametrize("reserved_word", PLSQL_RESERVED_WORDS)
def test_validacao_nome_com_palavra_reservada_plsql(page: Page, reserved_word: str):
    """
    Testa o preenchimento de um nome contendo uma palavra reservada de PL/SQL (inválido). 
    """
    nome_com_reservada = f"Teste {reserved_word} Nome" 
    assert not is_valid_name(nome_com_reservada) 

    page.fill('input#nomeEmpregado', nome_com_reservada)
    page.press('input#nomeEmpregado', 'Tab')

    # Verifica se a mensagem de erro para palavras reservadas aparece
    # assert page.is_visible('div#erroNomeEmpregado')
    # assert "Nome contém termos inválidos" in page.text_content('div#erroNomeEmpregado')