# Insere uma quantidade
quantidade = int(input('Digite a quantidade: '))

# Percorre
for i in range(quantidade):
    # Cria um conjunto vazio
    lista_compras = set()
    # Recebe uma lista de produtos
    lista = [str(x) for x in input('Digite a lista: ').split()]
    # Percorre os produtos no conjunto
    for produto in lista:
        # Adiciona o produto no conjunto
        lista_compras.add(produto)
    # Imprime a lista de compras
    print('A lista de compras é:')
    print(lista_compras)