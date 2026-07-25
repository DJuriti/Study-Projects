from flask import Flask, request

app = Flask(__name__)

produtos = [
    {"id": 1, "nome": "Arroz", "preco": 25.90},
    {"id": 2, "nome": "Feijao", "preco": 8.50},
    {"id": 3, "nome": "Macarrao", "preco": 6.80},
]

@app.route('/')
def inicio():
    return "Olá, mundo!"

@app.route('/produtos')
def listar_produtos():
    return produtos

@app.route("/produtos/<int:id>")
def buscar_produto(id):

    for produto in produtos:

        if produto["id"] == id:
            return produto

    return {"erro": "Produto não encontrado"}, 404

@app.route("/produtos", methods=["POST"])
def adicionar_produto():
    novo_produto = request.json
    produtos.append(novo_produto)
    return novo_produto

@app.route("/produtos/<int:id>", methods=["DELETE"])
def excluir_produto(id):

    for produto in produtos:

        if produto["id"] == id:

            produtos.remove(produto)

            return {"mensagem": "Produto removido com sucesso!"}

    return ({"erro": "Produto não encontrado."}, 404)

@app.route("/produtos/<int:id>", methods=["PUT"])
def atualizar_produto(id):

    dados = request.json

    for produto in produtos:

        if produto["id"] == id:

            produto["nome"] = dados["nome"]
            produto["preco"] = dados["preco"]

            return produto

    return {"erro": "Produto não encontrado"}, 404

if __name__ == '__main__':
    app.run(debug=True)