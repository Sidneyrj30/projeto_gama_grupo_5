

import os
produtos = [{'nome':"arroz", 'preco': 15.00}, {'nome':"feijao",'preco': 20.00}, {'nome':"carne", 'preco': 30.00},
{'nome':'cebola', 'preco': 5.56}]
opcao = '0'
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
        menu_cadastro=input('''
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
            produto={}
            produto_cadastro = input("Digite o nome do produto: ")
            while produto_cadastro.isalpha() == False:
                produto_cadastro = input("Nome invalido digite o nome novamente: ")
            os.system('cls')
            preco = input(f"Digite o preço de {produto_cadastro}: ")         #replace(",", ".")
            while preco.replace('.','',1).isdigit()==False:                  #preco.isdecimal() == False: #rever logo pela manha
                preco = input(f"Preço invalido digite novamente um preço para {produto_cadastro}: ")
                                                                             #while preco.isdecimal() == False: #rever logo pela manha
                                                                             #    preco = input(f"Preço invalido digite novamente um preço para {produto_cadastro}: ")
            produto['nome']=produto_cadastro
            produto['preco']=float(preco)
            produtos.append(produto)
            #print(produtos)
            print(f'\nProduto {produto_cadastro}, com valor de {preco}, cadastrado com sucesso!!')
            input('\nPressione Enter para voltar ao menu ')
            opcao == '1'

       
            


        elif menu_cadastro == '2':
            os.system('cls')
            print('Voce entrou na aba de Listagem de produtos')
            print('Seu estoque atual é \n')
            contador=1
            for item in range(len(produtos)):
                print(f"produto {contador}: {produtos[item]['nome']} R$ {produtos[item]['preco']}")
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