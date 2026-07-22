import pandas as pd

dados = {
    'Data': [
        '01/01/2026',
        '02/01/2026',
        '02/01/2026'
    ],
    'Produto': [
        'Notebook',
        'Mouse',
        'Teclado'
    ],
    'Categoria': [
        'Eletrônico',
        'Acessório',
        'Acessório'
    ],
    'Quantidade': [
        2,
        5,
        3
    ],
    'Preço':[
        2500,
        100,
        200
    ],
    'Cliente': [
        'João',
        'Maria',
        'Pedro'
    ]
}

#Transforma os dados em uma estrutura chamada "DataFrame"
df = pd.DataFrame(dados)

#Escreve a tabela em um arquivo Excel
df.to_excel('../dados/vendas.xlsx', index=False)

print ('Arquivo criado com sucesso!')