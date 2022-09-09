def linha():
    print('-'*70)


linha()    
print(               "                 *** MENU NAVEGAÇÃO ***"              )
linha()



menu = ("Cadastro Menu" , "Vendas" , "Relatório", "Sair")
c = 1
for item in menu:
 print(f'{c} - {item}')
 c += 1


opcao = '1', 
while opcao != '0':
    linha()
    opcao = input('Digite Opção: ')
    linha()


