# Pede o numero de carros e o numero de voltas
num_carros, num_voltas = [int(x) for x in input('Digite o número de carros e o número de voltas: ').split()]
# Cria uma lista vazia para os tempos
tempos = []
# Pede os tempos de cada carro e adiciona a lista tempos
for i in range(num_carros):
    # Adiciona uma lista vazia para cada carro
    tempos.append([float(x) for x in input('Digite os tempos do carro {}: '.format(i+1)).split()])
# Cria uma lista vazia para os tempos somados
tempos_somados = []
# Soma os tempos de cada carro e adiciona a lista tempos_somados
for tempo in tempos:
    # Adiciona a soma dos tempos de cada carro
    tempos_somados.append(sum(tempo))

# Imprime o carro mais rápido
print(f'O carro {tempos_somados.index(min(tempos_somados))+1} foi o mais rápido com o tempo de {min(tempos_somados)}')
# Ordena os tempos
tempos_ordenados = sorted(tempos_somados)
# Pega os 3 primeiros colocados
tres_colocados = tempos_ordenados[:3]

# Imprime os 3 primeiros colocados
print(f'O segundo colocado foi o carro {tempos_somados.index(tres_colocados[1])+1} com o tempo de {tres_colocados[1]}')
print(f'O terceiro colocado foi o carro {tempos_somados.index(tres_colocados[2])+1} com o tempo de {tres_colocados[2]}')