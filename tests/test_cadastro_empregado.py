import pytest
from playwright.sync_api import Page, TimeoutError
import os
import datetime # Para adicionar data e hora nas screenshots

# URL da aplicação (pode ser removida daqui se definida e usada apenas do conftest)
APP_URL = "http://analista-teste.seatecnologia.com.br/"

# Caminho base para os screenshots, relativo ao diretório deste arquivo de teste
BASE_SCREENSHOTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screenshots")

# Dados de teste para o fluxo
TEST_EMPLOYEE_DATA = {
    "nome": "Carlos Testador Unico", 
    "cpf": "123.456.789-00",       
    "rg": "12.345.678-9",
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
    return screenshot_path # Retorna o caminho absoluto

# --- Funções de interação (selecionar_dropdown_por_label, selecionar_sexo_externo) ---
# MANTENHA AS VERSÕES CORRIGIDAS DESSAS FUNÇÕES DA RESPOSTA ANTERIOR

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

# --- Função de Inclusão ---
def incluir_cadastro_externo(page: Page, dados: dict, item_do_teste): # 'item_do_teste' é request.node
    print(f"Tentando incluir cadastro: {dados['nome']} (CPF: {dados['cpf']})")
    
    page.locator('button:has-text("+ Adicionar Funcionário")').wait_for(state="visible", timeout=10000)
    s_path = take_screenshot(page, "01_antes_clicar_adicionar_funcionario", dados_empregado=dados)
    if pytest_html and hasattr(item_do_teste, 'extras'): item_do_teste.extras.append(pytest_html.extras.image(s_path))

    page.locator('button:has-text("+ Adicionar Funcionário")').click()
    
    page.wait_for_selector('input[name="name"]', timeout=10000) 
    s_path = take_screenshot(page, "02_apos_abrir_formulario_cadastro", dados_empregado=dados)
    if pytest_html and hasattr(item_do_teste, 'extras'): item_do_teste.extras.append(pytest_html.extras.image(s_path))
    
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

    s_path = take_screenshot(page, "03_formulario_cadastro_preenchido", dados_empregado=dados)
    if pytest_html and hasattr(item_do_teste, 'extras'): item_do_teste.extras.append(pytest_html.extras.image(s_path))
    
    page.locator('button.save[type="submit"]:has-text("Salvar")').click()
    page.wait_for_selector('button.save[type="submit"]', state="hidden", timeout=10000) 
    print(f"✅ Cadastro incluído: {dados['nome']}")
    
    if hasattr(pytest, 'global_data_for_cleanup'):
        pytest.global_data_for_cleanup.append(dados) 

# --- Classes de Teste ---

class TestFuncionaisCadastro:
    @pytest.fixture(scope="function") # Removido autouse=False, pois queremos que seja injetada
    def employee_data_for_test(self):
        return TEST_EMPLOYEE_DATA.copy()

    def test_01_inclusao_cadastro_empregado(self, request, page: Page, employee_data_for_test: dict):
        print("\n--- TESTE 01: Inclusão de Cadastro de Empregado ---")
        page.goto(APP_URL)
        page.wait_for_load_state("networkidle")
        s_path = take_screenshot(page, "00_pagina_inicial_limpa_teste01")
        if pytest_html and hasattr(request.node, 'extras'): request.node.extras.append(pytest_html.extras.image(s_path))
        
        incluir_cadastro_externo(page, employee_data_for_test, request.node)

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
        elif not encontrado_sem_refresh and encontrado_apos_scroll:
            pytest.fail(
                f"FALHA (TESTE 02): O cadastro de '{nome_empregado}' (CPF: {cpf_empregado}) só é visível após rolagem. "
                f"Falta de paginação automática."
            )
        elif encontrado_sem_refresh:
            pytest.fail(
                f"FALHA (DIVERGÊNCIA NO TESTE 02): O cadastro de '{nome_empregado}' (CPF: {cpf_empregado}) foi encontrado imediatamente."
            )


    def test_03_tentativa_alteracao_menu_ausente(self, request, page: Page, employee_data_for_test: dict):
        print("\n--- TESTE 03: Tentativa de Alteração/Exclusão - Menu Ausente ---")
        page.goto(APP_URL) 
        page.wait_for_load_state("networkidle")
        
        nome_empregado = employee_data_for_test["nome"]
        cpf_empregado = employee_data_for_test["cpf"]

        empregado_locator_unico = page.locator(
            f'div.c-bXqUbA:has-text("{nome_empregado}"):has(div.c-iYbcAK:has-text("{cpf_empregado}"))'
        ).first
        
        try:
            empregado_locator_unico.scroll_into_view_if_needed(timeout=10000)
            print(f"DEBUG: Rolou a tela para '{nome_empregado}' (CPF: {cpf_empregado}) para tentar visualizá-lo.")
        except TimeoutError:
            s_path = take_screenshot(page, f"10_NAO_VISIVEL_PARA_MENU_DOTS_teste03", dados_empregado=employee_data_for_test)
            if pytest_html and hasattr(request.node, 'extras'): request.node.extras.append(pytest_html.extras.image(s_path))
            pytest.fail(f"FALHA (TESTE 03): Empregado '{nome_empregado}' não visível para interagir com o menu '...'.")
        
        s_path = take_screenshot(page, f"10_antes_clicar_dots_teste03", dados_empregado=employee_data_for_test)
        if pytest_html and hasattr(request.node, 'extras'): request.node.extras.append(pytest_html.extras.image(s_path))
        
        dots_locator = empregado_locator_unico.locator('div.c-jyZWAy') 
        dots_locator.wait_for(state="visible", timeout=5000) 
        dots_locator.click()

        menu_apareceu = False
        try:
            page.locator('button:has-text("Editar")').wait_for(state="visible", timeout=5000)
            menu_apareceu = True
            s_path = take_screenshot(page, f"11_MENU_ALTERAR_EXCLUIR_APARECEU_teste03", dados_empregado=employee_data_for_test)
            if pytest_html and hasattr(request.node, 'extras'): request.node.extras.append(pytest_html.extras.image(s_path))
            pytest.fail(
                f"FALHA (DIVERGÊNCIA NO TESTE 03): O menu 'Alterar/Excluir' APARECEU para '{nome_empregado}' (CPF: {cpf_empregado}), "
                f"contrariando a observação de não-implementação no protótipo."
            )
        except TimeoutError:
            s_path = take_screenshot(page, f"11_NAO_IMPLEMENTADO_Menu_Alterar_Excluir_teste03", dados_empregado=employee_data_for_test)
            if pytest_html and hasattr(request.node, 'extras'): request.node.extras.append(pytest_html.extras.image(s_path))
            pytest.fail(
                f"FALHA (TESTE 03): A funcionalidade de 'Alterar/Excluir' não está implementada. "
                f"O menu não apareceu ao clicar nos '...' para o funcionário '{nome_empregado}' (CPF: {cpf_empregado})."
            )

# Importe pytest_html no início do arquivo se for usar extras
try:
    import pytest_html.extras
except ImportError:
    pytest_html = None # Define como None se não puder ser importado
