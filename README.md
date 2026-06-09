# Análise de Faturamento e Desempenho de Vendas (E-commerce) com Python

Este projeto realiza uma análise estatística e visual sobre o desempenho de vendas de uma plataforma de e-commerce brasileira com 50 registros de transações distribuídas ao longo do ano de 2026.

O objetivo principal foi responder a três perguntas de negócio:

1. Qual é a evolução do faturamento mensal da empresa ao longo do ano?
2. Quais são as 5 categorias de produtos líderes em faturamento acumulado?
3. Qual é o ticket médio (valor médio gasto) por pedido registrado?

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Pandas**: Para a manipulação, tratamento de tipos (`datetime` e `string`) e agrupamento (`groupby`) dos dados de vendas.
* **Seaborn e Matplotlib**: Para a geração de gráficos de linha temporais e barras horizontais independentes.

## 📈 Resultados e Insights de Negócio

O processamento e a agregação dos dados geram insights automáticos que auxiliam na tomada de decisões estratégicas:

* **Sazonalidade Temporal**: O mapeamento mensal em linha contínua permite identificar os meses com picos de vendas e vales de faturamento, otimizando o planejamento de estoque e campanhas de marketing.
* **Curva de Performance de Produtos**: O ranking das 5 principais mercadorias aponta visualmente quais itens sustentam a maior fatia da receita do e-commerce.
* **Eficiência Comercial**: O cálculo automatizado do Ticket Médio estabelece a métrica base para avaliar o poder de compra do cliente e a eficácia de estratégias de *cross-selling*.