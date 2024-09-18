import pygame
import sys
import random

# Inicializar pygame
pygame.init()

# Definir cores
PRETO = (0, 0, 0)
AMARELO = (255, 255, 0)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)
BRANCO = (255, 255, 255)

# Tamanho da janela
largura, altura = 680, 480
tela = pygame.display.set_mode((largura, altura))

# Título da janela
pygame.display.set_caption("Pacman com Labirinto e Fantasmas")

# Relógio para controle de FPS
relogio = pygame.time.Clock()

# Definir as variáveis do Pacman
pacman_pos = [50, 50]
pacman_velocidade = 5
pacman_tamanho = 20

# Definir o fantasma
fantasma_pos = [120, 120]  # Ajuste para o fantasma estar dentro do labirinto
fantasma_velocidade = 2
fantasma_tamanho = 20

# Labirinto (0 = vazio, 1 = parede, 2 = ponto)
labirinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Função para desenhar o Pacman
def desenhar_pacman(tela, pos):
    pygame.draw.circle(tela, AMARELO, pos, pacman_tamanho)

# Função para desenhar o fantasma
def desenhar_fantasma(tela, pos):
    pygame.draw.circle(tela, VERMELHO, pos, fantasma_tamanho)

# Função para desenhar o labirinto
def desenhar_labirinto(tela, labirinto):
    for y, linha in enumerate(labirinto):
        for x, bloco in enumerate(linha):
            if bloco == 1:  # Parede
                pygame.draw.rect(tela, AZUL, pygame.Rect(x*40, y*40, 40, 40))
            elif bloco == 2:  # Ponto
                pygame.draw.circle(tela, BRANCO, (x*40 + 20, y*40 + 20), 5)

# Movimentação do fantasma
def mover_fantasma():
    direcao = random.choice(['esquerda', 'direita', 'cima', 'baixo'])
    # Confere se o fantasma está dentro dos limites do labirinto
    fantasma_grid_pos = [fantasma_pos[1] // 40, fantasma_pos[0] // 40]

    if direcao == 'esquerda' and labirinto[fantasma_grid_pos[0]][fantasma_grid_pos[1] - 1] != 1:
        fantasma_pos[0] -= fantasma_velocidade
    elif direcao == 'direita' and labirinto[fantasma_grid_pos[0]][fantasma_grid_pos[1] + 1] != 1:
        fantasma_pos[0] += fantasma_velocidade
    elif direcao == 'cima' and labirinto[fantasma_grid_pos[0] - 1][fantasma_grid_pos[1]] != 1:
        fantasma_pos[1] -= fantasma_velocidade
    elif direcao == 'baixo' and labirinto[fantasma_grid_pos[0] + 1][fantasma_grid_pos[1]] != 1:
        fantasma_pos[1] += fantasma_velocidade

# Função principal do jogo
def jogo():
    global direcao
    direcao = 'parado'
    rodando = True
    pontos = 0

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Movimentação do Pacman
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    direcao = 'esquerda'
                elif evento.key == pygame.K_RIGHT:
                    direcao = 'direita'
                elif evento.key == pygame.K_UP:
                    direcao = 'cima'
                elif evento.key == pygame.K_DOWN:
                    direcao = 'baixo'

        # Atualizar a posição do Pacman
        pacman_grid_pos = [pacman_pos[1] // 40, pacman_pos[0] // 40]
        if direcao == 'esquerda' and labirinto[pacman_grid_pos[0]][pacman_grid_pos[1] - 1] != 1:
            pacman_pos[0] -= pacman_velocidade
        elif direcao == 'direita' and labirinto[pacman_grid_pos[0]][pacman_grid_pos[1] + 1] != 1:
            pacman_pos[0] += pacman_velocidade
        elif direcao == 'cima' and labirinto[pacman_grid_pos[0] - 1][pacman_grid_pos[1]] != 1:
            pacman_pos[1] -= pacman_velocidade
        elif direcao == 'baixo' and labirinto[pacman_grid_pos[0] + 1][pacman_grid_pos[1]] != 1:
            pacman_pos[1] += pacman_velocidade

        # Comer pontos
        if labirinto[pacman_grid_pos[0]][pacman_grid_pos[1]] == 2:
            labirinto[pacman_grid_pos[0]][pacman_grid_pos[1]] = 0
            pontos += 1

        # Mover o fantasma
        mover_fantasma()

        # Preencher o fundo da tela
        tela.fill(PRETO)

        # Desenhar o labirinto
        desenhar_labirinto(tela, labirinto)

        # Desenhar o Pacman
        desenhar_pacman(tela, pacman_pos)

        # Desenhar o Fantasma
        desenhar_fantasma(tela, fantasma_pos)

        # Atualizar a tela
        pygame.display.flip()

        # Controlar FPS
        relogio.tick(30)

# Rodar o jogo
jogo()