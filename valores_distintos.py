# Conjuntos
distintos = set()

# Adicionando valores
for i in range(4):
    # Recebe o número
    numero = int(input('Digite o número: '))
    # Adiciona o número ao conjunto
    distintos.add(numero)
# Imprime a quantidade de números distintos
print(f'Os números distintos digitados foram: {len(distintos)}')