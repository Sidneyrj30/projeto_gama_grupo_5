import os
relatorio = []

def menu_relatorio(relatorio):
    os.system('cls')

    if len(relatorio) == 0:
        print("Não tem produtos para o relatório")
        input("Aperte enter para continuar... ")
    else: 
        preco = 0

        for item in range(len(relatorio)):
            preco = preco + relatorio[item]['preco']

        print('''
        -------------------------------------------------
                Você entrou no relatório de Vendas        
        ------------------------------------------------- 
                ''')

        for item in range(len(relatorio)):
            print(f"Produto: {relatorio[item]['nome']} preço: R$ {relatorio[item]['preco']:.2f}")

        print("==========================================")
        print(f"Total de Produtos: {len(relatorio)} Unidades Valor Total: R${preco:.2f}" )
        input("Aperte enter para continuar... ")  
