import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

print ('Fantasia: fantasy_19')
categoria = str(input("Categoria:"))
url = f"https://books.toscrape.com/catalogue/category/books/{categoria}/index.html"
resposta = requests.get(url)

soup = BeautifulSoup(resposta.text, "html.parser")

#Procura todos os livros dentro de uma tag <article> e queremos apenas os class dentro da "class_='product_pod'
livros = soup.find_all('article', class_='product_pod')

dados = []

for livro in livros:
    #Nessa linha ele procura a tag <h3> e dentro dela encontra a tag <a> na classe [title].
    titulo = livro.find('h3').find('a')['title']
    preco = livro.find('p', class_='price_color').text.strip()
    preco = float(re.sub(r'[^0-9.]', '', preco)) #Substitui tudo que não for  número ou . por espaços vazios.
    cotacao_libra = 7.20
    preco_real = preco * cotacao_libra
    avaliacao = livro.find('p')['class'][1]
    if avaliacao == 'One':
        avaliacao = 1
    elif avaliacao == 'Two':
        avaliacao = 2
    elif avaliacao == 'Three':
        avaliacao = 3
    elif avaliacao == 'Four':
        avaliacao = 4
    elif avaliacao == 'Five':
        avaliacao = 5
    disponibilidade = livro.find(
        'p',
        class_='instock availability'
    ).text.strip()

    dados.append({
        'Título': titulo,
        'Preço Libra': preco,
        'Preço Reais': preco_real,
        'Avaliação': avaliacao,
        "Disponibilidade": disponibilidade


    })
df = pd.DataFrame(data=dados)
print(df)
df.to_excel('livros.xlsx', index=False)

