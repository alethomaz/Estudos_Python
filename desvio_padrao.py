quantidade = int(input('Quantos números deseja inserir? '))
numeros = []
for i in range(quantidade):
    numero = float(input('Digite um número: '))
    numeros.append(numero)
    
media = sum(numeros) / len(numeros)

desvios = []

for numero in numeros:
    desvio = numero - media
    desvios.append(desvio)

variância = sum([desvio ** 2 for desvio in desvios]) / len(numeros)

desvio_padrao = variância ** 0.5

print(f'A média é: {media:.2f}')
print(f'A variância é: {variância:.2f}')
print(f'O desvio padrão é: {desvio_padrao:.2f}')