# Pede o numéro de perguntas e a frequência necessária
num_perguntas, frequencia = [int(x) for x in input('Digite as perguntas realizadas e a frequência necessária: ').split()]

# Pede as perguntas
perguntas = [int(x) for x in input('Digite as perguntas: ').split()]

# Verifica se alguma pergunta foi realizada a quantidade de vezes necessária
for p in range(1, num_perguntas + 1):
    # Verifica se a pergunta foi realizada a quantidade de vezes necessária
    if perguntas.count(p) >= frequencia:
        # Imprime a pergunta
        print(f'Pergunta mais realizada: {p}', end=' ')
# Caso nenhuma pergunta tenha sido realizada a quantidade de vezes necessária
else:
    print(0)



