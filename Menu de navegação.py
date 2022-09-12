def linha():
    print('-'*70)


linha()
print(               "  MENU DE NAVEGAÇÃO "              )
linha()
opcao = 0
while opcao != "4":
    print('''
    [1] - Cadastro
    [2] - Vendas
    [3] - Relatório
    [4] - Sair ''')
    opcao = (input('Digite onde deseja ir.'))
    if opcao == "1":
        print('Você entrou no cadastro de produtos')

    elif opcao == "2":
        print('Você entrou nas vendas')

    elif opcao == "3":
        print('Você entrou no relatório')

    elif opcao == "4":
        print('Você está saindo')

    else:
        print('Retornando ao início')
        print('=-=' * 10)





