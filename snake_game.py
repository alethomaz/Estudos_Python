# Configurações iniciais do jogo
import pygame
import random

# Inicia
pygame.init()
# Coloca o nome
pygame.display.set_caption('Jogo da Cobra')
# Tamanho da tela
largura, altura = 1000, 600
# Criar a tela
tela = pygame.display.set_mode((largura, altura))
# Cria um relógio:
relogio = pygame.time.Clock()

# Cores RGB
preto = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)

# Parâmetros da cobrinha:
# Tamanho:
tamanho_quadrado = 20
# Velocidade:
velocidade_cobra = 10

def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = 20
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = -20
    elif tecla == pygame.K_LEFT:
        velocidade_x = -20
        velocidade_y = 0
    elif tecla == pygame.K_RIGHT:
        velocidade_x = 20
        velocidade_y = 0

    return velocidade_x, velocidade_y

def desenha_potuacao(pontuacao):
    fonte = pygame.font.SysFont('Helvetica', 30)
    texto = fonte.render(f'Pontuação: {pontuacao}', True, vermelha)
    # Coloca na tela
    tela.blit(texto, [1, 1])


def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])


def desenhar_cobra(tamanho, pixel_cobra):
    for pixel in pixel_cobra:
        pygame.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho])


def gerar_comida():
    # Gera a comida exatamente do mesmo tamanho da snake
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / 20.0) * 20.0

    return comida_x, comida_y



def rodar_jogo():
    fim_jogo = False

    x = largura / 2
    y = altura / 2
    
    velocidade_x = 0
    velocidade_y = 0

    # Tamanho dela é a pontuação
    tamanho_cobra = 1
    pixel_cobra = []

    comida_x, comida_y = gerar_comida()

    while not fim_jogo:
        tela.fill(preto)

        # Capturar eventos
        for event in pygame.event.get():
            # Evento de fechar a tela
            if event.type == pygame.QUIT:
                fim_jogo = True
            elif event.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(event.key)
            
            # Atualizar posição da cobra:
            x += velocidade_x
            y += velocidade_y

            if x < 0 or x > largura or y < 0 or y > altura:
                fim_jogo = True


            # Desenhar os objetos
            desenhar_comida(tamanho_quadrado, comida_x, comida_y)

            # Pontuação
            desenha_potuacao(tamanho_cobra-1)
            # Cobra
            pixel_cobra.append([x, y])

            if len(pixel_cobra) > tamanho_cobra:
                del pixel_cobra[0]

            for pixel in pixel_cobra[:-1]:
                if pixel == [x, y]:
                    fim_jogo = True
            
            desenhar_cobra(tamanho_quadrado, pixel_cobra)
            # Comida

            # Atualização da tela:
            pygame.display.update()

            if x == comida_x and y == comida_y:
                tamanho_cobra += 1
                comida_x, comida_y = gerar_comida()

            # Atualização do relógio:
            relogio.tick(velocidade_cobra)
  
# Criar um looping infinito do jog0

# Criar a lógica de terminar o jogo
# Cobra bateu na parede
# Cobra bateu em si mesma

# Pegar a iteração do usuário
# Fechar a tela
# apertou as teclas do teclado pra mover a cobra 

rodar_jogo()