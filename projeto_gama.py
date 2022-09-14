import os
from menu_cadastro import menu_cadastro
from menu_vendas import menu_vendas
from menu_relatorio import menu_relatorio

produtos = []
carrinho = []
relatorio = []

print('''
=------------------------------------------=
|        Seja bem-vindo à Orgânicos        |
=------------------------------------------=
''')

input("Aperte enter para continuar... ")

def linha():
    print('-'*40)
opcao = 1
while opcao != "0":
    os.system('cls')
    linha()
    print(               "           MENU DE NAVEGAÇÃO "              )
    linha()
    print('''
    [1] - Cadastro
    [2] - Vendas
    [3] - Relatório
    [0] - Sair 
     ''')

    opcao = input("Escolha uma das opçôes: ")

    if opcao == "1":
        menu_cadastro(produtos)

    elif opcao == "2":
        menu_vendas(produtos, carrinho, relatorio)

    elif opcao == "3":
        menu_relatorio(relatorio)

    elif opcao == "0":
        print('Você está saindo')

    else:
        print('Retornando ao início')
        print('-' * 25)
