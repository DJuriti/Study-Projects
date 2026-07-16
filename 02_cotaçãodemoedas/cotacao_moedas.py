import requests
from dotenv import load_dotenv
import os

load_dotenv()

print ('''=== MOEDAS BÁSICAS ===
[ 1 ] USD - Dólar Americano
[ 2 ] EUR - Euro
[ 3 ] JPY - Iene Japonês
[ 4 ] BTC - Bitcoin
''')
code = str(input('MOEDA PARA CONVERSÃO: ')).upper().strip()

key = os.getenv("API_KEY")
url = f'https://economia.awesomeapi.com.br/json/last/{code}?key={key}'
resposta = requests.get(url)
dados = resposta.json()

if resposta.status_code == 200:
    cotacao = dados[f'{code}BRL']
    print ('='*35)
    print (f'{cotacao['name']} Comercial')
    print ('='*35)
    print (f'''    Compra........... R$ {cotacao['bid']}
    Venda............ R$ {cotacao['ask']}
    
    Máxima........... R$ {cotacao['high']}
    Mínima........... R$ {cotacao['low']}
    
    Variação......... {cotacao['pctChange']}%
    
    Atualizado ás.... {cotacao['create_date']}
    ''')
else:
    print ('Moeda inválida')

