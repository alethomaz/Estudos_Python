frase = input('Digite uma frase: ')

contagem = {}

for letra in frase:
    if letra in contagem:
        contagem[letra] += 1
    else:
        contagem[letra] = 1

print('Contagem de letras: ')
print(contagem)
print(f'A letra que mais aparece é: {max(contagem, key=contagem.get)}')