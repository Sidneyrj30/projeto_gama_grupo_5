relatorio = [{'nome':"arroz", 'preco': 15.00}, {'nome':"feijao",'preco': 20.00}, {'nome':"carne", 'preco': 30.00},
{'nome':'cebola', 'preco': 5.56}]

preco = 0

for item in range(len(relatorio)):
    preco = preco + relatorio[item]['preco']

print('''
        --------------------------------
                Relatório de Vendas        
        -------------------------------- 
        ''')

for item in range(len(relatorio)):
    print(f"Produto: {relatorio[item]['preco']}")

print(f" Valor Total: R${preco}" )   
