import os
produtos = []
opcao = '0'
while opcao == '0' or opcao != '1234':
    os.system('cls')
    opcao=input('''
    --------------------------------------------
        Voce entrou no menu principal:
    --------------------------------------------
    1 -Cadastro
    2 -Vendas
    3 -Relatório
    4- Sair
    entre com o numero da solicitação ''')


    while opcao == '1' or opcao != '1234':
        os.system('cls')
        menu_cadastro=input('''
        --------------------------------------------
                Voce entrou no menu de cadastro:
        --------------------------------------------
        1 -Cadastramento de produtos
        2 -Listar produtos cadastrados
        3 -Deleção de produtos
        4 -Sair para o menu principal
        entre com o numero da solicitação ''')

        if menu_cadastro == '1' :
            os.system('cls')
            print('Voce entrou na aba de cadastramento de produtos:')
            print(produtos)
            produto_cadastro = input("Digite o nome do produto: ")
            while produto_cadastro.isalpha() == False:
                produto_cadastro = input("Nome invalido digite o nome novamente: ")
            os.system('cls')
            preco = input(f"Digite o preço de {produto_cadastro}: ")       #replace(",", ".")
            while type(preco) % 0:#preco.isdecimal() == False: #rever logo pela manha
                preco = input(f"Preço invalido digite novamente um preço para {produto_cadastro}: ")
            produto=[]
            produto.append(produto_cadastro)
            produto.append(preco)
            produtos.append(produto)
            print(f'\nProduto {produto_cadastro}, com valor de {preco}, cadastrado com sucesso!!')
            input('\nPressione Enter para voltar ao menu ')
            opcao == '1'
       
            


        elif menu_cadastro == '2':
            print('Voce entrou na aba de Listagem de produtos')
            print('Seu estoque atual é \n',list(produtos))

            input('\nDigite qualquer coisa para voltar ao menu ')
            opcao == '1'

        elif menu_cadastro == '3':
            os.system('cls')
            print('Voce entrou na aba de Deleção')
            contador=0
            for produto in produtos:
                print(f'produto {contador}: ', produto)
                contador+=1
                
                
            print('qual produto deseja remover digite o numero correspondente:\n')
            numero = int(input("Digite o numero do produto da lista "))
            produtos.pop(numero)
            print('Seu estoque atual é \n',produtos)
            input('\nDigite qualquer coisa para voltar ao menu ')
            opcao == '1'

        else:
            os.system('cls')
            opcao='0'