import os
relatorio = []

def menu_relatorio(relatorio):
    os.system('cls')

    preco = 0

    for item in range(len(relatorio)):
        preco = preco + relatorio[item]['preco']

    print('''
    -------------------------------------------------
            Você entrou no relatório de Vendas        
    ------------------------------------------------- 
            ''')

    for item in range(len(relatorio)):
        print(f"Produto: {relatorio[item]['nome']} preço: R$ {relatorio[item]['preco']}")

    print(f"Total de Produtos: {len(relatorio)} Unidades Valor Total: R${preco}" ) 
    input("Aperte enter para continuar... ")  
