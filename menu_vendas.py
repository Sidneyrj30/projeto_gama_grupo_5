import os

produtos = [["arroz", 15.00], ["feijao",20.00], ["carne", 30.00], ["pao", 15.20]]
carrinho = []

def menu_vendas():
    print("="* 20)
    print("Menu Vendas")
    print("="* 20)


    print('''   
    1- Adição de produtos ao carrinho
    2- Remoção de produtos do carrinho
    3- Finalização da venda do carrinho
    0- Para sair
    ''')

menu_vendas()

opcao = input("Escolha uma das opçôes: ")

while opcao != "0":

    if opcao == "1":
        #Variavel em que o usuario vai digitar se quer continuar ou não no programa
        terminar_continuar = "1"

        while terminar_continuar != "0":
            print("")
            for item in range(len(produtos)):
                print(f"{item + 1}-{produtos[item][0]}: R$ {produtos[item][1]:.2f}")

            produto = int(input("\nEscolha o produto que deseja adicionar no carrinho: "))
            if (produto - 1) in range(len(produtos)):
                carrinho.append(produtos[produto - 1])
                del produtos[produto - 1]

                print(f"\nSua lista do carrinho é:")
                for item in range(len(carrinho)):
                    print(f"{carrinho[item][0]}")

            else:
                print("Você digitou um produto inexistente")
            
            print(" ")

            terminar_continuar = input(f"Clique enter para continuar ou 0 para sair: ")

    elif opcao == "2":
        terminar_continuar = "1"
        
        while terminar_continuar != "0":
            print("")
            for item in range(len(carrinho)):
                print(f"{item + 1}-{carrinho[item][0]}: R${carrinho[item][1]:.2f}")

            produto_carrinho = int(input("\nEscolha o produto que deseja exluir no carrinho: "))
            if (produto_carrinho - 1) in range(len(carrinho)):
                produtos.append(carrinho[produto_carrinho - 1])
                del carrinho[produto_carrinho - 1]

                print(f"\nSua lista do carrinho é:")
                for item in range(len(carrinho)):
                    print(f"{carrinho[item][0]}")
            else:
                print("Você digitou um produto inexistente")
            
            print(" ")

            terminar_continuar = input(f"Clique enter para continuar ou 0 para sair: ")


    elif opcao == "3":
        preco = 0
        for item in range(len(carrinho)):
            preco = preco + carrinho[item][1]

        print("="*15)
        print("Produtos vendidos")
        print("="*15)

        for item in range(len(carrinho)):
            print(f"Produto: {carrinho[item][0]}, preço: R${carrinho[item][1]:.2f}")
        print(f"Total de {len(carrinho)} produtos por R${preco:.2f}")

        input("Aperte enter para finalizar a venda")
        #Break é para caso o usuário escolher a opção 3 de finalizar, o loop será encerrado 
        break  

    os.system('cls')    

    menu_vendas()

    opcao = input("Escolha uma das opçôes: ")
    
