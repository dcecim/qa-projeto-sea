import csv
import pytest
from playwright.sync_api import Page

# URL da aplicação
APP_URL = "http://analista-teste.seatecnologia.com.br/"

# Caminho do arquivo CSV
CSV_FILE = "C:/Temp/qa-projeto-sea/tests/dados_teste.csv"

class TestFuncionais:
    """
    Testes funcionais para inclusão, alteração e exclusão de cadastros.
    """

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Configuração inicial para cada teste."""
        page.goto(APP_URL)
        page.wait_for_load_state("networkidle")

    def ler_dados_csv(self):
        """Lê os dados do arquivo CSV."""
        print("Lendo o arquivo CSV...")
        with open(CSV_FILE, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return [row for row in reader]

    def selecionar_dropdown(self, page: Page, dropdown_selector: str, valor: str):
        """
        Seleciona um valor em um campo dropdown customizado (Ant Design).
        :param dropdown_selector: Seletor do dropdown.
        :param valor: Valor a ser selecionado.
        """
        # Clica no dropdown para abrir as opções
        page.locator(dropdown_selector).click()
        # Seleciona o valor desejado
        page.locator(f"li[title='{valor}']").click()

    def selecionar_sexo(self, page: Page, sexo: str):
        """
        Seleciona o sexo (Feminino ou Masculino).
        :param sexo: Valor do sexo (feminino/masculino).
        """
        page.locator(f'input.ant-radio-input[value="{sexo.lower()}"]').click()

    def incluir_cadastro(self, page: Page, dados: dict):
        """Inclui um novo cadastro com os dados fornecidos."""
        page.locator('button:has-text("+ Adicionar Funcionário")').click()
        page.fill('input[name="nome"]', dados["nome"])
        page.fill('input[name="cpf"]', dados["cpf"])
        page.fill('input[name="rg"]', dados["rg"])

        # Seleciona o cargo no dropdown
        self.selecionar_dropdown(page, '.ant-select-selector', dados["cargo"])

        # Preenche a data de nascimento
        page.fill('input[name="birthDay"]', dados["data_nascimento"])

        # Seleciona o sexo
        self.selecionar_sexo(page, dados["sexo"])

        # Seleciona o EPI (Sim/Não)
        if dados["epi"].lower() == "sim":
            page.locator('span.ant-switch-inner-checked').click()
        else:
            page.locator('span.ant-switch-inner-unchecked').click()

        page.locator('button:has-text("Salvar")').click()
        page.wait_for_timeout(1000)  # Aguarda a finalização do processo
        print(f"✅ Cadastro incluído: {dados}")

    def alterar_cadastro(self, page: Page, dados_antigos: dict, dados_novos: dict):
        """Altera um cadastro existente."""
        page.locator(f'tr:has-text("{dados_antigos["nome"]}") button:has-text("Editar")').click()
        page.fill('input[name="nome"]', dados_novos["nome"])
        page.fill('input[name="cpf"]', dados_novos["cpf"])
        page.fill('input[name="rg"]', dados_novos["rg"])

        # Seleciona o novo cargo no dropdown
        self.selecionar_dropdown(page, '.ant-select-selector', dados_novos["cargo"])

        # Preenche a nova data de nascimento
        page.fill('input[name="birthDay"]', dados_novos["data_nascimento"])

        # Seleciona o novo sexo
        self.selecionar_sexo(page, dados_novos["sexo"])

        # Seleciona o novo EPI (Sim/Não)
        if dados_novos["epi"].lower() == "sim":
            page.locator('span.ant-switch-inner-checked').click()
        else:
            page.locator('span.ant-switch-inner-unchecked').click()

        page.locator('button:has-text("Salvar")').click()
        page.wait_for_timeout(1000)  # Aguarda a finalização do processo
        print(f"✅ Cadastro alterado: {dados_novos}")

    def excluir_cadastro(self, page: Page, dados: dict):
        """Exclui um cadastro existente."""
        page.locator(f'tr:has-text("{dados["nome"]}") button:has-text("Excluir")').click()
        page.locator('button:has-text("Confirmar")').click()
        page.wait_for_timeout(1000)  # Aguarda a finalização do processo
        print(f"✅ Cadastro excluído: {dados}")

    def test_fluxo_cadastro(self, page: Page):
        """
        Testa o fluxo completo de inclusão, alteração e exclusão de cadastros.
        """
        print("Executando o teste de fluxo de cadastro...")
        dados_teste = self.ler_dados_csv()

        for dados in dados_teste:
            # Etapa 1: Inclusão
            self.incluir_cadastro(page, dados)

            # Dados para alteração
            dados_alterados = {
                "nome": f"{dados['nome']} Alterado",
                "cpf": dados["cpf"],
                "rg": dados["rg"],
                "cargo": "Supervisor",  # Alteração para um cargo diferente
                "data_nascimento": "2000-01-01",  # Nova data de nascimento
                "sexo": "masculino" if dados["sexo"].lower() == "feminino" else "feminino",
                "epi": "Nao" if dados["epi"].lower() == "sim" else "Sim"
            }

            # Etapa 2: Alteração
            self.alterar_cadastro(page, dados, dados_alterados)

            # Etapa 3: Exclusão
            self.excluir_cadastro(page, dados_alterados)