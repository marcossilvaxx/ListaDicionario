produtos = {}

def cadastrarProduto(produto, preco):
    produtos[produto] = preco
    print("Produto cadastrado.")

    main()

def exibirProdutos():
    for produto, valor in produtos.items():
        print(produto, "-", valor)

    main()

def removerProduto(produto):
    del produtos[produto]
    print("Produto", produto, "removido.")

    main()
    
def exibirCaroProduto():
    caro = (0,0)
    for produto in list(produtos.items()):
        if produto[1] > caro[1]:
            caro = produto
    print("O produto mais caro é:", caro[0], "-", caro[1])

    main()

def exibirBaratoProduto():
    barato = (0, 100000)
    for produto in list(produtos.items()):
        if produto[1] < barato[1]:
            barato = produto
    print("O produto mais barato é:", barato[0], "-", barato[1])

    main()

def main():
    pergunta = eval(input("Digite 1 para cadastrar um produto; Digite 2 para exibir os produtos; Digite 3 para remover um produto; Digite 4 para exibir o produto mais caro; Digite 5 para exibir o produto mais barato.\n"))
    if pergunta == 1:
        produto = str(input("Informe o nome do produto:\n"))
        preco = eval(input("Informe o preço do produto:\n"))
        cadastrarProduto(produto, preco)
    elif pergunta == 2:
        exibirProdutos()
    elif pergunta == 3:
        produto = str(input("Informe o nome do produto que você quer remover:\n"))
        removerProduto(produto)
    elif pergunta == 4:
        exibirCaroProduto()
    elif pergunta == 5:
        exibirBaratoProduto()
        
if __name__ == "__main__":
    main()
