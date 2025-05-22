import pytest
import os

def pytest_configure(config):
    """
    Configuração inicial do pytest.
    """
    # Cria diretório para screenshots se não existir
    os.makedirs("C:/Temp/qa-projeto-sea/tests/screenshots", exist_ok=True)
    
    print("Iniciando testes automatizados para o projeto SEA Tecnologia")
    print("URL da aplicação: https://analista-teste.seatecnologia.com.br/")
    print("URL do protótipo: https://tinyurl.com/yl58hs4m")

def pytest_sessionfinish(session, exitstatus):
    """
    Executa ao finalizar a sessão de testes.
    """
    print("\n===== Resumo da Execução de Testes =====")
    print(f"Total de testes executados: {session.testscollected}")
    print(f"Testes com sucesso: {session.testscollected - session.testsfailed}")
    print(f"Testes com falha: {session.testsfailed}")
    
    if session.testsfailed == 0:
        print("\n✅ Todos os testes foram executados com sucesso!")
    else:
        print(f"\n⚠️ {session.testsfailed} teste(s) falharam. Verifique os logs para mais detalhes.")
    
    print("\nEvidências de teste disponíveis em: /home/ubuntu/qa-projeto-sea/tests/screenshots")
    print("=======================================")
