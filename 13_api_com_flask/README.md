# Projeto 12 - API Web com Flask

## Sobre o projeto

Este projeto teve como objetivo aprender os fundamentos do desenvolvimento de APIs REST utilizando Flask.

Foi construída uma API capaz de realizar operações de cadastro, consulta, atualização e exclusão de produtos, simulando o funcionamento de um pequeno sistema de gerenciamento.

Todos os testes da API foram realizados utilizando o Postman.

---

## Tecnologias utilizadas

- Python
- Flask
- Postman

---

## Funcionalidades

- Listar todos os produtos
- Buscar um produto pelo ID
- Cadastrar novos produtos
- Atualizar produtos existentes
- Excluir produtos
- Retornar respostas em formato JSON
- Utilizar códigos HTTP para tratamento de erros

---

## Rotas disponíveis

| Método | Rota | Função |
|---------|------|--------|
| GET | / | Página inicial |
| GET | /produtos | Lista todos os produtos |
| GET | /produtos/<id> | Busca um produto |
| POST | /produtos | Cadastra um novo produto |
| PUT | /produtos/<id> | Atualiza um produto |
| DELETE | /produtos/<id> | Exclui um produto |

---

## Conceitos praticados

- Desenvolvimento de APIs REST
- Rotas no Flask
- Métodos HTTP
- Manipulação de JSON
- Parâmetros de rota
- CRUD
- request.json
- Listas e dicionários
- Testes de API com Postman
- Tratamento de respostas HTTP

---

## Aprendizados

Durante este projeto foi possível compreender como aplicações se comunicam através de APIs, utilizando requisições HTTP para enviar e receber informações em formato JSON.

Também foi desenvolvido um CRUD completo, base para praticamente qualquer sistema backend moderno.

---

## Próximos passos

No próximo projeto, a lista de produtos será substituída por um banco de dados SQLite, tornando os dados persistentes e aproximando a aplicação de um sistema real.
