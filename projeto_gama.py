import os
from menu_cadastro import menu_cadastro
from menu_vendas import menu_vendas
from menu_relatorio import menu_relatorio

produtos = [{'nome':"arroz", 'preco': 15.00}, {'nome':"feijao",'preco': 20.00}, {'nome':"carne", 'preco': 30.00},
{'nome':'cebola', 'preco': 5.56}]
carrinho = []
relatorio = []

os.system('cls')

print('''
=------------------------------------------=
|        Seja bem-vindo ao Orgânicos        |
=------------------------------------------=
''')

input("Aperte enter para continuar... ")

opcao = 1
while opcao != "0":
    os.system('cls')

    opcao = input('''
    --------------------------------------------
                Menu de navegação
    --------------------------------------------
    
    [1] - Cadastro
    [2] - Vendas
    [3] - Relatório
    [0] - Sair 

    Escolha uma das opções:  ''')

    if opcao == "1":
        menu_cadastro(produtos)

    elif opcao == "2":
        menu_vendas(produtos, carrinho, relatorio)

    elif opcao == "3":
        menu_relatorio(relatorio)

    elif opcao == "0":
        print('Você está saindo')

