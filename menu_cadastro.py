import os
import time
menu=0
produtos = [['tomate',25.9] , ['banana',5.9] , ['repolho',2.9]]
produto =[]
while menu == 0 :
    os.system('cls')
    menu=int(input('''
    1 -Cadastro
    2 -Vendas
    3 -Relatório
    4- Sair
    entre com o numero da solicitação '''))
    while menu == 1:
        os.system('cls')
        menu_cadastro=int(input('''
        --------------------------------------------
                Voce entrou no menu de cadastro:
        --------------------------------------------
        1 -Cadastramento de produtos
        2 -Listar produtos cadastrados
        3 -Deleção de produtos
        4 -Sair para o menu principal
        entre com o numero da solicitação '''))

        if menu_cadastro == 1:
            os.system('cls')
            print('Voce entrou na aba de cadastramento de produtos:')
            print(produtos)
            produto_cadastro = input("Digite o produto: ")
            preco = input(f"Digite o preço de {produto_cadastro}: ")
            produto.append = [produto_cadastro , preco]

        elif menu_cadastro == 2:
            print('Voce entrou na aba de cListagem de produtos')
            print('Seu estoque atual é \n',list(produtos))
            time.sleep(20)

        elif menu_cadastro == 3:
            os.system('cls')
            print('Voce entrou na aba de Deleção')
            produto = input("Digite o produto que deseja remover: ")
            produtos.pop(produto)
            print('Seu estoque atual é \n',list(produtos))
        else:
            os.system('cls')
            menu=0