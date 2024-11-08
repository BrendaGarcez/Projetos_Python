import pygame 
from pygame.locals import *
from sys import exit 
from random import randint

pygame.init()

largura = 640
altura = 480
x = largura/2
y = altura/2

x_a = randint(40, 600)
y_a = randint(50, 430)


pontos = 0
fonte = pygame.font.SysFont('arial', 40, True, True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock()

while True:
    relogio.tick(20)
    tela.fill((0,0,0))
    mensagem = f'Pontos: {pontos}'
    texte_formatado = fonte.render(mensagem, False, (255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        '''if event.type == KEYDOWN:
            if event.key == K_a:
                x = x - 20
            if event.key == K_d:
                x = x + 20
            if event.key == K_w:
                y = y - 20
            if event.key == K_s:
                y = y + 20'''
    if pygame.key.get_pressed()[K_LEFT]:
        x = x - 20
    if pygame.key.get_pressed()[K_RIGHT]:
        x = x + 20
    if pygame.key.get_pressed()[K_UP]:
        y = y - 20
    if pygame.key.get_pressed()[K_DOWN]:
        y = y + 20

    rect_ver = pygame.draw.rect(tela, (255,0,0), (x, y, 40, 50))
    rect_azul = pygame.draw.rect(tela, (0,0,255), (x_a,y_a, 40, 50))

    if rect_ver.colliderect(rect_azul):
        x_a = randint(40, 600)
        y_a = randint(50, 430)
        pontos = pontos + 1

    tela.blit(texte_formatado,(450,40))
    pygame.display.update()

#Figuras geometricas pelo plano cartesiano