import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# Lendo o CSV
escolas = pd.read_csv("escolas.csv")

# vê se o csv foi carregado de forma correta e os nomes das colunas
escolas.head()


#Processamento de dados
# Respondendo pergunta 1 (média maior que 80%, 80% de 800 é 640)
best_math_escolas = (
    escolas[escolas["media_matematica"] >= 640][["nome_escola", "media_matematica"]]
    .sort_values(by="media_matematica", ascending=False)
)


# Respondendo pergunta 2: calculo do total SAT de cada escola(soma de todas as médias das escola)
escolas["total_SAT"] = (
    escolas["media_matematica"]
    + escolas["media_portugues"]
    + escolas["media_redacao"]
)
#Selecionando o top 10 em ordem decrescente
top_10_escolas = (
    escolas[["nome_escola", "total_SAT"]]
    .sort_values(by="total_SAT", ascending=False)
    .head(10)
)


# Respondendo pergunta 3: Região com o maior desvio padrão no total_SAT
# Agrupa por região e calcula a quantidade de escolas da região, média daquela região e desvio padrão
regiao_stats = (
    escolas.groupby("regiao")["total_SAT"]
    .agg(["count", "mean", "std"])
    #tranformando as regiões em coluna comum novamente
    .reset_index()
)

# Colocando os nomes das colunas conforme o problema
regiao_stats.columns = ["regiao", "num_escolas", "media_SAT", "desvio_padrão_SAT"]

# Separando apenas a linha com o maior desvio padrão
largest_std_dev = regiao_stats.sort_values(by="desvio_padrão_SAT", ascending=False).head( 1)

# Arredondando os valores numéricos para duas casas decimais
largest_std_dev = largest_std_dev.round({"media_SAT": 2, "desvio_padrão_SAT": 2})


# 3. Exibição no console
print("\n" + "=" * 50)
print("1. MELHORES ESCOLAS EM MATEMÁTICA (Top 5):")
print("=" * 50)
print(best_math_escolas.head())

print("\n" + "=" * 50)
print("2. TOP 10 ESCOLAS GERAL (SAT TOTAL):")
print("=" * 50)
print(top_10_escolas)

print("\n" + "=" * 50)
print("3. Região COM MAIOR DESVIO PADRÃO:")
print("=" * 50)
print(largest_std_dev)
print("=" * 50 + "\n")


#Mostrando os gráficos
# Configurando estilo visual do gráfico
sns.set_theme(style="whitegrid")
plt.figure(1, figsize=(12, 6))

# Criando o gráfico de barras horizontais usando o Top 10 médias
sns.barplot(
    data=top_10_escolas, x="total_SAT", y="nome_escola",
    hue="nome_escola", palette="viridis", legend=False
)

# Criando títulos e formatações
plt.title(
    "Top 10 Escolas do Brasil por Pontuação Combinada do SAT", fontsize=14, pad=15,)
plt.xlabel("Pontuação Total do SAT (Máx 2400)", fontsize=12)
plt.ylabel("Nome da Escola", fontsize=12)


# Ajusta o espaçamento para não cortar o nome das escolas
plt.tight_layout()

# Gráfico 2 com as 5 melhores escolas em matemática
plt.figure(2, figsize=(10, 5))

sns.barplot(
    data=best_math_escolas.head(5),  # Mostrando apenas o top 5
    x="media_matematica",
    y="nome_escola",
    hue="nome_escola",
    palette="magma",                 # paleta diferente do outro gráfico
    legend=False
)
plt.title("Top 5 Escolas com Melhor Desempenho em Matemática", fontsize=14, pad=15)
plt.xlabel("Nota Média em Matemática (Máx 800)", fontsize=12)
plt.ylabel("Nome da Escola", fontsize=12)
plt.tight_layout()


# Abre as janelas dos gráficos no pycharm
plt.show()
