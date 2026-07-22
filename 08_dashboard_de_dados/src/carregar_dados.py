import pandas as pd


def carregar_vendas():

    dados = pd.read_excel('dados/vendas.xlsx')

    dados['Faturamento'] = dados['Quantidade'] * dados['Preço']

    return dados