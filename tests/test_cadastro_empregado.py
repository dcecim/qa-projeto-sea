import pytest
from playwright.sync_api import Page, TimeoutError
import os
import datetime 

# URL da aplicação (pode ser removida se definida e usada apenas do conftest)
APP_URL = "http://analista-teste.seatecnologia.com.br/"

# Caminho base para os screenshots, relativo ao diretório deste arquivo de teste
BASE_SCREENSHOTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screenshots")

# Dados de teste para o fluxo 
TEST_EMPLOYEE_DATA = {
    "nome": "Carlos Testador Numro 1", # Nome bem único
    "cpf": "001.888.999-00",      # CPF único e válido
    "rg": "33.345.678-9",
    "cargo": "Cargo 02", 
    "data_nascimento": "1985-07-15",
    "sexo": "masculino",
    "epi": "nao",
    "atividade": "", 
    "ca_number": "", 
    "epi_tipo": ""   
}

# --- Funções Auxiliares Comuns ---
def take_screenshot(page: Page, step_name: str, dados_empregado: dict = None):
    if not os.path.exists(BASE_SCREENSHOTS_DIR):
        os.makedirs(BASE_SCREENSHOTS_DIR)
    
    sufixo_nome_dados = ""
    if dados_empregado and "nome" in dados_empregado:
        nome_limpo = dados_empregado["nome"].replace(' ', '_')
        sufixo_nome_dados = f"_{nome_limpo}"
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{step_name}{sufixo_nome_dados}_{timestamp}.png"
    screenshot_path = os.path.join(BASE_SCREENSHOTS_DIR, filename)
    page.screenshot(path=screenshot_path)
    print(f"📸 Screenshot salva: {screenshot_path}")
    return screenshot_path 

def selecionar_dropdown_por_label(page: Page, label_text: str, valor: str):
    print(f"DEBUG: Abrindo dropdown para '{label_text}' com valor '{valor}'")
    dropdown_input_locator = page.locator(f'div.c-hJlbiD:has(label:has-text("{label_text}")) .ant-select-selector')
    dropdown_input_locator.wait_for(state="visible", timeout=10000)
    dropdown_input_locator.click()
    option_content_locator = page.locator(f'div.ant-select-item-option-content:has-text("{valor}")')
    option_content_locator.wait_for(state="visible", timeout=20000)
    print(f"DEBUG: Item '{valor}' encontrado e visível. Clicando...")
    option_content_locator.click()
    selected_value_span = page.locator(f'div.c-hJlbiD:has(label:has-text("{label_text}")) span.ant-select-selection-item[title="{valor}"]')
    selected_value_span.wait_for(state="visible", timeout=10000)
    print(f"DEBUG: Seleção de '{valor}' confirmada para '{label_text}'.")

def selecionar_sexo_externo(page: Page, sexo: str):
    selector = f'input.ant-radio-input[value="{sexo.lower()}"]'
    page.locator(selector).wait_for(state="visible", timeout=10000)
    page.locator(selector).click()

def incluir_cadastro_logica(page: Page, dados: dict): # Removido test_item por enquanto
    print(f"Tentando incluir cadastro: {dados['nome']} (CPF: {dados['cpf']})")
    page.locator('button:has-text("+ Adicionar Funcionário")').wait_for(state="visible", timeout=10000)
    take_screenshot(page, "01_antes_clicar_adicionar_funcionario", dados_empregado=dados)
    page.locator('button:has-text("+ Adicionar Funcionário")').click()
    page.wait_for_selector('input[name="name"]', timeout=10000) 
    take_screenshot(page, "02_apos_abrir_formulario_cadastro", dados_empregado=dados)
    page.fill('input[name="name"]', dados["nome"])
    page.fill('input[name="cpf"]', dados["cpf"])
    page.fill('input[name="rg"]', dados["rg"])
    page.fill('input[name="birthDay"]', dados["data_nascimento"])
    selecionar_dropdown_por_label(page, "Cargo", dados["cargo"])
    selecionar_sexo_externo(page, dados["sexo"])
    checkbox_epi_nao_selector = 'label.ant-checkbox-wrapper:has-text("O trabalhador não usa EPI.") input.ant-checkbox-input'
    if dados["epi"].lower() == "nao":
        if not page.locator(checkbox_epi_nao_selector).is_checked():
            page.locator(checkbox_epi_nao_selector).click()
    else: 
        if page.locator(checkbox_epi_nao_selector).is_checked():
            page.locator(checkbox_epi_nao_selector).click()
        selecionar_dropdown_por_label(page, "Selecione a atividade:", dados.get("atividade", "Ativid 01"))
        selecionar_dropdown_por_label(page, "Selecione o EPI:", dados.get("epi_tipo", "Capacete de segurança"))
        page.fill('input[name="caNumber"]', dados.get("ca_number", "12345")) 
    take_screenshot(page, "03_formulario_cadastro_preenchido", dados_empregado=dados)
    page.locator('button.save[type="submit"]:has-text("Salvar")').click()
    page.wait_for_selector('button.save[type="submit"]', state="hidden", timeout=10000) 
    print(f"✅ Cadastro incluído: {dados['nome']}")
    if hasattr(pytest, 'global_data_for_cleanup'):
        pytest.global_data_for_cleanup.append(dados) 

