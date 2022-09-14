import os
produtos = []

def menu_cadastro(produtos):
    os.system('cls')
    menu_cadastro = input('''
    --------------------------------------------
            Voce entrou no menu de cadastro:
    --------------------------------------------
    
    [1] -Cadastramento de produtos
    [2] -Listar produtos cadastrados
    [3] -Deleção de produtos
    [0] -Sair para o menu principal

    Escolha uma das opções:  ''')

    if menu_cadastro == '1' :
        os.system('cls')
        print('Voce entrou na aba de cadastramento de produtos:')
        #produto_cadastro ={}
        produto = {}
        produto_cadastro = input("Digite o nome do produto: ")
        while produto_cadastro.isalpha() == False:
            produto_cadastro = input("Nome invalido digite o nome novamente: ")
        os.system('cls')
        preco = input(f"Digite o preço de {produto_cadastro}: ")     
        while preco.replace('.','',1).isdigit() == False:                
            preco = input(f"Preço invalido digite novamente um preço para {produto_cadastro}: ")

        preco = float(preco)
        produto['nome'] = produto_cadastro
        produto['preco'] = preco
        produtos.append(produto)
        print(f'\nProduto {produto_cadastro}, com valor de R${preco:.2f}, cadastrado com sucesso!!')
        input('\nPressione Enter para voltar ao menu ')
        

    elif menu_cadastro == '2':
        os.system('cls')
        print('Voce entrou na aba de Listagem de produtos')
        print('Seu estoque atual é \n')
        contador=1
        for item in range(len(produtos)):
            print(f"produto {contador}: {produtos[item]['nome']} R$ {produtos[item]['preco']:.2f}")
            contador+=1

        input('\nDigite qualquer coisa para voltar ao menu ')

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