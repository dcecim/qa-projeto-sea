from test_funcionais import TestFuncionais

def test_ler_dados_csv():
    test = TestFuncionais()
    dados = test.ler_dados_csv()
    assert len(dados) > 0, "O arquivo CSV está vazio ou não foi lido corretamente."
    print("Dados lidos do CSV:", dados)
