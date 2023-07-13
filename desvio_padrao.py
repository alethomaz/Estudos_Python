# Digite a quantidade de números
quantidade = int(input('Quantos números deseja inserir? '))
# Cria uma lista vazia
numeros = []
# Para cada número na quantidade de números
for i in range(quantidade):
    # Pede um número
    numero = float(input('Digite um número: '))
    # Adiciona o número na lista
    numeros.append(numero)

# Calcula a média    
media = sum(numeros) / len(numeros)

# Cria uma lista vazia
desvios = []

# Para cada número na lista de números
for numero in numeros:
    # Calcula o desvio
    desvio = numero - media
    # Adiciona o desvio na lista de desvios
    desvios.append(desvio)

# Calcula a variância
variância = sum([desvio ** 2 for desvio in desvios]) / len(numeros)
# Calcula o desvio padrão
desvio_padrao = variância ** 0.5

# Imprime os resultados
print(f'A média é: {media:.2f}')
print(f'A variância é: {variância:.2f}')
print(f'O desvio padrão é: {desvio_padrao:.2f}')