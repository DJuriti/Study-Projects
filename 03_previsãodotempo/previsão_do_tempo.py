import requests
from dotenv import load_dotenv
import os

load_dotenv()

cidade = str(input('Cidade: ')).strip().title()

key = os.getenv('API_KEY')
lang = 'pt_br'

url = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={key}&lang={lang}&units=metric'

resposta = requests.get(url)
dados = resposta.json()

if resposta.status_code == 200:
    print('='*35)
    print('        PREVISÃO DO TEMPO')
    print('='*35)
    print(f'''    Cidade..............{dados['name']}
    
    Temperatura.........{dados['main']['temp']:.2f}°C
    Temp. Máxima........{dados['main']['temp_max']:.2f}°C
    Temp. Mínima........{dados['main']['temp_min']:.2f}°C
    Sensação térmica....{dados['main']['feels_like']:.2f}°C
    Umidade.............{dados['main']['humidity']}%
    Vento...............{dados['wind']['speed'] * 3.6:.1f}km/h
    Condiçao............{dados['weather'][0]['description']}
    ''')
else:
    print('Cidade não encontrada!')


