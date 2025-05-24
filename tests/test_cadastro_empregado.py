import pytest
from playwright.sync_api import Page, TimeoutError
import os

# URL da aplicação
APP_URL = "http://analista-teste.seatecnologia.com.br/"

# Dados de teste para o fluxo (usaremos um dado único por teste para clareza)
TEST_EMPLOYEE_DATA = {
    "nome": "João Silva Teste Autom", # Nome único para este teste
    "cpf": "999.888.777-66",         # CPF único
    "rg": "11.111.111-1",
    "cargo": "Cargo 01", 
    "data_nascimento": "1990-05-15",
    "sexo": "masculino",
    "epi": "nao",
    "atividade": "",
    "ca_number": ""
}

# --- Funções Auxiliares Comuns ---

def take_screenshot(page: Page, step_name: str, dados_empregado: dict = None):
    """
    Captura uma screenshot da página atual no diretório de screenshots.
    Garante que o diretório exista.
    :param dados_empregado: Opcional, dicionário com 'nome' e 'cpf' para sufixo do nome do arquivo.
    """
    screenshots_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screenshots")
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)
    
    sufixo_nome = ""
    if dados_empregado and "nome" in dados_empregado and "cpf" in dados_empregado:
        nome_limpo = dados_empregado["nome"].replace(' ', '_')
        cpf_limpo = dados_empregado["cpf"].replace('.', '').replace('-', '')
        sufixo_nome = f"_{nome_limpo}_{cpf_limpo}"
    
    filename = f"{step_name}{sufixo_nome}.png"
    screenshot_path = os.path.join(screenshots_dir, filename)
    page.screenshot(path=screenshot_path)
    print(f"📸 Screenshot salva: {screenshot_path}")


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

def incluir_cadastro_externo(page: Page, dados: dict):
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
    # Adiciona o empregado à lista global para limpeza
    pytest.global_data_for_cleanup.append(dados) 


# Função de exclusão para limpeza, independente dos resultados do teste.
# Esta função será chamada pela fixture de teardown no conftest.py
def limpar_cadastro_final_conftest(page: Page, dados_empregado: dict):
    nome_empregado = dados_empregado["nome"]
    cpf_empregado = dados_empregado["cpf"]

    print(f"INFO: [LIMPEZA] Tentando limpar o cadastro de '{nome_empregado}' (CPF: {cpf_empregado})...")
    try:
        page.goto(APP_URL) # Recarrega para ter certeza que está na página principal
        page.wait_for_load_state("networkidle")
        
        # Seletor para encontrar o registro único pelo nome e CPF
        empregado_locator_unico = page.locator(
            f'div.c-bXqUbA:has-text("{nome_empregado}"):has(div.c-iYbcAK:has-text("{cpf_empregado}"))'
        ).first 

        # Espera e clica nos dots do registro
        dots_locator_limpeza = empregado_locator_unico.locator('div.c-jyZWAy')
        
        dots_locator_limpeza.wait_for(state="visible", timeout=5000) 
        dots_locator_limpeza.click()
        
        # Espera e clica no botão Excluir
        page.locator('button:has-text("Excluir")').wait_for(state="visible", timeout=5000)
        page.locator('button:has-text("Excluir")').click()
        
        # Espera e clica no botão Confirmar
        page.locator('button:has-text("Confirmar")').wait_for(state="visible", timeout=5000)
        page.locator('button:has-text("Confirmar")').click()
        
        # Espera que o registro desapareça da lista
        empregado_locator_unico.wait_for(state="detached", timeout=10000)
        print(f"✅ [LIMPEZA] Cadastro '{nome_empregado}' (CPF: {cpf_empregado}) excluído com sucesso.")
    except Exception as e:
        print(f"AVISO: [LIMPEZA] Falha ao excluir o cadastro '{nome_empregado}' (CPF: {cpf_empregado}): {e}. Pode ser necessário excluir manualmente.")
        # take_screenshot(page, f"LIMPEZA_FALHA_{nome_empregado.replace(' ', '_')}_{cpf_empregado.replace('.', '').replace('-', '')}") # Não tira screenshot aqui para não gerar muitos em caso de falha de limpeza

# --- Classes de Teste ---

