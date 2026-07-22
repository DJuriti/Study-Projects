import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_excel('../dados/vendas.xlsx')

dados['Faturamento'] = dados['Quantidade'] * dados['Preço']

faturamento_produto = dados.groupby('Produto')['Faturamento'].sum()

#Transforma os dados em um gráfico de barras, o 'kind' define o tipo 'bar=barras'
faturamento_produto.plot(kind='bar')

#Titulo, nome do gráfico
plt.title('Faturamento por Produto')
#Nome do eixo horizontal
plt.xlabel('Produto')
#Nome do eixo vertical
plt.ylabel('Faturamento (R$)')

#Mostra o gráfico
plt.show()

faturamento_categoria = dados.groupby("Categoria")["Faturamento"].sum()
#Cria gráfico de pizza 'kind='pie'/Coloca porcentagem dentro da pizza 'autopct'
faturamento_categoria.plot(kind="pie", autopct="%1.1f%%")
plt.title("Distribuição do Faturamento por Categoria")
plt.ylabel("")

plt.show()

#Transforma a data do Excel em um formato que o Pandas entende
dados["Data"] = pd.to_datetime(dados["Data"])

vendas_por_data = dados.groupby("Data")["Faturamento"].sum()

#Gria gráfico de linhas 'kind="line'/Coloca pontos nas vendas 'market="o"
vendas_por_data.plot(kind="line", marker="o")

plt.title("Evolução do Faturamento")
plt.xlabel("Data")
plt.ylabel("Faturamento (R$)")

plt.grid()

plt.show()