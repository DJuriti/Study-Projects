# Projeto 04 - Catálogo de Filmes

Aplicação desenvolvida em Python que consulta informações de filmes utilizando a OMDb API.

## Funcionalidades

- Pesquisa de filmes pelo título
- Exibição do título
- Ano de lançamento
- Diretor
- Gênero
- Duração
- País de origem
- Idioma
- Avaliação IMDb
- Classificação indicativa
- Data de lançamento
- Sinopse
- Atores principais

## Tecnologias Utilizadas

- Python
- Requests
- Python-dotenv
- OMDb API

## Como executar

1. Clone o repositório.

2. Instale as dependências:

```bash
pip install requests python-dotenv
```

3. Crie um arquivo `.env` na pasta do projeto:

```env
API_KEY=SUA_API_KEY
```

4. Execute o programa:

```bash
python catalogo_filmes.py
```

## Exemplo de saída

```
===================================
        CATÁLOGO DE FILMES
===================================

Digite o nome do filme: Interestelar

===================================
Interestelar
===================================

Ano..............2014
Diretor.........Christopher Nolan
Gênero..........Adventure, Drama, Sci-Fi
Duração.........169 min
País............USA
Idioma..........English
Avaliação.......8.7/10
Classificação...PG-13
Lançamento......07 Nov 2014

Sinopse

A team of explorers travel through a wormhole in space...

Atores Principais

Matthew McConaughey, Anne Hathaway,
Jessica Chastain
```

## Aprendizados

Neste projeto foram praticados:

- Consumo de APIs REST
- Leitura e interpretação de JSON
- Utilização de API Key
- Variáveis de ambiente com `.env`
- Tratamento de erros
- Organização e formatação da saída no terminal
