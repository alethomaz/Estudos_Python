# Seleciona uma linha para somar
linha_selecionada = int(input('Digite a linha: '))
# Operação de soma ou média
operacao = input('Digite a operação[S/N]: ').upper()

# Cria a matriz
matriz = []

# Preenche a matriz
for i in range(12):
    # Linha
    linha = []
    # Coluna
    for coluna in range(12):
        # Elemento
        elemento = float(input('Digite o elemento: '))
        # Coloca o elemento na linha
        linha.append(elemento)
    # Coloca a linha na matriz
    matriz.append(linha)
# Seleciona a linha
if operacao == 'S':
    # Soma os elementos da linha
    soma = sum(matriz[linha_selecionada])
    # Imprime o resultado
    print(f'A soma dos elementos da linha {linha} é {soma:.1f}')
# Seleciona a linha
elif operacao == 'M':
    # Calcula a média dos elementos da linha
    media = sum(matriz[linha_selecionada]) / len(matriz[linha_selecionada])
    print(f'A média dos elementos da {linha_selecionada} é {media:.1f}')