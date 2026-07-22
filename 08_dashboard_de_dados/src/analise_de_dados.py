from carregar_dados import carregar_vendas


dados = carregar_vendas()


print(dados)

print('\nPrimeiras linhas:')
print(dados.head())

print('\nInformações dos dados:')
dados.info()

print('\nEstatísticas:')
print(dados.describe())

print('\nTamanho da tabela:')
print(dados.shape)


print('='*35)

faturamento_total = dados['Faturamento'].sum()
print(f'Faturamento total: R$ {faturamento_total}')

quantidade_total = dados['Quantidade'].sum()
print(f'Quantidade vendida: {quantidade_total} unidades')

ticket_medio = dados['Faturamento'].mean()
print(f'Ticket médio: R$ {ticket_medio}')


print('='*35)

print('\nFaturamento por produto:')
faturamento_produto = dados.groupby('Produto')['Faturamento'].sum()
print(faturamento_produto)


print('='*35)

print('\nFaturamento por categoria:')
faturamento_categoria = dados.groupby('Categoria')['Faturamento'].sum()
print(faturamento_categoria)

print('='*35)