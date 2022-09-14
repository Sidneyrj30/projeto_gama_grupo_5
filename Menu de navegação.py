def linha():
    print('-'*40)
opcao = 0
while opcao != "0":
    linha()
    print(               "           MENU DE NAVEGAÇÃO "              )
    linha()
    print('''
    [1] - Cadastro
    [2] - Vendas
    [3] - Relatório
    [0] - Sair ''')

    opcao = (input('Digite onde deseja ir.'))
    if opcao == "1":
        print('Você entrou no cadastro de produtos')

    elif opcao == "2":
        print('Você entrou nas vendas')

    elif opcao == "3":
        print('Você entrou no relatório')

    elif opcao == "0":
        print('Você está saindo')

    else:
        print('Retornando ao início')
        print('-' * 25)
