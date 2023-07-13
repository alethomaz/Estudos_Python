# Define um limite:
limite = int(input('Digite o limite de altura do pulo: '))
# Define a quantidade de pulos:
qtd_pulos = int(input('Digite a quantidade de pulos: '))
# Define as alturas:
alturas = [int(x) for x in input('Digite as alturas: ').split()]
# Define o contador:
contador = 0
# Define a diferença:
for i in range(qtd_pulos-1):
     # Diferença entre as alturas:
     diferenca = abs(alturas[i+1] - alturas[i])
    # Se a diferença for menor ou igual ao limite:
     if diferenca <= limite:
         # Incrementa o contador:
         contador += 1
# Se o contador for igual a quantidade de pulos - 1:
if contador == qtd_pulos-1:
    
    print('Você venceu')
else:
    print('Você perdeu')