import sqlite3
from funcoes import cadastrar_produto, listar_produtos, atualizar_produto, excluir_produto


# Conexão com banco
conexao = sqlite3.connect("../dados/produtos.db")


# Criar tabela caso não exista
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    preco REAL,
    quantidade INTEGER
)
""")

conexao.commit()

def menu():

    while True:

        print("\n===== SISTEMA DE PRODUTOS =====")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Atualizar produto")
        print("4 - Excluir produto")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto(conexao)

        elif opcao == "2":
            listar_produtos(conexao)

        elif opcao == "3":
            atualizar_produto(conexao)

        elif opcao == "4":
            excluir_produto(conexao)

        elif opcao == "5":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida!")

# Executar funções
menu()