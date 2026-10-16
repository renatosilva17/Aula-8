import json

def carregar_produtos():
    arquivo = open("produtos.json", "r", encoding="utf-8")
    produtos = json.load(arquivo)
    arquivo.close()
    return produtos

def salvar_produtos(produtos):
    arquivo = open("produtos.json", "w", encoding="utf-8")
    json.dump(produtos, arquivo, indent=4, ensure_ascii=False)
    arquivo.close()


produtos = carregar_produtos()

while True:
    print("--->Central do Estoque<---")
    print("1 - Ver Todos os produtos")
    print("2 - Pesquisar produto")
    print("3 - pesquisar ID ")
    print("4 - cadastrar produto")
    print("5 - excluir produto")
    print("6 - modificar produto")
    print("0 - Sair do Sistema")

    opcao = input("digite um numero: ")
    
    if opcao == "1":
        print("--->Ver todos os produtos<---")
        print(produtos)


    if opcao =="2":
        print("--->Pesquisa por item<---")
        chamar_produto = input("Qual produto quer ver? ")
        for produto in produtos:
            if produto ["nome"] == chamar_produto:
                print(produto)

    if opcao == "3":
        print("--->Pesquisa por ID<---")
        chamar_ID = int(input("Qual ID? "))
        for produto in produtos:
            if produto ["id"] == chamar_ID:
                print(produto)

    if opcao == "4":
        print("--->Cadastrar Produto<---") 
        id = input("Qual o id? ")
        nome = input ("qual o nome do produto? ")
        categoria = input ("Qual a categoria do produto? ")
        preco = input("qual o preco do produto? ")
        estoque = input("quantos tem no estoque? ")

        novo_produto = {
            "id": id,
            "nome": nome,
            "categoria": categoria,
            "preco": preco,
            "estoque": estoque,
        }
        produtos.append(novo_produto)
        
        salvar_produtos(produtos)

        print(f"Produto '{nome}' foi cadastrado e salvo com sucesso!")

    if opcao == "5":
        print("--->Excluir Produto<---")
        excluir_produto = input("Qual produto (ID) quer excluir? ")
        for produto in produtos:
            if produto ["id"] == excluir_produto:
                produtos.remove(produto)
                
                salvar_produtos(produtos)
                print(f"Produto Excluido com sucesso!")
                produto_encontrado = True
                break
            if not produto_encontrado:
                print("Produto com este ID nao foi encontrado!")