

import os

produtos = [{'nome':"arroz", 'preco': 15.00}, {'nome':"feijao",'preco': 20.00}, {'nome':"carne", 'preco': 30.00},
{'nome':'cebola', 'preco': 5.56}]

carrinho = []
opcao = '0'
relatorio = []
while opcao != '4':
    os.system('cls')
    print('''
    --------------------------------------------
                   Menu Navegação:
    --------------------------------------------
   
        [1]  -   Cadastro
        [2]  -   Vendas
        [3]  -   Relatório
        [0]  -   Sair 
    ''')

    opcao = (input('     Digite onde deseja ir: '))


    while opcao == '1':
        os.system('cls')
        menu_cadastro = input('''
        --------------------------------------------
                Voce entrou no menu de cadastro:
        --------------------------------------------
        
        [1] -Cadastramento de produtos
        [2] -Listar produtos cadastrados
        [3] -Deleção de produtos
        [0] -Sair para o menu principal


        Entre com o numero da solicitação:  ''')

        if menu_cadastro == '1' :
            os.system('cls')
            print('Voce entrou na aba de cadastramento de produtos:')
            #produto_cadastro ={}
            produto = {}
            produto_cadastro = input("Digite o nome do produto: ")
            while produto_cadastro.isalpha() == False:
                produto_cadastro = input("Nome invalido digite o nome novamente: ")
            os.system('cls')
            preco = input(f"Digite o preço de {produto_cadastro}: ")         #replace(",", ".")
            while preco.replace('.','',1).isdigit() == False:                  #preco.isdecimal() == False: #rever logo pela manha
                preco = input(f"Preço invalido digite novamente um preço para {produto_cadastro}: ")
                                                                             #while preco.isdecimal() == False: #rever logo pela manha
                                                                             #    preco = input(f"Preço invalido digite novamente um preço para {produto_cadastro}: ")
            preco = float(preco)
            produto['nome'] = produto_cadastro
            produto['preco'] = preco
            produtos.append(produto)
            #print(produtos)
            print(f'\nProduto {produto_cadastro}, com valor de R${preco:.2f}, cadastrado com sucesso!!')
            input('\nPressione Enter para voltar ao menu ')
            opcao == '1'

       
            


        elif menu_cadastro == '2':
            os.system('cls')
            print('Voce entrou na aba de Listagem de produtos')
            print('Seu estoque atual é \n')
            contador=1
            for item in range(len(produtos)):
                print(f"produto {contador}: {produtos[item]['nome']} R$ {produtos[item]['preco']:.2f}")
                contador+=1

            input('\nDigite qualquer coisa para voltar ao menu ')
            opcao == '1'

        elif menu_cadastro == '3':
            os.system('cls')
            print('Voce entrou na aba de Deleção')
            contador=1
            for item in range(len(produtos)):
                print(f"produto {contador}: {produtos[item]['nome']}")
                contador+=1
                
                
            print('qual produto deseja remover digite o numero correspondente:\n')
            numero = int(input("Digite o numero do produto da lista "))
            numero = numero-1
            produtos.pop(numero)
            print('Seu estoque atual é \n')
            contador = 1
            for item in range(len(produtos)):
                print(f"produto {contador}: {produtos[item]['nome']}")
                contador +=1
            input('\nDigite qualquer coisa para voltar ao menu ')
            opcao == '1'

        else:
            os.system('cls')
            opcao='0'
        
    while opcao == "2":
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
            relatorio.append(carrinho)
            print(f"Total de {len(carrinho)} produtos por R${preco:.2f}")

            input("Aperte [enter] para finalizar a venda... ")
            #relatorio.append(carrinho)
            carrinho = []
            opcao = "0"

            #break  

    while opcao == "3":
        #os.system('cls') 
        #print(relatorio)
        #input('Enter para finalizar')

            #relatorio = [{'nome':"arroz", 'preco': 15.00}, {'nome':"feijao",'preco': 20.00}, {'nome':"carne", 'preco': 30.00},{'nome':'cebola', 'preco': 5.56}]
            preco = 0

            for item in range(len(relatorio)):
                preco = preco + relatorio[item][item-1]['preco']

            print('''
                --------------------------------
                        #Relatório de Vendas        
                -------------------------------- 
            ''')

            for item in range(len(relatorio)):
                print(f"Produto: {relatorio[item][item-1]['nome']} preço: R$ {relatorio[item][item-1]['preco']}")

            print(f"Total de Produtos: {len(relatorio)} unidades \nValor Total: R${preco}" ) 
            
            input("Aperte enter para continuar: ")

            break