# Inputa duas variáveis
num_posto_agua, dist_maxima = [int(x) for x in input('Digite o número de postos e a distância máxima: ').split()]
# Inputa as distâncias
distancias_postos = [int(x) for x in input('Digite as distâncias dos postos: ').split()]

# Ordena as distâncias
resultado = 'Não consegue!'

# Para cada índice da lista
for i in range(num_posto_agua-1):
    # Calcula a distância real
    dist_real = abs(distancias_postos[i+1] - distancias_postos[i])
    # Se a distância real for menor ou igual a distância máxima
    if dist_real <= dist_maxima:
        resultado = 'Consegue!'
    # Se não
    else:
        resultado = 'Não consegue!'
        # Para o loop
        break
    
# Imprime o resultado
print('O resultado é: ', resultado)