# --- Classes de Teste ---
class TestFuncionaisCadastro:
    @pytest.fixture(scope="function") 
    def employee_data_for_test(self):
        # Retorna uma cópia nova para cada teste para evitar modificações entre testes
        return TEST_EMPLOYEE_DATA.copy()

    def test_01_inclusao_cadastro_empregado(self, request, page: Page, employee_data_for_test: dict):
        print("\n--- TESTE 01: Inclusão de Cadastro de Empregado ---")
        page.goto(APP_URL)
        page.wait_for_load_state("networkidle")
        s_path = take_screenshot(page, "00_pagina_inicial_limpa_teste01")
        if pytest_html and hasattr(request.node, 'extras'): request.node.extras.append(pytest_html.extras.image(s_path))
        
        incluir_cadastro_logica(page, employee_data_for_test) # Não precisa passar request.node aqui

        assert page.locator('button.save[type="submit"]:has-text("Salvar")').is_hidden(), \
            "Formulário de cadastro ainda visível após tentar salvar."
        
        s_path = take_screenshot(page, "03b_apos_salvar_inclusao_teste01", dados_empregado=employee_data_for_test)
        if pytest_html and hasattr(request.node, 'extras'): request.node.extras.append(pytest_html.extras.image(s_path))
        print(f"✅ TESTE 01 CONCLUÍDO: Cadastro de '{employee_data_for_test['nome']}' (CPF: {employee_data_for_test['cpf']}) foi incluído com sucesso na aplicação.")

    def test_02_consulta_registro_nao_visivel(self, request, page: Page, employee_data_for_test: dict):
        print("\n--- TESTE 02: Consulta de Registro - Não Visível Após Inclusão e Refresh ---")
        page.goto(APP_URL) 
        page.wait_for_load_state("networkidle")
        s_path = take_screenshot(page, "04_pagina_principal_antes_consulta_teste02", dados_empregado=employee_data_for_test)
        if pytest_html and hasattr(request.node, 'extras'): request.node.extras.append(pytest_html.extras.image(s_path))

        nome_empregado = employee_data_for_test["nome"]
        cpf_empregado = employee_data_for_test["cpf"]
        
        empregado_locator_unico = page.locator(
            f'div.c-bXqUbA:has-text("{nome_empregado}"):has(div.c-iYbcAK:has-text("{cpf_empregado}"))'
        ).first 

        print(f"DEBUG: Tentando encontrar '{nome_empregado}' (CPF: {cpf_empregado}) sem refresh (expectativa: NÃO visível)...")
        encontrado_sem_refresh = False
        try:
            empregado_locator_unico.wait_for(state="visible", timeout=5000)
            encontrado_sem_refresh = True
            s_path = take_screenshot(page, f"05_ENCONTRADO_IMEDIATAMENTE_teste02", dados_empregado=employee_data_for_test)
            if pytest_html and hasattr(request.node, 'extras'): request.node.extras.append(pytest_html.extras.image(s_path))
        except TimeoutError:
            s_path = take_screenshot(page, f"05_NAO_ENCONTRADO_IMEDIATAMENTE_teste02", dados_empregado=employee_data_for_test)
            if pytest_html and hasattr(request.node, 'extras'): request.node.extras.append(pytest_html.extras.image(s_path))

        print("DEBUG: Realizando refresh da página...")
        page.reload(wait_until="networkidle")
        s_path = take_screenshot(page, "06_pagina_principal_apos_refresh_teste02", dados_empregado=employee_data_for_test)
        if pytest_html and hasattr(request.node, 'extras'): request.node.extras.append(pytest_html.extras.image(s_path))
        
        print(f"DEBUG: Tentando encontrar '{nome_empregado}' (CPF: {cpf_empregado}) após refresh (expectativa: NÃO visível, por falta de paginação)...")
        # ... (Restante da lógica de verificação de visibilidade e scroll como antes) ...
        encontrado_apos_refresh = False
        try:
            empregado_locator_unico.wait_for(state="visible", timeout=10000)
            encontrado_apos_refresh = True
            s_path = take_screenshot(page, f"07_ENCONTRADO_APOS_REFRESH_SEM_SCROLL_teste02", dados_empregado=employee_data_for_test)
            if pytest_html and hasattr(request.node, 'extras'): request.node.extras.append(pytest_html.extras.image(s_path))
        except TimeoutError:
            s_path = take_screenshot(page, f"07_NAO_ENCONTRADO_APOS_REFRESH_SEM_SCROLL_teste02", dados_empregado=employee_data_for_test)
            if pytest_html and hasattr(request.node, 'extras'): request.node.extras.append(pytest_html.extras.image(s_path))

        print("DEBUG: Tentando rolar a página para baixo para verificar se o registro aparece...")
        page.mouse.wheel(0, 10000) 
        page.wait_for_timeout(2000) 
        s_path = take_screenshot(page, f"08_pagina_principal_apos_scroll_teste02", dados_empregado=employee_data_for_test)
        if pytest_html and hasattr(request.node, 'extras'): request.node.extras.append(pytest_html.extras.image(s_path))

        encontrado_apos_scroll = False
        try:
            empregado_locator_unico.wait_for(state="visible", timeout=10000)
            encontrado_apos_scroll = True
            s_path = take_screenshot(page, f"09_ENCONTRADO_APOS_SCROLL_teste02", dados_empregado=employee_data_for_test)
            if pytest_html and hasattr(request.node, 'extras'): request.node.extras.append(pytest_html.extras.image(s_path))
        except TimeoutError:
            s_path = take_screenshot(page, f"09_NAO_ENCONTRADO_APOS_SCROLL_teste02", dados_empregado=employee_data_for_test)
            if pytest_html and hasattr(request.node, 'extras'): request.node.extras.append(pytest_html.extras.image(s_path))

        if not encontrado_apos_scroll:
            pytest.fail(
                f"FALHA CRÍTICA (TESTE 02): O cadastro de '{nome_empregado}' (CPF: {cpf_empregado}) NÃO É VISUALIZADO na lista "
                f"mesmo após inclusão, refresh E rolagem da página. Defeito de persistência/sincronização/paginação."
            )
        # ... (outras condições de falha para o teste 02) ...

    def test_03_tentativa_alteracao_menu_ausente(self, request, page: Page, employee_data_for_test: dict):
        print("\n--- TESTE 03: Tentativa de Alteração - Menu Ausente ---")
        page.goto(APP_URL) 
        page.wait_for_load_state("networkidle")
        
        nome_empregado = employee_data_for_test["nome"]
        cpf_empregado = employee_data_for_test["cpf"]

        empregado_locator_unico = page.locator(
            f'div.c-bXqUbA:has-text("{nome_empregado}"):has(div.c-iYbcAK:has-text("{cpf_empregado}"))'
        ).first
        
        try:
            empregado_locator_unico.scroll_into_view_if_needed(timeout=10000)
        except TimeoutError:
            s_path = take_screenshot(page, f"10_NAO_VISIVEL_PARA_MENU_DOTS_teste03", dados_empregado=employee_data_for_test)
            if pytest_html and hasattr(request.node, 'extras'): request.node.extras.append(pytest_html.extras.image(s_path))
            pytest.fail(f"FALHA (TESTE 03): Empregado '{nome_empregado}' não visível para interagir com o menu '...'.")
        
        s_path = take_screenshot(page, f"10_antes_clicar_dots_teste03", dados_empregado=employee_data_for_test)
        if pytest_html and hasattr(request.node, 'extras'): request.node.extras.append(pytest_html.extras.image(s_path))
        
        dots_locator = empregado_locator_unico.locator('div.c-jyZWAy') 
        dots_locator.wait_for(state="visible", timeout=5000) 
        dots_locator.click()

        try:
            page.locator('button:has-text("Editar")').wait_for(state="visible", timeout=5000)
            s_path = take_screenshot(page, f"11_MENU_ALTERAR_APARECEU_teste03", dados_empregado=employee_data_for_test)
            if pytest_html and hasattr(request.node, 'extras'): request.node.extras.append(pytest_html.extras.image(s_path))
            pytest.fail(
                f"FALHA (DIVERGÊNCIA NO TESTE 03): O menu 'Editar' APARECEU para '{nome_empregado}' (CPF: {cpf_empregado}), "
                f"contrariando a observação de não-implementação no protótipo."
            )
        except TimeoutError:
            s_path = take_screenshot(page, f"11_NAO_IMPLEMENTADO_Menu_Editar_teste03", dados_empregado=employee_data_for_test)
            if pytest_html and hasattr(request.node, 'extras'): request.node.extras.append(pytest_html.extras.image(s_path))
            pytest.fail(
                f"FALHA (TESTE 03): A funcionalidade de 'Alterar' (botão Editar) não está implementada. "
                f"O menu não apareceu ou o botão 'Editar' não foi encontrado após clicar nos '...'."
            )

    def test_04_tentativa_exclusao_menu_ausente(self, request, page: Page, employee_data_for_test: dict):
        print("\n--- TESTE 04: Tentativa de Exclusão - Menu Ausente ---")
        page.goto(APP_URL) 
        page.wait_for_load_state("networkidle")
        
        nome_empregado = employee_data_for_test["nome"]
        cpf_empregado = employee_data_for_test["cpf"]

        empregado_locator_unico = page.locator(
            f'div.c-bXqUbA:has-text("{nome_empregado}"):has(div.c-iYbcAK:has-text("{cpf_empregado}"))'
        ).first
        
        try:
            empregado_locator_unico.scroll_into_view_if_needed(timeout=10000)
        except TimeoutError:
            s_path = take_screenshot(page, f"12_NAO_VISIVEL_PARA_MENU_DOTS_teste04", dados_empregado=employee_data_for_test)
            if pytest_html and hasattr(request.node, 'extras'): request.node.extras.append(pytest_html.extras.image(s_path))
            pytest.fail(f"FALHA (TESTE 04): Empregado '{nome_empregado}' não visível para interagir com o menu '...'.")
        
        s_path = take_screenshot(page, f"12_antes_clicar_dots_teste04", dados_empregado=employee_data_for_test)
        if pytest_html and hasattr(request.node, 'extras'): request.node.extras.append(pytest_html.extras.image(s_path))
        
        dots_locator = empregado_locator_unico.locator('div.c-jyZWAy') 
        dots_locator.wait_for(state="visible", timeout=5000) 
        dots_locator.click()

        try:
            page.locator('button:has-text("Excluir")').wait_for(state="visible", timeout=5000)
            s_path = take_screenshot(page, f"13_MENU_EXCLUIR_APARECEU_teste04", dados_empregado=employee_data_for_test)
            if pytest_html and hasattr(request.node, 'extras'): request.node.extras.append(pytest_html.extras.image(s_path))
            pytest.fail(
                f"FALHA (DIVERGÊNCIA NO TESTE 04): O menu 'Excluir' APARECEU para '{nome_empregado}' (CPF: {cpf_empregado}), "
                f"contrariando a observação de não-implementação no protótipo."
            )
        except TimeoutError:
            s_path = take_screenshot(page, f"13_NAO_IMPLEMENTADO_Menu_Excluir_teste04", dados_empregado=employee_data_for_test)
            if pytest_html and hasattr(request.node, 'extras'): request.node.extras.append(pytest_html.extras.image(s_path))
            pytest.fail(
                f"FALHA (TESTE 04): A funcionalidade de 'Excluir' (botão Excluir) não está implementada. "
                f"O menu não apareceu ou o botão 'Excluir' não foi encontrado após clicar nos '...'."
            )

# Importe pytest_html no início do arquivo se for usar extras
try:
    import pytest_html.extras
except ImportError:
    pytest_html = None # Define como None se não puder ser importado
