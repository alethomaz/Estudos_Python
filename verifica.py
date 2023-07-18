# Pede as sequencias para verificação
sequencia1 = [int(x) for x in input('Digite os plugs(0/1): ').split()]
sequencia2 = [int(x) for x in input('Digite os plugs(0/1): ').split()]

# Para cada índice da lista
for i in range(5):
    # Se o índice da sequencia1 for igual ao índice da sequencia2
    if sequencia1[i] == sequencia2[i]:
        # Imprime N
        print('N')
        break
    # Se o índice da sequencia1 for igual ao índice da sequencia2
    else:
        # Imprime Y
        print('Y')
        # Para o loop
        break

