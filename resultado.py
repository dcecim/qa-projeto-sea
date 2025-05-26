import pandas as pd
import io
import matplotlib.pyplot as plt
import os
import numpy as np

def generate_test_report_data(csv_file_path):
    """
    Lê um arquivo CSV de resultados de testes, calcula estatísticas,
    gera gráficos e retorna os dados para o relatório.
    """
    df_results = None
    encodings_to_try = ['utf-8', 'latin1', 'cp1252']
    delimiters_to_try = [';', ','] # Prioriza ponto e vírgula

    try:
        for delimiter in delimiters_to_try:
            for encoding in encodings_to_try:
                try:
                    print(f"DEBUG: Tentando ler CSV com delimitador '{delimiter}' e codificação '{encoding}'...")
                    df_temp = pd.read_csv(csv_file_path, encoding=encoding, delimiter=delimiter)
                    # Verifica se a coluna 'Resultado' E 'Cenário' existem
                    if 'Resultado' in df_temp.columns and 'Cenário' in df_temp.columns:
                        df_results = df_temp
                        print(f"DEBUG: CSV lido com sucesso (delimitador '{delimiter}', codificação '{encoding}'). Colunas: {df_results.columns.tolist()}")
                        break 
                    else:
                        missing_cols = []
                        if 'Resultado' not in df_temp.columns: missing_cols.append('Resultado')
                        if 'Cenário' not in df_temp.columns: missing_cols.append('Cenário')
                        print(f"DEBUG: Coluna(s) {', '.join(missing_cols)} não encontrada(s) com delimitador '{delimiter}' e codificação '{encoding}'.")
                        df_results = None 
                except UnicodeDecodeError:
                    print(f"DEBUG: Falha de UnicodeDecodeError com delimitador '{delimiter}' e codificação '{encoding}'.")
                    continue
                except pd.errors.ParserError:
                    print(f"DEBUG: Falha de ParserError com delimitador '{delimiter}' e codificação '{encoding}'.")
                    continue
                except Exception as e:
                    print(f"DEBUG: Erro inesperado ({e}) com delimitador '{delimiter}' e codificação '{encoding}'.")
                    continue
            if df_results is not None and 'Resultado' in df_results.columns and 'Cenário' in df_results.columns:
                break 
        
        if df_results is None or 'Resultado' not in df_results.columns or 'Cenário' not in df_results.columns:
            raise ValueError("Não foi possível ler o CSV corretamente ou as colunas 'Resultado' e 'Cenário' estão ausentes após todas as tentativas.")

    except FileNotFoundError:
        print(f"ERRO: Arquivo CSV não encontrado em '{csv_file_path}'")
        print("Usando dados de exemplo internos para demonstração (com coluna 'Cenário').")
        csv_content_fallback = """Cenário;Caso de Teste;Resultado
Testes de Compatibilidade;CT-COMP-001;Passou
Testes de Compatibilidade;CT-COMP-002;Falhou
Testes de Navegação;CT-NAV-001;Passou
"""
        df_results = pd.read_csv(io.StringIO(csv_content_fallback), delimiter=';')
        if 'Resultado' not in df_results.columns or 'Cenário' not in df_results.columns:
            print(f"ERRO CRÍTICO: Colunas essenciais não encontradas nos dados de fallback. Colunas: {df_results.columns.tolist()}")
            return {}
            
    except ValueError as ve:
        print(f"ERRO CRÍTICO: {ve}")
        # ... (código de fallback como antes, mas garantindo que tenha 'Cenário' e 'Resultado') ...
        csv_content_fallback = """Cenário;Caso de Teste;Resultado
Testes de Exemplo;Exemplo CT1;Passou
"""
        df_results = pd.read_csv(io.StringIO(csv_content_fallback), delimiter=';')
        if 'Resultado' not in df_results.columns or 'Cenário' not in df_results.columns:
             return {} # Retorna vazio se o fallback também falhar
            
    except Exception as e:
        print(f"ERRO INESPERADO ao ler o CSV: {e}")
        # ... (código de fallback como antes) ...
        csv_content_fallback = """Cenário;Caso de Teste;Resultado
Testes de Exemplo;Exemplo CT1;Passou
"""
        df_results = pd.read_csv(io.StringIO(csv_content_fallback), delimiter=';')
        if 'Resultado' not in df_results.columns or 'Cenário' not in df_results.columns:
            return {}

    # --- 1. Calcular Estatísticas ---
    total_tests = len(df_results)
    results_counts = df_results['Resultado'].value_counts()
    passed_tests = results_counts.get('Passou', 0)
    failed_tests = results_counts.get('Falhou', 0)
    blocked_tests = results_counts.get('Bloqueado', 0) # Considerar se "Bloqueado" existe no seu CSV

    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0
    fail_percentage = (failed_tests / total_tests) * 100 if total_tests > 0 else 0
    block_percentage = (blocked_tests / total_tests) * 100 if total_tests > 0 else 0

    # USA A COLUNA "Cenário" EM VEZ DE "Funcionalidade"
    tests_per_group = df_results['Cenário'].value_counts().sort_values(ascending=False)

    # --- 2. Gerar Gráficos ---
    output_dir = "reports_graphs"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    pie_chart_path = None
    if passed_tests + failed_tests + blocked_tests > 0:
        labels = []
        sizes = []
        colors = []
        explode_values = []
        if passed_tests > 0:
            labels.append(f'Passaram ({passed_tests})'); sizes.append(passed_tests); colors.append('#66bb6a'); explode_values.append(0.05)
        if failed_tests > 0:
            labels.append(f'Falharam ({failed_tests})'); sizes.append(failed_tests); colors.append('#ef5350'); explode_values.append(0.05)
        if blocked_tests > 0:
            labels.append(f'Bloqueados ({blocked_tests})'); sizes.append(blocked_tests); colors.append('#ffab40'); explode_values.append(0.05)
        
        if sizes:
            fig1, ax1 = plt.subplots(figsize=(8, 7))
            ax1.pie(sizes, explode=tuple(explode_values), labels=labels, colors=colors, autopct='%1.1f%%',
                    shadow=True, startangle=140, pctdistance=0.85, labeldistance=1.05)
            ax1.axis('equal') 
            plt.title('Visão Geral dos Resultados dos Testes', pad=20, fontsize=16)
            pie_chart_path = os.path.join(output_dir, "test_results_pie_chart.png")
            plt.savefig(pie_chart_path, bbox_inches='tight')
            plt.close(fig1)
            print(f"\nGráfico de Pizza salvo em: {pie_chart_path}")

    bar_chart_path = None
    if not tests_per_group.empty:
        fig2, ax2 = plt.subplots(figsize=(10, max(6, len(tests_per_group) * 0.5)))
        tests_per_group.sort_values(ascending=True).plot(kind='barh', ax=ax2, color='skyblue')
        ax2.set_title('Número de Casos de Teste por Cenário', fontsize=16, pad=20) # Título alterado
        ax2.set_xlabel('Número de Casos de Teste', fontsize=12)
        ax2.set_ylabel('Cenário', fontsize=12) # Label alterada
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        for index, value in enumerate(tests_per_group.sort_values(ascending=True)):
            ax2.text(value + 0.1, index, str(value), va='center', fontsize=10)
        plt.tight_layout()
        bar_chart_path = os.path.join(output_dir, "tests_per_scenario_bar_chart.png") # Nome do arquivo alterado
        plt.savefig(bar_chart_path)
        plt.close(fig2)
        print(f"Gráfico de Barras salvo em: {bar_chart_path}")

    # Ajusta para colunas existentes no seu CSV para detalhes
    cols_para_detalhes = ['Cenário', 'Caso de Teste', 'Resultado'] 
    # Se 'Observações' existir, adicione-a. Caso contrário, o fillna('') lidará com isso.
    if 'Observações' in df_results.columns:
        cols_para_detalhes.append('Observações')
    
    failed_tests_details = df_results[df_results['Resultado'] == 'Falhou'][cols_para_detalhes].fillna('')
    blocked_tests_details = df_results[df_results['Resultado'] == 'Bloqueado'][cols_para_detalhes].fillna('')
    
    # Para data de execução, se a coluna 'Data' não existir, defina como "N/A"
    execution_date_str = "N/A"
    # O CSV fornecido não tem coluna 'Data', então esta parte não será usada, mas é bom manter se você adicionar a coluna.
    # if 'Data' in df_results.columns and not df_results['Data'].dropna().empty:
    #     try:
    #         valid_dates = pd.to_datetime(df_results['Data'], errors='coerce').dropna()
    #         if not valid_dates.empty:
    #             execution_date_str = valid_dates.max().strftime('%Y-%m-%d')
    #         else:
    #             execution_date_str = df_results['Data'].iloc[-1] if not df_results['Data'].empty else "N/A"
    #     except Exception as e_date:
    #         print(f"AVISO: Não foi possível processar a coluna 'Data' corretamente: {e_date}")
    #         execution_date_str = df_results['Data'].iloc[-1] if 'Data' in df_results.columns and not df_results['Data'].empty else "N/A"

    report_data = {
        "total_tests": total_tests, "passed_tests": passed_tests, "failed_tests": failed_tests,
        "blocked_tests": blocked_tests, "pass_percentage": f"{pass_percentage:.2f}%",
        "fail_percentage": f"{fail_percentage:.2f}%", "block_percentage": f"{block_percentage:.2f}%",
        "tests_per_group_dict": tests_per_group.to_dict(), # Alterado de 'tests_per_functionality_dict'
        "pie_chart_path": pie_chart_path, "bar_chart_path": bar_chart_path,
        "failed_tests_details_html": failed_tests_details.to_html(index=False, classes='table table-striped table-sm', justify='left', border=0) if not failed_tests_details.empty else "<p>Nenhum teste falhou.</p>",
        "blocked_tests_details_html": blocked_tests_details.to_html(index=False, classes='table table-striped table-sm', justify='left', border=0) if not blocked_tests_details.empty else "<p>Nenhum teste foi bloqueado.</p>",
        "execution_date": execution_date_str # Será N/A se a coluna Data não existir
    }
    return report_data

