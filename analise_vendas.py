import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Nome do arquivo CSV (se estiver na mesma pasta do script)
caminho_arquivo = 'vendas.csv'


# 1. Verifica se o arquivo existe e carrega o mesmo
try:
    df = pd.read_csv(caminho_arquivo)
    print(f"Arquivo '{caminho_arquivo}' carregado com sucesso!\n")
except FileNotFoundError:
    print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
    print("Certifique-se de que o CSV está na mesma pasta do seu código Python.")
    exit()

# 2. LIMPEZA E TRATAMENTO
# Garantir que a coluna de data seja reconhecida como datetime
df['data'] = pd.to_datetime(df['data'])

# Criar a coluna de Faturamento Total (Quantidade x Preço)
df['faturamento_total'] = df['quantidade'] * df['preco_unitario']

# Criar uma coluna de Ano-Mês para o agrupamento mensal
df['ano_mes'] = df['data'].dt.strftime('%m/%Y')


# 3. Análise

# Pergunta 1: Faturamento mensal
faturamento_mensal = df.groupby('ano_mes')['faturamento_total'].sum().reset_index()

# Pergunta 2: Top 5 produtos por faturamento
top_produtos = df.groupby('produto')['faturamento_total'].sum().reset_index()
top_produtos = top_produtos.sort_values(by='faturamento_total', ascending=False).head(5)

# Pergunta 3: Ticket Médio Geral
ticket_medio = df['faturamento_total'].mean()

print("Resultados")
print(f"Faturamento Mensal:\n{faturamento_mensal}\n")
print(f"Top Produtos por Faturamento:\n{top_produtos}\n")
print(f"Ticket Médio por Pedido: R$ {ticket_medio:.2f}\n")


# 4. Gráficos com os resultados da análise

# Configurando o estilo dos gráficos
sns.set_theme(style="whitegrid")

# GUIA 1: Faturamento Mensal
plt.figure(1, figsize=(10, 5))
plt.clf()

# Desenha a linha unida e contínua
#Não precisa do hue por ser uma "informação" só
sns.lineplot(data=faturamento_mensal, x='ano_mes', y='faturamento_total', marker='o', color='b', linewidth=2.5)

plt.title('Evolução do Faturamento Mensal (2026)', fontsize=14, pad=15)
plt.xlabel('Mês/Ano', fontsize=12)
plt.ylabel('Faturamento (R$)', fontsize=12)
plt.tight_layout()


# GUIA 2 Top Produtos
plt.figure(2, figsize=(10, 5))
plt.clf()

# Gráfico de barras
sns.barplot(data=top_produtos, x='faturamento_total', y='produto', hue='produto', palette='Blues_r', legend=False)

plt.title('Top 5 Produtos por Faturamento', fontsize=14, pad=15)
plt.xlabel('Faturamento Acumulado (R$)', fontsize=12)
plt.ylabel('Produto', fontsize=12)
plt.tight_layout()

#abre as duas janelas ao mesmo tempo
plt.show()
