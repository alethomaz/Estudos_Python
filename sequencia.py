# Pede uma sequência:
sequencia = [int(x) for x in input('Digite os números da sequência: ').split()]

# Cria cópias da sequência
seq_crescente = sequencia.copy()
seq_descrescente = sequencia.copy()

# Ordena as cópias
seq_crescente.sort()
# Ordena as cópias
seq_descrescente.sort(reverse=True)

# Se a sequência for igual a sequência crescente
if sequencia == seq_crescente:
    print('Crescente!')
# Se a sequência for igual a sequência decrescente
elif sequencia == seq_descrescente:
    print('Descrescente! ')
# Se não
else:
    print('Não estava em ordem!')



