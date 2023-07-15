# Quantos jogos
#path: Introdução Orientação Objetos/POO/Estudos_Dados/adivinha.py
jogos = int(input('Quantos jogos deseja inserir? '))

# Para cada jogo
for jogo in range(jogos):
    # Recebe a quantidade de palpites e o número secreto
    qtd_palpites, numero_secreto = [int(x) for x in input('Digite a quantidade de alunos e o número secreto: ').split()]
    # Recebe os palpites
    palpites = [int(x) for x in input('Digite os valores dos alunos: ').split()]
    # Calcula a diferença entre o palpite e o número secreto
    diferença = [abs(palpite - numero_secreto) for palpite in palpites]

    # O ganhador é o menor valor da lista de diferenças
    ganhador = min(diferença)
    # O índice do ganhador é o índice do menor valor da lista de diferenças
    indice = diferença.index(ganhador)

    # Imprime o ganhador
    print(f'O ganhador foi o aluno que deu o palpite numero: {palpites[indice]}')
    print(f'A diferença entre o palpite e o número secreto foi: {ganhador}')
    print(palpites)

