import os

produtos = [{'nome':"arroz", 'preco': 15.00}, {'nome':"feijao",'preco': 20.00}, {'nome':"carne", 'preco': 30.00},
{'nome':'cebola', 'preco': 5.56}]
carrinho = []
opcao = 0

while opcao != "0":
    os.system('cls') 

    opcao = input('''
    -------------------------------------------
            Você entrou no menu vendas
    -------------------------------------------
    [1] - Adição de produtos ao carrinho
    [2] - Remoção de produtos do carrinho
    [3] - Finalização da venda do carrinho
    [0] - Para sair
    Escolha uma das opçôes: ''')   

    if opcao == "1":
        os.system('cls') 
        terminar_continuar = "1"

        print('''
        --------------------------------
                Adicionar produtos        
        -------------------------------- 
        ''')

        while terminar_continuar != "0":
            print("")
            for item in range(len(produtos)):
                print(f"{item + 1}-{produtos[item]['nome']}: R$ {produtos[item]['preco']:.2f}")

            produto = int(input("\nEscolha o produto que deseja adicionar no carrinho: "))
            if (produto - 1) in range(len(produtos)):
                carrinho.append(produtos[produto - 1])
                del produtos[produto - 1]

                print(f"\nSua lista do carrinho é:")
                for item in range(len(carrinho)):
                    print(f"{carrinho[item]['nome']}")

            else:
                print("Você digitou um produto inexistente")
            
            print(" ")
            terminar_continuar = input(f"Digite 0 para sair ou apenas aperte enter para continuar [0/Enter]: ")

    elif opcao == "2":
        os.system('cls') 
        terminar_continuar = "1"

        print('''
        --------------------------------
                Remover produtos        
        -------------------------------- 
        ''')
        
        while terminar_continuar != "0":
            print("")
            for item in range(len(carrinho)):
                print(f"{item + 1}-{carrinho[item]['nome']}: R${carrinho[item]['preco']:.2f}")

            produto_carrinho = int(input("\nEscolha o produto que deseja exluir no carrinho: "))
            if (produto_carrinho - 1) in range(len(carrinho)):
                produtos.append(carrinho[produto_carrinho - 1])
                del carrinho[produto_carrinho - 1]

                print(f"\nSua lista do carrinho é:")
                for item in range(len(carrinho)):
                    print(f"{carrinho[item]['nome']}")
            else:
                print("Você digitou um produto inexistente")
            
            print(" ")
            terminar_continuar = input(f"Digite 0 para sair ou apenas aperte enter para continuar [0/Enter]: ")

    elif opcao == "3":
        os.system('cls') 
        preco = 0
        for item in range(len(carrinho)):
            preco = preco + carrinho[item]['preco']

        print('''
        --------------------------------
                Finalizar vendas        
        -------------------------------- 
        ''')

        print(f"Total de {len(carrinho)} produtos por R${preco:.2f}")

        input("Aperte [enter] para finalizar a venda... ")
        break  

       
