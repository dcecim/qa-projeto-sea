import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# Carregar os dados do arquivo CSV
try:
    # Tenta ler com o separador padrão (vírgula)
    df_results = pd.read_csv("Resultado dos testes.csv")
except Exception as e:
    print(f"Erro ao ler o CSV com separador padrão: {e}")
    try:
        # Tenta ler com ponto e vírgula como separador (comum em algumas regiões)
        df_results = pd.read_csv("Resultado dos testes.csv", sep=';')
        print("CSV lido com sucesso usando ';' como separador.")
    except Exception as e_sep:
        print(f"Erro ao ler o CSV com ';' como separador: {e_sep}")
        print("Verifique o separador do seu arquivo CSV ou o caminho do arquivo.")
        exit()

# --- Limpeza e Preparação dos Dados ---
# Remover espaços em branco extras dos nomes das colunas, se houver
df_results.columns = df_results.columns.str.strip()

# Padronizar os valores da coluna 'Resultado' (ex: 'Passou ' para 'Passou')
if 'Resultado' in df_results.columns:
    df_results['Resultado'] = df_results['Resultado'].str.strip().str.capitalize()
else:
    print("Erro: A coluna 'Resultado' não foi encontrada no arquivo CSV. Verifique os nomes das colunas.")
    exit()

# --- Estatísticas Gerais ---
total_test_cases = len(df_results)
results_counts = df_results['Resultado'].value_counts()
passed_count = results_counts.get('Passou', 0)
failed_count = results_counts.get('Falhou', 0)
blocked_count = results_counts.get('Bloqueado', 0)
other_statuses_count = total_test_cases - (passed_count + failed_count + blocked_count)

pass_rate = (passed_count / total_test_cases) * 100 if total_test_cases > 0 else 0
fail_rate = (failed_count / total_test_cases) * 100 if total_test_cases > 0 else 0
blocked_rate = (blocked_count / total_test_cases) * 100 if total_test_cases > 0 else 0

# --- Estatísticas por Funcionalidade ---
tests_per_functionality = df_results['Funcionalidade'].value_counts()
results_by_functionality = df_results.groupby('Funcionalidade')['Resultado'].value_counts().unstack(fill_value=0)

# --- Geração do Gráfico de Resultados ---
plt.style.use('seaborn-v0_8-whitegrid') # Usando um estilo visualmente agradável
fig, ax = plt.subplots(figsize=(10, 6))

# Cores para as barras
colors = {'Passou': 'green', 'Falhou': 'red', 'Bloqueado': 'orange', 'Outros': 'grey'}
status_labels = ['Passou', 'Falhou', 'Bloqueado']
counts = [passed_count, failed_count, blocked_count]
bar_colors = [colors.get(label, 'grey') for label in status_labels]

if other_statuses_count > 0:
    status_labels.append('Outros')
    counts.append(other_statuses_count)
    bar_colors.append(colors['Outros'])

bars = ax.bar(status_labels, counts, color=bar_colors)

# Adicionar porcentagens no topo das barras
for bar in bars:
    yval = bar.get_height()
    percentage = (yval / total_test_cases) * 100
    ax.text(bar.get_x() + bar.get_width()/2.0, yval + (total_test_cases*0.01), f'{percentage:.1f}% ({yval})', ha='center', va='bottom', fontsize=10, color='black')

ax.set_title('Resumo Geral dos Resultados dos Testes', fontsize=16, fontweight='bold')
ax.set_ylabel('Número de Casos de Teste', fontsize=12)
ax.set_xlabel('Resultado', fontsize=12)
ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True)) # Garante que o eixo Y mostre apenas inteiros
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout() # Ajusta o layout para evitar sobreposição

# Salvar o gráfico como imagem
graph_path = "relatorio_testes_grafico.png"
plt.savefig(graph_path)
print(f"Gráfico salvo em: {graph_path}")
plt.close() # Fecha a figura para liberar memória

# --- Preparar Dados para o Relatório ---
print("\n--- DADOS PARA O RELATÓRIO ---")
print(f"Total de Casos de Teste Executados: {total_test_cases}")
print(f"Passaram: {passed_count} ({pass_rate:.2f}%)")
print(f"Falharam: {failed_count} ({fail_rate:.2f}%)")
print(f"Bloqueados: {blocked_count} ({blocked_rate:.2f}%)")
if other_statuses_count > 0:
    print(f"Outros Status: {other_statuses_count} ({(other_statuses_count/total_test_cases)*100:.2f}%)")

print("\nResultados Detalhados por Funcionalidade:")
print(results_by_functionality.to_string())

print(f"\nCaminho do gráfico gerado: {graph_path}")

# Detalhes dos testes que falharam ou foram bloqueados (para a seção de Análise)
failed_tests_details = df_results[df_results['Resultado'] == 'Falhou'][['ID', 'Funcionalidade', 'Caso de Teste', 'Observações']]
blocked_tests_details = df_results[df_results['Resultado'] == 'Bloqueado'][['ID', 'Funcionalidade', 'Caso de Teste', 'Observações']]

print("\nCasos de Teste que Falharam:")
if not failed_tests_details.empty:
    print(failed_tests_details.to_string(index=False))
else:
    print("Nenhum caso de teste falhou.")

print("\nCasos de Teste Bloqueados:")
if not blocked_tests_details.empty:
    print(blocked_tests_details.to_string(index=False))
else:
    print("Nenhum caso de teste foi bloqueado.")

