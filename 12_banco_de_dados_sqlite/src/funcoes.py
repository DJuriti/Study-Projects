def cadastrar_produto(conexao):

    cursor = conexao.cursor()

    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade: "))

    cursor.execute("""
    INSERT INTO produtos (nome, preco, quantidade)
    VALUES (?, ?, ?)
    """, (nome, preco, quantidade))

    conexao.commit()

    print("Produto cadastrado com sucesso!")


def listar_produtos(conexao):

    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM produtos")

    produtos = cursor.fetchall()

    for produto in produtos:
        print(
            f"ID: {produto[0]} | "
            f"Nome: {produto[1]} | "
            f"Preço: R${produto[2]} | "
            f"Quantidade: {produto[3]}"
        )

def atualizar_produto(conexao):
    cursor = conexao.cursor()
    id_produto = int(input("ID do produto: "))

    print("\nO que deseja atualizar?")
    print("1 - Nome")
    print("2 - Preço")
    print("3 - Quantidade")
    print("4 - Todos os dados")

    opcao = input("Escolha: ")

    if opcao == "1":

        novo_nome = input("Novo nome: ")

        cursor.execute("""
        UPDATE produtos
        SET nome = ?
        WHERE id = ?
        """, (novo_nome, id_produto))


    elif opcao == "2":

        novo_preco = float(input("Novo preço: "))

        cursor.execute("""
        UPDATE produtos
        SET preco = ?
        WHERE id = ?
        """, (novo_preco, id_produto))


    elif opcao == "3":

        nova_quantidade = int(input("Nova quantidade: "))

        cursor.execute("""
        UPDATE produtos
        SET quantidade = ?
        WHERE id = ?
        """, (nova_quantidade, id_produto))


    elif opcao == "4":

        novo_nome = input("Novo nome: ")
        novo_preco = float(input("Novo preço: "))
        nova_quantidade = int(input("Nova quantidade: "))

        cursor.execute("""
        UPDATE produtos
        SET nome = ?, preco = ?, quantidade = ?
        WHERE id = ?
        """, (novo_nome, novo_preco, nova_quantidade, id_produto))

    else:
        print("Opção inválida!")
        return


    conexao.commit()

    print("Produto atualizado com sucesso!")

def excluir_produto(conexao):

    cursor = conexao.cursor()

    id_produto = int(input("ID do produto que deseja excluir: "))

    cursor.execute("""
    DELETE FROM produtos
    WHERE id = ?
    """, (id_produto,))

    conexao.commit()

    print("Produto excluido com sucesso!")