if __name__ == '__main__':
    csv_path = 'Resultado dos testes.csv' # Nome do seu arquivo CSV
    
    if not os.path.exists(csv_path):
        print(f"AVISO: O arquivo '{csv_path}' não foi encontrado no diretório atual.")
        print("O script continuará usando dados de exemplo internos para demonstração.")
    
    report_data_output = generate_test_report_data(csv_path)
    
    if report_data_output: 
        print("\n\n--- Dados para o Relatório ---")
        # ... (impressão dos dados)
        md_content = f"""
# Relatório de Execução de Testes

**Data da Execução:** {report_data_output.get('execution_date', 'N/A')}

## 1. Resumo Geral
- **Total de Casos de Teste Executados:** {report_data_output.get('total_tests', 0)}
- **Passaram:** {report_data_output.get('passed_tests', 0)} ({report_data_output.get('pass_percentage', '0.00%')})
- **Falharam:** {report_data_output.get('failed_tests', 0)} ({report_data_output.get('fail_percentage', '0.00%')})
- **Bloqueados:** {report_data_output.get('blocked_tests', 0)} ({report_data_output.get('block_percentage', '0.00%')})

## 2. Visão Geral dos Resultados (Gráfico)
![Visão Geral dos Resultados dos Testes]({report_data_output.get('pie_chart_path', 'reports_graphs/test_results_pie_chart.png') if report_data_output.get('pie_chart_path') else ''})

## 3. Casos de Teste por Cenário
![Casos de Teste por Cenário]({report_data_output.get('bar_chart_path', 'reports_graphs/tests_per_scenario_bar_chart.png') if report_data_output.get('bar_chart_path') else ''})
"""
        # Alterado de tests_per_functionality_dict para tests_per_group_dict
        tests_per_group_dict = report_data_output.get('tests_per_group_dict', {})
        if tests_per_group_dict:
            md_content += "\n### Detalhes por Cenário:\n" # Alterado
            for grupo, count in tests_per_group_dict.items(): # Alterado
                md_content += f"- **{grupo}:** {count} caso(s) de teste\n" # Alterado

        md_content += f"""
## 4. Detalhes dos Testes que Falharam
{report_data_output.get('failed_tests_details_html', '<p>N/A</p>')}

## 5. Detalhes dos Testes Bloqueados
{report_data_output.get('blocked_tests_details_html', '<p>N/A</p>')}

## 6. Conclusão e Recomendações
(Espaço para suas conclusões e recomendações)
"""
        report_filename = "relatorio_testes_gerado.md"
        with open(report_filename, "w", encoding="utf-8") as f:
            f.write(md_content)
        print(f"\nRelatório Markdown simplificado gerado: {report_filename}")
    else:
        print("Não foi possível gerar os dados do relatório devido a um erro na leitura do CSV.")


