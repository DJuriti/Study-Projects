from dotenv import load_dotenv
import os
import requests
from requests import status_codes

load_dotenv()

print ('='*35)
print ('        CATÁLOGO DE FILMES')
print ('='*35)
filme = str(input('Digite o nome do filme: ')).strip

key = os.getenv('API_KEY')
url =  f'http://www.omdbapi.com/?apikey={key}&t={filme}'

resposta = requests.get(url)
dados = resposta.json()

if dados['Response'] == 'True':
    print('='*35)
    print(f'{dados['Title']}')
    print('='*35)

    print (f'Ano............{dados["Year"]}')
    print (f'Diretor........{dados["Director"]}')
    print (f'Gênero.........{dados["Genre"]}')
    print (f'Duração........{dados["Runtime"]}')
    print (f'País...........{dados["Country"]}')
    print (f'Idioma.........{dados["Language"]}')
    print (f'Avaliação......{dados["imdbRating"]}/10')
    print (f'Classificação..{dados['Rated']}')
    print (f'Lançamento.....{dados["Released"]}')
    print('')
    print (f'Sinopse')
    print (f'{dados["Plot"]}')
    print('')
    print (f'Atores Principais:')
    print (f'{dados["Actors"]}')
else:
    print('Filme não encontrado!')