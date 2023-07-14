# Quantidade de operações
quant_op = int(input('Digite a quantidade de notas: '))

# Listas
cedulas = []
quant_notas = []

# Adicionando valores
for i in range(quant_op):
    # Recebe o valor da nota
    nota = float(input('Digite o valor da nota: '))
    # Adiciona o valor da nota a lista
    cedulas.append(nota)
    # Recebe a quantidade de notas
    quant_cedula = int(input('Digite a quantidade de notas: '))
    # Adiciona a quantidade de notas a lista
    quant_notas.append(quant_cedula)
# Pede um saque
saque = float(input('Digite o valor do saque: '))
# Inverte as listas
cedulas.reverse()
quant_notas.reverse()
# Lista que recebe as cédulas retiradas
cedulas_retiradas = []

# Enquanto o saque for diferente de 0:
while saque != 0:
    # Para cada valor na lista de cédulas:
    for i in range(len(cedulas)):
        # Número de cédulas
        numero_cedulas = saque // cedulas[i]
        # Se o número de cédulas for menor ou igual a quantidade de notas:
        if numero_cedulas <= quant_notas[i]:
            # Subtrai o valor do saque
            saque -= numero_cedulas * cedulas[i]
            # Adiciona o número de cédulas a lista
            cedulas_retiradas.append(numero_cedulas)
        # Se o número de cédulas for maior que a quantidade de notas:
        else:
            # Subtrai o valor do saque
            saque -= quant_notas[i] * cedulas[i]
            # Adiciona a quantidade de notas a lista
            cedulas_retiradas.append(quant_notas[i])

print(cedulas)
print(quant_notas)
print(f'Serão retiradas {cedulas_retiradas} cédulas de {cedulas}')
