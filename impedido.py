# Inputa o número de atacantes e defensores, e os valores de cada um
num_atacantes, num_defensores = [int(w) for w in input().split()]

# Enquanto houver atacantes, o programa continua
while num_atacantes != 0:
    # Se o último atacante for menor que o penúltimo defensor, e o penúltimo defensor não for repetido, o impedimento é verdadeiro
    impedido = 'N'
    # Inputa os valores dos atacantes e defensores
    ultimo_atacante = min(int(w) for w in input().split())
    # Se o último atacante for menor que o penúltimo defensor, e o penúltimo defensor não for repetido, o impedimento é verdadeiro
    defensores = [int(w) for w in input().split()]
    defensores_2 = defensores.copy()
    defensores_2.remove(min(defensores))
    penultimo_defensor = min(defensores_2)
    
    # Se o último atacante for menor que o penúltimo defensor, e o penúltimo defensor não for repetido, o impedimento é verdadeiro
    if (ultimo_atacante <= penultimo_defensor) and (defensores.count(penultimo_defensor) < 2):
        impedido = 'Y'
        
    print(impedido)
    
    num_atacantes, num_defensores = [int(w) for w in input().split()]