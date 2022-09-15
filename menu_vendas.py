import os

produtos = []
carrinho = []
relatorio = []

def menu_vendas(produtos, carrinho, relatorio):
    opcao = 0

    while opcao != "0":
        os.system('cls')

        opcao = input('''
        ---------------------------------------------
                Você entrou no menu de vendas
        ---------------------------------------------
        
        [1] - Adição de produtos ao carrinho
        [2] - Remoção de produtos do carrinho
        [3] - Finalização da venda do carrinho
        [0] - Sair para o menu principal

        Escolha uma das opçôes: ''')   

        if opcao == "1":
            os.system('cls') 

            print('''
            --------------------------------
                    Adicionar produtos        
            -------------------------------- 
            ''')
            print("")
            for item in range(len(produtos)):
                print(f"[{item + 1}] - {produtos[item]['nome']}: R$ {produtos[item]['preco']:.2f}")

            valor_valido = False
            while valor_valido == False:
                produto = input("\nEscolha o produto que deseja adicionar no carrinho: ")
                valor_valido = produto.isnumeric()
                if valor_valido == True:
                    produto_num = int(produto)
                    if (produto_num - 1) in range(len(produtos)):
                        carrinho.append(produtos[produto_num - 1])
                        del produtos[produto_num - 1]

                        print(f"\nSua lista do carrinho é:")
                        for item in range(len(carrinho)):
                            print(f"{carrinho[item]['nome']}")
                    elif len(produtos) == 0:
                        print("Não tem mais produtos")
                        valor_valido = True
                    else:
                        print("Você digitou um produto inexistente")
                        valor_valido = False
                else:
                    print("Você digitou um produto inexistente")
            
            input("\nAperte enter para continuar... ")

        elif opcao == "2":
            os.system('cls')

            print('''
            ------------------------------------------
                    Remover produtos do carrinho       
            ------------------------------------------ 
            ''')
            
            print("")
            for item in range(len(carrinho)):
                print(f"{item + 1}-{carrinho[item]['nome']}: R${carrinho[item]['preco']:.2f}")

            valor_valido = False
            while valor_valido == False:
                produto = input("\nEscolha o produto que deseja remover no carrinho: ")
                valor_valido = produto.isnumeric()
                if valor_valido == True:
                    produto_num = int(produto)
                    if (produto_num - 1) in range(len(carrinho)):
                        produtos.append(carrinho[produto_num - 1])
                        del carrinho[produto_num - 1]

                        print(f"\nSua lista do carrinho é:")
                        for item in range(len(carrinho)):
                            print(f"{carrinho[item]['nome']}")
                    elif len(carrinho) == 0:
                        print("Não tem produtos no carrinho")
                        valor_valido = True
                    else:
                        print("Você digitou um produto inexistente")
                        valor_valido = False
                else:
                    print("Você digitou um produto inexistente")
                       
            input("\nAperte enter para continuar... ")

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
            
            print(f"Total de produtos: {len(carrinho)}  por R${preco:.2f}")           

            input("Aperte [enter] para finalizar a venda... ")
            relatorio.extend(carrinho)
            carrinho.clear()
            break  

       
