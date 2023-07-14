# Quantidade de números a serem digitados
quantidade = int(input('Quantos números deseja digitar? '))
# Variável para receber o número
multiplicativo = 1

# Loop para receber os números
for i in range(quantidade):
    # Recebe o número
    numero = int(input('Digite o número: '))
    # Multiplica o número à variável
    multiplicativo *= numero
# Calcula a média geométrica
media_geometrica = (multiplicativo) ** (1/quantidade)
# Imprime a média geométrica
print('A média geométrica é: {:.2f}'.format(media_geometrica))  