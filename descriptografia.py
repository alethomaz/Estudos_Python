# Recebe alfabeto normal
alfabeto_normal = input("Digite o alfabeto normal: ").lower()
# Recebe alfabeto cifrado
alfabeto_cifrado = input("Digite o alfabeto cifrado: ").lower()
# Recebe frase cifrada
frase_cifrada = input("Digite a frase cifrada: ").lower()
# Recebe frase decifrada
frase_decifrada = ""

# Loop para decifrar a frase
for caracter in frase_cifrada:
    # Verifica se o caracter é uma letra
    if caracter.isalpha():
        # Recebe a posição da letra no alfabeto cifrado
        cifragem = alfabeto_cifrado.index(caracter)
        # Recebe a letra correspondente no alfabeto normal
        frase_decifrada += alfabeto_normal[cifragem]
    # Caso não seja uma letra, adiciona o caracter na frase decifrada
    else:
        # Adiciona o caracter na frase decifrada
        frase_decifrada += caracter

print('Frase decifrada:')
print(frase_decifrada)


