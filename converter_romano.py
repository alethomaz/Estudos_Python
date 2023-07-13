# Dicionário com os valores romanos:
valores_romanos = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V':5,  
                   'I': 1, 'CM': 900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4}

# Variável que recebe o número romano:
numero_romano = input('Digite um número romano: ').upper()

# Numero arábico:
numero_arabico = 0

# Contador:
i = 0

# Enquanto o contador for menor que o tamanho do número romano:
while i < len(numero_romano):
    # Seleção do número romano:
    grupo = numero_romano[i:i+2]
    # Se o grupo estiver no dicionário:
    if grupo in valores_romanos:
        # Soma o valor do grupo ao número arábico:
        numero_arabico += valores_romanos[grupo]
        # Incrementa o contador:
        i += 2
    # Se o grupo não estiver no dicionário:
    else:
        # Seleciona o algarismo:
        algarismo = numero_romano[i]
        # Soma o valor do algarismo ao número arábico:
        numero_arabico += valores_romanos[algarismo]
        # Incrementa o contador:
        i += 1

print('O número romano {} é igual a {} em arábico.'.format(numero_romano, numero_arabico))

