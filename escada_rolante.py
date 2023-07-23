# Quantidade de pessoas
num_pessoas = int(input())

while num_pessoas != 0:
    
    # Recebe uma lista dos tempos
    tempos = [int(w) for w in input().split()]
    
    # Tempo de uma pessoa
    tempo_total = 10
    
    # Percorre cada tempo
    for i in range(1, len(tempos)):
        
        # Se o tempo que a pessoa entrou for maior que o tempo que ela esteve ligada
        if tempos[i] >= (tempos[i - 1] + 10):
            # Soma mais 10 ao tempo pois ela vai so entrar e ficar 10
            tempo_total += 10
        
        # Se o tempo que a proxima pessoa entrou for menor que o tempo q ela esteve ligada
        else:
            # Soma a diferença dos tempos
            tempo_total += (tempos[i] - tempos[i - 1])
    
    print(tempo_total)
    
    num_pessoas = int(input()