import os
produtos = []

def menu_cadastro(produtos):

    def isfloat(num):
        try:
            float(num)
            return True
        except ValueError:
            return False

    opcao = 0
    while opcao != '0':
        os.system('cls')
        opcao = input('''
        --------------------------------------------
                Voce entrou no menu de cadastro
        --------------------------------------------
        
        [1] -Cadastramento de produtos
        [2] -Listar produtos cadastrados
        [3] -Deleção de produtos
        [0] -Sair para o menu principal

        Escolha uma das opções:  ''')

        if opcao == '1':
            os.system('cls')
            print('Voce entrou na aba de cadastramento de produtos:')
            produto = {}
            produto_cadastro = input("Digite o nome do produto: ")
            while produto_cadastro.isalpha() == False:
                produto_cadastro = input("Nome invalido digite o nome novamente: ")
            os.system('cls')
            preco = input(f"Digite o preço de {produto_cadastro}: ")
            preco = preco.replace(",", ".")
            while isfloat(preco) == False:
                preco = input(f"Preço invalido digite novamente um preço para {produto_cadastro}: ")
                preco = preco.replace(",", ".")
            #Código anterior
            # while preco.replace('.','',1).isdigit() == False:                
            #     preco = input(f"Preço invalido digite novamente um preço para {produto_cadastro}: ")

            preco = float(preco)
            produto['nome'] = produto_cadastro
            produto['preco'] = preco
            produtos.append(produto)
            print(f'\nProduto {produto_cadastro}, com valor de R${preco:.2f}, cadastrado com sucesso!!')
            input('\nPressione Enter para voltar ao menu ')
            

        elif opcao == '2':
            os.system('cls')
            if len(produtos) == 0:
                input('Lista vazia de Enter para voltar ao menu')
            else:
                print('Voce entrou na aba de Listagem de produtos')
                print('Seu estoque atual é \n')
                contador=1
                for item in range(len(produtos)):
                    print(f"produto {contador}: {produtos[item]['nome']} R$ {produtos[item]['preco']:.2f}")
                    contador+=1

                input('\nDigite qualquer coisa para voltar ao menu ')
 
        elif opcao == '3':
            os.system('cls')
            if len(produtos) == 0:
                input('Lista vazia de Enter para voltar ao menu')
            else:
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