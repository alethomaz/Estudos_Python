# Pede uma frase 
nome_completo = input('Digite seu nome: ').split()
# Cria uma lista vazia
letras_abreviadas = []
# Cria uma lista com os nomes do meio
nomes_meio = nome_completo[1:-1]

# Para cada nome na lista de nomes do meio:
for nome in nomes_meio:
    # Se o nome tiver mais de 3 letras:
    if len(nome) > 3:
        # Adiciona a letra abreviada na lista de letras abreviadas:
        letras_abreviadas.append(nome[0].upper() + '.')
# Imprime o nome completo com a primeira e última letra e as letras abreviadas:
print(nome_completo[0], *letras_abreviadas, nome_completo[-1])