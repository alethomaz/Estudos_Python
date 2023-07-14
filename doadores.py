# Quantidade de calouros
quant_cal = int(input('Digite a quantidade de doadores: '))
# Lista de calouros
calouros = []
# Contador
contador = 0

# Adicionando valores
for i in range(quant_cal):
    # Recebe o nome do calouro
    nome = input('Digite o nome do calouro: ')
    # Adiciona o nome do calouro a lista
    calouros.append(nome)

# Quantidade de doadores
doadores = []

# Variável que recebe a quantidade de doadores
quant_doador = int(input('Digite a quantidade de doadores: '))
# Adicionando valores
for i in range(quant_doador):
    # Recebe o nome do doador
    nome = input('Digite o nome do doador: ')
    # Adiciona o nome do doador a lista
    doadores.append(nome)

# O que interessa à comissão é calcular a proporção de calouros que doaram sangue em relação ao total de calouros.

# Percorre a lista de doadores
for doador in doadores:
    # Se o doador estiver na lista de calouros:
    if doador in calouros:
        # Adiciona 1 ao contador
        contador += 1

# Imprime o número de calouros que doaram sangue
print(f'{contador} calouros doaram sangue')

# Proporção:
porcentagem = contador / quant_cal
# Imprime a proporção
print(f'{porcentagem:.2f}% dos calouros doaram sangue')