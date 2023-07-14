# Quantidade de nomes a serem digitados
quantidade = int(input('Quantos nomes deseja digitar? '))
# Lista vazia para receber os nomes
nomes = []

# Loop para receber os nomes
for i in range(quantidade):
    # Recebe o nome
    nome = input('Digite o nome: ')
    # Adiciona o nome à lista
    nomes.append(nome)
# Imprime os nomes em ordem alfabética
for palavra in sorted(nomes):
    print(palavra)