class TestFuncionaisCadastro:
    """
    Testes funcionais para o fluxo de cadastro, focando na inclusão e nas falhas de visibilidade/interação.
    """
    @pytest.fixture(scope="function", autouse=False) # Não autouse, pois queremos controlar a criação do empregado
    def employee_data_for_test(self):
        """
        Fixture para fornecer os dados de um empregado para o teste atual.
        """
        return TEST_EMPLOYEE_DATA.copy() # Retorna uma cópia para não alterar o original entre testes

    def test_01_inclusao_cadastro_empregado(self, page: Page, employee_data_for_test: dict):
        """
        Cenário: Verificar se o cadastro de um novo empregado pode ser incluído com sucesso.
        """
        print("\n--- TESTE 01: Inclusão de Cadastro de Empregado ---")
        page.goto(APP_URL)
        page.wait_for_load_state("networkidle")
        take_screenshot(page, "00_pagina_inicial_limpa")
        
        incluir_cadastro_externo(page, employee_data_for_test)

        # Esta asserção valida APENAS que o formulário de cadastro sumiu e a inclusão lógica ocorreu.
        # A validação da visibilidade na lista é feita no próximo teste.
        assert page.locator('button.save[type="submit"]:has-text("Salvar")').is_hidden(), \
            "Formulário de cadastro ainda visível após tentar salvar."
        
        print(f"✅ TESTE 01 CONCLUÍDO: Cadastro de '{employee_data_for_test['nome']}' (CPF: {employee_data_for_test['cpf']}) foi incluído com sucesso na aplicação.")


    def test_02_consulta_registro_nao_visivel_apos_inclusao_e_refresh(self, page: Page, employee_data_for_test: dict):
        """
        Cenário: Validar a visibilidade do registro recém-incluído na lista
        (problema de persistência/sincronização/paginação).
        """
        print("\n--- TESTE 02: Consulta de Registro - Não Visível Após Inclusão e Refresh ---")
        # Pré-condição: O cadastro já deve existir (assumimos que test_01 o criou).
        # Para garantir, o ideal seria criar o dado via API ou em um setup específico se este teste pudesse rodar isolado.
        # Como estamos num fluxo sequencial por enquanto, dependemos do teste anterior.
        
        page.goto(APP_URL) # Garante que estamos na página principal com a lista
        page.wait_for_load_state("networkidle")
        take_screenshot(page, "04_pagina_principal_apos_inclusao_teste_01", dados_empregado=employee_data_for_test)

        nome_empregado = employee_data_for_test["nome"]
        cpf_empregado = employee_data_for_test["cpf"]
        
        # Seletor AGORA COMBINA NOME E CPF para ser único e evitar "strict mode violation"
        # Usamos .first para pegar o primeiro que Playwright encontrar, caso haja múltiplos.
        empregado_locator_unico = page.locator(
            f'div.c-bXqUbA:has-text("{nome_empregado}"):has(div.c-iYbcAK:has-text("{cpf_empregado}"))'
        ).first 

        # Passo 1: Tentar encontrar o empregado recém-incluído IMEDIATAMENTE (sem refresh)
        print(f"DEBUG: Tentando encontrar '{nome_empregado}' (CPF: {cpf_empregado}) sem refresh (expectativa: NÃO visível)...")
        encontrado_sem_refresh = False
        try:
            empregado_locator_unico.wait_for(state="visible", timeout=5000)
            encontrado_sem_refresh = True
            print(f"AVISO: O empregado '{nome_empregado}' (CPF: {cpf_empregado}) foi encontrado imediatamente após a inclusão. Isso diverge do esperado de não-visualização sem refresh.")
            take_screenshot(page, f"05_ENCONTRADO_IMEDIATAMENTE", dados_empregado=employee_data_for_test)
        except TimeoutError:
            print(f"INFO: Empregado '{nome_empregado}' (CPF: {cpf_empregado}) NÃO encontrado imediatamente. Comportamento esperado. Prosseguindo para refresh...")
            take_screenshot(page, f"05_NAO_ENCONTRADO_IMEDIATAMENTE", dados_empregado=employee_data_for_test)

        # Passo 2: Fazer refresh da página
        print("DEBUG: Realizando refresh da página...")
        page.reload(wait_until="networkidle")
        print("DEBUG: Página recarregada.")
        take_screenshot(page, "06_pagina_principal_apos_refresh", dados_empregado=employee_data_for_test)
        
        # Passo 3: Tentar encontrar o empregado após o refresh (sem scroll)
        print(f"DEBUG: Tentando encontrar '{nome_empregado}' (CPF: {cpf_empregado}) após refresh (expectativa: NÃO visível, por falta de paginação)...")
        encontrado_apos_refresh = False
        try:
            empregado_locator_unico.wait_for(state="visible", timeout=10000)
            encontrado_apos_refresh = True
            print(f"AVISO: Empregado '{nome_empregado}' (CPF: {cpf_empregado}) encontrado após refresh (sem scroll). Isso diverge do esperado de paginação ausente.")
            take_screenshot(page, f"07_ENCONTRADO_APOS_REFRESH_SEM_SCROLL", dados_empregado=employee_data_for_test)
        except TimeoutError:
            print(f"INFO: Empregado '{nome_empregado}' (CPF: {cpf_empregado}) AINDA NÃO encontrado após refresh (sem scroll). Comportamento esperado. Prosseguindo para scroll...")
            take_screenshot(page, f"07_NAO_ENCONTRADO_APOS_REFRESH_SEM_SCROLL", dados_empregado=employee_data_for_test)

        # Passo 4: Tentar rolar a página para baixo e verificar novamente
        print("DEBUG: Tentando rolar a página para baixo para verificar se o registro aparece...")
        page.mouse.wheel(0, 10000) # Rola 10000 pixels para baixo. Ajuste se necessário.
        page.wait_for_timeout(2000) # Pequena pausa para a rolagem e renderização
        take_screenshot(page, f"08_pagina_principal_apos_scroll", dados_empregado=employee_data_for_test)

        encontrado_apos_scroll = False
        try:
            empregado_locator_unico.wait_for(state="visible", timeout=10000)
            encontrado_apos_scroll = True
            print(f"AVISO: Empregado '{nome_empregado}' (CPF: {cpf_empregado}) encontrado após scroll. Isso indica falta de paginação, mas o registro foi encontrado.")
            take_screenshot(page, f"09_ENCONTRADO_APOS_SCROLL", dados_empregado=employee_data_for_test)
        except TimeoutError:
            print(f"INFO: Empregado '{nome_empregado}' (CPF: {cpf_empregado}) AINDA NÃO encontrado APÓS SCROLL. Isso confirma o defeito de visualização/paginação.")
            take_screenshot(page, f"09_NAO_ENCONTRADO_APOS_SCROLL", dados_empregado=employee_data_for_test)

        # Passo 5: Falhar o teste com base nas observações do defeito de visualização/paginação
        # Se a expectativa é que ele NUNCA seja visível sem paginação/scroll e ele não foi encontrado nem com scroll
        if not encontrado_apos_scroll:
            pytest.fail(
                f"FALHA CRÍTICA: O cadastro de '{nome_empregado}' (CPF: {cpf_empregado}) NÃO É VISUALIZADO na lista "
                f"mesmo após inclusão, refresh E rolagem da página. Isso indica um defeito grave de persistência, "
                f"sincronização de dados E/OU ausência de paginação/scroll adequado. "
                f"Verifique as screenshots '05_NAO_ENCONTRADO_IMEDIATAMENTE', '07_NAO_ENCONTRADO_APOS_REFRESH_SEM_SCROLL' e '09_NAO_ENCONTRADO_APOS_SCROLL'."
            )
        # Se ele só foi encontrado após o scroll (o que você descreveu como um defeito)
        elif not encontrado_sem_refresh and encontrado_apos_scroll:
            pytest.fail(
                f"FALHA: O cadastro de '{nome_empregado}' (CPF: {cpf_empregado}) só é visível após rolagem da página. "
                f"Isso evidencia a falta de paginação automática, comprometendo a usabilidade e visibilidade dos dados."
            )
        elif encontrado_sem_refresh:
            pytest.fail(
                f"FALHA (DIVERGÊNCIA): O cadastro de '{nome_empregado}' (CPF: {cpf_empregado}) foi encontrado imediatamente, "
                f"divergindo da expectativa de não-visualização sem refresh. "
                f"Verifique a screenshot '05_ENCONTRADO_IMEDIATAMENTE'."
            )


    def test_03_tentativa_alteracao_e_exclusao_menu_ausente(self, page: Page, employee_data_for_test: dict):
        """
        Cenário: Tentar acessar as opções de alteração/exclusão via menu '...'
        e reportar a não-implementação/ausência do menu.
        """
        print("\n--- TESTE 03: Tentativa de Alteração/Exclusão - Menu Ausente ---")
        # Pré-condição: O cadastro já deve existir (criado por test_01).
        # É possível que este teste falhe se o registro não for encontrado ou
        # se o menu de dots estiver sob algum problema de visibilidade/interação.
        
        page.goto(APP_URL) # Garante que estamos na página principal com a lista
        page.wait_for_load_state("networkidle")
        
        nome_empregado = employee_data_for_test["nome"]
        cpf_empregado = employee_data_for_test["cpf"]

        # Seletor para encontrar o registro único pelo nome e CPF
        # Usamos .first para pegar o primeiro, caso haja múltiplos.
        empregado_locator_unico = page.locator(
            f'div.c-bXqUbA:has-text("{nome_empregado}"):has(div.c-iYbcAK:has-text("{cpf_empregado}"))'
        ).first
        
        # Tenta rolar para o elemento, caso ele esteja fora da viewport (se o teste anterior não fez isso ou falhou)
        try:
            empregado_locator_unico.scroll_into_view_if_needed(timeout=10000)
            print(f"DEBUG: Rolou a tela para '{nome_empregado}' (CPF: {cpf_empregado}) para tentar visualizá-lo.")
        except TimeoutError:
            print(f"AVISO: Não foi possível rolar a tela até '{nome_empregado}' (CPF: {cpf_empregado}) para tentar acessar o menu. Pode não estar visível.")
            take_screenshot(page, f"10_NAO_VISIVEL_PARA_MENU_DOTS", dados_empregado=employee_data_for_test)
            pytest.fail(f"FALHA: Empregado '{nome_empregado}' não visível para interagir com o menu '...'. "
                       f"Requisito: Tentar alteração/exclusão. Pode ser um desdobramento do problema de visualização.")
        
        take_screenshot(page, f"10_antes_clicar_dots", dados_empregado=employee_data_for_test)
        
        # Espera e clica nos dots do registro
        dots_locator = empregado_locator_unico.locator('div.c-jyZWAy') # Selector para o div que contém a imagem dos dots
        
        dots_locator.wait_for(state="visible", timeout=5000) 
        dots_locator.click()

        # Tenta esperar que o botão 'Editar' ou 'Excluir' apareça no menu
        menu_apareceu = False
        try:
            page.locator('button:has-text("Editar")').wait_for(state="visible", timeout=5000)
            menu_apareceu = True
            print(f"AVISO: Menu 'Alterar/Excluir' APARECEU para {nome_empregado}. Isso difere do esperado (não implementação no protótipo).")
            take_screenshot(page, f"11_MENU_ALTERAR_EXCLUIR_APARECEU", dados_empregado=employee_data_for_test)
            
            # Se o menu apareceu e a expectativa é que não apareça, o teste falha aqui.
            pytest.fail(
                f"FALHA: O menu 'Alterar/Excluir' APARECEU para '{nome_empregado}' (CPF: {cpf_empregado}), "
                f"contrariando a observação de não-implementação no protótipo. "
                f"Verifique a screenshot '11_MENU_ALTERAR_EXCLUIR_APARECEU...'. "
                f"Se a funcionalidade foi implementada, o teste precisa ser ajustado."
            )
        except TimeoutError:
            print(f"INFO: Menu 'Alterar/Excluir' NÃO APARECEU para {nome_empregado} após 5 segundos. Comportamento esperado (não implementação).")
            take_screenshot(page, f"11_NAO_IMPLEMENTADO_Menu_Alterar_Excluir", dados_empregado=employee_data_for_test)
            # Falha o teste intencionalmente para reportar o bug de não-implementação do menu
            pytest.fail(
                f"FALHA: A funcionalidade de 'Alterar/Excluir' não está implementada. "
                f"O menu não apareceu ao clicar nos '...' para o funcionário '{nome_empregado}' (CPF: {cpf_empregado}). "
                f"Verifique a screenshot '11_NAO_IMPLEMENTADO_Menu_Alterar_Excluir...'. "
                f"Este é um defeito de funcionalidade conforme o protótipo."
            )

