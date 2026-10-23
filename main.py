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
    
    if opcao == "0":
     print("Saindo do sistema... :p Flwww")
     break

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
        id = int(input("Qual o id? "))
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
        produto_encontrado = False

        for produto in produtos:
            # ADD str() TO BOTH SIDES TO FIX THE TYPE CONFLICT
            if str(produto["id"]) == str(excluir_produto):
                produtos.remove(produto)
                salvar_produtos(produtos)
                print(f"Produto Excluido com sucesso!")
                produto_encontrado = True
                break

        if not produto_encontrado:
            print("Produto com este ID nao foi encontrado!")

    if opcao == "6":
        print("--->Modificar Produto<---")
        id_modificar = input("Qual o ID do produto que deseja modificar? ")
        produto_encontrado = False

        for produto in produtos:    #str para mesmo se o numero for int na comparação vira texto :p#
            if str(produto["id"]) == str(id_modificar):
                print(f"Produto encontrado: {produto['nome']}")
                
                novo_nome = input(f"Novo nome ({produto['nome']}): ") or produto['nome']
                nova_cat = input(f"Nova categoria ({produto['categoria']}): ") or produto['categoria']
                novo_preco = input(f"Novo preço ({produto['preco']}): ") or produto['preco']
                novo_est = input(f"Novo estoque ({produto['estoque']}): ") or produto['estoque']
                
                produto['nome'] = novo_nome
                produto['categoria'] = nova_cat
                produto['preco'] = novo_preco
                produto['estoque'] = novo_est
                
                salvar_produtos(produtos)
                print("Produto modificado e salvo com sucesso!")
                produto_encontrado = True
                break

        if not produto_encontrado:
            print("Produto com este ID nao foi encontrado!")